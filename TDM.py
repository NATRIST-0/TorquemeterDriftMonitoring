# Form implementation generated from reading ui file 'TDM.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(888, 604)
        self.page_menu = QtWidgets.QWidget()
        self.page_menu.setObjectName("page_menu")
        self.label_TDM = QtWidgets.QLabel(parent=self.page_menu)
        self.label_TDM.setEnabled(True)
        self.label_TDM.setGeometry(QtCore.QRect(150, 30, 591, 50))
        self.label_TDM.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_TDM.setFont(font)
        self.label_TDM.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.label_TDM.setScaledContents(False)
        self.label_TDM.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_TDM.setObjectName("label_TDM")
        self.label_logo = QtWidgets.QLabel(parent=self.page_menu)
        self.label_logo.setGeometry(QtCore.QRect(0, 0, 161, 101))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("add_ons/EVO.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_logo.setWordWrap(True)
        self.label_logo.setObjectName("label_logo")
        self.widget = PlotWidget(parent=self.page_menu)
        self.widget.setGeometry(QtCore.QRect(140, 310, 601, 191))
        self.widget.setObjectName("widget")
        self.splitter = QtWidgets.QSplitter(parent=self.page_menu)
        self.splitter.setGeometry(QtCore.QRect(140, 110, 601, 179))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(100)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(parent=self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_suivi_verif = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_suivi_verif.setObjectName("pushButton_suivi_verif")
        self.buttonGroup = QtWidgets.QButtonGroup(StackedWidget)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.pushButton_suivi_verif)
        self.verticalLayout.addWidget(self.pushButton_suivi_verif)
        self.pushButton_nouvelle_verif = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_nouvelle_verif.setObjectName("pushButton_nouvelle_verif")
        self.buttonGroup.addButton(self.pushButton_nouvelle_verif)
        self.verticalLayout.addWidget(self.pushButton_nouvelle_verif)
        self.pushButton_archives = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_archives.setObjectName("pushButton_archives")
        self.buttonGroup.addButton(self.pushButton_archives)
        self.verticalLayout.addWidget(self.pushButton_archives)
        self.pushButton_nouvel_instru = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_nouvel_instru.setObjectName("pushButton_nouvel_instru")
        self.buttonGroup.addButton(self.pushButton_nouvel_instru)
        self.verticalLayout.addWidget(self.pushButton_nouvel_instru)
        self.pushButton_export = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_export.setObjectName("pushButton_export")
        self.buttonGroup.addButton(self.pushButton_export)
        self.verticalLayout.addWidget(self.pushButton_export)
        self.groupBox_date_2 = QtWidgets.QGroupBox(parent=self.splitter)
        self.groupBox_date_2.setAutoFillBackground(False)
        self.groupBox_date_2.setFlat(False)
        self.groupBox_date_2.setCheckable(False)
        self.groupBox_date_2.setObjectName("groupBox_date_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_date_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.groupBox_date_2)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_date_2)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        StackedWidget.addWidget(self.page_menu)
        self.page_suivi = QtWidgets.QWidget()
        self.page_suivi.setObjectName("page_suivi")
        self.label_3 = QtWidgets.QLabel(parent=self.page_suivi)
        self.label_3.setGeometry(QtCore.QRect(110, 10, 181, 16))
        self.label_3.setObjectName("label_3")
        self.suivi_menu = QtWidgets.QPushButton(parent=self.page_suivi)
        self.suivi_menu.setGeometry(QtCore.QRect(10, 0, 93, 28))
        self.suivi_menu.setObjectName("suivi_menu")
        self.label_8 = QtWidgets.QLabel(parent=self.page_suivi)
        self.label_8.setGeometry(QtCore.QRect(260, 10, 211, 16))
        self.label_8.setObjectName("label_8")
        self.comboBox_nom = QtWidgets.QComboBox(parent=self.page_suivi)
        self.comboBox_nom.setGeometry(QtCore.QRect(470, 10, 151, 22))
        self.comboBox_nom.setObjectName("comboBox_nom")
        StackedWidget.addWidget(self.page_suivi)
        self.page_nouvelle_verification = QtWidgets.QWidget()
        self.page_nouvelle_verification.setObjectName("page_nouvelle_verification")
        self.nouvelle_verification_menu = QtWidgets.QPushButton(parent=self.page_nouvelle_verification)
        self.nouvelle_verification_menu.setGeometry(QtCore.QRect(0, 0, 93, 28))
        self.nouvelle_verification_menu.setObjectName("nouvelle_verification_menu")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.page_nouvelle_verification)
        self.groupBox_3.setGeometry(QtCore.QRect(300, 20, 311, 131))
        self.groupBox_3.setObjectName("groupBox_3")
        self.widget1 = QtWidgets.QWidget(parent=self.groupBox_3)
        self.widget1.setGeometry(QtCore.QRect(30, 30, 251, 90))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_14 = QtWidgets.QLabel(parent=self.widget1)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)
        self.comboBox_instru_nv_verif = QtWidgets.QComboBox(parent=self.widget1)
        self.comboBox_instru_nv_verif.setObjectName("comboBox_instru_nv_verif")
        self.gridLayout.addWidget(self.comboBox_instru_nv_verif, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(parent=self.widget1)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 1, 0, 1, 1)
        self.dateEdit_nv_verif = QtWidgets.QDateEdit(parent=self.widget1)
        self.dateEdit_nv_verif.setObjectName("dateEdit_nv_verif")
        self.gridLayout.addWidget(self.dateEdit_nv_verif, 1, 1, 1, 1)
        self.pushButton_save_nv_verif = QtWidgets.QPushButton(parent=self.widget1)
        self.pushButton_save_nv_verif.setObjectName("pushButton_save_nv_verif")
        self.gridLayout.addWidget(self.pushButton_save_nv_verif, 2, 0, 1, 2)
        self.widget2 = QtWidgets.QWidget(parent=self.page_nouvelle_verification)
        self.widget2.setGeometry(QtCore.QRect(80, 270, 68, 181))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_22 = QtWidgets.QLabel(parent=self.widget2)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_7.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(parent=self.widget2)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_7.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(parent=self.widget2)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_7.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(parent=self.widget2)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_7.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(parent=self.widget2)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_7.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(parent=self.widget2)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_7.addWidget(self.label_27)
        self.widget3 = QtWidgets.QWidget(parent=self.page_nouvelle_verification)
        self.widget3.setGeometry(QtCore.QRect(163, 212, 625, 241))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_16 = QtWidgets.QLabel(parent=self.widget3)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.line_2 = QtWidgets.QFrame(parent=self.widget3)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_17 = QtWidgets.QLabel(parent=self.widget3)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_3.addWidget(self.label_17)
        self.label_Cmin = QtWidgets.QLabel(parent=self.widget3)
        self.label_Cmin.setObjectName("label_Cmin")
        self.horizontalLayout_3.addWidget(self.label_Cmin)
        self.label_28 = QtWidgets.QLabel(parent=self.widget3)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_3.addWidget(self.label_28)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.Cmin_1 = QtWidgets.QLineEdit(parent=self.widget3)
        self.Cmin_1.setObjectName("Cmin_1")
        self.verticalLayout_3.addWidget(self.Cmin_1)
        self.Cmin_2 = QtWidgets.QLineEdit(parent=self.widget3)
        self.Cmin_2.setObjectName("Cmin_2")
        self.verticalLayout_3.addWidget(self.Cmin_2)
        self.Cmin_3 = QtWidgets.QLineEdit(parent=self.widget3)
        self.Cmin_3.setObjectName("Cmin_3")
        self.verticalLayout_3.addWidget(self.Cmin_3)
        self.Cmin_4 = QtWidgets.QLineEdit(parent=self.widget3)
        self.Cmin_4.setObjectName("Cmin_4")
        self.verticalLayout_3.addWidget(self.Cmin_4)
        self.Cmin_5 = QtWidgets.QLineEdit(parent=self.widget3)
        self.Cmin_5.setObjectName("Cmin_5")
        self.verticalLayout_3.addWidget(self.Cmin_5)
        self.label_Cmin_moy = QtWidgets.QLabel(parent=self.widget3)
        self.label_Cmin_moy.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Cmin_moy.setObjectName("label_Cmin_moy")
        self.verticalLayout_3.addWidget(self.label_Cmin_moy)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(parent=self.widget3)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_4.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_19 = QtWidgets.QLabel(parent=self.widget3)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_4.addWidget(self.label_19)
        self.line_3 = QtWidgets.QFrame(parent=self.widget3)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_21 = QtWidgets.QLabel(parent=self.widget3)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_2.addWidget(self.label_21)
        self.label_Cmilieu = QtWidgets.QLabel(parent=self.widget3)
        self.label_Cmilieu.setObjectName("label_Cmilieu")
        self.horizontalLayout_2.addWidget(self.label_Cmilieu)
        self.label_31 = QtWidgets.QLabel(parent=self.widget3)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_2.addWidget(self.label_31)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.Cmilieu_1 = QtWidgets.QLineEdit(parent=self.widget3)
        self.Cmilieu_1.setObjectName("Cmilieu_1")
        self.verticalLayout_4.addWidget(self.Cmilieu_1)
        self.Cmilieu_2 = QtWidgets.QLineEdit(parent=self.widget3)
        self.Cmilieu_2.setObjectName("Cmilieu_2")
        self.verticalLayout_4.addWidget(self.Cmilieu_2)
        self.Cmilieu_3 = QtWidgets.QLineEdit(parent=self.widget3)
        self.Cmilieu_3.setObjectName("Cmilieu_3")
        self.verticalLayout_4.addWidget(self.Cmilieu_3)
        self.Cmilieu_4 = QtWidgets.QLineEdit(parent=self.widget3)
        self.Cmilieu_4.setObjectName("Cmilieu_4")
        self.verticalLayout_4.addWidget(self.Cmilieu_4)
        self.Cmilieu_5 = QtWidgets.QLineEdit(parent=self.widget3)
        self.Cmilieu_5.setObjectName("Cmilieu_5")
        self.verticalLayout_4.addWidget(self.Cmilieu_5)
        self.label_Cmilieu_moy = QtWidgets.QLabel(parent=self.widget3)
        self.label_Cmilieu_moy.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Cmilieu_moy.setObjectName("label_Cmilieu_moy")
        self.verticalLayout_4.addWidget(self.label_Cmilieu_moy)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.line_5 = QtWidgets.QFrame(parent=self.widget3)
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_4.addWidget(self.line_5)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_20 = QtWidgets.QLabel(parent=self.widget3)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_5.addWidget(self.label_20)
        self.line_4 = QtWidgets.QFrame(parent=self.widget3)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_5.addWidget(self.line_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_18 = QtWidgets.QLabel(parent=self.widget3)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout.addWidget(self.label_18)
        self.label_Cmax = QtWidgets.QLabel(parent=self.widget3)
        self.label_Cmax.setObjectName("label_Cmax")
        self.horizontalLayout.addWidget(self.label_Cmax)
        self.label_32 = QtWidgets.QLabel(parent=self.widget3)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout.addWidget(self.label_32)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.Cmax_1 = QtWidgets.QLineEdit(parent=self.widget3)
        self.Cmax_1.setObjectName("Cmax_1")
        self.verticalLayout_5.addWidget(self.Cmax_1)
        self.Cmax_2 = QtWidgets.QLineEdit(parent=self.widget3)
        self.Cmax_2.setObjectName("Cmax_2")
        self.verticalLayout_5.addWidget(self.Cmax_2)
        self.Cmax_3 = QtWidgets.QLineEdit(parent=self.widget3)
        self.Cmax_3.setObjectName("Cmax_3")
        self.verticalLayout_5.addWidget(self.Cmax_3)
        self.Cmax_4 = QtWidgets.QLineEdit(parent=self.widget3)
        self.Cmax_4.setObjectName("Cmax_4")
        self.verticalLayout_5.addWidget(self.Cmax_4)
        self.Cmax_5 = QtWidgets.QLineEdit(parent=self.widget3)
        self.Cmax_5.setObjectName("Cmax_5")
        self.verticalLayout_5.addWidget(self.Cmax_5)
        self.label_Cmax_moy = QtWidgets.QLabel(parent=self.widget3)
        self.label_Cmax_moy.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Cmax_moy.setObjectName("label_Cmax_moy")
        self.verticalLayout_5.addWidget(self.label_Cmax_moy)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        StackedWidget.addWidget(self.page_nouvelle_verification)
        self.page_archives = QtWidgets.QWidget()
        self.page_archives.setObjectName("page_archives")
        self.label_5 = QtWidgets.QLabel(parent=self.page_archives)
        self.label_5.setGeometry(QtCore.QRect(360, 310, 171, 16))
        self.label_5.setObjectName("label_5")
        self.archives_menu = QtWidgets.QPushButton(parent=self.page_archives)
        self.archives_menu.setGeometry(QtCore.QRect(0, 10, 93, 28))
        self.archives_menu.setObjectName("archives_menu")
        StackedWidget.addWidget(self.page_archives)
        self.page_enregistrer_instrument = QtWidgets.QWidget()
        self.page_enregistrer_instrument.setObjectName("page_enregistrer_instrument")
        self.label_6 = QtWidgets.QLabel(parent=self.page_enregistrer_instrument)
        self.label_6.setGeometry(QtCore.QRect(240, 10, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.enregistrer_instrument_menu = QtWidgets.QPushButton(parent=self.page_enregistrer_instrument)
        self.enregistrer_instrument_menu.setGeometry(QtCore.QRect(0, 0, 93, 28))
        self.enregistrer_instrument_menu.setObjectName("enregistrer_instrument_menu")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.page_enregistrer_instrument)
        self.groupBox_2.setGeometry(QtCore.QRect(160, 140, 551, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget = QtWidgets.QWidget(parent=self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 511, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_9 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.label_11 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_13)
        self.label_10 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.ref_instrument = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.ref_instrument.setObjectName("ref_instrument")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.ref_instrument)
        self.Cmin = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.Cmin.setObjectName("Cmin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.Cmin)
        self.Cmilieu = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.Cmilieu.setObjectName("Cmilieu")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.Cmilieu)
        self.Cmax = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.Cmax.setObjectName("Cmax")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.Cmax)
        self.tolerance = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.tolerance.setObjectName("tolerance")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tolerance)
        self.bouton_confirmer_instrument = QtWidgets.QPushButton(parent=self.page_enregistrer_instrument)
        self.bouton_confirmer_instrument.setGeometry(QtCore.QRect(390, 400, 93, 28))
        self.bouton_confirmer_instrument.setObjectName("bouton_confirmer_instrument")
        StackedWidget.addWidget(self.page_enregistrer_instrument)
        self.page_export = QtWidgets.QWidget()
        self.page_export.setObjectName("page_export")
        self.label_7 = QtWidgets.QLabel(parent=self.page_export)
        self.label_7.setGeometry(QtCore.QRect(330, 260, 221, 31))
        self.label_7.setObjectName("label_7")
        self.export_menu = QtWidgets.QPushButton(parent=self.page_export)
        self.export_menu.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.export_menu.setObjectName("export_menu")
        StackedWidget.addWidget(self.page_export)

        self.retranslateUi(StackedWidget)
        StackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget"))
        self.label_TDM.setText(_translate("StackedWidget", "Torquemeters Drift Monitoring"))
        self.groupBox.setTitle(_translate("StackedWidget", "Menu"))
        self.pushButton_suivi_verif.setText(_translate("StackedWidget", "Suivi des Vérifications"))
        self.pushButton_nouvelle_verif.setText(_translate("StackedWidget", "Nouvelle Vérification"))
        self.pushButton_archives.setText(_translate("StackedWidget", "Archives"))
        self.pushButton_nouvel_instru.setText(_translate("StackedWidget", "Enregistrer un Nouvel  Instrument"))
        self.pushButton_export.setText(_translate("StackedWidget", "Export Excel"))
        self.groupBox_date_2.setTitle(_translate("StackedWidget", "Date limite"))
        self.label.setText(_translate("StackedWidget", "Date pour prochaine vérification :"))
        self.label_2.setText(_translate("StackedWidget", "01/01/2000"))
        self.label_3.setText(_translate("StackedWidget", "Suivi des Vérifications"))
        self.suivi_menu.setText(_translate("StackedWidget", "Menu"))
        self.label_8.setText(_translate("StackedWidget", "Sélectionner l\'Instrument à afficher"))
        self.nouvelle_verification_menu.setText(_translate("StackedWidget", "Menu"))
        self.groupBox_3.setTitle(_translate("StackedWidget", "Nouvelle Vérification"))
        self.label_14.setText(_translate("StackedWidget", "Instrument à vérifier :"))
        self.label_15.setText(_translate("StackedWidget", "Date de vérification :"))
        self.pushButton_save_nv_verif.setText(_translate("StackedWidget", "Enregistrer les mesures"))
        self.label_22.setText(_translate("StackedWidget", "Mesure n°1"))
        self.label_23.setText(_translate("StackedWidget", "Mesure n°2"))
        self.label_24.setText(_translate("StackedWidget", "Mesure n°3"))
        self.label_25.setText(_translate("StackedWidget", "Mesure n°4"))
        self.label_26.setText(_translate("StackedWidget", "Mesure n°5"))
        self.label_27.setText(_translate("StackedWidget", "Moyennes"))
        self.label_16.setText(_translate("StackedWidget", "Couple de vérification minimal"))
        self.label_17.setText(_translate("StackedWidget", "Cmin = "))
        self.label_Cmin.setText(_translate("StackedWidget", "_______"))
        self.label_28.setText(_translate("StackedWidget", "N.m"))
        self.label_Cmin_moy.setText(_translate("StackedWidget", "_________________________"))
        self.label_19.setText(_translate("StackedWidget", "Couple de vérification milieu de gamme"))
        self.label_21.setText(_translate("StackedWidget", "Cmilieu = "))
        self.label_Cmilieu.setText(_translate("StackedWidget", "_______"))
        self.label_31.setText(_translate("StackedWidget", "N.m"))
        self.label_Cmilieu_moy.setText(_translate("StackedWidget", "________________________________"))
        self.label_20.setText(_translate("StackedWidget", "Couple de vérification maximal"))
        self.label_18.setText(_translate("StackedWidget", "Cmax = "))
        self.label_Cmax.setText(_translate("StackedWidget", "_______"))
        self.label_32.setText(_translate("StackedWidget", "N.m"))
        self.label_Cmax_moy.setText(_translate("StackedWidget", "_________________________"))
        self.label_5.setText(_translate("StackedWidget", "Archives"))
        self.archives_menu.setText(_translate("StackedWidget", "Menu"))
        self.label_6.setText(_translate("StackedWidget", "Enregistrer un Nouvel Instruement"))
        self.enregistrer_instrument_menu.setText(_translate("StackedWidget", "Menu"))
        self.groupBox_2.setTitle(_translate("StackedWidget", "Information de l\'instrument"))
        self.label_9.setText(_translate("StackedWidget", "Référence de l\'instrument :"))
        self.label_11.setText(_translate("StackedWidget", "Couple de vérification milieu de gamme [N.m] :"))
        self.label_12.setText(_translate("StackedWidget", "Couple de vérification milieu maximal [N.m]:"))
        self.label_13.setText(_translate("StackedWidget", "Tolérance [N.m]:"))
        self.label_10.setText(_translate("StackedWidget", "Couple de vérification minimal [N.m]:"))
        self.bouton_confirmer_instrument.setText(_translate("StackedWidget", "Confirmer"))
        self.label_7.setText(_translate("StackedWidget", "export"))
        self.export_menu.setText(_translate("StackedWidget", "Menu"))
from pyqtgraph import PlotWidget
