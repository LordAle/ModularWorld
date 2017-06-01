import sys
from PyQt5 import QtCore, QtWidgets, QtSql
import add_dialogs
import building
import character
import city
import db_connector
import db_loader
import delete_dialogs
import family
import models
import populator
import visitor_manager
from ModularWorldUi.mainwindow import Ui_MainWindow
from catalogs import catalog_character


class Controller(QtWidgets.QMainWindow, Ui_MainWindow):
    """Initialize main window, attribute models and define Actions method. Also keep sqlAlcehmy database interface alive"""

    def __init__(self, loader):
        super(self.__class__, self).__init__()
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.add_dialog = None
        self.delete_dialog = None

        self.loader = loader

        # Models triggers
        self.listViewCities.clicked.connect(self.action_city_click)
        self.listViewBuildings.clicked.connect(self.action_building_click)
        self.listViewCharacters.clicked.connect(self.action_character_click)

        # Buttons triggers
        self.pushButtonAddCity.clicked.connect(self.add_city_click)
        self.pushButtonAddBuilding.clicked.connect(self.add_building_click)
        self.pushButtonAddCharacter.clicked.connect(self.add_character_click)
        self.pushButtonDeleteCity.clicked.connect(self.delete_city_click)
        self.pushButtonDeleteBuilding.clicked.connect(self.delete_building_click)
        self.pushButtonDeleteCharacter.clicked.connect(self.delete_character_click)

        self.pushButtonShowFamily.clicked.connect(self.show_family_click)
        self.pushButtonVisitor.clicked.connect(self.show_visitor_click)

        self.actionNewDatabase.triggered.connect(self.action_new_database)
        self.actionLoadDatabase.triggered.connect(self.action_load_database)

        self.actionCity_table.triggered.connect(self.action_full_city)
        self.actionBuilding_table.triggered.connect(self.action_full_building)
        self.actionCharacter_table.triggered.connect(self.action_full_character)

        # Other variable
        self.side_values_list = []

    def new_database(self):
        dbname = self.new_file_dialog('New database', 'C:\\Users\LordAle\PycharmProjects\ModularWorld\database')
        if dbname[0]:
            self.loader.create_new(dbname[0])
            self.open_QConnection(dbname[0])
            self.setup_new_db()

    def load_database(self):
        dbname = self.open_file_dialog('Open database', 'C:\\Users\LordAle\PycharmProjects\ModularWorld\database')
        if dbname[0]:
            self.loader.create_new(dbname[0])
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
        self.query_cities_name()

    def set_models(self):

        #Assign models
        self.cities_list_model = models.SqlQueryModel()
        self.listViewCities.setModel(self.cities_list_model)
        self.buildings_list_model = models.SqlQueryModel()
        self.listViewBuildings.setModel(self.buildings_list_model)
        self.characters_list_model = models.SqlQueryModel()
        self.listViewCharacters.setModel(self.characters_list_model)

        self.table_content_model = models.SqlRelationalModel(db=self.QConnection)
        self.tableViewContent.setModel(self.table_content_model)
        self.tableViewContent.setItemDelegate(QtSql.QSqlRelationalDelegate(self.tableViewContent))

        self.table_special_model = models.SqlRelationalModel(db=self.QConnection)
        self.tableViewSpecial.setModel(self.table_special_model)
        self.tableViewSpecial.setItemDelegate(QtSql.QSqlRelationalDelegate(self.tableViewSpecial))

        self.side_view_value_model = models.StringListModel()
        self.listViewSelectedValue.setModel(self.side_view_value_model)

        self.wealth_model = models.StringListModel()
        self.wealth_model.setStringList(catalog_character.wealth)
        self.comboBoxVisitor.setModel(self.wealth_model)

    def setup_new_db(self):
        self.add_traveller_city()
        self.query_cities_name()


# View query methods ---------------------------------------------------------------Begin

    #Selected object ID

    def get_selected_city_id(self):
        city_index = self.listViewCities.currentIndex()
        city_record = self.cities_list_model.record(city_index.row())
        city_id = city_record.field(1).value()
        return city_id

    def get_selected_building_id(self):
        building_index = self.listViewBuildings.currentIndex()
        building_record = self.buildings_list_model.record(building_index.row())
        building_id = building_record.field(1).value()
        return building_id

    def get_selected_character_id(self):
        character_index = self.listViewCharacters.currentIndex()
        character_record = self.characters_list_model.record(character_index.row())
        character_id = character_record.field(1).value()
        return character_id

    #Set correct list for city / building / character

    def query_cities_name(self):
        self.cities_list_model.clear()
        query = QtSql.QSqlQuery("SELECT name, id FROM cities")
        self.cities_list_model.setQuery(query)

    def query_buildings_name(self, city_id):
        self.buildings_list_model.clear()
        query = QtSql.QSqlQuery("SELECT name, id FROM buildings WHERE city_id = {0}".format(city_id))
        self.buildings_list_model.setQuery(query)

    def query_characters_name(self, building_id):
        self.characters_list_model.clear()
        query = QtSql.QSqlQuery("SELECT name, id FROM characters WHERE building_id = {0}".format(building_id))
        self.characters_list_model.setQuery(query)

    #Side view

    def set_city_side_view(self, city_id):
        self.side_values_list = ['ID: {0}'.format(city_id)]
        selected_city = self.get_cities_from_db('id', city_id)
        selected_city = selected_city[0]

        self.side_values_list.append('{0} ({1}) of {2}'.format(selected_city.kind.name, selected_city.size.name, selected_city.name))
        self.side_values_list.append('Population of {0}'.format(selected_city.population))
        self.side_values_list.append('Dominant culture is {0}'.format(selected_city.culture.name))
        self.side_values_list.append('Geographical features are :')
        if selected_city.plain:
            self.side_values_list.append('  Plain')
        if selected_city.forest:
            self.side_values_list.append('  Forest')
        if selected_city.river:
            self.side_values_list.append('  River')
        if selected_city.sea:
            self.side_values_list.append('  Sea')
        if selected_city.mountain:
            self.side_values_list.append('  Mountain')
        if selected_city.mine:
            self.side_values_list.append('  Mine')

        for x in range(len(self.side_values_list)):
            if type(self.side_values_list[x]) is not str:
                self.side_values_list[x] = str(self.side_values_list[x])
        self.side_view_value_model.setStringList(self.side_values_list)

    def set_building_side_view(self, building_id):
        self.side_values_list = ['ID: {0}'.format(building_id)]
        selected_building = self.get_buildings_from_db('id', building_id)
        selected_building = selected_building[0]

        self.side_values_list.append(selected_building.name)
        self.side_values_list.append('{0} {1}'.format(selected_building.subkind, selected_building.kind))

        for x in range(len(self.side_values_list)):
            if type(self.side_values_list[x]) is not str:
                self.side_values_list[x] = str(self.side_values_list[x])
        self.side_view_value_model.setStringList(self.side_values_list)

    def set_character_side_view(self, character_id):
        self.side_values_list = ['ID: {0}'.format(character_id)]
        selected_character = self.get_characters_from_db('id', character_id)
        selected_character = selected_character[0]

        self.side_values_list.append('{0} {1}'.format(selected_character.name, selected_character.fname))
        self.side_values_list.append('{0} {1}'.format(selected_character.gender, selected_character.race))
        self.side_values_list.append('Age: {0}'.format(selected_character.age))
        self.side_values_list.append('Profession: {0}'.format(selected_character.profession))
        self.side_values_list.append('Wealth: {0}'.format(selected_character.wealth))
        self.side_values_list.append('Role: {0}'.format(selected_character.role))
        self.side_values_list.append('Level {0} {1}'.format(selected_character.level, selected_character.classe))

        for x in range(len(self.side_values_list)):
            if type(self.side_values_list[x]) is not str:
                self.side_values_list[x] = str(self.side_values_list[x])
        self.side_view_value_model.setStringList(self.side_values_list)

    # Set main table model

    def set_building_table(self, city_id):
        self.table_content_model.setEditStrategy(models.SqlTableModel.OnFieldChange)
        self.table_content_model.setTable('buildings')
        self.set_view_table_header('buildings')
        self.table_content_model.setFilter('city_id = {0}'.format(city_id))
        self.table_content_model.setRelation(4, QtSql.QSqlRelation('cities', 'id', 'name'))
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
        self.table_content_model.setRelation(12, QtSql.QSqlRelation('cities', 'id', 'name'))
        self.table_content_model.setRelation(13, QtSql.QSqlRelation('buildings', 'id', 'name'))
        self.table_content_model.select()
        self.tableViewContent.resizeColumnsToContents()

    def set_view_table_header(self, table):
        if table == 'cities':
            self.table_content_model.setHeaderData(0, QtCore.Qt.Horizontal, 'ID')
            self.table_content_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Name')
            self.table_content_model.setHeaderData(2, QtCore.Qt.Horizontal, 'Kind')
            self.table_content_model.setHeaderData(3, QtCore.Qt.Horizontal, 'Population')
            self.table_content_model.setHeaderData(4, QtCore.Qt.Horizontal, 'Main race')
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
            self.table_content_model.setHeaderData(3, QtCore.Qt.Horizontal, 'Subkind')
            self.table_content_model.setHeaderData(4, QtCore.Qt.Horizontal, 'City')
            self.table_content_model.setHeaderData(5, QtCore.Qt.Horizontal, 'Note')
        elif table == 'characters':
            self.table_content_model.setHeaderData(0, QtCore.Qt.Horizontal, 'ID')
            self.table_content_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Name')
            self.table_content_model.setHeaderData(2, QtCore.Qt.Horizontal, 'Family')
            self.table_content_model.setHeaderData(3, QtCore.Qt.Horizontal, 'Race')
            self.table_content_model.setHeaderData(4, QtCore.Qt.Horizontal, 'Gender')
            self.table_content_model.setHeaderData(5, QtCore.Qt.Horizontal, 'Age')
            self.table_content_model.setHeaderData(6, QtCore.Qt.Horizontal, 'Role')
            self.table_content_model.setHeaderData(7, QtCore.Qt.Horizontal, 'Profession')
            self.table_content_model.setHeaderData(8, QtCore.Qt.Horizontal, 'Wealth')
            self.table_content_model.setHeaderData(9, QtCore.Qt.Horizontal, 'Class')
            self.table_content_model.setHeaderData(10, QtCore.Qt.Horizontal, 'Level')
            self.table_content_model.setHeaderData(11, QtCore.Qt.Horizontal, 'Family')
            self.table_content_model.setHeaderData(12, QtCore.Qt.Horizontal, 'City')
            self.table_content_model.setHeaderData(13, QtCore.Qt.Horizontal, 'Building')
            self.table_content_model.setHeaderData(14, QtCore.Qt.Horizontal, 'Visiting')
            self.table_content_model.setHeaderData(15, QtCore.Qt.Horizontal, 'Note')


    #Set special table model

    def show_selected_family(self):

        selected_character = self.get_characters_from_db('id', self.get_selected_character_id())
        selected_character = selected_character[0]
        selected_family_id = selected_character.family_id

        self.table_special_model.setEditStrategy(models.SqlTableModel.OnFieldChange)
        self.table_special_model.setTable('characters')
        self.set_special_table_header()
        self.table_special_model.setFilter('family_id = {0}'.format(selected_family_id))  # Parent
        self.table_special_model.setRelation(12, QtSql.QSqlRelation('cities', 'id', 'name'))
        self.table_special_model.setRelation(13, QtSql.QSqlRelation('buildings', 'id', 'name'))
        self.table_special_model.select()

        self.tableViewSpecial.resizeColumnsToContents()

    def show_visitor(self):

        selected_building_id = self.get_selected_building_id()
        selected_city_id = self.get_selected_city_id()

        try:
            manager = visitor_manager.Visitor_manager(selected_building_id, selected_city_id, self.comboBoxVisitor.currentText(), self.lineEditVisitor.text(), self.loader)
            manager.add_visitor()
        except:
            return

        self.table_special_model.setEditStrategy(models.SqlTableModel.OnFieldChange)
        self.table_special_model.setTable('characters')
        self.set_special_table_header()
        self.table_special_model.setFilter('visiting_id = {0}'.format(selected_building_id))
        self.table_special_model.setRelation(12, QtSql.QSqlRelation('cities', 'id', 'name'))
        self.table_special_model.setRelation(13, QtSql.QSqlRelation('buildings', 'id', 'name'))
        self.table_special_model.select()

        self.tableViewSpecial.resizeColumnsToContents()

    def set_special_table_header(self):
        self.table_special_model.setHeaderData(0, QtCore.Qt.Horizontal, 'ID')
        self.table_special_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Name')
        self.table_special_model.setHeaderData(2, QtCore.Qt.Horizontal, 'Family')
        self.table_special_model.setHeaderData(3, QtCore.Qt.Horizontal, 'Race')
        self.table_special_model.setHeaderData(4, QtCore.Qt.Horizontal, 'Gender')
        self.table_special_model.setHeaderData(5, QtCore.Qt.Horizontal, 'Age')
        self.table_special_model.setHeaderData(6, QtCore.Qt.Horizontal, 'Role')
        self.table_special_model.setHeaderData(7, QtCore.Qt.Horizontal, 'Profession')
        self.table_special_model.setHeaderData(8, QtCore.Qt.Horizontal, 'Wealth')
        self.table_special_model.setHeaderData(9, QtCore.Qt.Horizontal, 'Class')
        self.table_special_model.setHeaderData(10, QtCore.Qt.Horizontal, 'Level')
        self.table_special_model.setHeaderData(11, QtCore.Qt.Horizontal, 'Family')
        self.table_special_model.setHeaderData(12, QtCore.Qt.Horizontal, 'City')
        self.table_special_model.setHeaderData(13, QtCore.Qt.Horizontal, 'Building')
        self.table_special_model.setHeaderData(14, QtCore.Qt.Horizontal, 'Visiting')
        self.table_special_model.setHeaderData(15, QtCore.Qt.Horizontal, 'Note')
        self.tableViewSpecial.resizeColumnsToContents()

    #Qury items from DB

    def get_cities_from_db(self, filter_by, filter_value):
        connector = db_connector.City_Connector(self.loader)
        result = connector.load_from_db(filter_by, filter_value)
        connector.close_session()
        return result

    def get_buildings_from_db(self, filter_by, filter_value):
        connector = db_connector.Building_Connector(self.loader)
        result = connector.load_from_db(filter_by, filter_value)
        connector.close_session()
        return result

    def get_characters_from_db(self, filter_by, filter_value):
        connector = db_connector.Character_Connector(self.loader)
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

    def open_add_character_dialog(self):
        self.add_dialog = add_dialogs.add_character_dialog(self)
        self.add_dialog.show()

    def open_delete_city_dialog(self):
        self.delete_dialog = delete_dialogs.delete_dialog(self, 'cities', 'city')
        self.delete_dialog.show()

    def open_delete_building_dialog(self):
        self.delete_dialog = delete_dialogs.delete_dialog(self, 'buildings', 'building')
        self.delete_dialog.show()

    def open_delete_character_dialog(self):
        self.delete_dialog = delete_dialogs.delete_dialog(self, 'characters', 'character')
        self.delete_dialog.show()


# View open dialogs methods --------------------------------------------------------End

# Add entry from popup methods -----------------------------------------------------Begin

    def add_city(self, city_dict):
        new_city = city.City()
        new_city.set_from_dialog(city_dict)

        connector = db_connector.City_Connector(self.loader)
        new_city_id = connector.write_to_db(new_city)
        connector.close_session()

        self.add_floating_building(new_city_id)

        self.query_cities_name()

    def add_building(self, building_dict, auto_populate, core_character=None,  in_city_id='selected'):
        if in_city_id == 'selected':
            city_id = self.get_selected_city_id()
        else:
            city_id = in_city_id

        in_city = self.get_cities_from_db('id', city_id)
        in_city = in_city[0]

        new_building = building.Building(in_city)
        try:
            new_building.set_from_dialog(building_dict)
        except:
            raise Exception
        new_building.set_city_id(city_id)

        connector = db_connector.Building_Connector(self.loader)
        new_building_id = connector.write_to_db(new_building)
        connector.close_session()

        if auto_populate:
            # construction_info = catalogs_character.profession[new_building.kind][new_building.subkind]
            new_populator = populator.Populator(core_character, new_building, new_building_id, in_city, city_id,
                                                self.loader)
            new_populator.populate()

        self.query_buildings_name(city_id)

    def add_character(self, character_dict, building_id='selected', city_id='selected'):
        if city_id == 'selected':
            city_id = self.get_selected_city_id()

        if building_id == 'selected':
            building_id = self.get_selected_building_id()

        in_city = self.get_cities_from_db('id', city_id)
        in_city = in_city[0]
        in_building = self.get_buildings_from_db('id', building_id)
        in_building = in_building[0]

        core_character = self.get_core_character(building_id)

        new_character = character.Character(in_city=in_city, in_building=in_building, core=core_character)
        new_character.set_from_dialog(character_dict)
        new_character.set_building_id(building_id)
        new_character.set_city_id(city_id)

        if core_character and new_character.role == 'Child':
            new_character.set_family_id(core_character.family_id)
        else:
            family_id = self.add_family(new_character.fname)
            new_character.set_family_id(family_id)

        connector = db_connector.Character_Connector(self.loader)
        connector.write_to_db(new_character)
        connector.close_session()

        self.query_characters_name(building_id)

        return new_character

    def add_family(self, family_name):
        new_family = family.Family(family_name)

        connector = db_connector.Family_Connector(self.loader)
        family_id = connector.write_to_db(new_family)
        connector.close_session()

        return family_id

    def add_traveller_city(self):
        traveller_city = city.City()
        traveller_city.special_traveller()

        connector = db_connector.City_Connector(self.loader)
        traveller_city_id = connector.write_to_db(traveller_city)
        connector.close_session()

        self.add_floating_building(traveller_city_id)

    def add_floating_building(self, city_id):
        floating_building = building.Building()
        floating_building.special_floating(city_id)

        connector = db_connector.Building_Connector(self.loader)
        new_building_id = connector.write_to_db(floating_building)
        connector.close_session()

    def get_core_character(self, building_id):
        connector = db_connector.Character_Connector(self.loader)
        characters = connector.load_from_db('building_id', building_id)
        for character in characters:
            if character.role == 'Master':
                return character
        return None

# Add entry from popup methods -----------------------------------------------------End

# Delete entry from popup methods ---------------------------------------------------Begin

    def delete_character(self, character_id='selected'):
        if character_id == 'selected':
            character_id = self.get_selected_character_id()

        connector = db_connector.Character_Connector(self.loader)
        connector.delete_entry(character_id)
        connector.close_session()

        self.query_characters_name(self.get_selected_building_id())

    def delete_building(self, building_id='selected'):
        if building_id == 'selected':
            building_id = self.get_selected_building_id()

        char_connector = db_connector.Character_Connector(self.loader)
        characters = char_connector.load_from_db('building_id', building_id)
        char_connector.close_session()
        for deleted in characters:
            self.delete_character(deleted.id)

        connector = db_connector.Building_Connector(self.loader)
        connector.delete_entry(building_id)
        connector.close_session()

        self.query_buildings_name(self.get_selected_city_id())

    def delete_city(self, city_id='selected'):
        if city_id == 'selected':
            city_id = self.get_selected_city_id()

        building_connector = db_connector.Building_Connector(self.loader)
        buildings = building_connector.load_from_db('city_id', city_id)
        building_connector.close_session()
        for deleted in buildings:
            self.delete_building(deleted.id)

        connector = db_connector.City_Connector(self.loader)
        connector.delete_entry(city_id)
        connector.close_session()

        self.query_cities_name()

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
        self.query_buildings_name(selected_city_id)
        self.set_building_table(selected_city_id)
        self.set_city_side_view(selected_city_id)

    def action_building_click(self):
        selected_building_id = self.get_selected_building_id()
        self.query_characters_name(selected_building_id)
        self.set_character_table(selected_building_id)
        self.set_building_side_view(selected_building_id)

    def action_character_click(self):
        selected_character_id = self.get_selected_character_id()
        self.set_character_side_view(selected_character_id)

    def add_city_click(self):
        self.open_add_city_dialog()

    def add_building_click(self):
        self.open_add_building_dialog()

    def add_character_click(self):
        self.open_add_character_dialog()

    def delete_city_click(self):
        self.open_delete_city_dialog()

    def delete_building_click(self):
        self.open_delete_building_dialog()

    def delete_character_click(self):
        self.open_delete_character_dialog()

    def show_family_click(self):
        self.show_selected_family()

    def show_visitor_click(self):
        self.show_visitor()

# View Actions methods -------------------------------------------------------------End



def main():
    app = QtWidgets.QApplication(sys.argv)
    loader = db_loader.Db_Loader()
    controller = Controller(loader)

    controller.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


