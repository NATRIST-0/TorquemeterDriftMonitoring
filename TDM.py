#!/usr/bin/python3
# author: Tristan Gayrard

"""
Torquemeters Drift Monitoring Menu
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QStyle, QSizePolicy, QStackedWidget
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt  # Import de Qt


class InstrumentApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Torquemeters Drift Monitoring")
        self.setGeometry(250, 100, 1440, 810)  # Taille initiale de la fenêtre

        # Créer le QStackedWidget
        self.stacked_widget = QStackedWidget()
        
        # Page principale
        self.main_page = QWidget()
        self.setup_main_page()

        # Pages secondaires
        self.suivi_page = SuiviVerificationPage(self)
        self.nouvelle_verification_page = NouvelleVerificationPage(self)
        self.archives_page = ArchivesPage(self)
        self.enregistrer_instrument_page = EnregistrerInstrumentPage(self)

        # Ajouter les pages au QStackedWidget
        self.stacked_widget.addWidget(self.main_page)  # Index 0
        self.stacked_widget.addWidget(self.suivi_page)  # Index 1
        self.stacked_widget.addWidget(self.nouvelle_verification_page)  # Index 2
        self.stacked_widget.addWidget(self.archives_page)  # Index 3
        self.stacked_widget.addWidget(self.enregistrer_instrument_page)  # Index 4

        # Mettre le QStackedWidget en layout principal
        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

    def setup_main_page(self):
        """
        Configure la page principale.
        """
        main_layout = QVBoxLayout()

        # Titre
        title_label = QLabel("Suivi Interne de la dérive des Couplemètres")
        title_label.setStyleSheet("font-size: 25px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Logo EvO
        self.pixmap = QPixmap(r"C:\Users\GAYRARD\Documents\GitHub\TorquemeterDriftMonitoring\add_ons\EVO.jpg")
        logo_label = QLabel()
        logo_label.setPixmap(self.pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(logo_label)

        # Boutons
        btn_verification = self.create_button("Suivi des Vérifications", QStyle.SP_FileDialogContentsView)
        btn_verification.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.suivi_page))
        main_layout.addWidget(btn_verification)

        btn_nouvelle_verification = self.create_button("Nouvelle Vérification", QStyle.SP_FileDialogNewFolder)
        btn_nouvelle_verification.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.nouvelle_verification_page))
        main_layout.addWidget(btn_nouvelle_verification)

        btn_archives = self.create_button("Archives", QStyle.SP_DialogOpenButton)
        btn_archives.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.archives_page))
        main_layout.addWidget(btn_archives)

        btn_enregistrer = self.create_button("Enregistrer un Nouvel Instrument", QStyle.SP_DialogSaveButton)
        btn_enregistrer.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.enregistrer_instrument_page))
        main_layout.addWidget(btn_enregistrer)

        main_layout.addStretch()  # Pousse les boutons vers le haut
        self.main_page.setLayout(main_layout)

    def create_button(self, text, icon_style):
        """
        Crée un bouton avec une icône et une taille réglable.
        """
        button = QPushButton(text, self)
        button.setIcon(self.style().standardIcon(icon_style))
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # Largeur adaptable, hauteur fixe
        button.setMinimumHeight(70)  # Hauteur minimale pour un meilleur aspect
        return button


# ----- Pages secondaires -----
class SuiviVerificationPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Suivi des Vérifications")

        layout = QVBoxLayout()
        label = QLabel("Page de Suivi des Vérifications")
        label.setStyleSheet("font-size: 25px; font-weight: bold;")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        btn_home = QPushButton("Retour à l'accueil")
        btn_home.clicked.connect(lambda: parent.stacked_widget.setCurrentWidget(parent.main_page))
        layout.addWidget(btn_home)

        self.setLayout(layout)


class NouvelleVerificationPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nouvelle Vérification")

        layout = QVBoxLayout()
        label = QLabel("Page de Nouvelle Vérification")
        label.setStyleSheet("font-size: 25px; font-weight: bold;")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        btn_home = QPushButton("Retour à l'accueil")
        btn_home.clicked.connect(lambda: parent.stacked_widget.setCurrentWidget(parent.main_page))
        layout.addWidget(btn_home)

        self.setLayout(layout)


class ArchivesPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Archives")

        layout = QVBoxLayout()
        label = QLabel("Page des Archives")
        label.setStyleSheet("font-size: 25px; font-weight: bold;")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        btn_home = QPushButton("Retour à l'accueil")
        btn_home.clicked.connect(lambda: parent.stacked_widget.setCurrentWidget(parent.main_page))
        layout.addWidget(btn_home)

        self.setLayout(layout)


class EnregistrerInstrumentPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Enregistrer un Nouvel Instrument")

        layout = QVBoxLayout()
        label = QLabel("Page d'Enregistrement d'un Nouvel Instrument")
        label.setStyleSheet("font-size: 25px; font-weight: bold;")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        btn_home = QPushButton("Retour à l'accueil")
        btn_home.clicked.connect(lambda: parent.stacked_widget.setCurrentWidget(parent.main_page))
        layout.addWidget(btn_home)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InstrumentApp()
    window.show()
    sys.exit(app.exec_())
