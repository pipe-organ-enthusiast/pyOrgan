"""Stop Editor"""
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout
)
from PySide6.QtGui import Qt
#------------------------------------------------------------------------------
from .forms.stopeditortabs import StopEditorTabs


class StopEditor(QFrame):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.__ui_settings()
        self.__ui_layout()

    def __init_ui(self):
        # Header
        self.header_label = QLabel("Stop:")
        self.header_edit = QLineEdit()
        # Editor
        self.editor = StopEditorTabs()
        # Options
        self.load_button = QPushButton("Load Stop")
        self.clear_button = QPushButton("Clear Changes")
        self.save_button = QPushButton("Save Stop")

    def __ui_settings(self):
        self.setWindowTitle("pyOrgan - Stop Editor")
        self.setFixedWidth(560)
        #----------------------------------------------------------------------
        self.header_edit.setFixedWidth(410)
        self.header_edit.setReadOnly(True)
        #----------------------------------------------------------------------
        self.editor.setFixedWidth(445)

    def __ui_layout(self):
        header = (
            self.header_label,
            self.header_edit
        )
        header_layout = QHBoxLayout()
        for widget in header:
            header_layout.addWidget(widget)
        #----------------------------------------------------------------------
        options_layout = QVBoxLayout()
        options_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        options = (
            self.load_button,
            self.clear_button,
            self.save_button
        )
        for widget in options:
            options_layout.addWidget(widget)
        #----------------------------------------------------------------------
        form_layout = QVBoxLayout()
        form_layout.addLayout(header_layout)
        form_layout.addWidget(self.editor)
        #----------------------------------------------------------------------
        main_layout = QHBoxLayout()
        layouts = (
            form_layout,
            options_layout
        )
        for layout in layouts:
            main_layout.addLayout(layout)
        #----------------------------------------------------------------------
        self.setLayout(main_layout)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication


    app = QApplication([])
    form = StopEditor()
    form.show()
    app.exec()
