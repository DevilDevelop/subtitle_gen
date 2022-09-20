from PyQt6.QtWidgets import QComboBox
from window import Window


class ComboBox(QComboBox):
    def __init__(self, window: Window, items: list[str], action) -> None:
        super().__init__(window)
        self.addItems(items)
        self.currentTextChanged.connect(action)
