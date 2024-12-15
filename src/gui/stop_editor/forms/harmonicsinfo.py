"""Harmonics Info"""
from PySide6.QtWidgets import (
    QGroupBox,
    QLabel,
    QSpinBox,
    QFormLayout,
    QVBoxLayout
)
from PySide6.QtGui import Qt
#------------------------------------------------------------------------------
from .adsrinfo import ADSRInfo


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
        self.setTitle("Harmonics Settings")
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        # SpinBoxes
        spins = (
            self.harmonicnum_spin,
            self.amplitude_spin
        )
        for spin in spins:
            spin.setFixedWidth(50)
            spin.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def __ui_layout(self):
        widgets = (
            (self.harmonicnum_label, self.harmonicnum_spin),
            (self.amplitude_label, self.amplitude_spin)
        )
        form_layout = QFormLayout()
        for widget in widgets:
            form_layout.addRow(widget[0], widget[1])
        #----------------------------------------------------------------------
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addLayout(form_layout)
        layout.addSpacing(20)
        layout.addWidget(self.adsr_info)
        self.setLayout(layout)
