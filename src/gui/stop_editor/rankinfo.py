"""Rank Info"""


from PySide6.QtWidgets import (
    QGroupBox,
    QLabel,
    QSpinBox,
    QComboBox
)
from PySide6.QtGui import Qt
#------------------------------------------------------------------------------
from harmonicsinfo import HarmonicsInfo
from adsrinfo import ADSRInfo


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
        # Harmonics Information
        self.harmonics_info = HarmonicsInfo()
        # ADSR Information
        self.adsr_info = ADSRInfo()

    def __ui_settings(self):
        ...

    def __ui_layout(self):
        ...