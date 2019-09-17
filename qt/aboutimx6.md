# support qtquick Virtual Keyboard
    apt install qml-module-qtquick2 qml-module-qtquick-window2


# rotate Mainwindow
    menu w;
    QGraphicsScene ww;
    ww.addWidget(&w);
    QGraphicsView www(&ww);
    www.rotate(-90);
    www.resize(800,480);
    www.setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
    www.setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
    www.show();
    w.setCursor(Qt::BlankCursor);
    w.show();