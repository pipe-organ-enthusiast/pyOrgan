"""Pipe Editor"""
from PySide6.QtWidgets import (
    QGroupBox,
    QVBoxLayout
)
from PySide6.QtGui import Qt
#------------------------------------------------------------------------------
from .pipeinfo import PipeInfo
from .finetuningtabs import FineTuningTabs


class PipeEditor(QGroupBox):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.__ui_settings()
        self.__ui_layout()

    def __init_ui(self):
        self.pipe_info = PipeInfo()
        self.finetuning = FineTuningTabs()

    def __ui_settings(self):
        self.setTitle("Pipe Editor")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def __ui_layout(self):
        widgets = (
            self.pipe_info,
            self.finetuning
        )
        layout = QVBoxLayout()
        for widget in widgets:
            layout.addWidget(widget)
            layout.addSpacing(20)
        self.setLayout(layout)
