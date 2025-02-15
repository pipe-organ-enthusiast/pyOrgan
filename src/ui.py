from gui import MainWindow, StopEditor
from organ import organlib
#------------------------------------------------------------------------------
from PySide6.QtWidgets import QApplication


class StopEditorUI(StopEditor):
    def __init__(self):
        super().__init__()
        self.__ui_settings()

    def __ui_settings(self):
        # Stop Name
        stop_names: tuple[str] = ("",) + organlib.STOP_NAMES
        self.stopname_combo_populate(stop_names)
        self.stopname_combo_action(self.update_stopname)
        # Stop Family
        stop_families: tuple[str] = ("",) + organlib.STOP_FAMILIES
        self.__stopfamily_combo.addItems(stop_families)

    #**************************************************************************
    # Actions
    #**************************************************************************
    def update_stopname(self):
        ...


if __name__ == "__main__":
    app = QApplication([])
    window = StopEditorUI()
    window.show()
    app.exec()
