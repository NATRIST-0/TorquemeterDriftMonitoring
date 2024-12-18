from PyQt6.QtWidgets import QApplication, QVBoxLayout, QComboBox, QListView, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Liste déroulante personnalisée")

        layout = QVBoxLayout(self)

        # Créer une QComboBox avec une QListView
        combo_box = QComboBox()
        combo_box.setView(QListView())  # Remplace la vue par QListView

        # Ajouter des éléments à la QComboBox
        combo_box.addItem("Pomme")
        combo_box.addItem("Poire")
        combo_box.addItem("Pêche")

        # Connecter le signal de changement de sélection
        combo_box.currentTextChanged.connect(self.on_option_selected)

        # Ajouter la QComboBox au layout
        layout.addWidget(combo_box)

    def on_option_selected(self, option):
        print(f"Vous avez sélectionné : {option}")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.resize(300, 200)
    window.show()
    app.exec()
