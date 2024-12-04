"""Harmonics Info"""


from PySide6.QtWidgets import (
    QGroupBox,
    QLabel,
    QSpinBox,
)
from PySide6.QtGui import Qt
#------------------------------------------------------------------------------
from adsrinfo import ADSRInfo


class HarmonicsInfo(QGroupBox):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.__ui_settings()
        self.__ui_layout()

    def __init_ui(self):
        # Harmonic #
        self.harmonicnum_label = QLabel("Harmonic #:")
        self.harmonicnum_spin = QSpinBox()
        # Amplitude
        self.amplitude_label = QLabel("Amplitude (%):")
        self.amplitude_spin = QSpinBox()
        # ADSR Information
        self.adsr_info = ADSRInfo()

    def __ui_settings(self):
        ...

    def __ui_layout(self):
        ...