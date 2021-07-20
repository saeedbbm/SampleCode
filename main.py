import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from ui_window import *
from Image_Processing_old import image_processor

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.upFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        print(self.upFolder)
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ImPr = image_processor()

        #UI_Camera
        self.ui.control_bt.clicked.connect(self.controlTimer)
        self.ui.camera_pic_btn.clicked.connect(lambda: self.ImPr.capturedPic(self.ui.InputPosition.text()))

        #UI_Table
        self.ui.btn_add.clicked.connect(self.ui.addRow)
        self.ui.btn_copy.clicked.connect(self.ui.copyRow)
        self.ui.btn_copy2.clicked.connect(self.ui.copyFunc)
        self.ui.btn_delete.clicked.connect(self.ui.deleteRow)
        #UI_Setting
        self.ui.SETsave.clicked.connect(self.ui.SETfunc)

        #UI_Camera
        self.Timer_Vid_recorder = QTimer()
        self.Timer_Vid_recorder.timeout.connect(self.ImPr.capturedVid_Start)

        # Other
        self.timer = QTimer()
        self.timer.timeout.connect(self.showResult)

    def showResult(self):

        my_flag1 = image_processor.checkOption(self.ImPr, self.ui.motion_check.isChecked(),self.ui.face_check.isChecked())
        if my_flag1:
            self.frame1 = self.ImPr.Result()
            self.frame1 = cv2.cvtColor(self.frame1, cv2.COLOR_BGR2RGB)
            height, width, channel = self.frame1.shape
            step = channel * width
            # create QImage from RGB frame
            qImg = QImage(self.frame1.data, width, height, step, QImage.Format_RGB888)
            qImg = qImg.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
            # show frame in img_label
            self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            self.ImPr.capture_frame()
            self.timer.start(20)
            self.ui.control_bt.setText("Stop")

        # if timer is started
        else:
            self.timer.stop()
            self.ImPr.cap.release()
            self.ui.control_bt.setText("Start")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())