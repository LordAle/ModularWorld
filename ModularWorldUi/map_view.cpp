#include "map_view.h"
#include "ui_map_view.h"

map_view::map_view(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::map_view)
{
    ui->setupUi(this);
}

map_view::~map_view()
{
    delete ui;
}
