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
        StackedWidget.resize(888, 551)
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
        icon = QtGui.QIcon.fromTheme("SP_FileDialogContentsView")
        self.pushButton_suivi_verif.setIcon(icon)
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
        self.label_4 = QtWidgets.QLabel(parent=self.page_nouvelle_verification)
        self.label_4.setGeometry(QtCore.QRect(340, 200, 261, 16))
        self.label_4.setObjectName("label_4")
        self.nouvelle_verification_menu = QtWidgets.QPushButton(parent=self.page_nouvelle_verification)
        self.nouvelle_verification_menu.setGeometry(QtCore.QRect(0, 0, 93, 28))
        self.nouvelle_verification_menu.setObjectName("nouvelle_verification_menu")
        self.dateEdit = QtWidgets.QDateEdit(parent=self.page_nouvelle_verification)
        self.dateEdit.setGeometry(QtCore.QRect(100, 170, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
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
        self.widget1 = QtWidgets.QWidget(parent=self.groupBox_2)
        self.widget1.setGeometry(QtCore.QRect(20, 30, 511, 161))
        self.widget1.setObjectName("widget1")
        self.formLayout = QtWidgets.QFormLayout(self.widget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_9 = QtWidgets.QLabel(parent=self.widget1)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.label_11 = QtWidgets.QLabel(parent=self.widget1)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(parent=self.widget1)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(parent=self.widget1)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_13)
        self.label_10 = QtWidgets.QLabel(parent=self.widget1)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.ref_instrument = QtWidgets.QLineEdit(parent=self.widget1)
        self.ref_instrument.setObjectName("ref_instrument")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.ref_instrument)
        self.Cmin = QtWidgets.QLineEdit(parent=self.widget1)
        self.Cmin.setObjectName("Cmin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.Cmin)
        self.Cmilieu = QtWidgets.QLineEdit(parent=self.widget1)
        self.Cmilieu.setObjectName("Cmilieu")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.Cmilieu)
        self.Cmax = QtWidgets.QLineEdit(parent=self.widget1)
        self.Cmax.setObjectName("Cmax")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.Cmax)
        self.tolerence = QtWidgets.QLineEdit(parent=self.widget1)
        self.tolerence.setObjectName("tolerence")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tolerence)
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
        self.label_4.setText(_translate("StackedWidget", "nouvelle_verification"))
        self.nouvelle_verification_menu.setText(_translate("StackedWidget", "Menu"))
        self.label_5.setText(_translate("StackedWidget", "Archives"))
        self.archives_menu.setText(_translate("StackedWidget", "Menu"))
        self.label_6.setText(_translate("StackedWidget", "Enregistrer un Nouvel Instruement"))
        self.enregistrer_instrument_menu.setText(_translate("StackedWidget", "Menu"))
        self.groupBox_2.setTitle(_translate("StackedWidget", "Information de l\'instrument"))
        self.label_9.setText(_translate("StackedWidget", "Référence de l\'instrument :"))
        self.label_11.setText(_translate("StackedWidget", "Couple de vérification milieu de gamme [N.m] :"))
        self.label_12.setText(_translate("StackedWidget", "Couple de vérification milieu maximal [N.m]:"))
        self.label_13.setText(_translate("StackedWidget", "Tolérence [N.m]:"))
        self.label_10.setText(_translate("StackedWidget", "Couple de vérification minimal [N.m]:"))
        self.bouton_confirmer_instrument.setText(_translate("StackedWidget", "Confirmer"))
        self.label_7.setText(_translate("StackedWidget", "export"))
        self.export_menu.setText(_translate("StackedWidget", "Menu"))
from pyqtgraph import PlotWidget
