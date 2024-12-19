#!/usr/bin/python3
# author: Tristan Gayrard

"""
Torquemeters Drift Monitoring fonctions
"""

import sqlite3
from PyQt6.QtWidgets import QStyle, QMessageBox, QLineEdit


def creer_table(window):
    conn = sqlite3.connect("TDM.db")
    cursor = conn.cursor()
    
    # Create instruments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS instruments (
            ref INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE)""")
        
    # Create measurements table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS measurements (
            ref INTEGER PRIMARY KEY AUTOINCREMENT,
            ref_instrument TEXT,
            timestamp TEXT NOT NULL,
            Cmin REAL NOT NULL,
            Cmilieu REAL NOT NULL,
            Cmax REAL NOT NULL,
            tolerance REAL NOT NULL,
            FOREIGN KEY (ref_instrument) REFERENCES instruments (name))""")
    conn.commit()
    conn.close()
        
def enregister_info_instru_sql(window, instrument_info):
    ref_instrument = instrument_info[0]
    Cmin = instrument_info[1]
    Cmilieu = instrument_info[2]
    Cmax = instrument_info[3]
    tolerance = instrument_info[4]

    conn = sqlite3.connect("TDM.db")
    cursor = conn.cursor()

    try:
        # Check if instrument exists in instruments table
        cursor.execute("SELECT ref FROM instruments WHERE name = ?", (ref_instrument,))
        result = cursor.fetchone()

        # If instrument doesn't exist, insert it
        if not result:
            cursor.execute("INSERT INTO instruments (name) VALUES (?)", (ref_instrument,))
            conn.commit()
            cursor.execute("SELECT ref FROM instruments WHERE name = ?", (ref_instrument,))
            result = cursor.fetchone()

        ref_instrument_id = result[0]

        # Insert measurements
        cursor.execute("""
            INSERT INTO measurements (ref_instrument, timestamp, Cmin, Cmilieu, Cmax, tolerance)
            VALUES (?, datetime('now'), ?, ?, ?, ?)""",
            (ref_instrument_id, Cmin, Cmilieu, Cmax, tolerance))
        conn.commit()

        QMessageBox.information(window, "Succès", "Données enregistrées dans la base de données.")
    except sqlite3.Error as e:
        QMessageBox.critical(window, "Erreur", f"Une erreur s'est produite : {e}")
    finally:
        conn.close()

def enregistrer_donnees_instrument(window):
    # Get values from input fields
    ref_instrument = window.ui.page_enregistrer_instrument.findChild(QLineEdit, "ref_instrument")
    Cmin = window.ui.page_enregistrer_instrument.findChild(QLineEdit, "Cmin")
    Cmilieu = window.ui.page_enregistrer_instrument.findChild(QLineEdit, "Cmilieu")
    Cmax = window.ui.page_enregistrer_instrument.findChild(QLineEdit, "Cmax")
    tolerance = window.ui.page_enregistrer_instrument.findChild(QLineEdit, "tolerance")
    
    if not ref_instrument or not Cmin or not Cmilieu or not Cmax or not tolerance:
        QMessageBox.warning(window, "Champs manquants", "Veuillez remplir tous les champs.")
        return

    try:
        Cmin = float(Cmin.text())
        Cmilieu = float(Cmilieu.text())
        Cmax = float(Cmax.text())
        tolerance = float(tolerance.text())
        
    except ValueError:
        QMessageBox.warning(window, "Erreur de saisie", "Les valeurs d'étendue doivent être des nombres.")
        return

    if Cmin >= Cmax:
        QMessageBox.warning(window, "Erreur de cohérence", "La valeur minimale doit être inférieure à la valeur maximale.")
        return

    # Confirmation message
    QMessageBox.information(
        window, 
        "Instrument Enregistré", 
        f"Instrument enregistré : {ref_instrument.text()}\n"
        f"Cibles de mesures : {Cmin}, {Cmilieu}, {Cmax}\n"
        f"Tolérence = {tolerance}")
    print(f"Instrument enregistré : {ref_instrument.text()}, Cibles de mesures : {Cmin}, {Cmilieu}, {Cmax}, Tolérance = {tolerance}")
    instrument_info = [ref_instrument.text(), Cmin, Cmilieu, Cmax, tolerance]
    
    #enregister_info_instru_sql(window, instrument_info)

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
