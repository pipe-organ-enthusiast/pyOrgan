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
        QFormLayout,
        QVBoxLayout,
        QHBoxLayout,
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt, QSize
import os
from functools import partial


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
        self.sidebar_items: tuple[tuple[QAction, QWidget], ...] = (
            (QAction(QIcon("icons/organ.png"), ""), OrganSettings()),
            (QAction(QIcon("icons/audio.png"), ""), AudioSettings()),
            (QAction(QIcon("icons/midi.png"), ""), MIDISettings())
        )
        self.settings_dock = QDockWidget()

    def settings_ui(self) -> None:
        self.settings_ui_sidebar()
        self.settings_ui_settings_dock()

    def settings_ui_sidebar(self) -> None:
        self.sidebar.setIconSize(QSize(30, 30))
        self.sidebar.setMovable(False)
        for item in self.sidebar_items:
            item[0].triggered.connect(partial(self.action_selected, item[0], item[1]))

            item[0].setCheckable(True)
            self.sidebar.addAction(item[0])
            self.sidebar.addSeparator()

    def settings_ui_settings_dock(self) -> None:
        self.settings_dock.setMaximumWidth(410)
        self.settings_dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)

    def layout_ui(self) -> None:
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.sidebar)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.settings_dock)

    def action_selected(
        self,
        selected_action: QAction,
        form: QWidget
    ) -> None:
        if not selected_action.isChecked():
            selected_action.setChecked(False)
            self.settings_dock.hide()
        else:
            self.settings_dock.show()
        for action in self.sidebar_items:
            if not action[0] == selected_action:
                action[0].setChecked(False)
        self.settings_dock.setWidget(form)


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
        self.init_ui()
        self.settings_ui()
        self.layout_ui()

    def init_ui(self) -> None:
        self.header_label: QLabel = QLabel("Audio Device Settings")
        self.device_label: QLabel = QLabel("Audio Device:")
        self.device_combo: QComboBox = QComboBox()
        self.samplerate_label: QLabel = QLabel("Samplerate (Hz):")
        self.samplerate_combo: QComboBox = QComboBox()
        self.blocksize_label: QLabel = QLabel("Block Size:")
        self.blocksize_combo: QComboBox = QComboBox()
        self.bitrate_label: QLabel = QLabel("Bitrate:")
        self.bitrate_combo: QComboBox = QComboBox()

    def settings_ui(self) -> None:
        self.header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def layout_ui(self) -> None:
        form_widgets: tuple[tuple[QLabel, QComboBox], ...] = (
            (self.device_label, self.device_combo),
            (self.samplerate_label, self.samplerate_combo),
            (self.blocksize_label, self.blocksize_combo),
            (self.bitrate_label, self.bitrate_combo)
        )
        form_layout: QFormLayout = QFormLayout()
        for widget in form_widgets:
            form_layout.addRow(widget[0], widget[1])
        main_layout: QVBoxLayout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        main_layout.setSpacing(10)
        main_layout.addWidget(self.header_label)
        main_layout.addSpacing(10)
        main_layout.addLayout(form_layout)
        self.setLayout(main_layout)


class MIDISettings(QFrame):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()
        self.settings_ui()
        self.layout_ui()

    def init_ui(self) -> None:
        self.header_label: QLabel = QLabel("General MIDI Settings")
        self.num_midi_Slots_label: QLabel = QLabel("Number of MIDI Slots:")
        self.num_midi_Slots_spin: QSpinBox = QSpinBox()
        self.midi_slots: QGroupBox = QGroupBox("MIDI Slots")
        self.slot_num_label: QLabel = QLabel("MIDI Slot #:")
        self.slot_num_spin: QSpinBox = QSpinBox()
        self.midi_in_label: QLabel = QLabel("MIDI In Device:")
        self.midi_in_combo: QComboBox = QComboBox()
        self.midi_out_label: QLabel = QLabel("MIDI Out Device:")
        self.midi_out_combo: QComboBox = QComboBox()

    def settings_ui(self) -> None:
        self.header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def layout_ui(self) -> None:
        num_midi_layout: QHBoxLayout = QHBoxLayout()
        num_midi_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        num_midi_widgets: tuple[QLabel, QSpinBox] = (
            self.num_midi_Slots_label, self.num_midi_Slots_spin
        )
        for widget in num_midi_widgets:
            num_midi_layout.addWidget(widget)
        slot_layout: QFormLayout = QFormLayout()
        slot_widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.slot_num_label, self.slot_num_spin),
            (self.midi_in_label, self.midi_in_combo),
            (self.midi_out_label, self.midi_out_combo)
        )
        for widget in slot_widgets:
            slot_layout.addRow(widget[0], widget[1])
        self.midi_slots.setLayout(slot_layout)
        main_layout: QVBoxLayout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        main_layout.setSpacing(10)
        main_layout.addWidget(self.header_label)
        main_layout.addSpacing(10)
        main_layout.addLayout(num_midi_layout)
        main_layout.addSpacing(10)
        main_layout.addWidget(self.midi_slots)
        self.setLayout(main_layout)




if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app: QApplication = QApplication()
    win: QWidget = MainWindow()
    win.show()
    app.exec()
