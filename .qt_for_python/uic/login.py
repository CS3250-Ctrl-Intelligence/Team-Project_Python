# Form implementation generated from reading ui file 'c:\Users\Marin\Documents\Team-Project_Python\backend_files\login.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(891, 561)
        Dialog.setStyleSheet("#leftMenuContainer{\n"
"    background-color:  #16191d;\n"
"}\n"
"#leftMenuContainer QPushButton{\n"
"    text-align: left;\n"
"    padding: 5px 10px;\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"}")
        self.leftMenuContainer = QtWidgets.QWidget(Dialog)
        self.leftMenuContainer.setGeometry(QtCore.QRect(0, 0, 123, 561))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuContainer.setSizePolicy(sizePolicy)
        self.leftMenuContainer.setObjectName("leftMenuContainer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.leftMenuContainer)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.leftMenuSubContainer = QtWidgets.QWidget(self.leftMenuContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuSubContainer.setSizePolicy(sizePolicy)
        self.leftMenuSubContainer.setObjectName("leftMenuSubContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.leftMenuSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.leftMenuSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.leftMenuSubContainer)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2.addWidget(self.frame_3)
        self.horizontalLayout_3.addWidget(self.leftMenuSubContainer)
        self.mainWindow = QtWidgets.QWidget(Dialog)
        self.mainWindow.setGeometry(QtCore.QRect(120, 40, 771, 521))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWindow.sizePolicy().hasHeightForWidth())
        self.mainWindow.setSizePolicy(sizePolicy)
        self.mainWindow.setStyleSheet("background-color:  #16191d;\n"
"")
        self.mainWindow.setObjectName("mainWindow")
        self.label_username = QtWidgets.QLabel(self.mainWindow)
        self.label_username.setGeometry(QtCore.QRect(230, 90, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_username.setFont(font)
        self.label_username.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_username.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_username.setObjectName("label_username")
        self.goBtn = QtWidgets.QPushButton(self.mainWindow)
        self.goBtn.setGeometry(QtCore.QRect(220, 250, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.goBtn.setFont(font)
        self.goBtn.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.goBtn.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(255, 85, 0);")
        self.goBtn.setObjectName("goBtn")
        self.lineEdit_username = QtWidgets.QLineEdit(self.mainWindow)
        self.lineEdit_username.setGeometry(QtCore.QRect(240, 120, 251, 31))
        self.lineEdit_username.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_username.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.label_password = QtWidgets.QLabel(self.mainWindow)
        self.label_password.setGeometry(QtCore.QRect(230, 160, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_password.setFont(font)
        self.label_password.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_password.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_password.setObjectName("label_password")
        self.lineEdit_password = QtWidgets.QLineEdit(self.mainWindow)
        self.lineEdit_password.setGeometry(QtCore.QRect(240, 190, 251, 31))
        self.lineEdit_password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_password.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.createBtn = QtWidgets.QPushButton(self.mainWindow)
        self.createBtn.setGeometry(QtCore.QRect(220, 310, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.createBtn.setFont(font)
        self.createBtn.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.createBtn.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(255, 85, 0);")
        self.createBtn.setObjectName("createBtn")
        self.label_result = QtWidgets.QLabel(self.mainWindow)
        self.label_result.setGeometry(QtCore.QRect(250, 230, 231, 16))
        self.label_result.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.header = QtWidgets.QWidget(Dialog)
        self.header.setGeometry(QtCore.QRect(120, 0, 771, 41))
        self.header.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.591, y1:0.0454545, x2:1, y2:0, stop:0  #16191d, stop:1 rgb(255, 85, 0))\n"
"")
        self.header.setObjectName("header")
        self.label = QtWidgets.QLabel(self.header)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:  #16191d;")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_username.setText(_translate("Dialog", "Username"))
        self.goBtn.setText(_translate("Dialog", "Sign in"))
        self.label_password.setText(_translate("Dialog", "Password"))
        self.createBtn.setText(_translate("Dialog", "Create Employee"))
        self.label.setText(_translate("Dialog", "Ctrl Intelligence"))
