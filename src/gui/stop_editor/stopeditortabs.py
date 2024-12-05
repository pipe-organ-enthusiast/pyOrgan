"""Editor Tabs"""
from PySide6.QtWidgets import (
    QTabWidget
)
from PySide6.QtGui import Qt
#------------------------------------------------------------------------------
from forms import StopInfo
from forms import RankInfo
from forms import HarmonicsInfo
from forms import ADSRInfo
from pipeeditor import PipeEditor


class StopEditorTabs(QTabWidget):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.__ui_settings()
        self.__ui_layout()

    def __init_ui(self):
        # Editor Forms
        self.stop_info = StopInfo()
        self.rank_info = RankInfo()
        self.harmonics_info = HarmonicsInfo()
        self.adsr_info = ADSRInfo()
        self.pipe_editor = PipeEditor()

    def __ui_settings(self):
        ...

    def __ui_layout(self):
        self.addTab(self.stop_info, "Stop Information")
        self.addTab(self.rank_info, "Rank Information")
        self.addTab(self.harmonics_info, "Harmonics Information")
        self.addTab(self.adsr_info, "ADSR Information")
        self.addTab(self.pipe_editor, "Pipe Editor")


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    widget = StopEditorTabs()
    widget.show()
    app.exec()
