
from PyQt5 import QtCore, QtWidgets
import numpy as np
import os
from model import DbModel
from comboCheck import CheckableComboBox
from Auto_Database import createConnection

class Ui_Form(object):
    def __init__(self):
        self.upFolder = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        self.dbModel = DbModel()

        self.old_user = 0
        self.AlarmPosition = -1
        self.AP_range = 1
        self.AlarmHeight = -0.25
        self.AH_range = 0.1
        self.AlarmAngle = -30
        self.AA_range = 30
        self.AlarmPicSignal = 0
        self.ID1 = 1000
        self.ID2 = 2000
        self.ID3 = 3000
        self.rowCount1 = 0
        self.rowCount2 = 0
        
    def setupUi(self, Form):

        self.SettingArray = np.loadtxt(self.upFolder+"/setting.txt", delimiter=',')
        createConnection(self.upFolder)
        self.dbModel = DbModel()

        self.layout = QtWidgets.QGridLayout(Form)
        Width = 1560
        Height = 860
        Form.setFixedWidth(Width)
        Form.setFixedHeight(Height)

        # Initialize tab screen
        self.tabs = QtWidgets.QTabWidget(Form)
        self.tab1 = QtWidgets.QWidget(Form)
        self.tab2 = QtWidgets.QWidget(Form)

        # Add tabs
        self.tabs.addTab(self.tab1, "Main")
        self.tabs.addTab(self.tab2, "Setting")

        # Create first tab
        VLayout_t1 = QtWidgets.QGridLayout()
        VLayout_t1.setVerticalSpacing(2)
        aLayout_t1 = QtWidgets.QHBoxLayout()
        bLayout_t1 = QtWidgets.QHBoxLayout()
        cLayout_t1 = QtWidgets.QHBoxLayout()

        VLayout_t1.addLayout(aLayout_t1,0,0)
        VLayout_t1.addLayout(bLayout_t1,1,0)
        VLayout_t1.addLayout(cLayout_t1,2,0)
        self.tab1.setLayout(VLayout_t1)

        frame11_t1=QtWidgets.QFrame()
        frame11_t1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        aLayout_t1.addWidget(frame11_t1,3)

        frame12_t1 = QtWidgets.QFrame()
        frame12_t1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        aLayout_t1.addWidget(frame12_t1,3)

        frame21_t1 = QtWidgets.QFrame()
        frame21_t1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        bLayout_t1.addWidget(frame21_t1,3)

        frame22_t1 = QtWidgets.QFrame()
        frame22_t1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        bLayout_t1.addWidget(frame22_t1,3)

        frame31_t1 = QtWidgets.QFrame()
        frame31_t1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        cLayout_t1.addWidget(frame31_t1,3)

        frame32_t1 = QtWidgets.QFrame()
        frame32_t1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        cLayout_t1.addWidget(frame32_t1,3)

        frame11_t1.setMinimumHeight(350)
        frame21_t1.setMaximumHeight(200)
        frame31_t1.setMaximumHeight(100)

        frame12_t1.setMinimumHeight(350)
        frame22_t1.setMaximumHeight(200)
        frame32_t1.setMaximumHeight(100)

        # Left Section
        layout_t1 = QtWidgets.QVBoxLayout()
        frame11_t1.setLayout(layout_t1)

        groupbox1_t1 = QtWidgets.QGroupBox("Camera")
        layout_t1.addWidget(groupbox1_t1,5)

        vbox_t1 = QtWidgets.QGridLayout()
        groupbox1_t1.setLayout(vbox_t1)

        self.control_bt = QtWidgets.QPushButton("Start")
        vbox_t1.addWidget(self.control_bt,0,0)

        self.motion_check = QtWidgets.QCheckBox("Motion Detection")
        vbox_t1.addWidget(self.motion_check,0,1)

        self.face_check = QtWidgets.QCheckBox("Face Detection")
        vbox_t1.addWidget(self.face_check,0,2)

        self.camera_pic_btn = QtWidgets.QPushButton("Take Picture")
        vbox_t1.addWidget(self.camera_pic_btn,0,3)

        self.camera_vid_btn = QtWidgets.QPushButton("Start Recording")
        vbox_t1.addWidget(self.camera_vid_btn,0,4)

        groupbox2_t1 = QtWidgets.QGroupBox("Live Camera")
        layout_t1.addWidget(groupbox2_t1, 95)

        vbox_t1 = QtWidgets.QVBoxLayout()
        groupbox2_t1.setLayout(vbox_t1)

        self.image_label = QtWidgets.QLabel()
        self.image_label.setStyleSheet("background-color: black; border: 1px solid black;")
        vbox_t1.addWidget(self.image_label)

        # Right Section
        layout2_t1 = QtWidgets.QVBoxLayout()
        frame12_t1.setLayout(layout2_t1)

        groupbox21_t1 = QtWidgets.QGroupBox("Thermal Camera")
        layout2_t1.addWidget(groupbox21_t1,10)

        vbox21_t1 = QtWidgets.QGridLayout()
        groupbox21_t1.setLayout(vbox21_t1)

        self.start_thermal_btn = QtWidgets.QPushButton("Start")
        vbox21_t1.addWidget(self.start_thermal_btn, 0, 0)

        self.thermal_pic_btn = QtWidgets.QPushButton("Take Picture")
        vbox21_t1.addWidget(self.thermal_pic_btn, 0, 3)

        self.thermal_vid_btn = QtWidgets.QPushButton("Start Recording")
        vbox21_t1.addWidget(self.thermal_vid_btn, 0, 4)

        groupbox22_t1 = QtWidgets.QGroupBox("Live Camera")
        layout2_t1.addWidget(groupbox22_t1, 90)

        vbox22_t1 = QtWidgets.QVBoxLayout()
        groupbox22_t1.setLayout(vbox22_t1)

        self.image_label2 = QtWidgets.QLabel()
        self.image_label2.setStyleSheet("background-color: black; border: 1px solid black;")
        vbox22_t1.addWidget(self.image_label2)

        # Frame 21
        layout21_t1 = QtWidgets.QGridLayout()
        frame21_t1.setLayout(layout21_t1)

        groupbox121 = QtWidgets.QGroupBox("Robot Movement")
        layout21_t1.addWidget(groupbox121,0,0)
        vbox121 = QtWidgets.QGridLayout()
        groupbox121.setLayout(vbox121)
        
        self.upbutton1 = QtWidgets.QPushButton("UP")
        vbox121.addWidget(self.upbutton1,0,1)
        
        self.stopbutton1 = QtWidgets.QPushButton("STOP")
        self.stopbutton1.setMaximumWidth(100)
        self.stopbutton1.setMaximumHeight(30)
        vbox121.addWidget(self.stopbutton1, 1, 1)

        self.downbutton1 = QtWidgets.QPushButton("DOWN")
        self.downbutton1.setMaximumWidth(100)
        self.downbutton1.setMaximumHeight(30)
        vbox121.addWidget(self.downbutton1,2,1)

        groupbox1211 = QtWidgets.QGroupBox()
        layout21_t1.addWidget(groupbox1211,1,0)

        layout21_t1.setVerticalSpacing(2)

        vbox1211 = QtWidgets.QGridLayout()
        groupbox1211.setLayout(vbox1211)

        self.homebutton1 = QtWidgets.QPushButton("HOME")
        self.homebutton1.setMaximumHeight(30)
        vbox1211.addWidget(self.homebutton1,0,0)
        vbox1211.setVerticalSpacing(2)
        groupbox1211.setMaximumHeight(50)

        groupbox120 = QtWidgets.QGroupBox("Speed")
        layout21_t1.addWidget(groupbox120, 0, 1)

        vbox120 = QtWidgets.QGridLayout()
        groupbox120.setLayout(vbox120)

        self.PositionSpeed_val = QtWidgets.QLineEdit()
        self.PositionSpeed_val.setPlaceholderText("Position")
        vbox120.addWidget(self.PositionSpeed_val, 0, 0)

        self.HeightSpeed_val = QtWidgets.QLineEdit()
        self.HeightSpeed_val.setPlaceholderText("Height")
        vbox120.addWidget(self.HeightSpeed_val, 1, 0)

        self.AngleSpeed_val = QtWidgets.QLineEdit()
        self.AngleSpeed_val.setPlaceholderText("Angle")
        vbox120.addWidget(self.AngleSpeed_val, 2, 0)

        groupbox12229 = QtWidgets.QGroupBox()
        layout21_t1.addWidget(groupbox12229, 1, 1)
        vbox12229 = QtWidgets.QGridLayout()
        groupbox12229.setLayout(vbox12229)
        self.changeSpeedbutton = QtWidgets.QPushButton("Change")
        self.changeSpeedbutton.setMaximumHeight(30)
        vbox12229.addWidget(self.changeSpeedbutton, 0, 0)

        groupbox122 = QtWidgets.QGroupBox("Camera Movement")
        layout21_t1.addWidget(groupbox122, 0, 2)

        vbox122 = QtWidgets.QGridLayout()
        groupbox122.setLayout(vbox122)

        self.upbutton2 = QtWidgets.QPushButton("UP")
        self.upbutton2.setGeometry(20, 15, 10, 100) 

        vbox122.addWidget(self.upbutton2, 0, 1)

        self.leftbutton2 = QtWidgets.QPushButton("LEFT")
        vbox122.addWidget(self.leftbutton2, 1, 0)
        
        self.stopbutton2 = QtWidgets.QPushButton("STOP")
        vbox122.addWidget(self.stopbutton2, 1, 1)

        self.rightbutton2 = QtWidgets.QPushButton("RIGHT")
        vbox122.addWidget(self.rightbutton2, 1, 2)

        self.downbutton2 = QtWidgets.QPushButton("DOWN")
        vbox122.addWidget(self.downbutton2, 2, 1)

        groupbox1222 = QtWidgets.QGroupBox()
        layout21_t1.addWidget(groupbox1222,1,2)

        vbox1222 = QtWidgets.QGridLayout()
        groupbox1222.setLayout(vbox1222)

        self.homebutton2 = QtWidgets.QPushButton("HOME")
        self.homebutton1.setMaximumHeight(30)
        vbox1222.addWidget(self.homebutton2,0,0)

        # Frame 22
        layout22_t1 = QtWidgets.QGridLayout()
        frame22_t1.setLayout(layout22_t1)
        
        groupbox22_t1 = QtWidgets.QGroupBox("Planing Table")
        layout22_t1.addWidget(groupbox22_t1)

        vbox22_t1 = QtWidgets.QGridLayout()
        vbox22_t1.setVerticalSpacing(2)
        groupbox22_t1.setLayout(vbox22_t1)
        vbox22_t1.setContentsMargins(2, 2, 2, 2)

        self.table = QtWidgets.QTableView()
        self.table.setModel(self.dbModel.modelAuto)
        self.table.setColumnHidden(0,True)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()

        self.table.setColumnWidth(0, 140)
        self.table.setColumnWidth(1, 140)
        self.table.setColumnWidth(2, 140)
        self.table.setColumnWidth(3, 140)
        self.table.setColumnWidth(4, 140)
        self.table.setColumnWidth(5, 140)
        self.table.setColumnWidth(6, 140)
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.dbModel.modelAuto.sort(4, QtCore.Qt.AscendingOrder)
        vbox22_t1.addWidget(self.table,0,0)

        # my_row
        groupbox23_t1 = QtWidgets.QGroupBox()
        vbox22_t1.addWidget(groupbox23_t1,1,0)

        vbox23_t1 = QtWidgets.QGridLayout()
        groupbox23_t1.setLayout(vbox23_t1)

        self.enterPic = QtWidgets.QCheckBox("Picture")
        vbox23_t1.addWidget(self.enterPic, 0, 0)
        self.enterPic.setMinimumHeight(20)
        self.enterPic.setMinimumWidth(140)

        self.enterVid = QtWidgets.QCheckBox("Video")
        vbox23_t1.addWidget(self.enterVid, 0, 1)
        self.enterVid.setMinimumHeight(20)
        self.enterVid.setMinimumWidth(140)

        self.enterProgram = QtWidgets.QComboBox()
        self.enterProgram.addItems(['Program 1', 'Program 2','Program 3', 'Program 4','Program 5', 'Program 6','Program 7', 'Program 8','Program 9'])
        vbox23_t1.addWidget(self.enterProgram,0,2)
        self.enterProgram.setMinimumHeight(20)
        self.enterProgram.setMinimumWidth(140)

        self.enterPosition = QtWidgets.QLineEdit()
        vbox23_t1.addWidget(self.enterPosition,0,3)
        self.enterPosition.setText('')
        self.enterPosition.setPlaceholderText("Position")
        self.enterPosition.setMinimumHeight(20)
        self.enterPosition.setMinimumWidth(140)

        self.enterHeight = QtWidgets.QLineEdit()
        vbox23_t1.addWidget(self.enterHeight,0,4)
        self.enterHeight.setText('')
        self.enterHeight.setPlaceholderText("Height")
        self.enterHeight.setMinimumHeight(20)
        self.enterHeight.setMinimumWidth(140)

        self.enterAngle = QtWidgets.QLineEdit()
        vbox23_t1.addWidget(self.enterAngle,0,5)
        self.enterAngle.setText('')
        self.enterAngle.setPlaceholderText("Angle")
        self.enterAngle.setMinimumHeight(20)
        self.enterAngle.setMinimumWidth(140)
        
        self.btn_go = QtWidgets.QPushButton("GO")
        vbox23_t1.addWidget(self.btn_go,1,2)

        self.btn_copy = QtWidgets.QPushButton("COPY")
        vbox23_t1.addWidget(self.btn_copy,1,3)

        self.btn_add = QtWidgets.QPushButton("ADD")
        vbox23_t1.addWidget(self.btn_add,1,4)

        self.btn_delete = QtWidgets.QPushButton("DELETE")
        vbox23_t1.addWidget(self.btn_delete,1,5)

        # Left 3
        layout31_t1 = QtWidgets.QGridLayout()
        frame31_t1.setLayout(layout31_t1)

        groupbox31_t1 = QtWidgets.QGroupBox("Sensor Data")
        layout31_t1.addWidget(groupbox31_t1,0,0)

        vbox31_t1 = QtWidgets.QGridLayout()
        groupbox31_t1.setLayout(vbox31_t1)

        self.spring_radio = QtWidgets.QRadioButton("Spring")
        vbox31_t1.addWidget(self.spring_radio, 0, 0)
        self.spring_radio.setMinimumHeight(20)

        self.summer_radio = QtWidgets.QRadioButton("Summer")
        vbox31_t1.addWidget(self.summer_radio, 0, 1)
        self.summer_radio.setMinimumHeight(20)

        self.fall_radio = QtWidgets.QRadioButton("Fall")
        vbox31_t1.addWidget(self.fall_radio, 1, 0)
        self.fall_radio.setMinimumHeight(20)

        self.winter_radio = QtWidgets.QRadioButton("Winter")
        vbox31_t1.addWidget(self.winter_radio, 1, 1)
        self.winter_radio.setMinimumHeight(20)

        self.spring_radio.setChecked(True)

        self.label_32_11 = QtWidgets.QLabel("O2")
        vbox31_t1.addWidget(self.label_32_11, 0, 2)
        self.label_32_11.setMinimumHeight(20)

        self.text_O2 = QtWidgets.QLineEdit()
        self.text_O2.setPlaceholderText("0")
        vbox31_t1.addWidget(self.text_O2, 0, 3)
        self.text_O2.setMaximumWidth(30)
        self.text_O2.setMinimumHeight(20)
        self.label_32_11.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        # 12
        self.label_32_12 = QtWidgets.QLabel("Co2")
        vbox31_t1.addWidget(self.label_32_12, 0, 4)
        self.label_32_12.setMinimumHeight(20)

        self.text_Co2 = QtWidgets.QLineEdit()
        self.text_Co2.setPlaceholderText("0")
        vbox31_t1.addWidget(self.text_Co2, 0, 5)
        self.text_Co2.setMaximumWidth(30)
        self.text_O2.setMinimumHeight(20)
        self.label_32_12.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        # 13
        self.label_32_13 = QtWidgets.QLabel("CH4")
        vbox31_t1.addWidget(self.label_32_13, 0, 6)
        self.label_32_13.setMinimumHeight(20)

        self.text_CH4 = QtWidgets.QLineEdit()
        self.text_CH4.setPlaceholderText("0")
        vbox31_t1.addWidget(self.text_CH4, 0, 7)
        self.text_CH4.setMaximumWidth(30)
        self.text_CH4.setMinimumHeight(20)
        self.label_32_13.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        # 14
        self.label_32_14 = QtWidgets.QLabel("Humidity")
        vbox31_t1.addWidget(self.label_32_14, 1, 2)
        self.label_32_14.setMinimumHeight(20)

        self.text_Humidity = QtWidgets.QLineEdit()
        self.text_Humidity.setPlaceholderText("0")
        vbox31_t1.addWidget(self.text_Humidity, 1, 3)
        self.text_Humidity.setMaximumWidth(30)
        self.text_Humidity.setMinimumHeight(20)
        self.label_32_14.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        # 15
        self.label_32_15 = QtWidgets.QLabel("Temperature")
        vbox31_t1.addWidget(self.label_32_15, 1, 4)
        self.label_32_15.setMinimumHeight(20)

        self.text_Temperature = QtWidgets.QLineEdit()
        self.text_Temperature.setPlaceholderText("0")
        vbox31_t1.addWidget(self.text_Temperature, 1, 5)
        self.text_Temperature.setMaximumWidth(30)
        self.text_Temperature.setMinimumHeight(20)
        self.label_32_15.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        # 21
        self.label_32_16 = QtWidgets.QLabel("Battery")
        vbox31_t1.addWidget(self.label_32_16, 1, 6)
        self.label_32_16.setMinimumHeight(20)

        self.text_Battery = QtWidgets.QLineEdit()
        self.text_Battery.setPlaceholderText("0")
        vbox31_t1.addWidget(self.text_Battery, 1, 7)
        self.text_Battery.setMaximumWidth(30)
        self.text_Battery.setMinimumHeight(20)
        self.label_32_16.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        # Right 3
        layout32_t1 = QtWidgets.QGridLayout()
        frame32_t1.setLayout(layout32_t1)

        groupbox32_t1 = QtWidgets.QGroupBox("Navigation")
        groupbox32_t1.setMaximumWidth(650)
        groupbox32_t1.setMaximumHeight(200)
        layout32_t1.addWidget(groupbox32_t1, 0, 0)

        vbox32_t1 = QtWidgets.QGridLayout()
        groupbox32_t1.setLayout(vbox32_t1)

        # 11
        self.InputPosition = QtWidgets.QLineEdit()
        vbox32_t1.addWidget(self.InputPosition, 0, 0)
        self.InputPosition.setText('')
        self.InputPosition.setPlaceholderText("Position")
        self.InputPosition.setMinimumHeight(20)

        self.InputHeight = QtWidgets.QLineEdit()
        vbox32_t1.addWidget(self.InputHeight, 0, 1)
        self.InputHeight.setText('')
        self.InputHeight.setPlaceholderText("Height")
        self.InputHeight.setMinimumHeight(20)

        self.InputAngle = QtWidgets.QLineEdit()
        vbox32_t1.addWidget(self.InputAngle, 0, 2)
        self.InputAngle.setText('')
        self.InputAngle.setPlaceholderText("Angle")
        self.InputAngle.setMinimumHeight(20)

        self.btn_copy2 = QtWidgets.QPushButton("COPY")
        vbox32_t1.addWidget(self.btn_copy2, 0, 3)
        self.btn_copy2.setMinimumHeight(20)

        self.Go_label_fake = QtWidgets.QLabel("")
        vbox32_t1.addWidget(self.Go_label_fake, 1, 0)

        self.Go_label = QtWidgets.QLabel("Select Programs:")
        vbox32_t1.addWidget(self.Go_label, 1, 1)
        self.Go_label.setMinimumHeight(20)

        comunes = ['Program 1', 'Program 2', 'Program 3', 'Program 4', 'Program 5', 'Program 6', 'Program 7', 'Program 8', 'Program 9']
        self.combo = CheckableComboBox()
        self.combo.addItems(comunes)
        vbox32_t1.addWidget(self.combo, 1, 2)
        self.combo.setMinimumHeight(20)

        self.btn_Automatic = QtWidgets.QPushButton("AUTO")
        vbox32_t1.addWidget(self.btn_Automatic, 1, 3)
        self.btn_Automatic.setMinimumHeight(20)

        # Create Second tab
        VLayout_t2 = QtWidgets.QVBoxLayout()
        aLayout_t2 = QtWidgets.QHBoxLayout()
        bLayout_t2 = QtWidgets.QHBoxLayout()
        VLayout_t2.addLayout(aLayout_t2,1)
        VLayout_t2.addLayout(bLayout_t2,5)
        self.tab2.setLayout(VLayout_t2)

        v1aLayout_t2 = QtWidgets.QVBoxLayout()
        v2aLayout_t2 = QtWidgets.QVBoxLayout()
        aLayout_t2.addLayout(v1aLayout_t2,1)
        aLayout_t2.addLayout(v2aLayout_t2,9)
        
        # frame top # tab 2
        frame10_t2 = QtWidgets.QFrame()
        frame10_t2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        v1aLayout_t2.addWidget(frame10_t2, 1)

        layout10_t2 = QtWidgets.QGridLayout()
        frame10_t2.setLayout(layout10_t2)
        groupbox10_t2 = QtWidgets.QGroupBox("Seasons")
        layout10_t2.addWidget(groupbox10_t2, 0, 0)
        vbox10_t2 = QtWidgets.QGridLayout()
        groupbox10_t2.setLayout(vbox10_t2)
        frame10_t2.setMaximumWidth(180)
        frame10_t2.setMaximumHeight(100)
        frame10_t2.setContentsMargins(1,1,1,1)
        groupbox10_t2.setContentsMargins(1,1,1,1)

        #11
        self.spring_radio_SET = QtWidgets.QRadioButton("Spring")
        vbox10_t2.addWidget(self.spring_radio_SET, 0, 0)

        self.summer_radio_SET = QtWidgets.QRadioButton("Summer")
        vbox10_t2.addWidget(self.summer_radio_SET, 0, 1)

        self.fall_radio_SET = QtWidgets.QRadioButton("Fall")
        vbox10_t2.addWidget(self.fall_radio_SET, 1, 0)

        self.winter_radio_SET = QtWidgets.QRadioButton("Winter")
        vbox10_t2.addWidget(self.winter_radio_SET, 1, 1)

        frame11_t2=QtWidgets.QFrame()
        frame11_t2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        v2aLayout_t2.addWidget(frame11_t2,1)

        layout11_t2 = QtWidgets.QGridLayout()
        frame11_t2.setLayout(layout11_t2)
        frame11_t2.setMaximumHeight(100)

        groupbox11_t2 = QtWidgets.QGroupBox("Setting")
        # size_2
        layout11_t2.addWidget(groupbox11_t2, 0, 0)

        vbox11_t2 = QtWidgets.QGridLayout()
        groupbox11_t2.setLayout(vbox11_t2)

        # 11
        label_11_1 = QtWidgets.QLabel("O2")
        vbox11_t2.addWidget(label_11_1,0,0)

        self.SETtext_O2 = QtWidgets.QLineEdit()
        vbox11_t2.addWidget(self.SETtext_O2, 0, 1)
        self.SETtext_O2.setMaximumWidth(60)
        label_11_1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        # 12
        label_11_2 = QtWidgets.QLabel("Co2")
        vbox11_t2.addWidget(label_11_2, 0, 2)

        self.SETtext_Co2 = QtWidgets.QLineEdit()
        vbox11_t2.addWidget(self.SETtext_Co2, 0, 3)
        self.SETtext_Co2.setMaximumWidth(60)
        label_11_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        # 13
        label_11_3 = QtWidgets.QLabel("CH4")
        vbox11_t2.addWidget(label_11_3, 0, 4)

        self.SETtext_CH4 = QtWidgets.QLineEdit()
        vbox11_t2.addWidget(self.SETtext_CH4, 0, 5)
        self.SETtext_CH4.setMaximumWidth(60)
        label_11_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        # 14
        label_11_4 = QtWidgets.QLabel("Humidity")
        vbox11_t2.addWidget(label_11_4, 0, 6)

        self.SETtext_Humidity = QtWidgets.QLineEdit()
        vbox11_t2.addWidget(self.SETtext_Humidity, 0, 7)
        self.SETtext_Humidity.setMaximumWidth(60)
        label_11_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        # 15
        label_11_5 = QtWidgets.QLabel("Temperature")
        vbox11_t2.addWidget(label_11_5, 0, 8)

        self.SETtext_Temperature = QtWidgets.QLineEdit()
        vbox11_t2.addWidget(self.SETtext_Temperature, 0, 9)
        self.SETtext_Temperature.setMaximumWidth(60)
        label_11_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        # 21
        label_11_6 = QtWidgets.QLabel("Battery")
        vbox11_t2.addWidget(label_11_6, 0, 10)

        self.SETtext_Battery = QtWidgets.QLineEdit()
        vbox11_t2.addWidget(self.SETtext_Battery, 0, 11)
        self.SETtext_Battery.setMaximumWidth(60)
        label_11_6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        
        # 22
        label_11_7 = QtWidgets.QLabel("   ")
        vbox11_t2.addWidget(label_11_7,0,12)
        label_11_7.setMaximumWidth(5)
        
        self.SETsave = QtWidgets.QPushButton("Save")
        vbox11_t2.addWidget(self.SETsave, 0, 13)

        # frame buttom
        frame21_t2=QtWidgets.QFrame()
        frame21_t2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        bLayout_t2.addWidget(frame21_t2,1)

        # Frame 22
        layout21_t2 = QtWidgets.QGridLayout()
        frame21_t2.setLayout(layout21_t2)

        groupbox21_t2 = QtWidgets.QGroupBox("Report")
        layout21_t2.addWidget(groupbox21_t2)

        vbox21_t2 = QtWidgets.QVBoxLayout()
        groupbox21_t2.setLayout(vbox21_t2)

        self.tableReport = QtWidgets.QTableView()
        self.tableReport.setModel(self.dbModel.modelReport)
        self.tableReport.setColumnHidden(0,True)

        self.tableReport.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableReport.resizeColumnsToContents()
        self.tableReport.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.dbModel.modelReport.sort(2, QtCore.Qt.AscendingOrder)

        vbox21_t2.addWidget(self.tableReport)

        # my_row
        groupbox22_t2 = QtWidgets.QGroupBox()
        vbox21_t2.addWidget(groupbox22_t2)

        vbox22_t2 = QtWidgets.QGridLayout()
        groupbox22_t2.setLayout(vbox22_t2)

        self.btn_createReport = QtWidgets.QPushButton("Create Report")
        vbox22_t2.addWidget(self.btn_createReport, 0, 9)

        self.layout.addWidget(self.tabs)
        Form.setLayout(self.layout)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def SETfunc(self):
        if self.spring_radio_SET.isChecked() or self.summer_radio_SET.isChecked() or self.fall_radio_SET.isChecked() or self.winter_radio_SET.isChecked():
            if self.spring_radio_SET.isChecked():
                self.SettingArray[:,0] = np.array([int(self.SETtext_O2.text()), int(self.SETtext_Co2.text()), int(
                    self.SETtext_CH4.text()), int(self.SETtext_Humidity.text()), int(
                    self.SETtext_Temperature.text()), int(self.SETtext_Battery.text())])

                np.savetxt(self.upFolder +'/setting.txt', self.SettingArray,delimiter=',')
            elif self.summer_radio_SET.isChecked():
                self.SettingArray[:,1] = np.array([int(self.SETtext_O2.text()), int(self.SETtext_Co2.text()), int(self.SETtext_CH4.text()), int(self.SETtext_Humidity.text()), int(self.SETtext_Temperature.text()), int(self.SETtext_Battery.text())])

                np.savetxt(self.upFolder +'/setting.txt', self.SettingArray,delimiter=',')
            elif self.fall_radio_SET.isChecked():
                self.SettingArray[:,2] = np.array([int(self.SETtext_O2.text()), int(self.SETtext_Co2.text()), int(self.SETtext_CH4.text()), int(self.SETtext_Humidity.text()), int(self.SETtext_Temperature.text()), int(self.SETtext_Battery.text())])

                np.savetxt(self.upFolder +'/setting.txt', self.SettingArray,delimiter=',')
            elif self.winter_radio_SET.isChecked():
                self.SettingArray[:,3] = np.array([int(self.SETtext_O2.text()), int(self.SETtext_Co2.text()), int(self.SETtext_CH4.text()), int(self.SETtext_Humidity.text()), int(self.SETtext_Temperature.text()), int(self.SETtext_Battery.text())])

                np.savetxt(self.upFolder +'/setting.txt', self.SettingArray,delimiter=',')
        else:
            self.SETerrordialog()

    def AlarmFunc(self):
        alarmBell=np.array([0,0,0,0,0,0])
        if self.spring_radio.isChecked():

            # O2
            if int(self.text_O2.text()) < int(self.SettingArray[0][0]):
                self.label_32_11.setStyleSheet("background-color: red;")
                alarmBell[0]=1
            elif int(self.text_O2.text()) > int(self.SettingArray[0][0]):
                self.label_32_11.setStyleSheet("")
            # Co2
            if int(self.text_Co2.text()) > int(self.SettingArray[1][0]):
                self.label_32_12.setStyleSheet("background-color: red;")
                alarmBell[1]=1
            elif int(self.text_Co2.text()) < int(self.SettingArray[1][0]):
                self.label_32_12.setStyleSheet("")
            # CH4
            if int(self.text_CH4.text()) > int(self.SettingArray[2][0]):
                self.label_32_13.setStyleSheet("background-color: red;")
                alarmBell[2]=1
            elif int(self.text_CH4.text()) < int(self.SettingArray[2][0]):
                self.label_32_13.setStyleSheet("")
            # Humidity
            if int(self.text_Humidity.text()) > int(self.SettingArray[3][0]):
                self.label_32_14.setStyleSheet("background-color: red;")
                alarmBell[3]=1
            elif int(self.text_Humidity.text()) < int(self.SettingArray[3][0]):
                self.label_32_14.setStyleSheet("")
            # Temperature
            if int(self.text_Temperature.text()) > int(self.SettingArray[4][0]):
                self.label_32_15.setStyleSheet("background-color: red;")
                alarmBell[4]=1
            elif int(self.text_Temperature.text()) < int(self.SettingArray[4][0]):
                self.label_32_15.setStyleSheet("")
            # Battery
            if int(self.text_Battery.text()) < int(self.SettingArray[5][0]):
                self.label_32_16.setStyleSheet("background-color: red;")
                alarmBell[5]=1
            elif int(self.text_Battery.text()) > int(self.SettingArray[5][0]):
                self.label_32_16.setStyleSheet("")

            if alarmBell.any():
                self.AlarmaddRow(alarmBell)

        if self.summer_radio.isChecked():
            # O2
            if int(self.text_O2.text()) < int(self.SettingArray[0][1]):
                self.label_32_11.setStyleSheet("background-color: red;")
                alarmBell[0]=1
            elif int(self.text_O2.text()) > int(self.SettingArray[0][1]):
                self.label_32_11.setStyleSheet("")
            # Co2
            if int(self.text_Co2.text()) > int(self.SettingArray[1][1]):
                self.label_32_12.setStyleSheet("background-color: red;")
                alarmBell[1]=1
            elif int(self.text_Co2.text()) < int(self.SettingArray[1][1]):
                self.label_32_12.setStyleSheet("")
            # CH4
            if int(self.text_CH4.text()) > int(self.SettingArray[2][1]):
                self.label_32_13.setStyleSheet("background-color: red;")
                alarmBell[2]=1
            elif int(self.text_CH4.text()) < int(self.SettingArray[2][1]):
                self.label_32_13.setStyleSheet("")
            # Humidity
            if int(self.text_Humidity.text()) > int(self.SettingArray[3][1]):
                self.label_32_14.setStyleSheet("background-color: red;")
                alarmBell[3]=1
            elif int(self.text_Humidity.text()) < int(self.SettingArray[3][1]):
                self.label_32_14.setStyleSheet("")
            # Temperature
            if int(self.text_Temperature.text()) > int(self.SettingArray[4][1]):
                self.label_32_15.setStyleSheet("background-color: red;")
                alarmBell[4]=1
            elif int(self.text_Temperature.text()) < int(self.SettingArray[4][1]):
                self.label_32_15.setStyleSheet("")
            # Battery
            if int(self.text_Battery.text()) < int(self.SettingArray[5][1]):
                self.label_32_16.setStyleSheet("background-color: red;")
                alarmBell[5]=1
            elif int(self.text_Battery.text()) > int(self.SettingArray[5][1]):
                self.label_32_16.setStyleSheet("")

            if alarmBell.any():
                self.AlarmaddRow(alarmBell)

        if self.fall_radio.isChecked():
            # O2
            if int(self.text_O2.text()) < int(self.SettingArray[0][2]):
                self.label_32_11.setStyleSheet("background-color: red;")
                alarmBell[0]=1
            elif int(self.text_O2.text()) > int(self.SettingArray[0][2]):
                self.label_32_11.setStyleSheet("")
            # Co2
            if int(self.text_Co2.text()) > int(self.SettingArray[1][2]):
                self.label_32_12.setStyleSheet("background-color: red;")
                alarmBell[1]=1
            elif int(self.text_Co2.text()) < int(self.SettingArray[1][2]):
                self.label_32_12.setStyleSheet("")
            # CH4
            if int(self.text_CH4.text()) > int(self.SettingArray[2][2]):
                self.label_32_13.setStyleSheet("background-color: red;")
                alarmBell[2]=1
            elif int(self.text_CH4.text()) < int(self.SettingArray[2][2]):
                self.label_32_13.setStyleSheet("")
            # Humidity
            if int(self.text_Humidity.text()) > int(self.SettingArray[3][2]):
                self.label_32_14.setStyleSheet("background-color: red;")
                alarmBell[3]=1
            elif int(self.text_Humidity.text()) < int(self.SettingArray[3][2]):
                self.label_32_14.setStyleSheet("")
            # Temperature
            if int(self.text_Temperature.text()) > int(self.SettingArray[4][2]):
                self.label_32_15.setStyleSheet("background-color: red;")
                alarmBell[4]=1
            elif int(self.text_Temperature.text()) < int(self.SettingArray[4][2]):
                self.label_32_15.setStyleSheet("")
            # Battery
            if int(self.text_Battery.text()) < int(self.SettingArray[5][2]):
                self.label_32_16.setStyleSheet("background-color: red;")
                alarmBell[5]=1
            elif int(self.text_Battery.text()) > int(self.SettingArray[5][2]):
                self.label_32_16.setStyleSheet("")

            if alarmBell.any():
                self.AlarmaddRow(alarmBell)

        if self.winter_radio.isChecked():
            # O2
            if int(self.text_O2.text()) < int(self.SettingArray[0][3]):
                self.label_32_11.setStyleSheet("background-color: red;")
                alarmBell[0]=1
            elif int(self.text_O2.text()) > int(self.SettingArray[0][3]):
                self.label_32_11.setStyleSheet("")
            # Co2
            if int(self.text_Co2.text()) > int(self.SettingArray[1][3]):
                self.label_32_12.setStyleSheet("background-color: red;")
                alarmBell[1]=1
            elif int(self.text_Co2.text()) < int(self.SettingArray[1][3]):
                self.label_32_12.setStyleSheet("")
            # CH4
            if int(self.text_CH4.text()) > int(self.SettingArray[2][3]):
                self.label_32_13.setStyleSheet("background-color: red;")
                alarmBell[2]=1
            elif int(self.text_CH4.text()) < int(self.SettingArray[2][3]):
                self.label_32_13.setStyleSheet("")
            # Humidity
            if int(self.text_Humidity.text()) > int(self.SettingArray[3][3]):
                self.label_32_14.setStyleSheet("background-color: red;")
                alarmBell[3]=1
            elif int(self.text_Humidity.text()) < int(self.SettingArray[3][3]):
                self.label_32_14.setStyleSheet("")
            # Temperature
            if int(self.text_Temperature.text()) > int(self.SettingArray[4][3]):
                self.label_32_15.setStyleSheet("background-color: red;")
                alarmBell[4]=1
            elif int(self.text_Temperature.text()) < int(self.SettingArray[4][3]):
                self.label_32_15.setStyleSheet("")
            # Battery
            if int(self.text_Battery.text()) < int(self.SettingArray[5][3]):
                self.label_32_16.setStyleSheet("background-color: red;")
                alarmBell[5]=1
            elif int(self.text_Battery.text()) > int(self.SettingArray[5][3]):
                self.label_32_16.setStyleSheet("")

            if alarmBell.any():
                self.AlarmaddRow(alarmBell)

    def AlarmaddRow(self,alarmBell):
        p = float(self.InputPosition.text())
        h = float(self.InputHeight.text())
        a = float(self.InputAngle.text())
        if (p>=self.AlarmPosition+self.AP_range)or(p<=self.AlarmPosition-self.AP_range) or(h>=self.AlarmHeight+self.AH_range)or(h<=self.AlarmHeight-self.AH_range) or(a>=self.AlarmAngle+self.AA_range)or(a<=self.AlarmAngle-self.AA_range):
            alarmcode = str(alarmBell[0])+str(alarmBell[1])+str(alarmBell[2])+str(alarmBell[3])+str(alarmBell[4])+str(alarmBell[5])
            self.AlarmPosition = p
            self.AlarmHeight = h
            self.AlarmAngle = a
            self.AlarmPicSignal = 1
            self.FaceMotionAddRow(alarmcode)

    def Auto_Report(self,array):
        self.ID1 += 1
        current_time = QtCore.QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        data = [self.ID1, array[1], array[2], array[3], array[4], array[5],array[6],array[7],
                label_time, self.text_O2.text(), self.text_Co2.text(), self.text_CH4.text(),
                self.text_Humidity.text(), self.text_Temperature.text(), self.text_Battery.text()]
        self.dbModel.addDataReport(data)

    def FaceMotionAddRow(self,alarmcode):
        self.ID2 += 1
        current_time = QtCore.QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        data = [self.ID2,111,1,1,alarmcode,self.InputPosition.text(),self.InputHeight.text(),self.InputAngle.text(),
                label_time,self.text_O2.text(),self.text_Co2.text(),self.text_CH4.text(),self.text_Humidity.text(),
                self.text_Temperature.text(),self.text_Battery.text()]
        self.dbModel.addDataReport(data)

    def OperatorAddRow(self,alarmcode):
        self.ID3 += 1
        current_time = QtCore.QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        data = [self.ID3, 111, 1, 1, alarmcode, self.InputPosition.text(), self.InputHeight.text(),
                self.InputAngle.text(),label_time, self.text_O2.text(), self.text_Co2.text(),
                self.text_CH4.text(), self.text_Humidity.text(), self.text_Temperature.text(),
                self.text_Battery.text()]
        self.dbModel.addDataReport(data)

    def addRow(self):
        if self.enterPic.isChecked(): A="1"
        else: A="0"
        if self.enterVid.isChecked(): B="1"
        else: B="0"
        data = [ A , B , self.enterProgram.currentText(),
                 "{:10.2f}".format(float(self.enterPosition.text())),
                 "{:10.2f}".format(float(self.enterHeight.text())),
                 "{:10.2f}".format(float(self.enterAngle.text()))]
        if data[2]!='' and data[3]!='' and data[4]!='' and data[5] != '':
            self.dbModel.addData(data)
            self.enterPic.setChecked(False)
            self.enterVid.setChecked(False)
            self.enterPosition.clear()
            self.enterHeight.clear()
            self.enterAngle.clear()

    def deleteRow(self):
        row = self.table.currentIndex().row()
        if row < 0:
            return
        self.dbModel.deleteData(row)

    def copyFunc(self):
        self.enterPosition.setText(self.InputPosition.text())
        self.enterHeight.setText(self.InputHeight.text())
        self.enterAngle.setText(self.InputAngle.text())

    def copyRow(self):
        if self.dbModel.modelAuto.rowCount() > 0:
            indexes = self.table.selectionModel().selectedRows()
            for index in sorted(indexes):
                self.enterPic.setChecked(int(self.dbModel.modelAuto.index(index.row(),1).data())==1)
                self.enterVid.setChecked(int(self.dbModel.modelAuto.index(index.row(),2).data()) == 1)
                prog = self.dbModel.modelAuto.index(index.row(), 3).data()
                self.enterProgram.setCurrentIndex(int(prog[8:])-1)
                self.enterPosition.setText(str(self.dbModel.modelAuto.index(index.row(),4).data()))
                self.enterHeight.setText(str(self.dbModel.modelAuto.index(index.row(),5).data()))
                self.enterAngle.setText(str(self.dbModel.modelAuto.index(index.row(),6).data()))
