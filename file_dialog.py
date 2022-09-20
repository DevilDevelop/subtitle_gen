from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import Qt
from button import Button
from window import Window
from layout import Layout
from combo_box import ComboBox
from label import Label
from video import Video


class FileDialog:
    def __init__(self) -> None:
        self.languages_options = ['Auto', 'pt-BR', 'en-US']
        self.translate_options = ['None', 'pt-BR', 'en-US']
        self.file_path = None
        self.video_language = None
        self.translate_language = None
        self.window = Window('Open File', 400, 200)
        self.layout = Layout(self.window)
        self.open_file_label = Label(self.window, 'Select File:', 11)
        self.browse_button = Button(self.window, 'Open Folder', self.open_folder)
        self.video_language_label = Label(self.window, 'Select video language:', 11)
        self.language_box = ComboBox(self.window, self.languages_options, self.change_video_language)
        self.translate_label = Label(self.window, 'Translate to:', 11)
        self.translate_box = ComboBox(self.window, self.translate_options, self.change_translate_language)
        self.continue_button = Button(self.window, 'Continue', self.proceed)
        self.layout.addWidget(self.open_file_label, 0, 0, Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.browse_button, 1, 0, Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.video_language_label, 2, 0, Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.language_box, 3, 0, Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.translate_label, 4, 0, Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.translate_box, 5, 0, Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.continue_button, 6, 1, Qt.AlignmentFlag.AlignRight)
        self.window.show()

    def open_folder(self) -> None:
        file_path = QFileDialog.getOpenFileName(self.window)
        self.file_path = file_path[0]

    def change_video_language(self) -> None:
        if self.language_box.currentText() != 'Auto':
            self.video_language = self.language_box.currentText()

    def change_translate_language(self) -> None:
        if self.translate_box.currentText() != 'None':
            self.translate_language = self.translate_box.currentText()

    def proceed(self) -> None:
        if self.file_path:
            self.browse_button.setEnabled(False)
            self.language_box.setEnabled(False)
            self.translate_box.setEnabled(False)
            self.continue_button.setEnabled(False)
            video = Video(self.file_path, self.video_language, self.translate_language)
            video.create_subtitles()
            self.window.close()
