#ifndef MAP_VIEW_H
#define MAP_VIEW_H

#include <QMainWindow>

namespace Ui {
class map_view;
}

class map_view : public QMainWindow
{
    Q_OBJECT

public:
    explicit map_view(QWidget *parent = 0);
    ~map_view();

private:
    Ui::map_view *ui;
};

#endif // MAP_VIEW_H
