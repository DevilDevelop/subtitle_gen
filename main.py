import sys
from PyQt6.QtWidgets import QApplication
from file_dialog import FileDialog


app = QApplication([])
file = FileDialog()
sys.exit(app.exec())

