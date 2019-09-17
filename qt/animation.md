# transform example
    pshowcamera = new QPropertyAnimation(cv, "geometry");
    pshowcamera->setDuration(300);
    pshowcamera->setStartValue(QRect(SCREEN_HEIGHT,0,0,0));
    pshowcamera->setEndValue(QRect(SCREEN_HEIGHT-ui->camerawidget->size().height()-100
                                   ,100
                                   ,640
                                   ,480));
    phidecamera = new QPropertyAnimation(cv, "geometry");
    phidecamera->setDuration(300);
    phidecamera->setEndValue(QRect(SCREEN_HEIGHT,0,0,0));
    phidecamera->setStartValue(QRect(SCREEN_HEIGHT-ui->camerawidget->size().height()-100
                                     ,100
                                     ,640
                                     ,480));