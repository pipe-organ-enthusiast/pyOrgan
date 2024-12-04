"""Stop Editor"""


from PySide6.QtWidgets import (
    QFrame
)
from PySide6.QtGui import Qt
#------------------------------------------------------------------------------
from generalstopeditor import GeneralStopEditor
from pipeeditor import PipeEditor


class StopEditor(QFrame):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.__ui_settings()
        self.__ui_layout()

    def __init_ui(self):
        self.general_stop_editor = GeneralStopEditor()
        self.pipe_editor = PipeEditor()

    def __ui_settings(self):
        ...

    def __ui_layout(self):
        ...
