"""Rank Info"""
from PySide6.QtWidgets import (
    QGroupBox,
    QLabel,
    QSpinBox,
    QComboBox,
    QFormLayout
)
from PySide6.QtGui import Qt


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

    def __ui_settings(self):
        self.setTitle("Rank Information")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
        layout = QFormLayout()
        for widget in widgets:
            layout.addRow(widget[0], widget[1])
        
        self.setLayout(layout)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    widget = RankInfo()
    widget.show()
    app.exec()
