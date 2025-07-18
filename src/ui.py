from PySide6.QtWidgets import (
        QMainWindow,
        QWidget,
        QFrame,
        QGroupBox,
        QLabel,
        QSpinBox,
        QComboBox,
        QFormLayout,
        QVBoxLayout
)
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()


class OrganSettings(QFrame):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()
        self.settings_ui()
        self.layout_ui()

    def init_ui(self) -> None:
        # ---------------------------------------------------------------------
        # General Organ Settings
        # ---------------------------------------------------------------------
        self.general_settings: QGroupBox = QGroupBox("General Organ")
        self.num_divisions_label: QLabel = QLabel("Number of Divisions:")
        self.num_divisions_spin: QSpinBox = QSpinBox()
        self.num_enclosures_label: QLabel = QLabel("Number of Enclosures:")
        self.num_enclosures_spin: QSpinBox = QSpinBox()
        self.num_stops_label: QLabel = QLabel("Number of Stops:")
        self.num_stops_spin: QSpinBox = QSpinBox()
        self.num_tremulants_label: QLabel = QLabel("Number of Tremulants:")
        self.num_tremulants_spin: QSpinBox = QSpinBox()
        self.num_generals_label: QLabel = QLabel("Number of Generals:")
        self.num_generals_spin: QSpinBox = QSpinBox()
        # ---------------------------------------------------------------------
        # Division Settings
        # ---------------------------------------------------------------------
        self.division_settings: QGroupBox = QGroupBox("Organ Divisions")
        self.division_num_label: QLabel = QLabel("Division #:")
        self.division_num_spin: QSpinBox = QSpinBox()
        self.division_name_label: QLabel = QLabel("Division Name:")
        self.division_name_combo: QComboBox = QComboBox()
        self.num_divisionals_label: QLabel = QLabel("Number of Divisionals:")
        self.num_divisionals_spin: QSpinBox = QSpinBox()
        # ---------------------------------------------------------------------
        # Enclosure Settings
        # ---------------------------------------------------------------------
        self.enclosure_settings: QGroupBox = QGroupBox("Enclosures")
        self.enclosure_num_label: QLabel = QLabel("Enclosure #:")
        self.enclosure_num_spin: QSpinBox = QSpinBox()
        self.enclosure_division_label: QLabel = QLabel("Division:")
        self.enclosure_division_combo: QComboBox = QComboBox()
        # ---------------------------------------------------------------------
        # Stop Settings
        # ---------------------------------------------------------------------
        self.stop_settings: QGroupBox = QGroupBox("Stops")
        self.stop_num_label: QLabel = QLabel("Stop #:")
        self.stop_num_spin: QSpinBox = QSpinBox()
        self.stop_name_label: QLabel = QLabel("Stop Name:")
        self.stop_name_combo: QComboBox = QComboBox()
        self.stop_division_label: QLabel = QLabel("Division:")
        self.stop_division_combo: QComboBox = QComboBox()
        # ---------------------------------------------------------------------
        # Tremulant Settings
        # ---------------------------------------------------------------------
        self.tremulant_settings: QGroupBox = QGroupBox("Tremulants")
        self.tremulant_num_label: QLabel = QLabel("Tremulant #:")
        self.tremulant_num_spin: QSpinBox = QSpinBox()
        self.tremulant_division_label: QLabel = QLabel("Division:")
        self.tremulant_division_combo: QComboBox = QComboBox()

    def settings_ui(self) -> None:
        self.general_settings.setFixedSize(400, 200)
        self.division_settings.setFixedSize(400, 125)
        self.enclosure_settings.setFixedSize(400, 100)
        self.stop_settings.setFixedSize(400, 125)
        self.tremulant_settings.setFixedSize(400, 100)
        groupboxes: list[QGroupBox] = [
            self.general_settings,
            self.division_settings,
            self.enclosure_settings,
            self.stop_settings,
            self.tremulant_settings
        ]
        for groupbox in groupboxes:
            groupbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        spinboxes: list[QSpinBox] = [
            self.num_divisions_spin,
            self.num_enclosures_spin,
            self.num_stops_spin,
            self.num_tremulants_spin,
            self.num_generals_spin,
            self.division_num_spin,
            self.num_divisionals_spin,
            self.enclosure_num_spin,
            self.stop_num_spin,
            self.tremulant_num_spin
        ]
        for spinbox in spinboxes:
            spinbox.setFixedWidth(50)

    def layout_ui(self) -> None:
        # ---------------------------------------------------------------------
        # General Settings Layout
        # ---------------------------------------------------------------------
        general_settings_layout: QFormLayout = QFormLayout()
        general_settings_widgets: list[tuple[QLabel, QWidget]] = [
            (self.num_divisions_label, self.num_divisions_spin),
            (self.num_enclosures_label, self.num_enclosures_spin),
            (self.num_stops_label, self.num_stops_spin),
            (self.num_tremulants_label, self.num_tremulants_spin),
            (self.num_generals_label, self.num_generals_spin)
        ]
        self.form_layout(
            layout=general_settings_layout,
            widgets=general_settings_widgets,
            form=self.general_settings
        )
        # ---------------------------------------------------------------------
        # Division Settings Layout
        # ---------------------------------------------------------------------
        division_settings_layout: QFormLayout = QFormLayout()
        division_settings_widgets: list[tuple[QLabel, QWidget]] = [
            (self.division_num_label, self.division_num_spin),
            (self.division_name_label, self.division_name_combo),
            (self.num_divisionals_label, self.num_divisionals_spin)
        ]
        self.form_layout(
            layout=division_settings_layout,
            widgets=division_settings_widgets,
            form=self.division_settings
        )
        # ---------------------------------------------------------------------
        # Enclosure Settings Layout
        # ---------------------------------------------------------------------
        enclosure_settings_layout: QFormLayout = QFormLayout()
        enclosure_settings_widgets: list[tuple[QLabel, QWidget]] = [
            (self.enclosure_num_label, self.enclosure_num_spin),
            (self.enclosure_division_label, self.enclosure_division_combo)
        ]
        self.form_layout(
            layout=enclosure_settings_layout,
            widgets=enclosure_settings_widgets,
            form=self.enclosure_settings
        )
        # ---------------------------------------------------------------------
        # Stop Settings Layout
        # ---------------------------------------------------------------------
        stop_settings_layout: QFormLayout = QFormLayout()
        stop_settings_widgets: list[tuple[QLabel, QWidget]] = [
            (self.stop_num_label, self.stop_num_spin),
            (self.stop_name_label, self.stop_name_combo),
            (self.stop_division_label, self.stop_division_combo)
        ]
        self.form_layout(
            layout=stop_settings_layout,
            widgets=stop_settings_widgets,
            form=self.stop_settings
        )
        # ---------------------------------------------------------------------
        # Tremulant Settings Layout
        # ---------------------------------------------------------------------
        tremulant_settings_layout: QFormLayout = QFormLayout()
        tremulant_settings_widgets: list[tuple[QLabel, QWidget]] = [
            (self.tremulant_num_label, self.tremulant_num_spin),
            (self.tremulant_division_label, self.tremulant_division_combo)
        ]
        self.form_layout(
            layout=tremulant_settings_layout,
            widgets=tremulant_settings_widgets,
            form=self.tremulant_settings
        )
        # ---------------------------------------------------------------------
        # Form Layout
        # ---------------------------------------------------------------------
        layout: QVBoxLayout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        widgets: list[QGroupBox] = [
            self.general_settings,
            self.division_settings,
            self.enclosure_settings,
            self.stop_settings,
            self.tremulant_settings
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
    win: OrganSettings = OrganSettings()
    win.show()
    app.exec()
