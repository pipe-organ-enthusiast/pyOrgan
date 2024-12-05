"""Pipe Info"""
from PySide6.QtWidgets import (
    QGroupBox,
    QLabel,
    QSpinBox,
    QComboBox,
    QFormLayout
)
from PySide6.QtGui import Qt


class PipeInfo(QGroupBox):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.__ui_settings()
        self.__ui_layout()

    def __init_ui(self):
        # Rank #
        self.ranknum_label = QLabel("Rank #:")
        self.ranknum_spin = QSpinBox()
        # Pipe #
        self.pipenum_label = QLabel("Pipe #:")
        self.pipenum_spin = QSpinBox()        
        # Note
        self.note_label = QLabel("Note:")
        self.note_combo = QComboBox()
        # Relative Note
        self.relnote_label = QLabel("Relative Note:")
        self.relnote_combo = QComboBox()

    def __ui_settings(self):
        self.setTitle("Pipe Information")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def __ui_layout(self):
        widgets = (
            (self.ranknum_label, self.ranknum_spin),
            (self.pipenum_label, self.pipenum_spin),
            (self.note_label, self.note_combo),
            (self.relnote_label, self.relnote_combo)
        )
        layout = QFormLayout()
        for widget in widgets:
            layout.addRow(widget[0], widget[1])
        self.setLayout(layout)
