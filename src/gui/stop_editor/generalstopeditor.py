"""General Stop Editor"""


from PySide6.QtWidgets import (
    QFrame
)
from PySide6.QtGui import Qt
#------------------------------------------------------------------------------
from stopinfo import StopInfo
from rankinfo import RankInfo


class GeneralStopEditor(QFrame):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.__ui_settings()
        self.__ui_layout()

    def __init_ui(self):
        self.stop_info = StopInfo()
        self.rank_info = RankInfo()

    def __ui_settings(self):
        ...

    def __ui_layout(self):
        ...