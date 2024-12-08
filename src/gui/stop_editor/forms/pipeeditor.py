"""Pipe Editor"""
from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout
)
from PySide6.QtGui import Qt
#------------------------------------------------------------------------------
from .pipeinfo import PipeInfo
from .harmonicsinfo import HarmonicsInfo
from .adsrinfo import ADSRInfo
#from pipeeditortabs import PipeEditorTabs


class PipeEditor(QFrame):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.__ui_settings()
        self.__ui_layout()

    def __init_ui(self):
        self.pipe_info = PipeInfo()
        #self.pipe_editor_tabs = PipeEditorTabs()
        self.harmonics_info = HarmonicsInfo()
        self.adsr_info = ADSRInfo()

    def __ui_settings(self):
        ...

    def __ui_layout(self):
        widgets = (
            self.pipe_info,
            #self.pipe_editor_tabs
            self.harmonics_info,
            self.adsr_info
        )
        layout = QVBoxLayout()
        for widget in widgets:
            layout.addWidget(widget)
        self.setLayout(layout)
