# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\new-sde-ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(362, 424)
        MainWindow.setMinimumSize(QtCore.QSize(362, 424))
        MainWindow.setMaximumSize(QtCore.QSize(362, 424))
        MainWindow.setStyleSheet("    font-family: SCG;\n"
"    font-size:15pt;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setMinimumSize(QtCore.QSize(344, 406))
        self.frame_6.setMaximumSize(QtCore.QSize(344, 406))
        self.frame_6.setStyleSheet("background-color:#222222;\n"
"border-radius: 10px;\n"
"padding: 0px 0px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.auto_stop_2 = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("SCG")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.auto_stop_2.setFont(font)
        self.auto_stop_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.auto_stop_2.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.auto_stop_2.setStyleSheet("QPushButton {\n"
"    background-color: #f44336; /* Red */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 2px 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d32f2f; /* Darker Red */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #b71c1c; /* Even Darker Red when pressed */\n"
"}")
        self.auto_stop_2.setCheckable(True)
        self.auto_stop_2.setChecked(False)
        self.auto_stop_2.setAutoRepeat(False)
        self.auto_stop_2.setAutoExclusive(False)
        self.auto_stop_2.setObjectName("auto_stop_2")
        self.gridLayout_2.addWidget(self.auto_stop_2, 8, 0, 1, 1)
        self.auto_start = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("SCG")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.auto_start.setFont(font)
        self.auto_start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.auto_start.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.auto_start.setStyleSheet("QPushButton {\n"
"    background-color: #4CAF50; /* Green */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 2px 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049; /* Darker Green */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #357a38; /* Even Darker Green when pressed */\n"
"}")
        self.auto_start.setCheckable(True)
        self.auto_start.setChecked(False)
        self.auto_start.setAutoRepeat(False)
        self.auto_start.setAutoExclusive(False)
        self.auto_start.setObjectName("auto_start")
        self.gridLayout_2.addWidget(self.auto_start, 7, 0, 1, 1)
        self.zdb_status_2 = QtWidgets.QLabel(self.frame_6)
        self.zdb_status_2.setMaximumSize(QtCore.QSize(16777210, 16777210))
        font = QtGui.QFont()
        font.setFamily("SCG")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.zdb_status_2.setFont(font)
        self.zdb_status_2.setStyleSheet("color:white;")
        self.zdb_status_2.setObjectName("zdb_status_2")
        self.gridLayout_2.addWidget(self.zdb_status_2, 1, 0, 1, 1)
        self.zb_erase_btn_3 = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("SCG")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.zb_erase_btn_3.setFont(font)
        self.zb_erase_btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zb_erase_btn_3.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.zb_erase_btn_3.setStyleSheet("QPushButton {\n"
"    background-color: #f44336; /* Red */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 2px 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #d32f2f; /* Darker Red */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #b71c1c; /* Even Darker Red when pressed */\n"
"}")
        self.zb_erase_btn_3.setCheckable(True)
        self.zb_erase_btn_3.setChecked(False)
        self.zb_erase_btn_3.setAutoRepeat(False)
        self.zb_erase_btn_3.setAutoExclusive(False)
        self.zb_erase_btn_3.setObjectName("zb_erase_btn_3")
        self.gridLayout_2.addWidget(self.zb_erase_btn_3, 5, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("SCG")
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:white;\n"
"    text-align:center;")
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 6, 0, 1, 1)
        self.zb_flash_btn_2 = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("SCG")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.zb_flash_btn_2.setFont(font)
        self.zb_flash_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zb_flash_btn_2.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.zb_flash_btn_2.setStyleSheet("QPushButton {\n"
"    background-color: #4CAF50; /* Green */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 2px 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049; /* Darker Green */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #357a38; /* Even Darker Green when pressed */\n"
"}")
        self.zb_flash_btn_2.setCheckable(True)
        self.zb_flash_btn_2.setChecked(False)
        self.zb_flash_btn_2.setAutoRepeat(False)
        self.zb_flash_btn_2.setAutoExclusive(False)
        self.zb_flash_btn_2.setObjectName("zb_flash_btn_2")
        self.gridLayout_2.addWidget(self.zb_flash_btn_2, 4, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("SCG")
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:white;\n"
"    text-align:center;")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.rf_type_box_3 = QtWidgets.QComboBox(self.frame_6)
        self.rf_type_box_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.rf_type_box_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rf_type_box_3.setStyleSheet("QComboBox{    \n"
"    background-color:white;\n"
"    border-radius: 5px;\n"
"    border:1px solid black;\n"
"    padding-left:5px;\n"
"    font-size:12pt;\n"
"}\n"
"QComboBox::drop-down{\n"
"    border:0px\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image:url(:/newPrefix/assets/arrow-down-sign-to-navigate.png);\n"
"    width:15px;    \n"
"    heigth:15px;\n"
"    margin-right:15px;\n"
"}\n"
"QComboBox:on{\n"
"    border:4px solid #c2dbfe;\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"    background-color:white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox QListView::item{\n"
"    padding-left:10px;\n"
"    border:1px solid rgba(0,0,0,10%);\n"
"    background-color:#fff;\n"
"    outline:0px;\n"
"}\n"
"")
        self.rf_type_box_3.setObjectName("rf_type_box_3")
        self.rf_type_box_3.addItem("")
        self.rf_type_box_3.addItem("")
        self.rf_type_box_3.addItem("")
        self.gridLayout_2.addWidget(self.rf_type_box_3, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_6, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("ZBProgrammer", "ZBProgrammer"))
        self.auto_stop_2.setText(_translate("MainWindow", "Stop"))
        self.auto_start.setText(_translate("MainWindow", "Start"))
        self.zdb_status_2.setText(_translate("MainWindow", "Status : "))
        self.zb_erase_btn_3.setText(_translate("MainWindow", "Erase"))
        self.label_10.setText(_translate("MainWindow", "Automatic Mode"))
        self.zb_flash_btn_2.setText(_translate("MainWindow", "Flash"))
        self.label_9.setText(_translate("MainWindow", "RF Programmer"))
        self.rf_type_box_3.setItemText(0, _translate("MainWindow", "Select Devices Type"))
        self.rf_type_box_3.setItemText(1, _translate("MainWindow", "Coordinator"))
        self.rf_type_box_3.setItemText(2, _translate("MainWindow", "Router"))
import sde_rc
