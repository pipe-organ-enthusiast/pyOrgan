"""Stop Info"""


from PySide6.QtWidgets import (
    QGroupBox,
    QLabel,
    QComboBox,
    QSpinBox,
    QFormLayout
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
        #self.stoptype_label = QLabel("Stop Type:")
        #self.stoptype_combo = QComboBox()
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
        self.setTitle("Stop Settings")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # ComboBoxes
        combos = (
            self.stopname_combo,
            #self.stoptype_combo,
            self.stopfamily_combo,
            self.organdivision_combo,
            self.rankseries_combo
        )
        for combo in combos:
            combo.setFixedWidth(300)
            combo.setEditable(True)
            edit = combo.lineEdit()
            edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
            edit.setReadOnly(True)
        # SpinBox
        self.numranks_spin.setFixedWidth(50)
        self.numranks_spin.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def __ui_layout(self):
        widgets = (
            (self.stopname_label, self.stopname_combo),
            #(self.stoptype_label, self.stoptype_combo),
            (self.stopfamily_label, self.stopfamily_combo),
            (self.organdivision_label, self.organdivision_combo),
            (self.numranks_label, self.numranks_spin),
            (self.rankseries_label, self.rankseries_combo)
        )
        layout = QFormLayout()
        for widget in widgets:
            layout.addRow(widget[0], widget[1])
        self.setLayout(layout)
