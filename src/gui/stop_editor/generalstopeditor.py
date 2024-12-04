"""General Stop Editor"""


from PySide6.QtWidgets import (
    QFrame
)
from PySide6.QtGui import Qt


class GeneralStopEditor(QFrame):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.__ui_settings()
        self.__ui_layout()

    def __init_ui(self):
        ...

    def __ui_settings(self):
        ...

    def __ui_layout(self):
        ...