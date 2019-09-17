#include "camera.h"
#include "ui_camera.h"
camera::camera(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::camera)
{
    ui->setupUi(this);


    icamera = new QCamera("/dev/video0",this);

//    QCameraViewfinderSettingsControl cvfsc = icamera->load();

    cvf = new QCameraViewfinder(this);
    cvf->resize(640,480);
    cvf->show();

    icamera->setViewfinder(cvf);

    icamera->setCaptureMode(QCamera::CaptureMode::CaptureStillImage);

    icap = new QCameraImageCapture(icamera,this);


    icap->setCaptureDestination(QCameraImageCapture::CaptureToFile);
    icap->setBufferFormat(QVideoFrame::Format_Jpeg);

    icamera->start();








}

camera::~camera()
{
    delete ui;
}


void camera::on_pushButton_clicked()
{


//    QList<QVideoFrame::PixelFormat> aa = icamera->supportedViewfinderPixelFormats();
//    QList<QSize> bb = icamera->supportedViewfinderResolutions();

//    ui->textBrowser->setText(QString("supportFormats:%1\nsupportResolution:%2\n").arg(aa.size()).arg(bb.length()));

}

void camera::on_pushButton_2_clicked()
{
      QString text;
//    switch(icamera->state()){
//    case QCamera::State::ActiveState:
//        text = "ActiveState";
//        break;
//    case QCamera::State::LoadedState:
//        text = "LoadedState";
//        break;
//    case QCamera::State::UnloadedState:
//        text = "UnloadedState";
//        break;
//    }
//    ui->pushButton_2->setText(text);
//    text = "";
//    if(icamera->isAvailable())
//        text += "camera available!\n";
//    text += QString("support %1 settings\n").arg(icamera->supportedViewfinderSettings().size());
//    if(icamera->isCaptureModeSupported(QCamera::CaptureMode::CaptureVideo))
//        text += "support CaptureVideo\n";
//    if(icamera->isCaptureModeSupported(QCamera::CaptureMode::CaptureStillImage))
//        text += "support CaptureStillImage\n";
//    if(icamera->isCaptureModeSupported(QCamera::CaptureMode::CaptureViewfinder))
//        text += "support CaptureViewfinder\n";


    QList<QVideoFrame::PixelFormat> bb = icamera->supportedViewfinderPixelFormats();
    foreach (const QVideoFrame::PixelFormat bbb, bb) {
        text += QString("support format %1\n").arg(bbb);
    }
    QList<QCamera::FrameRateRange> aa = icamera->supportedViewfinderFrameRateRanges();
    foreach (const QCamera::FrameRateRange aaa, aa) {
        text += QString("support framerate %1 ~ %2\n").arg(aaa.minimumFrameRate).arg(aaa.maximumFrameRate);
    }
    QList<QSize> cc = icamera->supportedViewfinderResolutions();
    foreach (const QSize ccc, cc) {
        text += QString("support resolution %1x%2\n").arg(ccc.width()).arg(ccc.height());
    }

    text += QString("now status %1\n").arg(icamera->status());


    text += QString("error %1\n").arg(icamera->error());


    QCameraViewfinderSettings isettings = icamera->viewfinderSettings();
    isettings.setResolution(640,480);
    isettings.setMinimumFrameRate(30.0);
    isettings.setMaximumFrameRate(30.0);
    isettings.setPixelFormat(QVideoFrame::Format_BGR32);
    icamera->setViewfinderSettings(isettings);

    ui->textBrowser->setText(text);
//    icap->capture("/home/th/test");

}
