"""Stop Info"""


from PySide6.QtWidgets import (
    QGroupBox,
    QLabel,
    QComboBox,
    QSpinBox
)
from PySide6.QtGui import Qt


class StopInfo(QGroupBox):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.__ui_settings()
        self.__ui_layout()

    def __init_ui(self):
        # Stop Name
        self.stopname_label = QLabel("Stop Name:")
        self.stopname_combo = QComboBox()
        # Stop Type
        self.stoptype_label = QLabel("Stop Type:")
        self.stoptype_combo = QComboBox()
        # Stop Family
        self.stopfamily_label = QLabel("Stop Family:")
        self.stopfamily_combo = QComboBox()
        # Organ Division
        self.organdivision_label = QLabel("Organ Division:")
        self.organdivision_combo = QComboBox()
        # Number of Ranks
        self.numranks_label = QLabel("Number of Rank:")
        self.numranks_spin = QSpinBox()
        # Rank Series
        self.rankseries_label = QLabel("Rank Series:")
        self.rankseries_combo = QComboBox()

    def __ui_settings(self):
        ...

    def __ui_layout(self):
        ...