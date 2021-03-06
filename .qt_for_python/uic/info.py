# Form implementation generated from reading ui file 'c:\Users\Marin\Documents\Team-Project_Python\backend_files\ui_files\info.ui'
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
        self.verticalLayout_2.setContentsMargins(0, 0, 10, 0)
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
        self.menuBtn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuBtn.sizePolicy().hasHeightForWidth())
        self.menuBtn.setSizePolicy(sizePolicy)
        self.menuBtn.setStyleSheet("background-color: #1f232a;\n"
"color: rgb(255, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/user.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QtCore.QSize(24, 24))
        self.menuBtn.setObjectName("menuBtn")
        self.horizontalLayout_2.addWidget(self.menuBtn)
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
        self.ordersBtn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ordersBtn.sizePolicy().hasHeightForWidth())
        self.ordersBtn.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 35, 42))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 35, 42))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 35, 42))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 35, 42))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 35, 42))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 35, 42))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 35, 42))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 35, 42))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 35, 42))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.ordersBtn.setPalette(palette)
        self.ordersBtn.setStyleSheet("background-color: #1f232a;\n"
"color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/inbox.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ordersBtn.setIcon(icon1)
        self.ordersBtn.setIconSize(QtCore.QSize(24, 24))
        self.ordersBtn.setObjectName("ordersBtn")
        self.verticalLayout_3.addWidget(self.ordersBtn)
        self.invBtn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.invBtn.sizePolicy().hasHeightForWidth())
        self.invBtn.setSizePolicy(sizePolicy)
        self.invBtn.setStyleSheet("background-color: #1f232a;\n"
"color: rgb(255, 255, 255)")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/list.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.invBtn.setIcon(icon2)
        self.invBtn.setIconSize(QtCore.QSize(24, 24))
        self.invBtn.setObjectName("invBtn")
        self.verticalLayout_3.addWidget(self.invBtn)
        self.marketBtn = QtWidgets.QPushButton(self.frame_2)
        self.marketBtn.setStyleSheet("background-color: #1f232a;\n"
"color: rgb(255, 255, 255)")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/printer.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.marketBtn.setIcon(icon3)
        self.marketBtn.setIconSize(QtCore.QSize(24, 24))
        self.marketBtn.setObjectName("marketBtn")
        self.verticalLayout_3.addWidget(self.marketBtn)
        self.financeBtn = QtWidgets.QPushButton(self.frame_2)
        self.financeBtn.setStyleSheet("background-color: #1f232a;\n"
"color: rgb(255, 255, 255)")
        self.financeBtn.setIcon(icon3)
        self.financeBtn.setIconSize(QtCore.QSize(24, 24))
        self.financeBtn.setObjectName("financeBtn")
        self.verticalLayout_3.addWidget(self.financeBtn)
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
        self.settingsBtn = QtWidgets.QPushButton(self.frame_3)
        self.settingsBtn.setStyleSheet("background-color: #1f232a;\n"
"color: rgb(255, 255, 255)")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/settings.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.settingsBtn.setIcon(icon4)
        self.settingsBtn.setIconSize(QtCore.QSize(24, 24))
        self.settingsBtn.setObjectName("settingsBtn")
        self.verticalLayout_4.addWidget(self.settingsBtn)
        self.infoBtn = QtWidgets.QPushButton(self.frame_3)
        self.infoBtn.setStyleSheet("background-color: #1f232a;\n"
"color: rgb(255, 255, 255)")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/info.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.infoBtn.setIcon(icon5)
        self.infoBtn.setIconSize(QtCore.QSize(24, 24))
        self.infoBtn.setObjectName("infoBtn")
        self.verticalLayout_4.addWidget(self.infoBtn)
        self.helpBtn = QtWidgets.QPushButton(self.frame_3)
        self.helpBtn.setStyleSheet("background-color: #1f232a;\n"
"color: rgb(255, 255, 255)")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/help-circle.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.helpBtn.setIcon(icon6)
        self.helpBtn.setIconSize(QtCore.QSize(24, 24))
        self.helpBtn.setObjectName("helpBtn")
        self.verticalLayout_4.addWidget(self.helpBtn)
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
        self.label_username.setGeometry(QtCore.QRect(10, 10, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_username.setFont(font)
        self.label_username.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_username.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_username.setObjectName("label_username")
        self.textEdit = QtWidgets.QTextEdit(self.mainWindow)
        self.textEdit.setGeometry(QtCore.QRect(0, 70, 721, 391))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.textEdit.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textEdit.setObjectName("textEdit")
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
        self.menuBtn.setToolTip(_translate("Dialog", "Menu"))
        self.menuBtn.setText(_translate("Dialog", "Signed In"))
        self.ordersBtn.setToolTip(_translate("Dialog", "Home"))
        self.ordersBtn.setText(_translate("Dialog", "Orders"))
        self.invBtn.setToolTip(_translate("Dialog", "Data Analysis"))
        self.invBtn.setText(_translate("Dialog", "Inventory"))
        self.marketBtn.setToolTip(_translate("Dialog", "View Reports"))
        self.marketBtn.setText(_translate("Dialog", "Marketing"))
        self.financeBtn.setToolTip(_translate("Dialog", "View Reports"))
        self.financeBtn.setText(_translate("Dialog", "Finance"))
        self.settingsBtn.setToolTip(_translate("Dialog", "Go To Settings"))
        self.settingsBtn.setText(_translate("Dialog", "Settings"))
        self.infoBtn.setToolTip(_translate("Dialog", "Information about the app"))
        self.infoBtn.setText(_translate("Dialog", "Info"))
        self.helpBtn.setToolTip(_translate("Dialog", "Get more help"))
        self.helpBtn.setText(_translate("Dialog", "Help"))
        self.label_username.setText(_translate("Dialog", "Information"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">We are a team based out of Colorado. There are five foundings members that go by the names:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Tho Le</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Matthew White</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Brian Vasquez</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Cameron Spear</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Seth Hamilton</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">We have created this ecommerce site and backend application to improve our skills. This is just one small stepping stone on our journey towards software engineering/development.</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "Ctrl Intelligence"))
