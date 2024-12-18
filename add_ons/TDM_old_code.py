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
    QStackedWidget, QLineEdit, QMessageBox, QGridLayout, QGroupBox
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

        # Layout principal vertical
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 30, 30, 30)  # Ajout de marges autour du layout
        main_layout.setSpacing(20)

        # Titre de la page
        label_titre = QLabel("Enregistrement d'un Nouvel Instrument")
        label_titre.setStyleSheet("font-size: 20px; font-weight: bold;")
        label_titre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(label_titre)

        # Groupe des champs de saisie
        group_box = QGroupBox("Informations de l'instrument")
        group_layout = QGridLayout()
        group_layout.setSpacing(15)  # Espacement entre les widgets

        # Champ de saisie du nom de l'instrument
        label_nom = QLabel("Nom de l'instrument :")
        self.txt_nom = QLineEdit()
        self.txt_nom.setPlaceholderText("Exemple : EC1166")
        group_layout.addWidget(label_nom, 0, 0)
        group_layout.addWidget(self.txt_nom, 0, 1)

        # Champ de saisie de la valeur cible minimale
        label_cible_min = QLabel("Valeur cible minimale de vérification :")
        self.txt_cible_min = QLineEdit()
        self.txt_cible_min.setPlaceholderText("Exemple : 5")
        group_layout.addWidget(label_cible_min, 1, 0)
        group_layout.addWidget(self.txt_cible_min, 1, 1)
        
        # Champ de saisie de la valeur en milieu de gamme
        label_cible_milieu = QLabel("Valeur cible milieu de gamme de vérification :")
        self.txt_cible_milieu = QLineEdit()
        self.txt_cible_milieu.setPlaceholderText("Exemple : 25")
        group_layout.addWidget(label_cible_milieu, 2, 0)
        group_layout.addWidget(self.txt_cible_milieu, 2, 1)

        # Champ de saisie de la valeur cible minimale
        label_cible_max = QLabel("Valeur cible maximale de vérification :")
        self.txt_cible_max = QLineEdit()
        self.txt_cible_max.setPlaceholderText("Exemple : 50")
        group_layout.addWidget(label_cible_max, 3, 0)
        group_layout.addWidget(self.txt_cible_max, 3, 1)

        group_box.setLayout(group_layout)
        main_layout.addWidget(group_box)

        # Layout pour les boutons
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)

        # Bouton d'enregistrement
        self.btn_save = QPushButton("Enregistrer l'instrument")
        self.btn_save.clicked.connect(self.enregistrer_instrument)
        button_layout.addWidget(self.btn_save)

        # Bouton de retour à l'accueil
        btn_home = QPushButton("Retour à l'accueil")
        btn_home.clicked.connect(lambda: parent.stacked_widget.setCurrentWidget(parent.main_page))
        button_layout.addWidget(btn_home)

        # Centrer les boutons
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addLayout(button_layout)

        # Appliquer le layout principal
        self.setLayout(main_layout)

    def enregistrer_instrument(self):
        """Récupère les informations des champs et vérifie leur validité."""
        nom_instrument = self.txt_nom.text()
        cible_min = self.txt_cible_min.text()
        cible_milieu = self.txt_cible_milieu.text()
        cible_max = self.txt_cible_max.text()

        # Vérifier si les champs sont remplis
        if not nom_instrument or not cible_min or not cible_max or not cible_milieu:
            QMessageBox.warning(self, "Champs manquants", "Veuillez remplir tous les champs.")
            return

        # Vérifier si les valeurs sont numériques
        try:
            cible_min = float(cible_min)
            cible_milieu = float(cible_milieu)
            cible_max = float(cible_max)
        except ValueError:
            QMessageBox.warning(self, "Erreur de saisie", "Les valeurs d'étendue doivent être des nombres.")
            return

        # Vérifier la cohérence des valeurs
        if cible_min >= cible_max:
            QMessageBox.warning(self, "Erreur de cohérence", "La valeur minimale doit être inférieure à la valeur maximale.")
            return

        # Confirmation d'enregistrement
        QMessageBox.information(
            self, 
            "Instrument Enregistré", 
            f"Instrument enregistré : {nom_instrument}\n"
            f"Cibles de mesures : {cible_min}, {cible_milieu}, {cible_max}"
        )
        print(f"Instrument enregistré : {nom_instrument}, Cibles de mesures : {cible_min}, {cible_milieu}, {cible_max}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InstrumentApp()
    window.show()
    sys.exit(app.exec())
