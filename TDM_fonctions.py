#!/usr/bin/python3
# author: Tristan Gayrard

"""
Torquemeters Drift Monitoring fonctions
"""

from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QStyle, QMessageBox, QPushButton, QLineEdit, QTextEdit

def print_instrument_data(self):
    # Récupérer les valeurs des champs sur la page "page_enregistrer_instrument"
    ref_instrument = self.ui.page_enregistrer_instrument.findChild(QTextEdit, "ref_instrument")
    Cmin = self.ui.page_enregistrer_instrument.findChild(QTextEdit, "Cmin")
    Cmilieu = self.ui.page_enregistrer_instrument.findChild(QTextEdit, "Cmilieu")
    Cmax = self.ui.page_enregistrer_instrument.findChild(QTextEdit, "Cmax")
    
    # Vérifier si les champs sont remplis
    if not ref_instrument or not Cmin or not Cmilieu or not Cmax:
        QMessageBox.warning(self, "Champs manquants", "Veuillez remplir tous les champs.")
        return

    # Vérifier si les valeurs sont numériques
    try:
        Cmin = float(Cmin)
        Cmilieu = float(Cmilieu)
        Cmax = float(Cmax)
    except ValueError:
        QMessageBox.warning(self, "Erreur de saisie", "Les valeurs d'étendue doivent être des nombres.")
        return
    # Vérifier la cohérence des valeurs
    if Cmin >= Cmax:
        QMessageBox.warning(self, "Erreur de cohérence", "La valeur minimale doit être inférieure à la valeur maximale.")
        return
    # Confirmation d'enregistrement
    QMessageBox.information(
        self, 
        "Instrument Enregistré", 
        f"Instrument enregistré : {ref_instrument}\n"
        f"Cibles de mesures : {Cmin}, {Cmilieu}, {Cmax}")
    print(f"Instrument enregistré : {ref_instrument}, Cibles de mesures : {Cmin}, {Cmilieu}, {Cmax}")

def icones_boutons(self):
    style = self.style()
    self.ui.pushButton_suivi_verif.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_FileDialogContentsView))
    self.ui.pushButton_nouvelle_verif.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_FileDialogNewFolder))
    self.ui.pushButton_archives.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_DialogOpenButton))
    self.ui.pushButton_nouvel_instru.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_DialogSaveButton))
    self.ui.pushButton_export.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_FileDialogToParent))
        
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
