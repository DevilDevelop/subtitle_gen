from PyQt6.QtWidgets import QWidget


class Window(QWidget):
    def __init__(self, title: str, width: int, height: int) -> None:
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(width, height)



