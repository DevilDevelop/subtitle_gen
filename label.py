from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QFont
from window import Window


class Label(QLabel):
    def __init__(self, window: Window, text: str, font_size: int) -> None:
        super().__init__(window)
        self.setText(text)
        self.setFont(QFont('Arial', font_size))