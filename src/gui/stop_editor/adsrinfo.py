"""ADSR Info"""


from PySide6.QtWidgets import (
    QGroupBox,
    QLabel,
    QSpinBox
)
from PySide6.QtGui import Qt


class ADSRInfo(QGroupBox):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.__ui_settings()
        self.__ui_layout()

    def __init_ui(self):
        # Attack Time
        self.attack_label = QLabel("Attack Time (ms):")
        self.attack_spin = QSpinBox()
        # Decay Time
        self.decay_label = QLabel("Decay Time (ms):")
        self.decay_spin = QSpinBox()
        # Sustain Level
        self.sustain_label = QLabel("Sustain Level (%):")
        self.sustain_spin = QSpinBox()
        # Release Time
        self.release_label = QLabel("Release Time (ms):")
        self.release_spin = QSpinBox()

    def __ui_settings(self):
        ...

    def __ui_layout(self):
        ...