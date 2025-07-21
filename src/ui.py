from PySide6.QtWidgets import (
        QMainWindow,
        QWidget,
        QToolBar,
        #QDockWidget,
        QFrame,
        QGroupBox,
        QLabel,
        QSpinBox,
        QComboBox,
        QCheckBox,
        #QPushButton,
        QFormLayout,
        QVBoxLayout
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt, QSize
import os


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()
        self.settings_ui()
        self.layout_ui()

    def init_ui(self) -> None:
        self.sidebar: QToolBar = QToolBar()

    def settings_ui(self) -> None:
        path = os.path.dirname(__file__)
        os.chdir(path)
        self.sidebar.setIconSize(QSize(30, 30))
        self.sidebar.setMovable(False)
        sidebar_actions: dict[str, QAction] = {
            "Organ Settings": QAction(QIcon("icons/organ.png"), "", self),
            "Audio Settings": QAction(QIcon("icons/audio.png"), "", self),
            "MIDI Settings": QAction(QIcon("icons/midi.png"), "", self)
        }
        for action in sidebar_actions.values():
            self.sidebar.addAction(action)
            self.sidebar.addSeparator()

    def layout_ui(self) -> None:
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.sidebar)


class OrganSettings(QFrame):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()
        self.settings_ui()
        self.layout_ui()

    def init_ui(self) -> None:
        self.header_label: QLabel = QLabel("General Organ Settings")
        # ---------------------------------------------------------------------
        # Organ Settings
        # ---------------------------------------------------------------------
        self.organ_settings: QGroupBox = QGroupBox("Organ")
        self.num_divisions_label: QLabel = QLabel("Number of Divisions:")
        self.num_divisions_spin: QSpinBox = QSpinBox()
        self.num_generals_label: QLabel = QLabel("Number of Generals:")
        self.num_generals_spin: QSpinBox = QSpinBox()
        # ---------------------------------------------------------------------
        # Division Settings
        # ---------------------------------------------------------------------
        self.division_settings: QGroupBox = QGroupBox("Divisions")
        self.division_num_label: QLabel = QLabel("Division #:")
        self.division_num_spin: QSpinBox = QSpinBox()
        self.division_name_label: QLabel = QLabel("Division Name:")
        self.division_name_combo: QComboBox = QComboBox()
        self.num_stops_label: QLabel = QLabel("Number of Stops:")
        self.num_stops_spin: QSpinBox = QSpinBox()
        self.num_divisionals_label: QLabel = QLabel("Number of Divisionals:")
        self.num_divisionals_spin: QSpinBox = QSpinBox()
        self.tremulant_label: QLabel = QLabel("Include Tremulant:")
        self.tremulant_check: QCheckBox = QCheckBox()
        self.enclosed_label: QLabel = QLabel("Enclosed:")
        self.enclosed_check: QCheckBox = QCheckBox()

    def settings_ui(self) -> None:
        self.header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.organ_settings.setFixedSize(400, 100)
        self.division_settings.setFixedSize(400, 210)
        groupboxes: list[QGroupBox] = [
            self.organ_settings,
            self.division_settings,
        ]
        for groupbox in groupboxes:
            groupbox.setAlignment(
                Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
            )

        spinboxes: list[QSpinBox] = [
            self.num_divisions_spin,
            self.num_generals_spin,
            self.division_num_spin,
            self.num_stops_spin,
            self.num_divisionals_spin,
        ]
        for spinbox in spinboxes:
            spinbox.setFixedWidth(50)
            spinbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def layout_ui(self) -> None:
        # ---------------------------------------------------------------------
        # Organ Settings Layout
        # ---------------------------------------------------------------------
        organ_settings_layout: QFormLayout = QFormLayout()
        organ_settings_widgets: list[tuple[QLabel, QWidget]] = [
            (self.num_divisions_label, self.num_divisions_spin),
            (self.num_generals_label, self.num_generals_spin)
        ]
        self.form_layout(
            layout=organ_settings_layout,
            widgets=organ_settings_widgets,
            form=self.organ_settings
        )
        # ---------------------------------------------------------------------
        # Division Settings Layout
        # ---------------------------------------------------------------------
        division_settings_layout: QFormLayout = QFormLayout()
        division_settings_widgets: list[tuple[QLabel, QWidget]] = [
            (self.division_num_label, self.division_num_spin),
            (self.division_name_label, self.division_name_combo),
            (self.num_stops_label, self.num_stops_spin),
            (self.num_divisionals_label, self.num_divisionals_spin),
            (self.tremulant_label, self.tremulant_check),
            (self.enclosed_label, self.enclosed_check),
        ]
        self.form_layout(
            layout=division_settings_layout,
            widgets=division_settings_widgets,
            form=self.division_settings
        )
        # ---------------------------------------------------------------------
        # Form Layout
        # ---------------------------------------------------------------------
        layout: QVBoxLayout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        widgets: list[QWidget] = [
            self.header_label,
            self.organ_settings,
            self.division_settings,
        ]
        for widget in widgets:
            layout.addWidget(widget)
            layout.addSpacing(10)
        self.setLayout(layout)

    def form_layout(
            self,
            layout: QFormLayout,
            widgets: list[tuple[QLabel, QWidget]],
            form: QGroupBox
    ) -> None:
        for widget in widgets:
            layout.addRow(widget[0], widget[1])
        form.setLayout(layout)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app: QApplication = QApplication()
    win: QWidget = MainWindow()
    win.show()
    app.exec()
