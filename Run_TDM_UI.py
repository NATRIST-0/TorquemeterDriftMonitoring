from TDM import Ui_StackedWidget
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QStyle

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 888, 551)
        
        # Créer un QStackedWidget comme widget central
        self.stackedWidget = QStackedWidget(self)
        self.setCentralWidget(self.stackedWidget)
        
        # Créer l'UI
        self.ui = Ui_StackedWidget()
        self.ui.setupUi(self.stackedWidget)
        
        # Ajout des icônes aux boutons
        style = self.style()
        self.ui.pushButton_suivi_verif.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_FileDialogContentsView))
        self.ui.pushButton_nouvelle_verif.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_FileDialogNewFolder))
        self.ui.pushButton_archives.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_DialogOpenButton))
        self.ui.pushButton_nouvel_instru.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_DialogSaveButton))
        self.ui.pushButton_export.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_FileDialogToParent))
        
        # Configuration des connexions pour naviguer entre les pages
        self.setup_navigation()
        
    def setup_navigation(self):
        # Boutons de navigation vers différentes pages
        self.ui.pushButton_suivi_verif.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.ui.page_suivi))
        
        self.ui.pushButton_nouvelle_verif.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.ui.page_nouvelle_verification))
        
        self.ui.pushButton_archives.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.ui.page_archives))
        
        self.ui.pushButton_nouvel_instru.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.ui.page_enregistrer_instrument))
        
        self.ui.pushButton_export.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.ui.page_export))
        
        # Boutons de retour au menu principal pour chaque pages
        self.ui.suivi_menu.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.ui.page_menu))
        
        self.ui.nouvelle_verification_menu.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.ui.page_menu))
        
        self.ui.archives_menu.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.ui.page_menu))
        
        self.ui.enregistrer_instrument_menu.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.ui.page_menu))
        
        self.ui.export_menu.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.ui.page_menu))

app = QApplication([])
window = Window()
window.show()
app.exec()