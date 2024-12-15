"""Pipe Editor"""


from PySide6.QtWidgets import (
    QTabWidget,
    QWidget,
    QVBoxLayout
)
from PySide6.QtGui import Qt
#------------------------------------------------------------------------------
from .pipeinfo import PipeInfo
from .harmonicsinfo import HarmonicsInfo
from .adsrinfo import ADSRInfo


class FineTuningTabs(QTabWidget):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.__ui_settings()
        self.__ui_layout()

    def __init_ui(self):
        self.harmonics_info = HarmonicsInfo()
        self.adsr_info = ADSRInfo()

    def __ui_settings(self):
        ...

    def __ui_layout(self):
        widgets = (
            (self.harmonics_info, "Harmonics"),
            (self.adsr_info, "ADSR")
        )
        for widget in widgets:
            w = QWidget()
            l = QVBoxLayout()
            l.addSpacing(10)
            l.addWidget(widget[0])
            w.setLayout(l)
            self.addTab(w, widget[1])


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    widget = FineTuningTabs()
    widget.show()
    app.exec()
