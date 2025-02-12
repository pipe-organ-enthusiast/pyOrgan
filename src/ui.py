from gui import MainWindow
#from gui.stop_editor import StopEditor
from organ import organlib
#------------------------------------------------------------------------------
from PySide6.QtWidgets import QApplication


class UI:
    def __init__(self):
        self.__init_ui()
        #self.__config()

    def __init_ui(self):
        self.ui = QApplication([])
        self.mainwindow = MainWindow()

    def __config(self):
        ...

    #**************************************************************************
    def run(self):
        self.ui.exec()


if __name__ == "__main__":
    ui = UI()
    ui.run()
