"""Pipe Editor"""


from PySide6.QtWidgets import (
    QTabWidget
)
from PySide6.QtGui import Qt
#------------------------------------------------------------------------------
from forms.pipeinfo import PipeInfo
from forms.harmonicsinfo import HarmonicsInfo
from forms.adsrinfo import ADSRInfo


class PipeEditorTabs(QTabWidget):
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
        self.addTab(self.harmonics_info, "Harmonics Information")
        self.addTab(self.adsr_info, "ADSR Information")


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    widget = PipeEditorTabs()
    widget.show()
    app.exec()
