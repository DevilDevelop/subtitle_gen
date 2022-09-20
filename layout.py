from PyQt6.QtWidgets import QGridLayout
from window import Window


class Layout(QGridLayout):
    def __init__(self, window: Window) -> None:
        super().__init__(window)
        
