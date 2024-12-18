#!/usr/bin/python3
# author: Tristan Gayrard
 
"""
Run Torquemeters Drift Monitoring UI
"""
 
import TDM_fonctions as tf
from TDM import Ui_StackedWidget
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QTextEdit
 
class Window(QMainWindow):
    def __init__(self):  # Note: Fixed typo in __init__
        super().__init__()
        self.setGeometry(50, 50, 888, 551)
       
        # Créer un QStackedWidget comme widget central
        self.stackedWidget = QStackedWidget(self)
        self.setCentralWidget(self.stackedWidget)
       
        # Créer l'UI
        self.ui = Ui_StackedWidget()
        self.ui.setupUi(self.stackedWidget)
       
        # Ajout des icônes aux boutons
        tf.icones_boutons(self)
       
        # Configuration des connexions pour naviguer entre les pages
        tf.setup_navigation(self)
       
        # Définiton des différente pages de l'application
        page_suivi = self.ui.page_suivi
        page_enregistrer = self.ui.page_enregistrer_instrument
        page_nouvelle_verification = self.ui.page_nouvelle_verification
        page_archives = self.ui.page_archives
        page_export = self.ui.page_export
       
        # Exemple pour appeler la fonction quand un bouton est cliqué
        self.ui.bouton_confirmer_instrument.clicked.connect(lambda: tf.print_instrument_data(self))

app = QApplication([])
window = Window()
window.show()
app.exec()