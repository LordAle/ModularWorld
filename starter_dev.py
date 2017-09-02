import catalog_writer
import sys
import json
from PyQt5 import Qt, QtCore, QtWidgets, QtSql, QtGui
from db_loader import loader
from ModularWorldUi.mainwindow import Ui_MainWindow
import models
import base
import city
import building
import group
import character
import family
import db_connector
import add_dialogs
import delete_dialogs
# import populator
import visitor_manager


class Controller(QtWidgets.QMainWindow, Ui_MainWindow):
    """Initialize main window, attribute models and define Actions method. Also keep sqlAlcehmy database interface alive"""

    def __init__(self):
        super(self.__class__, self).__init__()
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.add_dialog = None
        self.delete_dialog = None

        # Declare models
        self.treeModel = QtGui.QStandardItemModel()

        # Models triggers
        # self.listViewCities.clicked.connect(self.action_city_click)
        # self.listViewBuildings.clicked.connect(self.action_building_click)
        # self.listViewCharacters.clicked.connect(self.action_character_click)

        # Contextual menus
        self.treeView.addAction(self.actionAddCity)
        self.treeView.addAction(self.actionAddBuilding)
        self.treeView.addAction(self.actionAddGroup)
        self.treeView.addAction(self.actionAddCharacter)
        self.treeView.addAction(self.actionDelete)

        self.pushButtonShowFamily.clicked.connect(self.show_family_click)
        self.pushButtonVisitor.clicked.connect(self.show_visitor_click)

        # Actions triggers
        self.actionNewDatabase.triggered.connect(self.action_new_database)
        self.actionLoadDatabase.triggered.connect(self.action_load_database)

        self.actionAddCity.triggered.connect(self.add_city_click)
        self.actionAddBuilding.triggered.connect(self.add_building_click)
        self.actionAddGroup.triggered.connect(self.add_group_click)
        self.actionAddCharacter.triggered.connect(self.add_character_click)

        self.actionDelete.triggered.connect(self.delete_click)

        self.actionCity_table.triggered.connect(self.action_full_city)
        self.actionBuilding_table.triggered.connect(self.action_full_building)
        self.actionCharacter_table.triggered.connect(self.action_full_character)

    def new_database(self):
        dbname = self.new_file_dialog('New database', 'C:\\Users\LordAle\PycharmProjects\ModularWorld\database')
        if dbname[0]:
            loader.create_new(dbname[0])
            self.open_QConnection(dbname[0])
            self.setup_new_db()

    def load_database(self):
        dbname = self.open_file_dialog('Open database', 'C:\\Users\LordAle\PycharmProjects\ModularWorld\database')
        if dbname[0]:
            loader.create_new(dbname[0])
            self.open_QConnection(dbname[0])

    def open_QConnection(self, db_name):
        self.QConnection = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.QConnection.setDatabaseName(db_name)
        self.QConnection.open()
        if self.QConnection.open() == False:
            print('Error in connection!')
        else:
            print('Connection OK!')
        self.set_models()
        self.build_tree_model()

    def set_models(self):

        #Assign models
        self.table_content_model = models.SqlRelationalModel(db=self.QConnection)
        self.tableViewContent.setModel(self.table_content_model)
        self.tableViewContent.setItemDelegate(QtSql.QSqlRelationalDelegate(self.tableViewContent))

        self.table_special_model = models.SqlRelationalModel(db=self.QConnection)
        self.tableViewSpecial.setModel(self.table_special_model)
        self.tableViewSpecial.setItemDelegate(QtSql.QSqlRelationalDelegate(self.tableViewSpecial))

        self.side_view_value_model = models.StringListModel()
        self.listViewSelectedValue.setModel(self.side_view_value_model)

    def setup_new_db(self):
        pass


# View query methods ---------------------------------------------------------------Begin

    # Selected object ID
    def get_selected_id(self):
        selected_index = self.treeView.selectionModel().currentIndex()
        selected_item = self.treeModel.itemFromIndex(selected_index)
        return selected_item.data(20)

    # Set correct list for city / building / character
    def build_tree_model(self):
        # Data role 20 is for item id in database, 21 is for table name

        self.treeModel.clear()
        self.treeModel.setHorizontalHeaderItem(0, QtGui.QStandardItem('World'))
        parent_node = self.treeModel.invisibleRootItem()

        # Sql Queries
        city_query = QtSql.QSqlQuery("SELECT name, id FROM cities")
        cities_list = []
        while city_query.next():
            cities_list.append([city_query.value(0), city_query.value(1)])

        building_query = QtSql.QSqlQuery("SELECT name, id, city_id FROM buildings")
        buildings_list = []
        while building_query.next():
            buildings_list.append([building_query.value(0), building_query.value(1), building_query.value(2)])

        group_query = QtSql.QSqlQuery("SELECT name, id, building_id, characters FROM groups")
        group_list = []
        while group_query.next():
            group_list.append([group_query.value(0), group_query.value(1), group_query.value(2), group_query.value(3)])

        character_query = QtSql.QSqlQuery("SELECT name, id FROM characters")
        character_list = []
        while character_query.next():
            character_list.append([character_query.value(0), character_query.value(1)])

        for cit in cities_list:
            c = QtGui.QStandardItem(cit[0])
            c.setData(cit[1], 20)
            c.setData('cities', 21)
            parent_node.appendRow(c)
            parent_city = c

            city_buildings = [b for b in buildings_list if b[2] == c.data(20)]
            for bui in city_buildings:
                b = QtGui.QStandardItem(bui[0])
                b.setData(bui[1], 20)
                b.setData('buildings', 21)
                parent_city.appendRow(b)
                parent_building = b

                building_groups = [g for g in group_list if g[2] == b.data(20)]
                for gro in building_groups:
                    g = QtGui.QStandardItem(gro[0])
                    g.setData(gro[1], 20)
                    g.setData('groups', 21)
                    parent_building.appendRow(g)
                    parent_group = g

                    try:
                        group_characters_id = json.loads(gro[3])
                    except:
                        group_characters_id = []
                    group_characters = [ch for ch in character_list if ch[1] in group_characters_id]
                    for cha in group_characters:
                        ch = QtGui.QStandardItem(cha[0])
                        ch.setData(cha[1], 20)
                        ch.setData('characters', 21)
                        parent_group.appendRow(ch)

        self.treeView.setModel(self.treeModel)
        self.treeView.expandAll()

    # Unused, could be implemented to optimize item addition to view
    def update_tree_model(self, table, item_id, parent=None):
        query = None
        if table == 'cities':
            query = QtSql.QSqlQuery("SELECT name, id FROM cities WHERE id = {0}".format(item_id))
            parent = self.treeModel.invisibleRootItem()
        if table == 'buildings':
            query = QtSql.QSqlQuery("SELECT name, id, city_id FROM buildings WHERE id = {0}".format(item_id))
            if not parent:
                selected_index = self.treeView.selectionModel().currentIndex()
                parent = self.treeModel.itemFromIndex(selected_index)

        while query.next():
            new_item = QtGui.QStandardItem(query.value(0))
            new_item.setData(QtGui.QStandardItem(query.value(1)), 20)
            new_item.setData(QtGui.QStandardItem(table), 21)
            parent.appendRow(new_item)

    # Side view
    def set_city_side_view(self, city_id):
        side_values_list = ['ID: {0}'.format(city_id)]
        selected_city = self.get_cities_from_db('id', city_id)
        selected_city = selected_city[0]

        side_values_list.append('{0} of {1}'.format(selected_city.size.name, selected_city.name))
        side_values_list.append('Population of {0}'.format(selected_city.population))
        side_values_list.append('Dominant culture is {0}'.format(selected_city.culture.name))
        side_values_list.append('Geographical features are :')
        if selected_city.plain:
            side_values_list.append('  Plain')
        if selected_city.forest:
            side_values_list.append('  Forest')
        if selected_city.river:
            side_values_list.append('  River')
        if selected_city.sea:
            side_values_list.append('  Sea')
        if selected_city.mountain:
            side_values_list.append('  Mountain')
        if selected_city.mine:
            side_values_list.append('  Mine')

        for x in range(len(side_values_list)):
            if type(side_values_list[x]) is not str:
                side_values_list[x] = str(side_values_list[x])
        self.side_view_value_model.setStringList(side_values_list)

    def set_building_side_view(self, building_id):
        side_values_list = ['ID: {0}'.format(building_id)]
        selected_building = self.get_buildings_from_db('id', building_id)
        selected_building = selected_building[0]

        side_values_list.append(selected_building.name)
        side_values_list.append('{0}'.format(selected_building.kind.name))

        for x in range(len(side_values_list)):
            if type(side_values_list[x]) is not str:
                side_values_list[x] = str(side_values_list[x])
        self.side_view_value_model.setStringList(side_values_list)

    def set_character_side_view(self, character_id):
        side_values_list = ['ID: {0}'.format(character_id)]
        selected_character = self.get_characters_from_db('id', character_id)
        selected_character = selected_character[0]

        side_values_list.append('{0} {1}'.format(selected_character.name, selected_character.fname))
        side_values_list.append('{0} {1}'.format(selected_character.gender, selected_character.race))
        side_values_list.append('Age: {0}'.format(selected_character.age))
        side_values_list.append('Profession: {0}'.format(selected_character.profession))
        side_values_list.append('Wealth: {0}'.format(selected_character.wealth))
        side_values_list.append('Role: {0}'.format(selected_character.role))
        side_values_list.append('Level {0} {1}'.format(selected_character.level, selected_character.classe))

        for x in range(len(side_values_list)):
            if type(side_values_list[x]) is not str:
                side_values_list[x] = str(side_values_list[x])
        self.side_view_value_model.setStringList(side_values_list)

    # Set main table model
    def set_building_table(self, city_id):
        self.table_content_model.setEditStrategy(models.SqlTableModel.OnFieldChange)
        self.table_content_model.setTable('buildings')
        self.set_view_table_header('buildings')
        self.table_content_model.setFilter('city_id = {0}'.format(city_id))
        self.table_content_model.setRelation(3, QtSql.QSqlRelation('cities', 'id', 'name'))
        self.table_content_model.select()
        self.tableViewContent.resizeColumnsToContents()

    def set_character_table(self, building_id):
        self.table_content_model.setEditStrategy(models.SqlTableModel.OnFieldChange)
        self.table_content_model.setTable('characters')
        self.set_view_table_header('characters')
        self.table_content_model.setFilter('building_id = {0}'.format(building_id))
        self.table_content_model.setRelation(12, QtSql.QSqlRelation('cities', 'id', 'name'))
        self.table_content_model.setRelation(13, QtSql.QSqlRelation('buildings', 'id', 'name'))
        self.table_content_model.select()
        self.tableViewContent.resizeColumnsToContents()

    def set_full_city_table(self):
        self.table_content_model.setEditStrategy(models.SqlTableModel.OnFieldChange)
        self.table_content_model.setTable('cities')
        self.set_view_table_header('cities')
        self.table_content_model.select()
        self.tableViewContent.resizeColumnsToContents()

    def set_full_building_table(self):
        self.table_content_model.setEditStrategy(models.SqlTableModel.OnFieldChange)
        self.table_content_model.setTable('buildings')
        self.set_view_table_header('buildings')
        self.table_content_model.setRelation(4, QtSql.QSqlRelation('cities', 'id', 'name'))
        self.table_content_model.select()
        self.tableViewContent.resizeColumnsToContents()

    def set_full_character_table(self):
        self.table_content_model.setEditStrategy(models.SqlTableModel.OnFieldChange)
        self.table_content_model.setTable('characters')
        self.set_view_table_header('characters')
        self.table_content_model.select()
        self.tableViewContent.resizeColumnsToContents()

    def set_view_table_header(self, table):
        if table == 'cities':
            self.table_content_model.setHeaderData(0, QtCore.Qt.Horizontal, 'ID')
            self.table_content_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Name')
            self.table_content_model.setHeaderData(2, QtCore.Qt.Horizontal, 'Culture')
            self.table_content_model.setHeaderData(3, QtCore.Qt.Horizontal, 'Size')
            self.table_content_model.setHeaderData(4, QtCore.Qt.Horizontal, 'Population')
            self.table_content_model.setHeaderData(5, QtCore.Qt.Horizontal, 'Forest')
            self.table_content_model.setHeaderData(6, QtCore.Qt.Horizontal, 'Plain')
            self.table_content_model.setHeaderData(7, QtCore.Qt.Horizontal, 'River')
            self.table_content_model.setHeaderData(8, QtCore.Qt.Horizontal, 'Sea')
            self.table_content_model.setHeaderData(9, QtCore.Qt.Horizontal, 'Mountain')
            self.table_content_model.setHeaderData(10, QtCore.Qt.Horizontal, 'Mine')
            self.table_content_model.setHeaderData(11, QtCore.Qt.Horizontal, 'Note')
        elif table == 'buildings':
            self.table_content_model.setHeaderData(0, QtCore.Qt.Horizontal, 'ID')
            self.table_content_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Name')
            self.table_content_model.setHeaderData(2, QtCore.Qt.Horizontal, 'Kind')
            self.table_content_model.setHeaderData(3, QtCore.Qt.Horizontal, 'City')
            self.table_content_model.setHeaderData(4, QtCore.Qt.Horizontal, 'Note')
        elif table == 'characters':
            self.table_content_model.setHeaderData(0, QtCore.Qt.Horizontal, 'ID')
            self.table_content_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Name')
            self.table_content_model.setHeaderData(2, QtCore.Qt.Horizontal, 'Culture')
            self.table_content_model.setHeaderData(3, QtCore.Qt.Horizontal, 'Race')
            self.table_content_model.setHeaderData(4, QtCore.Qt.Horizontal, 'Gender')
            self.table_content_model.setHeaderData(5, QtCore.Qt.Horizontal, 'Age')
            self.table_content_model.setHeaderData(6, QtCore.Qt.Horizontal, 'Social Group')
            self.table_content_model.setHeaderData(7, QtCore.Qt.Horizontal, 'Profession')
            self.table_content_model.setHeaderData(8, QtCore.Qt.Horizontal, 'Wealth')
            self.table_content_model.setHeaderData(9, QtCore.Qt.Horizontal, 'Attributes')
            self.table_content_model.setHeaderData(10, QtCore.Qt.Horizontal, 'Morality')
            self.table_content_model.setHeaderData(11, QtCore.Qt.Horizontal, 'Family Role')
            self.table_content_model.setHeaderData(12, QtCore.Qt.Horizontal, 'Groups')
            self.table_content_model.setHeaderData(13, QtCore.Qt.Horizontal, 'Family')
            self.table_content_model.setHeaderData(14, QtCore.Qt.Horizontal, 'Spouse Family')
            self.table_content_model.setHeaderData(15, QtCore.Qt.Horizontal, 'Note')

    # Set special table model
    def show_selected_family(self):

        selected_character = self.get_characters_from_db('id', self.get_selected_character_id())
        selected_character = selected_character[0]
        selected_family_id = selected_character.family_id

        self.table_special_model.setEditStrategy(models.SqlTableModel.OnFieldChange)
        self.table_special_model.setTable('characters')
        self.set_special_table_header()
        self.table_special_model.setFilter('family_id = {0}'.format(selected_family_id))  # Parent
        self.table_special_model.setRelation(13, QtSql.QSqlRelation('cities', 'id', 'name'))
        self.table_special_model.setRelation(14, QtSql.QSqlRelation('buildings', 'id', 'name'))
        self.table_special_model.select()

        self.tableViewSpecial.resizeColumnsToContents()

    def show_visitor(self):

        selected_building_id = self.get_selected_building_id()
        selected_city_id = self.get_selected_city_id()

        try:
            manager = visitor_manager.Visitor_manager(selected_building_id, selected_city_id, self.comboBoxVisitor.currentText(), self.lineEditVisitor.text(), loader)
            manager.add_visitor()
        except:
            return

        self.table_special_model.setEditStrategy(models.SqlTableModel.OnFieldChange)
        self.table_special_model.setTable('characters')
        self.set_special_table_header()
        self.table_special_model.setFilter('visiting_id = {0}'.format(selected_building_id))
        self.table_special_model.setRelation(13, QtSql.QSqlRelation('cities', 'id', 'name'))
        self.table_special_model.setRelation(14, QtSql.QSqlRelation('buildings', 'id', 'name'))
        self.table_special_model.select()

        self.tableViewSpecial.resizeColumnsToContents()

    def set_special_table_header(self):
        self.table_content_model.setHeaderData(0, QtCore.Qt.Horizontal, 'ID')
        self.table_content_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Name')
        self.table_content_model.setHeaderData(2, QtCore.Qt.Horizontal, 'Family')
        self.table_content_model.setHeaderData(3, QtCore.Qt.Horizontal, 'Culture')
        self.table_content_model.setHeaderData(4, QtCore.Qt.Horizontal, 'Race')
        self.table_content_model.setHeaderData(5, QtCore.Qt.Horizontal, 'Gender')
        self.table_content_model.setHeaderData(6, QtCore.Qt.Horizontal, 'Age')
        self.table_content_model.setHeaderData(7, QtCore.Qt.Horizontal, 'Social Group')
        self.table_content_model.setHeaderData(8, QtCore.Qt.Horizontal, 'Profession')
        self.table_content_model.setHeaderData(9, QtCore.Qt.Horizontal, 'Wealth')
        self.table_content_model.setHeaderData(10, QtCore.Qt.Horizontal, 'Attributes')
        self.table_content_model.setHeaderData(11, QtCore.Qt.Horizontal, 'Morality')
        self.table_content_model.setHeaderData(12, QtCore.Qt.Horizontal, 'Family')
        self.table_content_model.setHeaderData(13, QtCore.Qt.Horizontal, 'City')
        self.table_content_model.setHeaderData(14, QtCore.Qt.Horizontal, 'Building')
        self.table_content_model.setHeaderData(15, QtCore.Qt.Horizontal, 'Visiting')
        self.table_content_model.setHeaderData(16, QtCore.Qt.Horizontal, 'Note')
        self.tableViewSpecial.resizeColumnsToContents()

    # Query items from DB
    @staticmethod
    def get_cities_from_db(filter_by, filter_value):
        connector = db_connector.Db_Connector(base.City)
        result = connector.load_from_db(filter_by, filter_value)
        connector.close_session()
        return result

    @staticmethod
    def get_buildings_from_db(filter_by, filter_value):
        connector = db_connector.Db_Connector(base.Building)
        result = connector.load_from_db(filter_by, filter_value)
        connector.close_session()
        return result

    @staticmethod
    def get_characters_from_db(filter_by, filter_value):
        connector = db_connector.Db_Connector(base.Character)
        result = connector.load_from_db(filter_by, filter_value)
        connector.close_session()
        return result


# View query methods ---------------------------------------------------------------End

# View open dialogs methods --------------------------------------------------------Begin

    def new_file_dialog(self, name, starting_dir):
        file_name = QtWidgets.QFileDialog.getSaveFileName(self, name, starting_dir)
        return file_name

    def open_file_dialog(self, name, starting_dir):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, name, starting_dir)
        return file_name

    def open_add_city_dialog(self):
        self.add_dialog = add_dialogs.add_city_dialog(self)
        self.add_dialog.show()

    def open_add_building_dialog(self):
        self.add_dialog = add_dialogs.add_building_dialog(self)
        self.add_dialog.show()

    def open_add_group_dialog(self):
        self.add_dialog = add_dialogs.add_group_dialog(self)
        self.add_dialog.show()

    def open_add_character_dialog(self):
        group_id = self.get_selected_id()
        group_connector = db_connector.Db_Connector(base.Group)
        in_group = group_connector.load_from_db('id', group_id)
        in_group = in_group[0]
        group_connector.close_session()

        self.add_dialog = add_dialogs.add_character_dialog(self, in_group)
        self.add_dialog.show()

    def open_delete_dialog(self, table):
        self.delete_dialog = delete_dialogs.delete_dialog(self, table)
        self.delete_dialog.show()

# View open dialogs methods --------------------------------------------------------End

# Add entry from popup methods -----------------------------------------------------Begin

    def add_city(self, city_dict):
        new_city = city.City()
        new_city.set_from_dialog(city_dict)

        connector = db_connector.Db_Connector(base.City)
        new_city_id = connector.write_to_db(new_city)
        connector.close_session()

        self.build_tree_model()

    def add_building(self, building_dict, auto_populate, in_city_id='selected'):
        if in_city_id == 'selected':
            city_id = self.get_selected_id()
        else:
            city_id = in_city_id

        new_building = building.Building()
        new_building.set_from_dialog(building_dict, city_id)

        connector = db_connector.Db_Connector(base.Building)
        new_building_id = connector.write_to_db(new_building)
        connector.close_session()

        # if auto_populate:
            # construction_info = catalogs_character.profession[new_building.kind][new_building.subkind]
            # new_populator = populator.Populator(new_building, new_building_id, city_id, loader)
            # new_populator.populate()

        self.build_tree_model()

    def add_group(self, group_dict, preset=False, preset_name=None, in_building_id='selected'):
        if in_building_id == 'selected':
            building_id = self.get_selected_id()
        else:
            building_id = in_building_id

        new_group = group.Group()
        if preset:
            new_group.set_from_catalog(preset_name, building_id)
            # Add auto populate (add_character method calls)
        else:
            new_group.set_from_dialog(group_dict, building_id)


        connector = db_connector.Db_Connector(base.Group)
        new_group_id = connector.write_to_db(new_group)
        connector.close_session()

        self.build_tree_model()

    def update_group(self, group_id, new_character_id):
        group_connector = db_connector.Db_Connector(base.Group)
        g = group_connector.load_from_db('id', group_id)
        g = g[0]
        g.add_character(new_character_id)

        group_connector.full_update(g, group_id)
        group_connector.close_session()

    def add_character(self, character_dict, in_group_id='selected'):
        if in_group_id == 'selected':
            group_id = self.get_selected_id()
        else:
            group_id = in_group_id

        new_character = character.Character()
        new_character.associate_group(group_id)
        new_character.build_character(character_dict)

        connector = db_connector.Db_Connector(base.Character)
        new_char_id = connector.write_to_db(new_character)
        connector.close_session()

        self.update_group(group_id, new_char_id)

        self.build_tree_model()

        return new_character

    def add_family(self, family_name):
        new_family = family.Family()
        new_family.set_name(family_name)

        connector = db_connector.Db_Connector(base.Family)
        family_id = connector.write_to_db(new_family)
        connector.close_session()

        return family_id

# Add entry from popup methods -----------------------------------------------------End

# Delete entry from popup methods ---------------------------------------------------Begin

    def delete_character(self, character_id='selected'):
        if character_id == 'selected':
            character_id = self.get_selected_id()

        connector = db_connector.Db_Connector(base.Character)
        connector.delete_entry(character_id)
        connector.close_session()

    def delete_group(self, group_id='selected'):
        if group_id == 'selected':
            group_id = self.get_selected_id()

        connector = db_connector.Db_Connector(base.Group)
        connector.delete_entry(group_id)
        connector.close_session()

    def delete_building(self, building_id='selected'):
        if building_id == 'selected':
            building_id = self.get_selected_id()

        group_connector = db_connector.Db_Connector(base.Group)
        groups = group_connector.load_from_db('building_id', building_id)
        group_connector.close_session()
        for deleted in groups:
            self.delete_group(deleted.id)

        connector = db_connector.Db_Connector(base.Building)
        connector.delete_entry(building_id)
        connector.close_session()

    def delete_city(self, city_id='selected'):
        if city_id == 'selected':
            city_id = self.get_selected_id()

        building_connector = db_connector.Db_Connector(base.Building)
        buildings = building_connector.load_from_db('city_id', city_id)
        building_connector.close_session()
        for deleted in buildings:
            self.delete_building(deleted.id)

        connector = db_connector.Db_Connector(base.City)
        connector.delete_entry(city_id)
        connector.close_session()

# Delete entry from popup methods -----------------------------------------------------End

# View Actions methods -------------------------------------------------------------Begin

    '''All action_ method are called by interaction in widgets'''
    def action_new_database(self):
        self.new_database()

    def action_load_database(self):
        self.load_database()

    def action_full_city(self):
        self.set_full_city_table()

    def action_full_building(self):
        self.set_full_building_table()

    def action_full_character(self):
        self.set_full_character_table()

    def action_city_click(self):
        selected_city_id = self.get_selected_city_id()
        self.set_building_table(selected_city_id)
        self.set_city_side_view(selected_city_id)

    def action_building_click(self):
        selected_building_id = self.get_selected_building_id()
        self.set_character_table(selected_building_id)
        self.set_building_side_view(selected_building_id)

    def action_character_click(self):
        selected_character_id = self.get_selected_character_id()
        self.set_character_side_view(selected_character_id)

    def add_city_click(self):
        self.open_add_city_dialog()

    def add_building_click(self):
        selected_index = self.treeView.selectionModel().currentIndex()
        selected_item = self.treeModel.itemFromIndex(selected_index)
        selected_table = selected_item.data(21)
        if selected_table == 'cities':
            self.open_add_building_dialog()
        else:
            print('Select a city to add a building to it')

    def add_group_click(self):
        selected_index = self.treeView.selectionModel().currentIndex()
        selected_item = self.treeModel.itemFromIndex(selected_index)
        selected_table = selected_item.data(21)
        if selected_table == 'buildings':
            self.open_add_group_dialog()
        else:
            print('Select a building to add a group to it')

    def add_character_click(self):
        selected_index = self.treeView.selectionModel().currentIndex()
        selected_item = self.treeModel.itemFromIndex(selected_index)
        selected_table = selected_item.data(21)
        if selected_table == 'groups':
            self.open_add_character_dialog()
        else:
            print('Select a group to add a character to it')

    def delete_click(self):
        selected_index = self.treeView.selectionModel().currentIndex()
        selected_item = self.treeModel.itemFromIndex(selected_index)
        self.open_delete_dialog(selected_item.data(21))

    def show_family_click(self):
        self.show_selected_family()

    def show_visitor_click(self):
        self.show_visitor()

# View Actions methods -------------------------------------------------------------End



def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()

    controller.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


