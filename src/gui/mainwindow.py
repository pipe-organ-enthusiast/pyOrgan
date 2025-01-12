"""Main Window"""
from PySide6.QtWidgets import (
    QMainWindow,
    QMenu,
)
from PySide6.QtGui import (
    Qt,
    QAction
)
#------------------------------------------------------------------------------
from .stop_editor import StopEditor


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
        self.menu = self.menuBar()
        # Settings Menu
        self.menu_settings = QMenu("&Settings", self)
        self.stopeditor_action = QAction("Stop Editor", self)
        self.menu_settings.addAction(self.stopeditor_action)
        # Add Menus to MenuBar
        self.menu.addMenu(self.menu_settings)

    def __init_ui_forms(self):
        self.stopeditor = StopEditor()

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

