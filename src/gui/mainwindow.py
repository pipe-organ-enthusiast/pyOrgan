"""Main Window"""
from PySide6.QtWidgets import (
    QMainWindow
)
from PySide6.QtGui import Qt
#------------------------------------------------------------------------------
from stop_editor import StopEditor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.__ui_settings()
        self.__ui_layout()

    #--------------------------------------------------------------------------
    # Widgets
    #--------------------------------------------------------------------------
    def __init_ui(self):
        self.__init_ui_menubar()
        self.__init_ui_forms()

    def __init_ui_menubar(self):
        menu = self.menuBar()

    def __init_ui_forms(self):
        self.stopeditor = StopEditor()
        #self.setCentralWidget(self.stopeditor)

    #--------------------------------------------------------------------------
    # Settings
    #--------------------------------------------------------------------------
    def __ui_settings(self):
        self.setWindowTitle("PyOrgan")

    #--------------------------------------------------------------------------
    # Layout
    #--------------------------------------------------------------------------
    def __ui_layout(self):
        self.showMaximized()


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication([])
    window = MainWindow()
    app.exec()
