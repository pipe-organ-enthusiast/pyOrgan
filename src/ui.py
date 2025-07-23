from PySide6.QtWidgets import (
        QMainWindow,
        QWidget,
        QToolBar,
        QDockWidget,
        QFrame,
        QGroupBox,
        QLabel,
        QSpinBox,
        QComboBox,
        QCheckBox,
        #QPushButton,
        #QSizePolicy,
        QFormLayout,
        QVBoxLayout
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt, QSize
import os


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        path = os.path.dirname(__file__)
        os.chdir(path)
        self.init_ui()
        self.settings_ui()
        self.layout_ui()

    def init_ui(self) -> None:
        self.sidebar: QToolBar = QToolBar()
        self.organ_settings_action: QAction = QAction(QIcon("icons/organ.png"), "")
        self.audio_settings_action: QAction = QAction(QIcon("icons/audio.png"), "")
        self.midi_settings_action: QAction = QAction(QIcon("icons/midi.png"), "")
        
        self.settings_dock = QDockWidget()
        self.organ_settings: OrganSettings = OrganSettings()
        self.audio_settings: AudioSettings = AudioSettings()
        self.midi_settings: MIDISettings = MIDISettings()

    def settings_ui(self) -> None:
        self.settings_ui_sidebar()
        self.settings_ui_settings_dock()

    def settings_ui_sidebar(self) -> None:
        self.sidebar.setIconSize(QSize(30, 30))
        self.sidebar.setMovable(False)
        self.organ_settings_action.triggered.connect(self.organ_settings_selected)
        self.audio_settings_action.triggered.connect(self.audio_settings_selected)
        self.midi_settings_action.triggered.connect(self.midi_settings_selected)
        sidebar_actions: tuple[QAction, ...] = (
            self.organ_settings_action,
            self.audio_settings_action,
            self.midi_settings_action
        )
        for action in sidebar_actions:
            self.sidebar.addAction(action)
            self.sidebar.addSeparator()
            action.setCheckable(True)

    def settings_ui_settings_dock(self) -> None:
        self.settings_dock.setMaximumWidth(410)
        self.settings_dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)

    def layout_ui(self) -> None:
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.sidebar)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.settings_dock)

    def organ_settings_selected(self) -> None:
        if not self.organ_settings_action.isChecked():
            self.organ_settings_action.setChecked(False)
            self.settings_dock.hide()
        else:
            if self.settings_dock.isHidden():
                self.settings_dock.show()
        self.audio_settings_action.setChecked(False)
        self.midi_settings_action.setChecked(False)
        self.settings_dock.setWidget(self.organ_settings)

    def audio_settings_selected(self) -> None:
        if not self.audio_settings_action.isChecked():
            self.audio_settings_action.setChecked(False)
        self.organ_settings_action.setChecked(False)
        self.midi_settings_action.setChecked(False)
        self.settings_dock.setWidget(self.audio_settings)

    def midi_settings_selected(self) -> None:
        if not self.midi_settings_action.isChecked():
            self.midi_settings_action.setChecked(False)
        self.organ_settings_action.setChecked(False)
        self.audio_settings_action.setChecked(False)
        self.settings_dock.setWidget(self.midi_settings)


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


class AudioSettings(QFrame):
    def __init__(self) -> None:
        super().__init__()


class MIDISettings(QFrame):
    def __init__(self) -> None:
        super().__init__()


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app: QApplication = QApplication()
    win: QWidget = MainWindow()
    win.show()
    app.exec()
