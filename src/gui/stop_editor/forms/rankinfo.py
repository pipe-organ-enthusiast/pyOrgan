"""Rank Info"""
from PySide6.QtWidgets import (
    QGroupBox,
    QTabWidget,
    QLabel,
    QSpinBox,
    QComboBox,
    QFormLayout,
    QVBoxLayout
)
from PySide6.QtGui import Qt
#------------------------------------------------------------------------------
from .finetuningtabs import FineTuningTabs


class RankInfo(QGroupBox):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.__ui_settings()
        self.__ui_layout()

    def __init_ui(self):
        # Rank #
        self.ranknum_label = QLabel("Rank #:")
        self.ranknum_spin = QSpinBox()
        # Rank Size
        self.ranksize_label = QLabel("Rank Size:")
        self.ranksize_combo = QComboBox()
        # Number of Pipes
        self.numpipes_label = QLabel("Number of Pipes:")
        self.numpipes_spin = QSpinBox()
        # Starting Note
        self.startnote_label = QLabel("Starting Note:")
        self.startnote_combo = QComboBox()
        # Pipe Type
        self.pipetype_label = QLabel("PipeType:")
        self.pipetype_combo = QComboBox()
        # Frequency Offset
        self.freqoffset_label = QLabel("Frequency Offset (Hz):")
        self.freqoffset_spin = QSpinBox()
        # Number of Harmonics
        self.numharmonics_label = QLabel("Number of Harmonics")
        self.numharmonics_spin = QSpinBox()
        # Fine Tuning
        self.finetuning = FineTuningTabs()

    def __ui_settings(self):
        self.setTitle("Rank Settings")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # ComboBoxes
        combos = (
            self.ranksize_combo,
            self.startnote_combo,
            self.pipetype_combo,
        )
        for combo in combos:
            combo.setFixedWidth(300)
            combo.setEditable(True)
            edit = combo.lineEdit()
            edit.setAlignment = Qt.AlignmentFlag.AlignCenter
            edit.setReadOnly(True)
        # SpinBoxes
        spins = (
            self.ranknum_spin,
            self.numpipes_spin,
            self.freqoffset_spin,
            self.numharmonics_spin
        )
        for spin in spins:
            spin.setFixedWidth(50)
            spin.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def __ui_layout(self):
        widgets = (
            (self.ranknum_label, self.ranknum_spin),
            (self.ranksize_label, self.ranksize_combo),
            (self.numpipes_label, self.numpipes_spin),
            (self.startnote_label, self.startnote_combo),
            (self.pipetype_label, self.pipetype_combo),
            (self.freqoffset_label, self.freqoffset_spin),
            (self.numharmonics_label, self.numharmonics_spin),
        )
        form_layout = QFormLayout()
        for widget in widgets:
            form_layout.addRow(widget[0], widget[1])
        #----------------------------------------------------------------------
        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addSpacing(20)
        layout.addWidget(self.finetuning)
        self.setLayout(layout)
