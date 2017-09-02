#-------------------------------------------------
#
# Project created by QtCreator 2017-01-04T17:13:43
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = ModularWorldUi
TEMPLATE = app

# The following define makes your compiler emit warnings if you use
# any feature of Qt which as been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0


SOURCES += main.cpp\
        mainwindow.cpp \
    map_view.cpp

HEADERS  += mainwindow.h \
    map_view.h

FORMS    += mainwindow.ui \
    add_city_dialog.ui \
    add_building_dialog.ui \
    add_char_dialog.ui \
    delete_dialog.ui \
    map_view.ui \
    mainwindow_dev.ui \
    add_group_dialog.ui \
    edit_city_dialog.ui

DISTFILES +=
