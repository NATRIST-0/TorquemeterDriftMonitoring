#!/usr/bin/python3
# author: Tristan Gayrard

"""
Torquemeters Drift Monitoring
"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QStyle


class InstrumentApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dérive Couplemètres")
        self.setGeometry(300, 300, 400, 200)

        # Layout principal
        self.layout = QVBoxLayout()

        # Titre principal
        self.label_title = QLabel("Suivi Interne de la dérive des Couplemètres")
        self.layout.addWidget(self.label_title)

        # Bouton 1: Nouvelle Vérification
        self.btn_verification = QPushButton("Nouvelle Vérification", self)
        icon_new = self.style().standardIcon(QStyle.SP_FileDialogNewFolder)
        self.btn_verification.setIcon(icon_new)
        self.btn_verification.clicked.connect(self.nouvelle_verification)
        self.layout.addWidget(self.btn_verification)

        # Bouton 2: Enregistrer un Nouvel Instrument
        self.btn_enregistrer = QPushButton("Enregistrer un Nouvel Instrument", self)
        icon_save = self.style().standardIcon(QStyle.SP_DialogSaveButton)
        self.btn_enregistrer.setIcon(icon_save)
        self.btn_enregistrer.clicked.connect(self.enregistrer_instrument)
        self.layout.addWidget(self.btn_enregistrer)

        # Bouton 3: Archives
        self.btn_archives = QPushButton("Archives", self)
        icon_open = self.style().standardIcon(QStyle.SP_DialogOpenButton)
        self.btn_archives.setIcon(icon_open)
        self.btn_archives.clicked.connect(self.archives)
        self.layout.addWidget(self.btn_archives)

        # Définir le layout principal
        self.setLayout(self.layout)

    # Méthodes associées aux boutons
    def enregistrer_instrument(self):
        QMessageBox.information(self, "Enregistrer Instrument", "Fonctionnalité à venir.")

    def nouvelle_verification(self):
        QMessageBox.information(self, "Nouvelle Vérification", "Fonctionnalité à venir.")

    def archives(self):
        QMessageBox.information(self, "Archives", "Fonctionnalité à venir.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InstrumentApp()
    window.show()
    sys.exit(app.exec_())
