from PyQt5 import uic


with open('mainwindow.py', mode='w') as pyfile:
    with open('mainwindow_dev.ui', mode='r') as uifile:
        uic.compileUi(uifile, pyfile)

with open('add_city_dialog.py', mode='w') as pyfile:
    with open('add_city_dialog.ui', mode='r') as uifile:
        uic.compileUi(uifile, pyfile)

with open('add_building_dialog.py', mode='w') as pyfile:
    with open('add_building_dialog.ui', mode='r') as uifile:
        uic.compileUi(uifile, pyfile)

with open('add_group_dialog.py', mode='w') as pyfile:
    with open('add_group_dialog.ui', mode='r') as uifile:
        uic.compileUi(uifile, pyfile)

with open('add_char_dialog.py', mode='w') as pyfile:
    with open('add_char_dialog.ui', mode='r') as uifile:
        uic.compileUi(uifile, pyfile)

with open('delete_dialog.py', mode='w') as pyfile:
    with open('delete_dialog.ui', mode='r') as uifile:
        uic.compileUi(uifile, pyfile)
