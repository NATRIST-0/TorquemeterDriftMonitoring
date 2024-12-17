#!/usr/bin/python3
# author: Tristan Gayrard

"""
Torquemeters Drift Monitoring
"""

import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QVBoxLayout, QHBoxLayout, QStyle, QSizePolicy, 
    QStackedWidget, QLineEdit, QMessageBox
)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

TITLE_STYLE = "font-size: 25px; font-weight: bold;"

class InstrumentApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Torquemeters Drift Monitoring")
        self.setGeometry(50, 50, 1440, 800)
        
        icon_path = os.path.join(os.path.dirname(__file__), "add_ons", "EVO.png")
        self.setWindowIcon(QIcon(icon_path))

        self.stacked_widget = QStackedWidget()

        # Initialize pages first
        self.suivi_page = SuiviVerificationPage(self)
        self.nouvelle_verification_page = NouvelleVerificationPage(self)
        self.archives_page = ArchivesPage(self)
        self.enregistrer_instrument_page = EnregistrerInstrumentPage(self)
        
        # Main page is initialized after other pages
        self.main_page = QWidget()
        self.setup_main_page()

        # Add pages to the stacked widget
        self.stacked_widget.addWidget(self.main_page)
        self.stacked_widget.addWidget(self.suivi_page)
        self.stacked_widget.addWidget(self.nouvelle_verification_page)
        self.stacked_widget.addWidget(self.archives_page)
        self.stacked_widget.addWidget(self.enregistrer_instrument_page)

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)


    def setup_main_page(self):
        main_layout = QVBoxLayout()
        title_label = QLabel("Suivi Interne de la dérive des Couplemètres")
        title_label.setStyleSheet(TITLE_STYLE)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)
        
        pixmap_path = os.path.join(os.path.dirname(__file__), "add_ons", "EVO.png")
        self.pixmap = QPixmap(pixmap_path).scaled(200, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        
        logo_label = QLabel()
        logo_label.setPixmap(self.pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(logo_label)

        buttons = [
            ("Suivi des Vérifications", QStyle.StandardPixmap.SP_FileDialogContentsView, self.suivi_page),
            ("Nouvelle Vérification", QStyle.StandardPixmap.SP_FileDialogNewFolder, self.nouvelle_verification_page),
            ("Archives", QStyle.StandardPixmap.SP_DialogOpenButton, self.archives_page),
            ("Enregistrer un Nouvel Instrument", QStyle.StandardPixmap.SP_DialogSaveButton, self.enregistrer_instrument_page)
        ]

        for text, icon, page in buttons:
            button = self.create_button(text, icon)
            button.clicked.connect(lambda checked, p=page: self.stacked_widget.setCurrentWidget(p))
            main_layout.addWidget(button)
        
        main_layout.addStretch()
        self.main_page.setLayout(main_layout)

    def create_button(self, text, icon_style):
        button = QPushButton(text, self)
        button.setIcon(self.style().standardIcon(icon_style))
        button.setMinimumHeight(70)
        return button


# ----- Pages secondaires -----
class SuiviVerificationPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Suivi des Vérifications")

        layout = QVBoxLayout()
        label = QLabel("Suivi des Vérifications")
        label.setStyleSheet("font-size: 25px; font-weight: bold;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        btn_home = QPushButton("Retour à l'accueil")
        btn_home.clicked.connect(lambda: parent.stacked_widget.setCurrentWidget(parent.main_page))
        layout.addWidget(btn_home)

        self.setLayout(layout)
        layout.addStretch()  # Pousse les boutons vers le haut



class NouvelleVerificationPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nouvelle Vérification")

        layout = QVBoxLayout()
        label = QLabel("Nouvelle Vérification")
        label.setStyleSheet("font-size: 25px; font-weight: bold;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        btn_home = QPushButton("Retour à l'accueil")
        btn_home.clicked.connect(lambda: parent.stacked_widget.setCurrentWidget(parent.main_page))
        layout.addWidget(btn_home)

        self.setLayout(layout)
        layout.addStretch()  # Pousse les boutons vers le haut



class ArchivesPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Archives")

        layout = QVBoxLayout()
        label = QLabel("Archives")
        label.setStyleSheet("font-size: 25px; font-weight: bold;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        btn_home = QPushButton("Retour à l'accueil")
        btn_home.clicked.connect(lambda: parent.stacked_widget.setCurrentWidget(parent.main_page))
        layout.addWidget(btn_home)

        self.setLayout(layout)
        layout.addStretch()  # Pousse les boutons vers le haut



class EnregistrerInstrumentPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Enregistrer un Nouvel Instrument")

        # Layout principal
        layout = QVBoxLayout()
        
        # Titre de la page
        label = QLabel("Enregistrement d'un Nouvel Instrument")
        label.setStyleSheet("font-size: 25px; font-weight: bold;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        
        # Champ de saisie du nom de l'instrument
        self.txt_nom = QLineEdit()
        self.txt_nom.setPlaceholderText("Nom du nouvel Instrument")
        layout.addWidget(self.txt_nom)
        
        # Champ de saisie de l'étendue de l'instrument
        self.txt_etendue = QLineEdit()
        self.txt_etendue.setPlaceholderText("Étendue de l'instrument (ex: Do1 - Do7)")
        layout.addWidget(self.txt_etendue)
        
        # Bouton d'enregistrement
        self.btn_save = QPushButton("Enregistrer l'instrument")
        self.btn_save.clicked.connect(self.enregistrer_instrument)
        layout.addWidget(self.btn_save)
        
        # Bouton de retour à l'accueil
        btn_home = QPushButton("Retour à l'accueil")
        btn_home.clicked.connect(lambda: parent.stacked_widget.setCurrentWidget(parent.main_page))
        layout.addWidget(btn_home)
        
        # Ajout d'espace flexible pour pousser les widgets vers le haut
        layout.addStretch()
        
        # Application du layout à la fenêtre
        self.setLayout(layout)
    
    def enregistrer_instrument(self):
        """Récupère les informations des champs et les affiche (ou les enregistre dans une base de données)."""
        nom_instrument = self.txt_nom.text()
        etendue_instrument = self.txt_etendue.text()
        
        if nom_instrument and etendue_instrument:
            print(f"Instrument enregistré : {nom_instrument}, Étendue : {etendue_instrument}")
        else:
            print("Veuillez remplir tous les champs avant d'enregistrer.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InstrumentApp()
    window.show()
    sys.exit(app.exec())
