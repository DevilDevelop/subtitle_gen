from PyQt6.QtWidgets import QPushButton
from window import Window

class Button(QPushButton):
    def __init__(self, window: Window, text: str, action) -> None:
        super().__init__(window)
        self.setText(text)
        self.clicked.connect(action)
