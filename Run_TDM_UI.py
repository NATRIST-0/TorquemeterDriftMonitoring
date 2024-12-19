#!/usr/bin/python3
# author: Tristan Gayrard
 
"""
Run Torquemeters Drift Monitoring UI
"""
 
import TDM_fonctions as tf
from TDM import Ui_StackedWidget
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
import sqlite3

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 888, 551)

        # Create a QStackedWidget as the central widget
        self.stackedWidget = QStackedWidget(self)
        self.setCentralWidget(self.stackedWidget)

        # Create the UI
        self.ui = Ui_StackedWidget()
        self.ui.setupUi(self.stackedWidget)
        
        # Créer table SQLite
        tf.creer_table(self)
        
        # Add icons to buttons
        tf.icones_boutons(self)

        # Setup navigation between pages
        tf.setup_navigation(self)

        # Define the various pages in the application
        self.ui.bouton_confirmer_instrument.clicked.connect(lambda: tf.enregistrer_donnees_instrument(self))

app = QApplication([])
window = Window()
window.show()
app.exec()