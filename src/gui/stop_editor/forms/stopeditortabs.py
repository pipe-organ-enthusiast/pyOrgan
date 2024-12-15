"""Editor Tabs"""
from PySide6.QtWidgets import (
    QTabWidget,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)
from PySide6.QtGui import Qt
#------------------------------------------------------------------------------
from .stopinfo import StopInfo
from .rankinfo import RankInfo
from .pipeeditor import PipeEditor


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
        self.pipe_editor = PipeEditor()
        self.play_button = QPushButton("Play Pipe")

    def __ui_settings(self):
        ...

    def __ui_layout(self):
        widgets = (
            (self.stop_info, "Stop Settings"),
            (self.rank_info, "Rank Settings"),
        )
        for widget in widgets:
            w = QWidget()
            l = QVBoxLayout()
            l.addSpacing(5)
            l.addWidget(widget[0])
            w.setLayout(l)
            self.addTab(w, widget[1])
        #----------------------------------------------------------------------
        pipe_widget = QWidget()
        pipe_layout = QHBoxLayout()
        widgets = (
            self.pipe_editor,
            self.play_button
        )
        for widget in widgets:
            pipe_layout.addWidget(widget, 0, Qt.AlignmentFlag.AlignTop)
        pipe_widget.setLayout(pipe_layout)
        self.addTab(pipe_widget, "Pipe Settings")


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    widget = StopEditorTabs()
    widget.show()
    app.exec()
