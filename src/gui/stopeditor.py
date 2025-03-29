"""Stop Editor"""
from typing import Callable
#------------------------------------------------------------------------------
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QWidget,
    QScrollArea,
    QScrollBar,
    QGroupBox,
    QLabel,
    QLineEdit,
    QComboBox,
    QSpinBox,
    QPushButton,
    QCheckBox,
    QFormLayout,
    QHBoxLayout,
    QVBoxLayout
)
from PySide6.QtCore import Qt
from icecream import ic  # type: ignore
#------------------------------------------------------------------------------


class StopEditor(QFrame):
    def __init__(self) -> None:
        ic("Initializing Stop Editor...")
        super().__init__()
        self.__init_ui()
        self.__ui_settings()
        self.__ui_layout()
        self.__rank_harmonics_checked()
        self.__rank_adsr_checked()
        self.__pipe_harmonics_checked()
        self.__pipe_adsr_checked()
        ic("Stop Editor Initialized.")

    #**************************************************************************
    # Widgets
    #**************************************************************************
    def __init_ui(self) -> None:
        ic("Initializing Widgets...")
        self.__init_ui_header()
        self.__init_ui_editor()
        self.__init_ui_options()
        ic("Widgets Initialized.")

    #==========================================================================
    # Header
    #==========================================================================
    def __init_ui_header(self) -> None:
        ic("Initializing Header...")
        self.__header_widget: QWidget = QWidget()
        ic(self.__header_widget)
        self.__header_label: QLabel = QLabel("Stop:")
        ic(self.__header_label)
        self.__header_edit: QLineEdit = QLineEdit()
        ic(self.__header_edit)
        ic("Header Initialized.")

    #==========================================================================
    # Editor
    #==========================================================================
    def __init_ui_editor(self) -> None:
        ic("Initializing Editor...")
        self.__editor = QWidget()
        ic(self.__editor)
        self.__init_ui_stop_settings()
        self.__init_ui_rank_settings()
        self.__init_ui_rank_harmonics_settings()
        self.__init_ui_rank_harmonic_adsr_settings()
        self.__init_ui_rank_adsr_settings()
        self.__init_ui_pipe_settings()
        self.__init_ui_pipe_harmonics_settings()
        self.__init_ui_pipe_harmonic_adsr_settings()
        self.__init_ui_pipe_adsr_settings()
        ic("Editor Initialized.")

    #--------------------------------------------------------------------------
    # Stop Settings
    #--------------------------------------------------------------------------
    def __init_ui_stop_settings(self) -> None:
        ic("Initializing Stop Settings...")
        self.__stop_settings: QGroupBox = QGroupBox("Stop Settings")
        ic(self.__stop_settings)
        # Stop Name
        self.__stopname_label: QLabel = QLabel("Stop Name:")
        ic(self.__stopname_label)
        self.__stop_name_combo: QComboBox = QComboBox()
        ic(self.__stop_name_combo)
        # Stop Family
        self.__stop_family_label: QLabel = QLabel("Stop Family:")
        ic(self.__stop_family_label)
        self.__stop_family_combo = QComboBox()
        ic(self.__stop_family_combo)
        # Organ Division
        self.__organ_division_label: QLabel = QLabel("Organ Division:")
        ic(self.__organ_division_label)
        self.__organ_division_combo: QComboBox = QComboBox()
        ic(self.__organ_division_combo)
        # Number of Ranks
        self.__number_ranks_label: QLabel = QLabel("Number of Ranks:")
        ic(self.__number_ranks_label)
        self.__number_ranks_spin: QSpinBox = QSpinBox()
        ic(self.__number_ranks_spin)
        # Rank Series
        self.__rank_series_label: QLabel = QLabel("Rank Series:")
        ic(self.__rank_series_label)
        self.__rank_series_combo: QComboBox = QComboBox()
        ic(self.__rank_series_combo)
        ic("Stop Settings Initialized.")

    #--------------------------------------------------------------------------
    # Rank Settings
    #--------------------------------------------------------------------------
    def __init_ui_rank_settings(self) -> None:
        ic("Initializing Rank Settings...")
        self.__rank_settings: QGroupBox = QGroupBox("Rank Settings")
        ic(self.__rank_settings)
        # Rank Number
        self.__rank_number_label: QLabel = QLabel("Rank #:")
        ic(self.__rank_number_label)
        self.__rank_number_spin: QSpinBox = QSpinBox()
        ic(self.__rank_number_spin)
        # Rank Size
        self.__rank_size_label: QLabel = QLabel("Rank Size:")
        ic(self.__rank_size_label)
        self.__rank_size_combo = QComboBox()
        ic(self.__rank_size_combo)
        # Number of Pipes
        self.__number_pipes_label: QLabel = QLabel("Number of Pipes:")
        ic(self.__number_pipes_label)
        self.__number_pipes_spin: QSpinBox = QSpinBox()
        ic(self.__number_pipes_spin)
        # Pipe Type
        self.__pipe_type_label: QLabel = QLabel("PipeType:")
        ic(self.__pipe_type_label)
        self.__pipe_type_combo: QComboBox = QComboBox()
        ic(self.__pipe_type_combo)
        # Starting Note
        self.__starting_note_label: QLabel = QLabel("Starting Note:")
        ic(self.__starting_note_label)
        self.__starting_note_combo: QComboBox = QComboBox()
        ic(self.__starting_note_combo)
        # Frequency Offset
        self.__frequency_offset_label: QLabel = QLabel(
            "Frequency Offset (Hz):"
        )
        ic(self.__frequency_offset_label)
        self.__frequency_offset_spin: QSpinBox = QSpinBox()
        ic(self.__frequency_offset_spin)
        # Number of Harmonics
        self.__number_harmonics_label: QLabel = QLabel("Number of Harmonics:")
        ic(self.__number_harmonics_label)
        self.__number_harmonics_spin: QSpinBox = QSpinBox()
        ic(self.__number_harmonics_spin)
        ic("Rank Settings Initialized.")

    def __init_ui_rank_harmonics_settings(self) -> None:
        ic("Initializing Rank Harmonics Settings...")
        # Edit Harmonics Option
        self.__rank_harmonics_button: QCheckBox = QCheckBox("Edit Harmonics")
        ic(self.__rank_harmonics_button)
        # Harmonic Group
        self.__rank_harmonic: QGroupBox = QGroupBox("Harmonic Settings - Rank")
        ic(self.__rank_harmonic)
        # Harmonic #
        self.__rank_harmonic_number_label: QLabel = QLabel("Harmonic #:")
        ic(self.__rank_harmonic_number_label)
        self.__rank_harmonic_number_spin: QSpinBox = QSpinBox()
        ic(self.__rank_harmonic_number_spin)
        # Amplitude
        self.__rank_amplitude_label: QLabel = QLabel("Amplitude (%):")
        ic(self.__rank_amplitude_label)
        self.__rank_amplitude_spin: QSpinBox = QSpinBox()
        ic(self.__rank_amplitude_spin)
        ic("Rank Harmonics Settings Initialized.")

    def __init_ui_rank_harmonic_adsr_settings(self) -> None:
        ic("Initializing Rank Harmonic ADSR Settings...")
        # Edit Harmonic ADSR Option
        self.__rankharm_adsr_button: QCheckBox = QCheckBox(
            "Edit Harmonics ADSR"
        )
        ic(self.__rankharm_adsr_button)
        # Harmonic ADSR Group
        self.__rank_harmonics_adsr: QGroupBox = QGroupBox(
            "Harmonic ADSR Settings - Rank"
        )
        ic(self.__rank_harmonics_adsr)
        # Attack
        self.__rank_harmonics_attack_label: QLabel = QLabel(
            "Attack Time (ms):"
        )
        ic(self.__rank_harmonics_attack_label)
        self.__rank_harmonics_attack_spin: QSpinBox = QSpinBox()
        ic(self.__rank_harmonics_attack_spin)
        # Decay
        self.__rank_harmonics_decay_label: QLabel = QLabel("Decay Time (ms):")
        ic(self.__rank_harmonics_decay_label)
        self.__rank_harmonics_decay_spin: QSpinBox = QSpinBox()
        ic(self.__rank_harmonics_decay_spin)
        # Sustain
        self.__rank_harmonics_sustain_label: QLabel = QLabel("Sustain Level (%):")
        ic(self.__rank_harmonics_sustain_label)
        self.__rank_harmonics_sustain_spin: QSpinBox = QSpinBox()
        ic(self.__rank_harmonics_sustain_spin)
        # Release
        self.__rank_harmonics_release_label: QLabel = QLabel("Release Time (ms):")
        ic(self.__rank_harmonics_release_label)
        self.__rank_harmonics_release_spin: QSpinBox = QSpinBox()
        ic(self.__rank_harmonics_release_spin)
        ic("Rank Harmonic ADSR Settings Initialized.")

    def __init_ui_rank_adsr_settings(self) -> None:
        ic("Initializing Rank ADSR Settings...")
        # Edit ADSR Option
        self.__rank_adsr_button: QCheckBox = QCheckBox("Edit ADSR")
        ic(self.__rank_adsr_button)
        # ADSR Group
        self.__rank_adsr: QGroupBox = QGroupBox("ADSR Settings - Rank")
        ic(self.__rank_adsr)
        # Attack
        self.__rank_attack_label: QLabel = QLabel("Attack Time (ms):")
        ic(self.__rank_attack_label)
        self.__rank_attack_spin: QSpinBox = QSpinBox()
        ic(self.__rank_attack_spin)
        # Decay
        self.__rank_decay_label: QLabel = QLabel("Decay Time (ms):")
        ic(self.__rank_decay_label)
        self.__rank_decay_spin: QSpinBox = QSpinBox()
        ic(self.__rank_decay_spin)
        # Sustain
        self.__rank_sustain_label: QLabel = QLabel("Sustain Level (%):")
        ic(self.__rank_sustain_label)
        self.__rank_sustain_spin: QSpinBox = QSpinBox()
        ic(self.__rank_sustain_spin)
        # Release
        self.__rank_release_label: QLabel = QLabel("Release Time (ms):")
        ic(self.__rank_release_label)
        self.__rank_release_spin: QSpinBox = QSpinBox()
        ic(self.__rank_release_spin)
        ic("Rank ADSR Settings Initialized.")

    #--------------------------------------------------------------------------
    # Pipe Settings
    #--------------------------------------------------------------------------
    def __init_ui_pipe_settings(self) -> None:
        ic("Initializing Pipe Settings...")
        self.__pipe_settings: QGroupBox = QGroupBox("Pipe Settings")
        ic(self.__pipe_settings)
        # Rank #
        self.__rank_number_pipe_label: QLabel = QLabel("Rank #:")
        ic(self.__rank_number_pipe_label)
        self.__rank_number_pipe_spin: QSpinBox = QSpinBox()
        ic(self.__rank_number_pipe_spin)
        # Pipe #
        self.__pipe_number_label: QLabel = QLabel("Pipe #:")
        ic(self.__pipe_number_label)
        self.__pipe_number_spin: QSpinBox = QSpinBox()
        ic(self.__pipe_number_spin)        
        # Note
        self.__note_label: QLabel = QLabel("Note:")
        ic(self.__note_label)
        self.__note_combo: QComboBox = QComboBox()
        ic(self.__note_combo)
        # Relative Note
        self.__relative_note_label: QLabel = QLabel("Relative Note:")
        ic(self.__relative_note_label)
        self.__relative_note_combo: QComboBox = QComboBox()
        ic(self.__relative_note_combo)
        ic("Pipe Settings Initialized.")

    def __init_ui_pipe_harmonics_settings(self) -> None:
        ic("Initializing Pipe Harmonics Settings...")
        # Edit Harmonics Option
        self.__pipe_harmonics_button: QCheckBox = QCheckBox("Edit Harmonics")
        # Harmonic Group
        self.__pipe_harmonic: QGroupBox = QGroupBox("Harmonic Settings - Pipe")
        # Harmonic #
        self.__pipe_harmonicnum_label: QLabel = QLabel("Harmonic #:")
        self.__pipe_harmonic_number_spin: QSpinBox = QSpinBox()
        # Amplitude
        self.__pipe_amplitude_label: QLabel = QLabel("Amplitude (%):")
        self.__pipe_amplitude_spin: QSpinBox = QSpinBox()
        ic("Pipe Harmonics Settings Initialized.")

    def __init_ui_pipe_harmonic_adsr_settings(self) -> None:
        ic("Initializing Pipe Harmonic ADSR Settings...")
        # Edit Harmonic ADSR Option
        self.__pipeharm_adsr_button: QCheckBox = QCheckBox(
            "Edit Harmonics ADSR"
        )
        # Harmonic ADSR Group
        self.__pipeharm_adsr: QGroupBox = QGroupBox(
            "Harmonic ADSR Settings - Pipe"
        )
        # Attack
        self.__pipeharm_attack_label: QLabel = QLabel("Attack Time (ms):")
        self.__pipe_harmonics_attack_spin: QSpinBox = QSpinBox()
        # Decay
        self.__pipeharm_decay_label: QLabel = QLabel("Decay Time (ms):")
        self.__pipe_harmonics_decay_spin: QSpinBox = QSpinBox()
        # Sustain
        self.__pipeharm_sustain_label: QLabel = QLabel("Sustain Level (%):")
        self.__pipe_harmonics_sustain_spin: QSpinBox = QSpinBox()
        # Release
        self.__pipeharm_release_label: QLabel = QLabel("Release Time (ms):")
        self.__pipe_harmonics_release_spin: QSpinBox = QSpinBox()
        ic("Pipe Harmonic ADSR Settings Initialized.")

    def __init_ui_pipe_adsr_settings(self) -> None:
        ic("Initializing Pipe ADSR Settings...")
        self.__pipe_adsr_button: QCheckBox = QCheckBox("Edit ADSR")
        # ADSR Group
        self.__pipe_adsr: QGroupBox = QGroupBox("ADSR Settings - Pipe")
        # Attack
        self.__pipe_attack_label: QLabel = QLabel("Attack Time (ms):")
        self.__pipe_attack_spin: QSpinBox = QSpinBox()
        # Decay
        self.__pipe_decay_label: QLabel = QLabel("Decay Time (ms):")
        self.__pipe_decay_spin: QSpinBox = QSpinBox()
        # Sustain
        self.__pipe_sustain_label: QLabel = QLabel("Sustain Level (%):")
        self.__pipe_sustain_spin: QSpinBox = QSpinBox()
        # Release
        self.__pipe_release_label: QLabel = QLabel("Release Time (ms):")
        self.__pipe_release_spin: QSpinBox = QSpinBox()
        ic("Pipe ADSR Settings Initialized.")

    #==========================================================================
    # Options
    #==========================================================================
    def __init_ui_options(self) -> None:
        ic("Initializing Options...")
        self.__options: QWidget = QWidget()
        self.__load_button: QPushButton = QPushButton("Load Stop")
        self.__cancel_button: QPushButton = QPushButton("Cancel Changes")
        self.__save_button: QPushButton = QPushButton("Save Stop")
        ic("Options Initialized.")

    #**************************************************************************
    # Settings
    #**************************************************************************
    def __ui_settings(self) -> None:
        ic("Setting Up Widgets...")
        self.setWindowTitle("pyOrgan - Stop Editor")
        self.__ui_settings_header()
        self.__ui_settings_editor()
        ic("Widgets Settings Complete.")

    #==========================================================================
    # Header
    #==========================================================================
    def __ui_settings_header(self) -> None:
        ic("Setting Up Header...")
        self.__header_edit.setReadOnly(True)
        self.__header_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ic("Header Settings Complete.")

    #==========================================================================
    # Editor
    #==========================================================================
    def __ui_settings_editor(self) -> None:
        ic("Setting Up Editor...")
        self.__ui_settings_editor_groupboxes()
        self.__ui_settings_editor_labels()
        self.__ui_settings_editor_comboboxes()
        self.__ui_settings_editor_spinboxes()
        self.__ui_settings_editor_checkboxes()
        ic("Editor Settings Complete.")

    def __ui_settings_editor_groupboxes(self) -> None:
        ic("Setting Up Group Boxes...")
        group_boxes: tuple[QGroupBox, ...] = (
            self.__stop_settings,
            self.__rank_settings,
            self.__pipe_settings,
            self.__rank_harmonic,
            self.__pipe_harmonic,
            self.__rank_harmonics_adsr,
            self.__rank_adsr,
            self.__pipeharm_adsr,
            self.__pipe_adsr
        )
        for group_box in group_boxes:
            group_box.setAlignment(
                Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft
            )
        top_level: tuple[QGroupBox, ...] = (
            self.__stop_settings,
            self.__rank_settings,
            self.__pipe_settings
        )
        for group_box in top_level:
            group_box.setFixedWidth(270)
        ic("Group Boxes Settings Complete.")

    def __ui_settings_editor_labels(self) -> None:
        ic("Setting Up Labels...")
        labels: tuple[QLabel, ...] = (
            self.__stopname_label,
            self.__stop_family_label,
            self.__organ_division_label,
            self.__number_ranks_label,
            self.__rank_series_label,
            self.__rank_number_label,
            self.__rank_size_label,
            self.__number_pipes_label,
            self.__starting_note_label,
            self.__pipe_type_label,
            self.__frequency_offset_label,
            self.__number_harmonics_label,
            self.__rank_harmonic_number_label,
            self.__rank_amplitude_label,
            self.__rank_harmonics_attack_label,
            self.__rank_harmonics_decay_label,
            self.__rank_harmonics_sustain_label,
            self.__rank_harmonics_release_label,
            self.__rank_attack_label,
            self.__rank_decay_label,
            self.__rank_sustain_label,
            self.__rank_release_label,
            self.__rank_number_pipe_label,
            self.__pipe_number_label,
            self.__note_label,
            self.__relative_note_label,
            self.__pipe_harmonicnum_label,
            self.__pipe_amplitude_label,
            self.__pipeharm_attack_label,
            self.__pipeharm_decay_label,
            self.__pipeharm_sustain_label,
            self.__pipeharm_release_label,
            self.__pipe_attack_label,
            self.__pipe_decay_label,
            self.__pipe_sustain_label,
            self.__pipe_release_label
        )
        for label in labels:
            label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        ic("Labels Settings Complete.")

    def __ui_settings_editor_comboboxes(self) -> None:
        ic("Setting Up Combo Boxes...")
        comboboxes: tuple[QComboBox, ...] = (
            self.__stop_name_combo,
            self.__stop_family_combo,
            self.__organ_division_combo,
            self.__rank_series_combo,
            self.__rank_size_combo,
            self.__pipe_type_combo,
            self.__starting_note_combo,
            self.__note_combo,
            self.__relative_note_combo,
        )
        for widget in comboboxes:
            widget.setEditable(True)
            edit: QLineEdit = widget.lineEdit() # type: ignore
            edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
            if widget == self.__stop_name_combo:
                edit.setReadOnly(False)
            else:
                edit.setReadOnly(True)
        self.__note_combo.setEnabled(False)
        ic("Combo Boxes Settings Complete.")

    def __ui_settings_editor_spinboxes(self) -> None:
        ic("Setting Up Spin Boxes...")
        spin_boxes: tuple[QSpinBox, ...] = (
            self.__number_ranks_spin,
            self.__rank_number_spin,
            self.__number_pipes_spin,
            self.__frequency_offset_spin,
            self.__number_harmonics_spin,
            self.__rank_harmonic_number_spin,
            self.__rank_amplitude_spin,
            self.__rank_harmonics_attack_spin,
            self.__rank_harmonics_decay_spin,
            self.__rank_harmonics_sustain_spin,
            self.__rank_harmonics_release_spin,
            self.__rank_attack_spin,
            self.__rank_decay_spin,
            self.__rank_sustain_spin,
            self.__rank_release_spin,
            self.__rank_number_pipe_spin,
            self.__pipe_number_spin,
            self.__pipe_harmonic_number_spin,
            self.__pipe_amplitude_spin,
            self.__pipe_harmonics_attack_spin,
            self.__pipe_harmonics_decay_spin,
            self.__pipe_harmonics_sustain_spin,
            self.__pipe_harmonics_release_spin,
            self.__pipe_attack_spin,
            self.__pipe_decay_spin,
            self.__pipe_sustain_spin,
            self.__pipe_release_spin
        )
        for spin_box in spin_boxes:
            spin_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ic("Spin Boxes Settings Complete.")

    def __ui_settings_editor_checkboxes(self) -> None:
        ic("Setting Up Check Boxes...")
        self.__rank_harmonics_button.checkStateChanged.connect(
            self.__rank_harmonics_checked
        )
        self.__rankharm_adsr_button.checkStateChanged.connect(
            self.__rankharm_adsr_checked
        )
        self.__rank_adsr_button.checkStateChanged.connect(
            self.__rank_adsr_checked
        )
        self.__pipe_harmonics_button.checkStateChanged.connect(
            self.__pipe_harmonics_checked
        )
        self.__pipeharm_adsr_button.checkStateChanged.connect(
            self.__pipeharm_adsr_checked
        )
        self.__pipe_adsr_button.checkStateChanged.connect(
            self.__pipe_adsr_checked
        )
        ic("Check Boxes Settings Complete.")

    #**************************************************************************
    # Layout
    #**************************************************************************
    def __ui_layout(self) -> None:
        ic("Setting Up Layout...")
        self.__ui_layout_header()
        self.__ui_layout_editor()
        self.__ui_layout_options()
        self.__ui_layout_main()
        ic("Layout Complete.")

    #==========================================================================
    # Header
    #==========================================================================
    def __ui_layout_header(self) -> None:
        ic("Laying Out Header...")
        header_layout: QHBoxLayout = QHBoxLayout()
        widgets: tuple[QWidget, ...] = (
            self.__header_label,
            self.__header_edit
        )
        for widget in widgets:
            header_layout.addWidget(widget)
        self.__header_widget.setLayout(header_layout)
        ic("Header Layout Complete.")
    #==========================================================================
    # Editor Forms
    #==========================================================================
    def __ui_layout_editor(self) -> None:
        ic("Laying Out Editor...")
        self.__ui_layout_stop_settings()
        self.__ui_layout_rank_settings()
        self.__ui_layout_pipe_settings()
        ic("Editor Layout Complete.")

    #--------------------------------------------------------------------------
    # Stop Settings
    #--------------------------------------------------------------------------
    def __ui_layout_stop_settings(self) -> None:
        ic("Laying Out Stop Settings...")
        stopsettings_layout: QFormLayout = QFormLayout()
        stopsettings_widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__stopname_label, self.__stop_name_combo),
            (self.__stop_family_label, self.__stop_family_combo),
            (self.__organ_division_label, self.__organ_division_combo),
            (self.__number_ranks_label, self.__number_ranks_spin),
            (self.__rank_series_label, self.__rank_series_combo)
        )
        for label, widget in stopsettings_widgets:
            stopsettings_layout.addRow(label, widget)
        self.__stop_settings.setLayout(stopsettings_layout)
        ic("Stop Settings Layout Complete.")
 
    #==========================================================================
    # Rank Settings
    #==========================================================================
    def __ui_layout_rank_settings(self) -> None:
        ic("Laying Out Rank Settings...")
        self.__ui_layout_rank_harmonic()
        self.__ui_layout_rank_harmonics_adsr()
        ranksettings_layout: QVBoxLayout = QVBoxLayout()
        ranksettings_widgets: tuple[QWidget, ...] = (
            self.__ui_layout_rank_header(),
            self.__ui_layout_rank_harmonic_settings(),
            self.__ui_layout_rank_adsr()
        )
        for widget in ranksettings_widgets:
            ranksettings_layout.addWidget(widget)
            ranksettings_layout.addSpacing(10)
        self.__rank_settings.setLayout(ranksettings_layout)
        ic("Rank Settings Layout Complete.")

    #--------------------------------------------------------------------------
    # Rank Header
    #--------------------------------------------------------------------------
    def __ui_layout_rank_header(self) -> QWidget:
        ic("Laying Out Rank Header...")
        rankheader_widget: QWidget = QWidget()
        rankheader_layout: QFormLayout = QFormLayout()
        rankheader_widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__rank_number_label, self.__rank_number_spin),
            (self.__rank_size_label, self.__rank_size_combo),
            (self.__pipe_type_label, self.__pipe_type_combo),
            (self.__starting_note_label, self.__starting_note_combo),
            (self.__frequency_offset_label, self.__frequency_offset_spin),
            (self.__number_pipes_label, self.__number_pipes_spin),
            (self.__number_harmonics_label, self.__number_harmonics_spin)
        )
        for label, widget in rankheader_widgets:
            rankheader_layout.addRow(label, widget)
        rankheader_widget.setLayout(rankheader_layout)
        ic("Rank Header Layout Complete.")
        return rankheader_widget

    #--------------------------------------------------------------------------
    # Rank Harmonics Settings
    #--------------------------------------------------------------------------
    def __ui_layout_rank_harmonic_settings(self) -> QWidget:
        ic("Laying Out Rank Harmonics Settings...")
        rankharmonicsettings_widget: QWidget = QWidget()
        rankharmonicsettings_layout: QVBoxLayout = QVBoxLayout()
        rankharmonicsettings_layout.addWidget(self.__rank_harmonics_button)
        rankharmonicsettings_layout.addWidget(self.__rank_harmonic)
        rankharmonicsettings_widget.setLayout(rankharmonicsettings_layout)
        ic("Rank Harmonics Settings Layout Complete.")
        return rankharmonicsettings_widget

    def __ui_layout_rank_harmonics_widget(self) -> QWidget:
        ic("Laying Out Rank Harmonics Widget...")
        rankharmonics_widget: QWidget = QWidget()
        rankharmonics_layout: QFormLayout = QFormLayout()
        rankharmonics_widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__rank_harmonic_number_label, self.__rank_harmonic_number_spin),
            (self.__rank_amplitude_label, self.__rank_amplitude_spin)
        )
        for label, widget in rankharmonics_widgets:
            rankharmonics_layout.addRow(label, widget)
        rankharmonics_widget.setLayout(rankharmonics_layout)
        ic("Rank Harmonics Widget Layout Complete.")
        return rankharmonics_widget

    def __ui_layout_rank_harmonics_adsr(self) -> None:
        ic("Laying Out Rank Harmonics ADSR...")
        rankharmonicsadsr_layout: QFormLayout = QFormLayout()
        rankharmonicsadsr_widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__rank_harmonics_attack_label, self.__rank_harmonics_attack_spin),
            (self.__rank_harmonics_decay_label, self.__rank_harmonics_decay_spin),
            (self.__rank_harmonics_sustain_label, self.__rank_harmonics_sustain_spin),
            (self.__rank_harmonics_release_label, self.__rank_harmonics_release_spin)
        )
        for label, widget in rankharmonicsadsr_widgets:
            rankharmonicsadsr_layout.addRow(label, widget)
        self.__rank_harmonics_adsr.setLayout(rankharmonicsadsr_layout)
        ic("Rank Harmonics ADSR Layout Complete.")

    def __ui_layout_rank_harmonic(self) -> None:
        ic("Laying Out Rank Harmonic...")
        rankharmonic_layout: QVBoxLayout = QVBoxLayout()
        rankharmonic_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        rankharmonic_layout.addWidget(self.__ui_layout_rank_harmonics_widget())
        rankharmonic_layout.addSpacing(10)
        rankharmonic_layout.addWidget(self.__rankharm_adsr_button)
        rankharmonic_layout.addWidget(self.__rank_harmonics_adsr)
        self.__rank_harmonic.setLayout(rankharmonic_layout)
        ic("Rank Harmonic Layout Complete.")

    #--------------------------------------------------------------------------
    # Rank ADSR Settings
    #--------------------------------------------------------------------------
    def __ui_layout_rank_adsr(self) -> QWidget:
        ic("Laying Out Rank ADSR...")
        rankadsr_widget: QWidget = QWidget()
        rankadsr_layout: QVBoxLayout = QVBoxLayout()
        rankadsr_form_layout: QFormLayout = QFormLayout()
        rankadsr_widgets: tuple[tuple[QLabel, QSpinBox], ...] = (
            (self.__rank_attack_label, self.__rank_attack_spin),
            (self.__rank_decay_label, self.__rank_decay_spin),
            (self.__rank_sustain_label, self.__rank_sustain_spin),
            (self.__rank_release_label, self.__rank_release_spin)
        )
        for label, widget in rankadsr_widgets:
            rankadsr_form_layout.addRow(label, widget)
        self.__rank_adsr.setLayout(rankadsr_form_layout)
        widgets: tuple[QWidget, ...] = (
            self.__rank_adsr_button,
            self.__rank_adsr
        )
        for widget in widgets:
            rankadsr_layout.addWidget(widget)
        rankadsr_widget.setLayout(rankadsr_layout)
        ic("Rank ADSR Layout Complete.")
        return rankadsr_widget

    #==========================================================================
    # Pipe Settings
    #==========================================================================
    def __ui_layout_pipe_settings(self) -> None:
        ic("Laying Out Pipe Settings...")
        self.__ui_layout_pipe_harmonic()
        self.__ui_layout_pipe_harmonics_adsr()
        pipesettings_layout: QVBoxLayout = QVBoxLayout()
        pipesettings_widgets: tuple[QWidget, ...] = (
            self.__ui_layout_pipe_header(),
            self.__ui_layout_pipe_harmonic_settings(),
            self.__ui_layout_pipe_adsr()
        )
        for widget in pipesettings_widgets:
            pipesettings_layout.addWidget(widget)
            pipesettings_layout.addSpacing(10)
        self.__pipe_settings.setLayout(pipesettings_layout)
        ic("Pipe Settings Layout Complete.")

    def __ui_layout_pipe_header(self) -> QWidget:
        ic("Laying Out Pipe Header...")
        pipeheader_widget: QWidget = QWidget()
        pipeheader_layout: QFormLayout = QFormLayout()
        pipeheader_widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__rank_number_pipe_label, self.__rank_number_pipe_spin),
            (self.__pipe_number_label, self.__pipe_number_spin),        
            (self.__note_label, self.__note_combo),
            (self.__relative_note_label, self.__relative_note_combo)
        )
        for label, widget in pipeheader_widgets:
            pipeheader_layout.addRow(label, widget)
        pipeheader_widget.setLayout(pipeheader_layout)
        ic("Pipe Header Layout Complete.")
        return pipeheader_widget

    #--------------------------------------------------------------------------
    # Pipe Harmonics Settings
    #--------------------------------------------------------------------------
    def __ui_layout_pipe_harmonic_settings(self) -> QWidget:
        ic("Laying Out Pipe Harmonic Settings...")
        pipeharmonicsettings_widget: QWidget = QWidget()
        pipeharmonicsettings_layout: QVBoxLayout = QVBoxLayout()
        pipeharmonicsettings_layout.addWidget(self.__pipe_harmonics_button)
        pipeharmonicsettings_layout.addWidget(self.__pipe_harmonic)
        pipeharmonicsettings_widget.setLayout(pipeharmonicsettings_layout)
        ic("Pipe Harmonic Settings Layout Complete.")
        return pipeharmonicsettings_widget

    def __ui_layout_pipe_harmonics_widget(self) -> QWidget:
        ic("Laying Out Pipe Harmonics Widget...")
        pipeharmonics_widget: QWidget = QWidget()
        pipeharmonics_layout: QFormLayout = QFormLayout()
        pipeharmonics_widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__pipe_harmonicnum_label, self.__pipe_harmonic_number_spin),
            (self.__pipe_amplitude_label, self.__pipe_amplitude_spin)
        )
        for label, widget in pipeharmonics_widgets:
            pipeharmonics_layout.addRow(label, widget)
        pipeharmonics_widget.setLayout(pipeharmonics_layout)
        ic("Pipe Harmonics Widget Layout Complete.")
        return pipeharmonics_widget

    def __ui_layout_pipe_harmonics_adsr(self) -> None:
        ic("Laying Out Pipe Harmonics ADSR...")
        pipeharmonicsadsr_layout: QFormLayout = QFormLayout()
        pipeharmonicsadsr_widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__pipeharm_attack_label, self.__pipe_harmonics_attack_spin),
            (self.__pipeharm_decay_label, self.__pipe_harmonics_decay_spin),
            (self.__pipeharm_sustain_label, self.__pipe_harmonics_sustain_spin),
            (self.__pipeharm_release_label, self.__pipe_harmonics_release_spin)
        )
        for label, widget in pipeharmonicsadsr_widgets:
            pipeharmonicsadsr_layout.addRow(label, widget)
        self.__pipeharm_adsr.setLayout(pipeharmonicsadsr_layout)
        ic("Pipe Harmonics ADSR Layout Complete.")

    def __ui_layout_pipe_harmonic(self) -> None:
        ic("Laying Out Pipe Harmonic...")
        pipeharmonic_layout: QVBoxLayout = QVBoxLayout()
        pipeharmonic_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        pipeharmonic_layout.addWidget(self.__ui_layout_pipe_harmonics_widget())
        pipeharmonic_layout.addSpacing(10)
        pipeharmonic_layout.addWidget(self.__pipeharm_adsr_button)
        pipeharmonic_layout.addWidget(self.__pipeharm_adsr)
        self.__pipe_harmonic.setLayout(pipeharmonic_layout)
        ic("Pipe Harmonic Layout Complete.")

    #--------------------------------------------------------------------------
    # Pipe ADSR Settings
    #--------------------------------------------------------------------------
    def __ui_layout_pipe_adsr(self) -> QWidget:
        ic("Laying Out Pipe ADSR...")
        pipeadsr_widget: QWidget = QWidget()
        pipeadsr_layout: QVBoxLayout = QVBoxLayout()
        pipeadsr_form_layout: QFormLayout = QFormLayout()
        pipeadsr_widgets: tuple[tuple[QLabel, QSpinBox], ...] = (
            (self.__pipe_attack_label, self.__pipe_attack_spin),
            (self.__pipe_decay_label, self.__pipe_decay_spin),
            (self.__pipe_sustain_label, self.__pipe_sustain_spin),
            (self.__pipe_release_label, self.__pipe_release_spin)
        )
        for label, widget in pipeadsr_widgets:
            pipeadsr_form_layout.addRow(label, widget)
        self.__pipe_adsr.setLayout(pipeadsr_form_layout)
        widgets: tuple[QWidget, ...] = (
            self.__pipe_adsr_button,
            self.__pipe_adsr
        )
        for widget in widgets:
            pipeadsr_layout.addWidget(widget)
        pipeadsr_widget.setLayout(pipeadsr_layout)
        ic("Pipe ADSR Layout Complete.")
        return pipeadsr_widget
        
    #==========================================================================
    # Editor Layout
    #==========================================================================
    def __ui_layout_editor_scroll(self) -> QScrollArea:
        ic("Laying Out Editor Scroll...")
        editor_scroll: QScrollArea = QScrollArea()
        editor_scroll.setVerticalScrollBar(QScrollBar())
        editor_scroll.setWidgetResizable(True)
        editor_scroll.setFixedWidth(310)
        editor_layout: QVBoxLayout = QVBoxLayout()
        editor_widgets: tuple[QWidget, ...] = (
            self.__stop_settings,
            self.__rank_settings,
            self.__pipe_settings
        )
        for widget in editor_widgets:
            editor_layout.addWidget(widget)
        self.__editor.setLayout(editor_layout)
        editor_scroll.setWidget(self.__editor)
        ic("Editor Scroll Layout Complete.")
        return editor_scroll

    #**************************************************************************
    # Options
    #**************************************************************************
    def __ui_layout_options(self) -> None:
        ic("Laying Out Options...")
        options_layout: QVBoxLayout = QVBoxLayout()
        options_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        buttons: tuple[QPushButton, ...] = (
            self.__load_button,
            self.__cancel_button,
            self.__save_button
        )
        for button in buttons:
            options_layout.addWidget(button)
        self.__options.setLayout(options_layout)
        ic("Options Layout Complete.")

    #**************************************************************************
    # Main Layout
    #**************************************************************************
    def __ui_layout_main(self) -> None:
        ic("Laying Out Main Layout...")
        main_layout: QHBoxLayout = QHBoxLayout()
        widgets: tuple[QWidget, ...] = (
            self.__ui_layout_form(),
            self.__options
        )
        for widget in widgets:
            main_layout.addWidget(widget)
        self.setLayout(main_layout)
        ic("Main Layout Complete.")

    def __ui_layout_form(self) -> QWidget:
        ic("Laying Out Form...")
        form_widget: QWidget = QWidget()
        form_layout: QVBoxLayout = QVBoxLayout()
        form_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        form_widgets: tuple[QWidget, ...] = (
            self.__header_widget,
            self.__ui_layout_editor_scroll(),
        )
        for widget in form_widgets:
            form_layout.addWidget(widget)
        form_widget.setLayout(form_layout)
        ic("Form Layout Complete.")
        return form_widget

    #**************************************************************************
    # Actions
    #**************************************************************************
    #==========================================================================
    # Widget Manipulation
    #==========================================================================
    def __rank_harmonics_checked(self) -> None:
        ic("Initiating Rank Harmonics CheckBox Clicked...")
        widgets: tuple[QWidget, ...] = (
            self.__rank_harmonic,
            self.__rank_harmonic_number_label,
            self.__rank_harmonic_number_spin,
            self.__rank_amplitude_label,
            self.__rank_amplitude_spin,
            self.__rankharm_adsr_button
        )
        match self.__rank_harmonics_button.isChecked():
            case True:
                for widget in widgets:
                    widget.setEnabled(True)
            case False:
                self.__rankharm_adsr_button.setChecked(False)
                self.__rankharm_adsr_checked()
                for widget in widgets:
                    widget.setEnabled(False)
        ic("Rank Harmonics CheckBox Clicked Complete.")

    def __rankharm_adsr_checked(self) -> None:
        ic("Initiating Rank Harmonic ADSR CheckBox Clicked...")
        widgets: tuple[QWidget, ...] = (
            self.__rank_harmonics_adsr,
            self.__rank_harmonics_attack_label,
            self.__rank_harmonics_attack_spin,
            self.__rank_harmonics_decay_label,
            self.__rank_harmonics_decay_spin,
            self.__rank_harmonics_sustain_label,
            self.__rank_harmonics_sustain_spin,
            self.__rank_harmonics_release_label,
            self.__rank_harmonics_release_spin
        )
        match self.__rankharm_adsr_button.isChecked():
            case True:
                for widget in widgets:
                    widget.setEnabled(True)
            case False:
                for widget in widgets:
                    widget.setEnabled(False)
        ic("Rank Harmonic ADSR CheckBox Clicked Complete.")

    def __rank_adsr_checked(self) -> None:
        ic("Initiating Rank ADSR CheckBox Clicked...")
        widgets: tuple[QWidget, ...] = (
            self.__rank_adsr,
            self.__rank_attack_label,
            self.__rank_attack_spin,
            self.__rank_decay_label,
            self.__rank_decay_spin,
            self.__rank_sustain_label,
            self.__rank_sustain_spin,
            self.__rank_release_label,
            self.__rank_release_spin
        )
        match self.__rank_adsr_button.isChecked():
            case True:
                for widget in widgets:
                    widget.setEnabled(True)
            case False:
                for widget in widgets:
                    widget.setEnabled(False)
        ic("Rank ADSR CheckBox Clicked Complete.")

    def __pipe_harmonics_checked(self) -> None:
        ic("Initiating Pipe Harmonics CheckBox Clicked...")
        widgets: tuple[QWidget, ...] = (
            self.__pipe_harmonic,
            self.__pipe_harmonicnum_label,
            self.__pipe_harmonic_number_spin,
            self.__pipe_amplitude_label,
            self.__pipe_amplitude_spin,
            self.__pipeharm_adsr_button
        )
        match self.__pipe_harmonics_button.isChecked():
            case True:
                for widget in widgets:
                    widget.setEnabled(True)
            case False:
                self.__pipeharm_adsr_button.setChecked(False)
                self.__pipeharm_adsr_checked()
                for widget in widgets:
                    widget.setEnabled(False)
        ic("Pipe Harmonics CheckBox Clicked Complete.")

    def __pipeharm_adsr_checked(self) -> None:
        ic("Initiating Pipe Harmonic ADSR CheckBox Clicked...")
        spins: tuple[QWidget, ...] = (
            self.__pipeharm_adsr,
            self.__pipeharm_attack_label,
            self.__pipe_harmonics_attack_spin,
            self.__pipeharm_decay_label,
            self.__pipe_harmonics_decay_spin,
            self.__pipeharm_sustain_label,
            self.__pipe_harmonics_sustain_spin,
            self.__pipeharm_release_label,
            self.__pipe_harmonics_release_spin
        )
        match self.__pipeharm_adsr_button.isChecked():
            case True:
                for spin in spins:
                    spin.setEnabled(True)
            case False:
                for spin in spins:
                    spin.setEnabled(False)
        ic("Pipe Harmonic ADSR CheckBox Clicked Complete.")

    def __pipe_adsr_checked(self) -> None:
        ic("Initiating Pipe ADSR CheckBox Clicked...")
        spins: tuple[QWidget, ...] = (
            self.__pipe_adsr,
            self.__pipe_attack_label,
            self.__pipe_attack_spin,
            self.__pipe_decay_label,
            self.__pipe_decay_spin,
            self.__pipe_sustain_label,
            self.__pipe_sustain_spin,
            self.__pipe_release_label,
            self.__pipe_release_spin
        )
        match self.__pipe_adsr_button.isChecked():
            case True:
                for spin in spins:
                    spin.setEnabled(True)
            case False:
                for spin in spins:
                    spin.setEnabled(False)
        ic("Pipe ADSR CheckBox Clicked Complete.")

    #==========================================================================
    # Widget Data
    #==========================================================================
    def stop_names_populate(self, stop_names: tuple[str, ...]) -> None:
        ic("Populating Stop Names...")
        ic(stop_names)
        self.__stop_name_combo.clear()
        self.__stop_name_combo.addItems(stop_names)
        ic("Stop Names Populated.")

    def stop_families_populate(self, stop_families: tuple[str, ...]) -> None:
        ic("Populating Stop Families...")
        ic(stop_families)
        self.__stop_family_combo.clear()
        self.__stop_family_combo.addItems(stop_families)
        ic("Stop Families Populated.")

    def organ_divisions_populate(self, divisions: tuple[str, ...]) -> None:
        ic("Populating Organ Divisions...")
        ic(divisions)
        self.__organ_division_combo.clear()
        self.__organ_division_combo.addItems(divisions)
        ic("Organ Divisions Populated.")

    def number_ranks_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Number of Ranks...")
        ic(min)
        self.__number_ranks_spin.setMinimum(min)
        ic("Minimum Number of Ranks Set.")

    def number_ranks_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Number of Ranks...")
        ic(max)
        self.__number_ranks_spin.setMaximum(max)
        ic("Maximum Number of Ranks Set.")

    def rank_series_populate(self, rank_series: tuple[str, ...]) -> None:
        ic("Populating Rank Series...")
        ic(rank_series)
        self.__rank_series_combo.clear()
        self.__rank_series_combo.addItems(rank_series)
        ic("Rank Series Populated.")

    def rank_number_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Rank Number...")
        ic(min)
        self.__rank_number_spin.setMinimum(min)
        ic("Minimum Rank Number Set.")

    def rank_number_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Rank Number...")
        ic(max)
        self.__rank_number_spin.setMaximum(max)
        ic("Maximum Rank Number Set.")

    def rank_size_populate(self, rank_sizes: tuple[str, ...]) -> None:
        ic("Populating Rank Sizes...")
        ic(rank_sizes)
        self.__rank_size_combo.clear()
        self.__rank_size_combo.addItems(rank_sizes)
        ic("Rank Sizes Populated.")

    def number_pipes_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Number of Pipes...")
        ic(min)
        self.__number_pipes_spin.setMinimum(min)
        ic("Minimum Number of Pipes Set.")

    def number_pipes_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Number of Pipes...")
        ic(max)
        self.__number_pipes_spin.setMaximum(max)
        ic("Maximum Number of Pipes Set.")

    def pipe_types_populate(self, pipe_types: tuple[str, ...]) -> None:
        ic("Populating Pipe Types...")
        ic(pipe_types)
        self.__pipe_type_combo.addItems(pipe_types)
        ic("Pipe Types Populated.")

    def starting_note_populate(self, starting_notes: tuple[str, ...]) -> None:
        ic("Populating Starting Notes...")
        ic(starting_notes)
        self.__starting_note_combo.addItems(starting_notes)
        ic("Starting Notes Populated.")

    def frequency_offset_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Frequency Offset...")
        ic(min)
        self.__frequency_offset_spin.setMinimum(min)
        ic("Minimum Frequency Offset Set.")

    def frequency_offset_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Frequency Offset...")
        ic(max)
        self.__frequency_offset_spin.setMaximum(max)
        ic("Maximum Frequency Offset Set.")

    def number_harmonics_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Number of Harmonics...")
        ic(min)
        self.__number_harmonics_spin.setMinimum(min)
        ic("Minimum Number of Harmonics Set.")

    def number_harmonics_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Number of Harmonics...")
        ic(max)
        self.__number_harmonics_spin.setMaximum(max)
        ic("Maximum Number of Harmonics Set.")

    def harmonic_number_rank_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Harmonic Number...")
        ic(min)
        self.__rank_harmonic_number_spin.setMinimum(min)
        ic("Minimum Harmonic Number Set.")

    def harmonic_number_rank_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Harmonic Number...")
        ic(max)
        self.__rank_harmonic_number_spin.setMaximum(max)
        ic("Maximum Harmonic Number Set.")

    def amplitude_rank_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Rank Amplitude...")
        ic(min)
        self.__rank_amplitude_spin.setMinimum(min)
        ic("Minimum Rank Amplitude Set.")

    def amplitude_rank_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Rank Amplitude...")
        ic(max)
        self.__rank_amplitude_spin.setMaximum(max)
        ic("Maximum Rank Amplitude Set.")

    def attack_time_rank_harmonic_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Rank Harmonic Attack Time...")
        ic(min)
        self.__rank_harmonics_attack_spin.setMinimum(min)
        ic("Minimum Rank Harmonic Attack Time Set.")

    def attack_time_rank_harmonic_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Rank Harmonic Attack Time...")
        ic(max)
        self.__rank_harmonics_attack_spin.setMaximum(max)
        ic("Maximum Rank Harmonic Attack Time Set.")

    def decay_time_rank_harmonic_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Rank Harmonic Decay Time...")
        ic(min)
        self.__rank_harmonics_decay_spin.setMinimum(min)
        ic("Minimum Rank Harmonic Decay Time Set.")

    def decay_time_rank_harmonic_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Rank Harmonic Decay Time...")
        ic(max)
        self.__rank_harmonics_decay_spin.setMaximum(max)
        ic("Maximum Rank Harmonic Decay Time Set.")

    def sustain_level_rank_harmonic_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Rank Harmonic Sustain Level...")
        ic(min)
        self.__rank_harmonics_sustain_spin.setMinimum(min)
        ic("Minimum Rank Harmonic Sustain Level Set.")

    def sustain_level_rank_harmonic_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Rank Harmonic Sustain Level...")
        ic(max)
        self.__rank_harmonics_sustain_spin.setMaximum(max)
        ic("Maximum Rank Harmonic Sustain Level Set.")

    def release_time_rank_harmonic_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Rank Harmonic Release Time...")
        ic(min)
        self.__rank_harmonics_release_spin.setMinimum(min)
        ic("Minimum Rank Harmonic Release Time Set.")

    def release_time_rank_harmonic_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Rank Harmonic Release Time...")
        ic(max)
        self.__rank_harmonics_release_spin.setMaximum(max)
        ic("Maximum Rank Harmonic Release Time Set.")

    def attack_time_rank_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Rank Attack Time...")
        ic(min)
        self.__rank_attack_spin.setMinimum(min)
        ic("Minimum Rank Attack Time Set.")

    def attack_time_rank_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Rank Attack Time...")
        ic(max)
        self.__rank_attack_spin.setMaximum(max)
        ic("Maximum Rank Attack Time Set.")

    def decay_time_rank_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Rank Decay Time...")
        ic(min)
        self.__rank_decay_spin.setMinimum(min)
        ic("Minimum Rank Decay Time Set.")

    def decay_time_rank_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Rank Decay Time...")
        ic(max)
        self.__rank_decay_spin.setMaximum(max)
        ic("Maximum Rank Decay Time Set.")

    def sustain_level_rank_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Rank Sustain Level...")
        ic(min)
        self.__rank_sustain_spin.setMinimum(min)
        ic("Minimum Rank Sustain Level Set.")

    def sustain_level_rank_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Rank Sustain Level...")
        ic(max)
        self.__rank_sustain_spin.setMaximum(max)
        ic("Maximum Rank Sustain Level Set.")

    def release_time_rank_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Rank Release Time...")
        ic()
        ic(min)
        self.__rank_release_spin.setMinimum(min)
        ic("Minimum Rank Release Time Set.")

    def release_time_rank_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Rank Release Time...")
        ic(max)
        self.__rank_release_spin.setMaximum(max)
        ic("Maximum Rank Release Time Set.")

    def rank_number_pipe_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Rank Number...")
        ic(min)
        self.__rank_number_pipe_spin.setMinimum(min)
        ic("Minimum Rank Number Set.")

    def rank_number_pipe_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Rank Number...")
        ic(max)
        self.__rank_number_pipe_spin.setMaximum(max)
        ic("Maximum Rank Number Set.")

    def pipe_number_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Pipe Number...")
        ic(min)
        self.__pipe_number_spin.setMinimum(min)
        ic("Minimum Pipe Number Set.")

    def pipe_number_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Pipe Number...")
        ic(max)
        self.__pipe_number_spin.setMaximum(max)
        ic("Maximum Pipe Number Set.")

    def note_populate(self, notes: tuple[str, ...]) -> None:
        ic("Populating Notes...")
        ic(notes)
        self.__note_combo.addItems(notes)
        ic("Notes Populated.")

    def relative_note_populate(self, notes: tuple[str, ...]) -> None:
        ic("Populating Relative Notes...")
        ic(notes)
        self.__relative_note_combo.addItems(notes)
        ic("Relative Notes Populated.")

    def harmonic_number_pipe_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Pipe Harmonic Number...")
        ic(min)
        self.__pipe_harmonic_number_spin.setMinimum(min)
        ic("Minimum Pipe Harmonic Number Set.")

    def harmonic_number_pipe_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Pipe Harmonic Number...")
        ic(max)
        self.__pipe_harmonic_number_spin.setMaximum(max)
        ic("Maximum Pipe Harmonic Number Set.")

    def amplitude_pipe_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Pipe Amplitude...")
        ic(min)
        self.__pipe_amplitude_spin.setMinimum(min)
        ic("Minimum Pipe Amplitude Set.")

    def amplitude_pipe_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Pipe Amplitude...")
        ic(max)
        self.__pipe_amplitude_spin.setMaximum(max)
        ic("Maximum Pipe Amplitude Set.")

    def attack_time_pipe_harmonic_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Pipe Harmonic Attack Time...")
        ic(min)
        self.__pipe_harmonics_attack_spin.setMinimum(min)
        ic("Minimum Pipe Harmonic Attack Time Set.")

    def attack_time_pipe_harmonic_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Pipe Harmonic Attack Time...")
        ic(max)
        self.__pipe_harmonics_attack_spin.setMaximum(max)
        ic("Maximum Pipe Harmonic Attack Time Set.")

    def decay_time_pipe_harmonic_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Pipe Harmonic Decay Time...")
        ic(min)
        self.__pipe_harmonics_decay_spin.setMinimum(min)
        ic("Minimum Pipe Harmonic Decay Time Set.")

    def decay_time_pipe_harmonic_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Pipe Harmonic Decay Time...")
        ic(max)
        self.__pipe_harmonics_decay_spin.setMaximum(max)
        ic("Maximum Pipe Harmonic Decay Time Set.")

    def sustain_level_pipe_harmonic_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Pipe Harmonic Sustain Level...")
        ic(min)
        self.__pipe_harmonics_sustain_spin.setMinimum(min)
        ic("Minimum Pipe Harmonic Sustain Level Set.")

    def sustain_level_pipe_harmonic_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Pipe Harmonic Sustain Level...")
        ic(max)
        self.__pipe_harmonics_sustain_spin.setMaximum(max)
        ic("Maximum Pipe Harmonic Sustain Level Set.")

    def release_time_pipe_harmonic_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Pipe Harmonic Release Time...")
        ic(min)
        self.__pipe_harmonics_release_spin.setMinimum(min)
        ic("Minimum Pipe Harmonic Release Time Set.")

    def release_time_pipe_harmonic_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Pipe Harmonic Release Time...")
        ic(max)
        self.__pipe_harmonics_release_spin.setMaximum(max)
        ic("Maximum Pipe Harmonic Release Time Set.")

    def attack_time_pipe_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Pipe Attack Time...")
        ic(min)
        self.__pipe_attack_spin.setMinimum(min)
        ic("Minimum Pipe Attack Time Set.")

    def attack_time_pipe_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Pipe Attack Time...")
        ic(max)
        self.__pipe_attack_spin.setMaximum(max)
        ic("Maximum Pipe Attack Time Set.")

    def decay_time_pipe_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Pipe Decay Time...")
        ic(min)
        self.__pipe_decay_spin.setMinimum(min)
        ic("Minimum Pipe Decay Time Set.")

    def decay_time_pipe_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Pipe Decay Time...")
        ic(max)
        self.__pipe_decay_spin.setMaximum(max)
        ic("Maximum Pipe Decay Time Set.")

    def sustain_level_pipe_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Pipe Sustain Level...")
        ic(min)
        self.__pipe_sustain_spin.setMinimum(min)
        ic("Minimum Pipe Sustain Level Set.")

    def sustain_level_pipe_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Pipe Sustain Level...")
        ic(max)
        self.__pipe_sustain_spin.setMaximum(max)
        ic("Maximum Pipe Sustain Level Set.")

    def release_time_pipe_set_minimum(self, min: int) -> None:
        ic("Setting Minimum Pipe Release Time...")
        ic(min)
        self.__pipe_release_spin.setMinimum(min)
        ic("Minimum Pipe Release Time Set.")

    def release_time_pipe_set_maximum(self, max: int) -> None:
        ic("Setting Maximum Pipe Release Time...")
        ic(max)
        self.__pipe_release_spin.setMaximum(max)
        ic("Maximum Pipe Release Time Set.")

    #==========================================================================
    # Data Manipulation
    #==========================================================================
    def update_stop_header(self) -> None:
        ic("Updating Stop Header...")
        match self.number_ranks:
            case 1:
                stop_name = f"{self.stop_name} {self.rank_size}"
            case 2:
                stop_name = f"{self.stop_name} II"
            case 3:
                stop_name = f"{self.stop_name} III"
            case 4:
                stop_name = f"{self.stop_name} IV"
            case 5:
                stop_name = f"{self.stop_name} V"
            case 6:
                stop_name = f"{self.stop_name} VI"
            case 7:
                stop_name = f"{self.stop_name} VII"
            case 8:
                stop_name = f"{self.stop_name} VIII"
            case 9:
                stop_name = f"{self.stop_name} IX"
            case 10:
                stop_name = f"{self.stop_name} X"
            case _:
                stop_name = ""
        ic(stop_name)
        self.__header_edit.setText(stop_name)
        ic("Stop Header Updated.")

    def stop_name_change(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Stop Name Change...")
        ic(action)
        self.__stop_name_combo.currentTextChanged.connect(action)
        ic("Stop Name Change Complete.")

    def stop_family_change(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Stop Family Change...")
        ic(action)
        self.__stop_family_combo.currentTextChanged.connect(action)
        ic("Stop Family Change Complete.")

    def organ_division_change(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Organ Division Change...")
        ic(action)
        self.__organ_division_combo.currentTextChanged.connect(action)
        ic("Organ Division Change Complete.")

    def number_ranks_change(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Number of Ranks Change...")
        ic(action)
        self.__number_ranks_spin.valueChanged.connect(action)
        ic("Number of Ranks Change Complete.")

    def rank_series_change(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Series Change...")
        self.__rank_series_combo.currentTextChanged.connect(action)
        ic("Rank Series Change Complete.")

    def rank_number_change(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Number Change...")
        ic(action)
        self.__rank_number_spin.valueChanged.connect(action)
        ic("Rank Number Change Complete.")

    def rank_size_change(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Size Change...")
        ic(action)
        self.__rank_size_combo.currentTextChanged.connect(action)
        ic("Rank Size Change Complete.")

    def number_pipes_change(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Number of Pipes Change...")
        ic(action)
        self.__number_pipes_spin.valueChanged.connect(action)
        ic("Number of Pipes Change Complete.")

    def pipe_type_change(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Type Change...")
        ic(action)
        self.__pipe_type_combo.currentTextChanged.connect(action)
        ic("Pipe Type Change Complete.")

    def starting_note_change(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Starting Note Change...")
        ic(action)
        self.__starting_note_combo.currentTextChanged.connect(action)
        ic("Starting Note Change Complete.")

    def frequency_offset_change(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Frequency Offset Change...")
        ic(action)
        self.__frequency_offset_spin.valueChanged.connect(action)
        ic("Frequency Offset Change Complete.")

    def number_harmonics_change(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Number of Harmonics Change...")
        ic(action)
        self.__number_harmonics_spin.valueChanged.connect(action)
        ic("Number of Harmonics Change Complete.")

    def harmonic_number_rank_change(
        self,
        action: Callable[[], None]
    ) -> None:
        ic("Initiating Harmonic Number Change...")
        ic(action)
        self.__rank_harmonic_number_spin.valueChanged.connect(action)
        ic("Harmonic Number Change Complete.")

    def amplitude_rank_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Amplitude Change...")
        ic(action)
        self.__rank_amplitude_spin.valueChanged.connect(action)
        ic("Rank Amplitude Change Complete.")

    def attack_time_rank_harmonic_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Harmonic Attack Time Change...")
        ic(action)
        self.__rank_harmonics_attack_spin.valueChanged.connect(action)
        ic("Rank Harmonic Attack Time Change Complete.")

    def decay_time_rank_harmonic_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Harmonic Decay Time Change...")
        ic(action)
        self.__rank_harmonics_decay_spin.valueChanged.connect(action)
        ic("Rank Harmonic Decay Time Change Complete.")

    def sustain_level_rank_harmonic_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Harmonic Sustain Level Change...")
        ic(action)
        self.__rank_harmonics_sustain_spin.valueChanged.connect(action)
        ic("Rank Harmonic Sustain Level Change Complete.")

    def release_time_rank_harmonic_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Harmonic Release Time Change...")
        ic(action)
        self.__rank_harmonics_release_spin.valueChanged.connect(action)
        ic("Rank Harmonic Release Time Change Complete.")

    def attack_time_rank_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Attack Time Change...")
        ic(action)
        self.__rank_attack_spin.valueChanged.connect(action)
        ic("Rank Attack Time Change Complete.")

    def decay_time_rank_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Decay Time Change...")
        ic(action)
        self.__rank_decay_spin.valueChanged.connect(action)
        ic("Rank Decay Time Change Complete.")

    def sustain_level_rank_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Sustain Level Change...")
        ic(action)
        self.__rank_sustain_spin.valueChanged.connect(action)
        ic("Rank Sustain Level Change Complete.")

    def release_time_rank_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Release Time Change...")
        ic(action)
        self.__rank_release_spin.valueChanged.connect(action)
        ic("Rank Release Time Change Complete.")

    def rank_number_pipe_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Rank Number Change...")
        ic(action)
        self.__rank_number_pipe_spin.valueChanged.connect(action)
        ic("Rank Number Change Complete.")

    def pipe_number_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Number Change...")
        ic(action)
        self.__pipe_number_spin.valueChanged.connect(action)
        ic("Pipe Number Change Complete.")

    def note_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Note Change...")
        ic(action)
        self.__note_combo.currentTextChanged.connect(action)
        ic("Note Change Complete.")

    def relative_note_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Relative Note Change...")
        ic(action)
        self.__relative_note_combo.currentTextChanged.connect(action)
        ic("Relative Note Change Complete.")

    def harmonic_number_pipe_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Harmonic Number Change...")
        ic(action)
        self.__pipe_harmonic_number_spin.valueChanged.connect(action)
        ic("Pipe Harmonic Number Change Complete.")

    def amplitude_pipe_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Amplitude Change...")
        ic(action)
        self.__pipe_amplitude_spin.valueChanged.connect(action)
        ic("Pipe Amplitude Change Complete.")

    def attack_time_pipe_harmonic_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Harmonic Attack Time Change...")
        ic(action)
        self.__pipe_harmonics_attack_spin.valueChanged.connect(action)
        ic("Pipe Harmonic Attack Time Change Complete.")

    def decay_time_pipe_harmonic_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Harmonic Decay Time Change...")
        ic(action)
        self.__pipe_harmonics_decay_spin.valueChanged.connect(action)
        ic("Pipe Harmonic Decay Time Change Complete.")

    def sustain_level_pipe_harmonic_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Harmonic Sustain Level Change...")
        ic(action)
        self.__pipe_harmonics_sustain_spin.valueChanged.connect(action)
        ic("Pipe Harmonic Sustain Level Change Complete.")

    def release_time_pipe_harmonic_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Harmonic Release Time Change...")
        ic(action)
        self.__pipe_harmonics_release_spin.valueChanged.connect(action)
        ic("Pipe Harmonic Release Time Change Complete.")

    def attack_time_pipe_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Attack Time Change...")
        ic(action)
        self.__pipe_attack_spin.valueChanged.connect(action)
        ic("Pipe Attack Time Change Complete.")

    def decay_time_pipe_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Decay Time Change...")
        ic(action)
        self.__pipe_decay_spin.valueChanged.connect(action)
        ic("Pipe Decay Time Change Complete.")

    def sustain_level_pipe_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Sustain Level Change...")
        ic(action)
        self.__pipe_sustain_spin.valueChanged.connect(action)
        ic("Pipe Sustain Level Change Complete.")

    def release_time_pipe_change(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Pipe Release Time Change...")
        ic(action)
        self.__pipe_release_spin.valueChanged.connect(action)
        ic("Pipe Release Time Change Complete.")

    def load_stop_action(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Load Stop Action...")
        ic(action)
        self.__load_button.clicked.connect(action)
        ic("Load Stop Action Complete.")

    def cancel_changes_action(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Cancel Changes Action...")
        ic(action)
        self.__cancel_button.clicked.connect(action)
        ic("Cancel Changes Action Complete.")

    def save_stop_action(
            self,
            action: Callable[[], None]
    ) -> None:
        ic("Initiating Save Stop Action...")
        ic(action)
        self.__save_button.clicked.connect(action)
        ic("Save Stop Action Complete.")

    #**************************************************************************
    # Properties
    #**************************************************************************
    #==========================================================================
    # Stop Header
    #==========================================================================
    @property
    def stop_header(self) -> str:
        ic("Getting Stop Header...")
        value: str = self.__header_edit.text()
        ic(value)
        ic("Stop Header Retrieved.")
        return value

    #==========================================================================
    # Stop Name
    #==========================================================================
    @property
    def stop_name(self) -> str:
        ic("Getting Stop Name...")
        value: str = self.__stop_name_combo.currentText()
        ic(value)
        ic("Stop Name Retrieved.")
        return value

    @stop_name.setter
    def stop_name(self, value: str) -> None:
        ic("Setting Stop Name...")
        ic(value)
        self.__stop_name_combo.setCurrentText(value)
        ic("Stop Name Set.")

    #==========================================================================
    # Stop Family
    #==========================================================================
    @property
    def stop_family(self) -> str:
        ic("Getting Stop Family...")
        value: str = self.__stop_family_combo.currentText()
        ic(value)
        ic("Stop Family Retrieved.")
        return value

    @stop_family.setter
    def stop_family(self, value: str) -> None:
        ic("Setting Stop Family...")
        ic(value)
        self.__stop_family_combo.setCurrentText(value)
        ic("Stop Family Set.")

    #==========================================================================
    # Organ Division
    #==========================================================================
    @property
    def organ_division(self) -> str:
        ic("Getting Organ Division...")
        value: str = self.__organ_division_combo.currentText()
        ic(value)
        ic("Organ Division Retrieved.")
        return value

    @organ_division.setter
    def organ_division(self, value: str) -> None:
        ic("Setting Organ Division...")
        ic(value)
        self.__organ_division_combo.setCurrentText(value)
        ic("Organ Division Set.")

    #==========================================================================
    # Number of Ranks
    #==========================================================================
    @property
    def number_ranks(self) -> int:
        ic("Getting Number of Ranks...")
        value: int = self.__number_ranks_spin.value()
        ic(value)
        ic("Number of Ranks Retrieved.")
        return value

    @number_ranks.setter
    def number_ranks(self, value: int) -> None:
        ic("Setting Number of Ranks...")
        ic(value)
        self.__number_ranks_spin.setValue(value)
        ic("Number of Ranks Set.")

    #==========================================================================
    # Rank Series
    #==========================================================================
    @property
    def rank_series(self) -> str:
        ic("Getting Rank Series...")
        value: str = self.__rank_series_combo.currentText()
        ic(value)
        ic("Rank Series Retrieved.")
        return value

    @rank_series.setter
    def rank_series(self, value: str) -> None:
        ic("Setting Rank Series...")
        ic(value)
        self.__rank_series_combo.setCurrentText(value)
        ic("Rank Series Set.")

    #==========================================================================
    # Rank Number
    #==========================================================================
    @property
    def rank_number(self) -> int:
        ic("Getting Rank Number...")
        value: int = self.__rank_number_spin.value()
        ic(value)
        ic("Rank Number Retrieved.")
        return value

    @rank_number.setter
    def rank_number(self, value: int) -> None:
        ic("Setting Rank Number...")
        ic(value)
        self.__rank_number_spin.setValue(value)
        ic("Rank Number Set.")

    #==========================================================================
    # Rank Size
    #==========================================================================
    @property
    def rank_size(self) -> str:
        ic("Getting Rank Size...")
        value: str = self.__rank_size_combo.currentText()
        ic(value)
        ic("Rank Size Retrieved.")
        return value

    @rank_size.setter
    def rank_size(self, value: str) -> None:
        ic("Setting Rank Size...")
        ic(value)
        self.__rank_size_combo.setCurrentText(value)
        ic("Rank Size Set.")

    #==========================================================================
    # Number of Pipes
    #==========================================================================
    @property
    def number_pipes(self) -> int:
        ic("Getting Number of Pipes...")
        value: int = self.__number_pipes_spin.value()
        ic(value)
        ic("Number of Pipes Retrieved.")
        return value

    @number_pipes.setter
    def number_pipes(self, value: int) -> None:
        ic("Setting Number of Pipes...")
        ic(value)
        self.__number_pipes_spin.setValue(value)
        ic("Number of Pipes Set.")

    #==========================================================================
    # Pipe Type
    #==========================================================================
    @property
    def pipe_type(self) -> str:
        ic("Getting Pipe Type...")
        value: str = self.__pipe_type_combo.currentText()
        ic(value)
        ic("Pipe Type Retrieved.")
        return value

    @pipe_type.setter
    def pipe_type(self, value: str) -> None:
        ic("Setting Pipe Type...")
        ic(value)
        self.__pipe_type_combo.setCurrentText(value)
        ic("Pipe Type Set.")

    #==========================================================================
    # Starting Note
    #==========================================================================
    @property
    def starting_note(self) -> str:
        ic("Getting Starting Note...")
        value: str = self.__starting_note_combo.currentText()
        ic(value)
        ic("Starting Note Retrieved.")
        return value

    @starting_note.setter
    def starting_note(self, value: str) -> None:
        ic("Setting Starting Note...")
        ic(value)
        self.__starting_note_combo.setCurrentText(value)
        ic("Starting Note Set.")

    #==========================================================================
    # Frequency Offset
    #==========================================================================
    @property
    def frequency_offset(self) -> int:
        ic("Getting Frequency Offset...")
        value: int = self.__frequency_offset_spin.value()
        ic(value)
        ic("Frequency Offset Retrieved.")
        return value

    @frequency_offset.setter
    def frequency_offset(self, value: int) -> None:
        ic("Setting Frequency Offset...")
        ic(value)
        self.__frequency_offset_spin.setValue(value)
        ic("Frequency Offset Set.")

    #==========================================================================
    # Number of Harmonics
    #==========================================================================
    @property
    def number_harmonics(self) -> int:
        ic("Getting Number of Harmonics...")
        value: int = self.__number_harmonics_spin.value()
        ic(value)
        ic("Number of Harmonics Retrieved.")
        return value

    @number_harmonics.setter
    def number_harmonics(self, value: int) -> None:
        ic("Setting Number of Harmonics...")
        ic(value)
        self.__number_harmonics_spin.setValue(value)
        ic("Number of Harmonics Set.")

    #==========================================================================
    # Harmonic Number - Rank
    #==========================================================================
    @property
    def harmonic_number_rank(self) -> int:
        ic("Getting Harmonic Number...")
        value: int = self.__rank_harmonic_number_spin.value()
        ic(value)
        ic("Harmonic Number Retrieved.")
        return self.__rank_harmonic_number_spin.value()

    @harmonic_number_rank.setter
    def harmonic_number_rank(self, value: int) -> None:
        ic("Setting Harmonic Number...")
        ic(value)
        self.__rank_harmonic_number_spin.setValue(value)
        ic("Harmonic Number Set.")

    #==========================================================================
    # Amplitude - Rank
    #==========================================================================
    @property
    def amplitude_rank(self) -> int:
        ic("Getting Rank Amplitude...")
        value: int = self.__rank_amplitude_spin.value()
        ic(value)
        ic("Rank Amplitude Retrieved.")
        return value

    @amplitude_rank.setter
    def amplitude_rank(self, value: int) -> None:
        ic("Setting Rank Amplitude...")
        ic(value)
        self.__rank_amplitude_spin.setValue(value)
        ic("Rank Amplitude Set.")

    #==========================================================================
    # Attack Time - Harmonic - Rank
    #==========================================================================
    @property
    def attack_time_harmonic_rank(self) -> int:
        ic("Getting Rank Harmonic Attack Time...")
        value: int = self.__rank_harmonics_attack_spin.value()
        ic(value)
        ic("Rank Harmonic Attack Time Retrieved.")
        return value

    @attack_time_harmonic_rank.setter
    def attack_time_harmonic_rank(self, value: int) -> None:
        ic("Setting Rank Harmonic Attack Time...")
        ic(value)
        self.__rank_harmonics_attack_spin.setValue(value)
        ic("Rank Harmonic Attack Time Set.")

    #==========================================================================
    # Decay Time - Harmonic - Rank
    #==========================================================================
    @property
    def decay_time_harmonic_rank(self) -> int:
        ic("Getting Rank Harmonic Decay Time...")
        value: int = self.__rank_harmonics_decay_spin.value()
        ic(value)
        ic("Rank Harmonic Decay Time Retrieved.")
        return value

    @decay_time_harmonic_rank.setter
    def decay_time_harmonic_rank(self, value: int) -> None:
        ic("Setting Rank Harmonic Decay Time...")
        ic(value)
        self.__rank_harmonics_decay_spin.setValue(value)
        ic("Rank Harmonic Decay Time Set.")

    #==========================================================================
    # Sustain Level - Harmonic - Rank
    #==========================================================================
    @property
    def sustain_level_harmonic_rank(self) -> int:
        ic("Getting Rank Harmonic Sustain Level...")
        value: int = self.__rank_harmonics_sustain_spin.value()
        ic(value)
        ic("Rank Harmonic Sustain Level Retrieved.")
        return value

    @sustain_level_harmonic_rank.setter
    def sustain_level_harmonic_rank(self, value: int) -> None:
        ic("Setting Rank Harmonic Sustain Level...")
        ic(value)
        self.__rank_harmonics_sustain_spin.setValue(value)
        ic("Rank Harmonic Sustain Level Set.")

    #==========================================================================
    # Release Time - Harmonic - Rank
    #==========================================================================
    @property
    def release_time_harmonic_rank(self) -> int:
        ic("Getting Rank Harmonic Release Time...")
        value: int = self.__rank_harmonics_release_spin.value()
        ic(value)
        ic("Rank Harmonic Release Time Retrieved.")
        return value

    @release_time_harmonic_rank.setter
    def release_time_harmonic_rank(self, value: int) -> None:
        ic("Setting Rank Harmonic Release Time...")
        ic(value)
        self.__rank_harmonics_release_spin.setValue(value)
        ic("Rank Harmonic Release Time Set.")

    #==========================================================================
    # Attack Time - Rank
    #==========================================================================
    @property
    def attack_time_rank(self) -> int:
        ic("Getting Rank Attack Time...")
        value: int = int(self.__rank_attack_spin.value())
        ic(value)
        ic("Rank Attack Time Retrieved.")
        return value

    @attack_time_rank.setter
    def attack_time_rank(self, value: int) -> None:
        ic("Setting Rank Attack Time...")
        ic(value)
        self.__rank_attack_spin.setValue(value)
        ic("Rank Attack Time Set.")

    #==========================================================================
    # Decay Time - Rank
    #==========================================================================
    @property
    def decay_time_rank(self) -> int:
        ic("Getting Rank Decay Time...")
        value: int = self.__rank_decay_spin.value()
        ic(value)
        ic("Rank Decay Time Retrieved.")
        return value

    @decay_time_rank.setter
    def decay_time_rank(self, value: int) -> None:
        ic("Setting Rank Decay Time...")
        ic(value)
        self.__rank_decay_spin.setValue(value)
        ic("Rank Decay Time Set.")

    #==========================================================================
    # Sustain Level - Rank
    #==========================================================================
    @property
    def sustain_level_rank(self) -> int:
        ic("Getting Rank Sustain Level...")
        value: int = self.__rank_sustain_spin.value()
        ic(value)
        ic("Rank Sustain Level Retrieved.")
        return value

    @sustain_level_rank.setter
    def sustain_level_rank(self, value: int) -> None:
        ic("Setting Rank Sustain Level...")
        ic(value)
        self.__rank_sustain_spin.setValue(value)
        ic("Rank Sustain Level Set.")

    #==========================================================================
    # Release Time - Rank
    #==========================================================================
    @property
    def release_time_rank(self) -> int:
        ic("Getting Rank Release Time...")
        value: int = self.__rank_release_spin.value()
        ic(value)
        ic("Rank Release Time Retrieved.")
        return value

    @release_time_rank.setter
    def release_time_rank(self, value: int) -> None:
        ic("Setting Rank Release Time...")
        ic(value)
        self.__rank_release_spin.setValue(value)
        ic("Rank Release Time Set.")

    #==========================================================================
    # Rank Number - Pipe
    #==========================================================================
    @property
    def rank_number_pipe(self) -> int:
        ic("Getting Rank Number...")
        value: int = self.__rank_number_pipe_spin.value()
        ic(value)
        ic("Rank Number Retrieved.")
        return value

    @rank_number_pipe.setter
    def rank_number_pipe(self, value: int) -> None:
        ic("Setting Rank Number...")
        ic(value)
        self.__rank_number_pipe_spin.setValue(value)
        ic("Rank Number Set.")

    #==========================================================================
    # Pipe Number
    #==========================================================================
    @property
    def pipe_number(self) -> int:
        ic("Getting Pipe Number...")
        value: int = self.__pipe_number_spin.value()
        ic(value)
        ic("Pipe Number Retrieved.")
        return value

    @pipe_number.setter
    def pipe_number(self, value: int) -> None:
        ic("Setting Pipe Number...")
        ic(value)
        self.__pipe_number_spin.setValue(value)
        ic("Pipe Number Set.")

    #==========================================================================
    # Note
    #==========================================================================
    @property
    def note(self) -> str:
        ic("Getting Note...")
        value: str = self.__note_combo.currentText()
        ic(value)
        ic("Note Retrieved.")
        return value

    @note.setter
    def note(self, value: str) -> None:
        ic("Setting Note...")
        ic(value)
        self.__note_combo.setCurrentText(value)
        ic("Note Set.")

    #==========================================================================
    # Relative Note
    #==========================================================================
    @property
    def relative_note(self) -> str:
        ic("Getting Relative Note...")
        value: str = self.__relative_note_combo.currentText()
        ic(value)
        ic("Relative Note Retrieved.")
        return value

    @relative_note.setter
    def relative_note(self, value: str) -> None:
        ic("Setting Relative Note...")
        ic(value)
        self.__relative_note_combo.setCurrentText(value)
        ic("Relative Note Set.")

    #==========================================================================
    # Harmonic Number - Pipe
    #==========================================================================
    @property
    def harmonic_number_pipe(self) -> int:
        ic("Getting Pipe Harmonic Number...")
        value: int = self.__pipe_harmonic_number_spin.value()
        ic(value)
        ic("Pipe Harmonic Number Retrieved.")
        return value

    @harmonic_number_pipe.setter
    def harmonic_number_pipe(self, value: int) -> None:
        ic("Setting Pipe Harmonic Number...")
        ic(value)
        self.__pipe_harmonic_number_spin.setValue(value)
        ic("Pipe Harmonic Number Set.")

    #==========================================================================
    # Amplitude - Pipe
    #==========================================================================
    @property
    def amplitude_pipe(self) -> int:
        ic("Getting Pipe Amplitude...")
        value: int = self.__pipe_amplitude_spin.value()
        ic(value)
        ic("Pipe Amplitude Retrieved.")
        return value

    @amplitude_pipe.setter
    def amplitude_pipe(self, value: int) -> None:
        ic("Setting Pipe Amplitude...")
        ic(value)
        self.__pipe_amplitude_spin.setValue(value)
        ic("Pipe Amplitude Set.")

    #==========================================================================
    # Attack Time - Harmonic - Pipe
    #==========================================================================
    @property
    def attack_time_harmonic_pipe(self) -> int:
        ic("Getting Pipe Harmonic Attack Time...")
        value: int = self.__pipe_harmonics_attack_spin.value()
        ic(value)
        ic("Pipe Harmonic Attack Time Retrieved.")
        return value

    @attack_time_harmonic_pipe.setter
    def attack_time_harmonic_pipe(self, value: int) -> None:
        ic("Setting Pipe Harmonic Attack Time...")
        ic(value)
        self.__pipe_harmonics_attack_spin.setValue(value)
        ic("Pipe Harmonic Attack Time Set.")

    #==========================================================================
    # Decay Time - Harmonic - Pipe
    #==========================================================================
    @property
    def decay_time_harmonic_pipe(self) -> int:
        ic("Getting Pipe Harmonic Decay Time...")
        value: int = self.__pipe_harmonics_decay_spin.value()
        ic(value)
        ic("Pipe Harmonic Decay Time Retrieved.")
        return value

    @decay_time_harmonic_pipe.setter
    def decay_time_harmonic_pipe(self, value: int) -> None:
        ic("Setting Pipe Harmonic Decay Time...")
        ic(value)
        self.__pipe_harmonics_decay_spin.setValue(value)
        ic("Pipe Harmonic Decay Time Set.")

    #==========================================================================
    # Sustain Level - Harmonic - Pipe
    #==========================================================================
    @property
    def sustain_level_harmonic_pipe(self) -> int:
        ic("Getting Pipe Harmonic Sustain Level...")
        value: int = self.__pipe_harmonics_sustain_spin.value()
        ic(value)
        ic("Pipe Harmonic Sustain Level Retrieved.")
        return value

    @sustain_level_harmonic_pipe.setter
    def sustain_level_harmonic_pipe(self, value: int) -> None:
        ic("Setting Pipe Harmonic Sustain Level...")
        ic(value)
        self.__pipe_harmonics_sustain_spin.setValue(value)
        ic("Pipe Harmonic Sustain Level Set.")

    #==========================================================================
    # Release Time - Harmonic - Pipe
    #==========================================================================
    @property
    def release_time_harmonic_pipe(self) -> int:
        ic("Getting Pipe Harmonic Release Time...")
        value: int = self.__pipe_harmonics_release_spin.value()
        ic(value)
        ic("Pipe Harmonic Release Time Retrieved.")
        return value

    @release_time_harmonic_pipe.setter
    def release_time_harmonic_pipe(self, value: int) -> None:
        ic("Setting Pipe Harmonic Release Time...")
        ic(value)
        self.__pipe_harmonics_release_spin.setValue(value)
        ic("Pipe Harmonic Release Time Set.")

    #==========================================================================
    # Attack Time - Pipe
    #==========================================================================
    @property
    def attack_time_pipe(self) -> int:
        ic("Getting Pipe Attack Time...")
        value: int = self.__pipe_attack_spin.value()
        ic(value)
        ic("Pipe Attack Time Retrieved.")
        return value

    @attack_time_pipe.setter
    def attack_time_pipe(self, value: int) -> None:
        ic("Setting Pipe Attack Time...")
        ic(value)
        self.__pipe_attack_spin.setValue(value)
        ic("Pipe Attack Time Set.")

    #==========================================================================
    # Decay Time - Pipe
    #==========================================================================
    @property
    def decay_time_pipe(self) -> int:
        ic("Getting Pipe Decay Time...")
        value: int = self.__pipe_decay_spin.value()
        ic(value)
        ic("Pipe Decay Time Retrieved.")
        return value

    @decay_time_pipe.setter
    def decay_time_pipe(self, value: int) -> None:
        ic("Setting Pipe Decay Time...")
        ic(value)
        self.__pipe_decay_spin.setValue(value)
        ic("Pipe Decay Time Set.")

    #==========================================================================
    # Sustain Level - Pipe
    #==========================================================================
    @property
    def sustain_level_pipe(self) -> int:
        ic("Getting Pipe Sustain Level...")
        value: int = self.__pipe_sustain_spin.value()
        ic(value)
        ic("Pipe Sustain Level Retrieved.")
        return value

    @sustain_level_pipe.setter
    def sustain_level_pipe(self, value: int) -> None:
        ic("Setting Pipe Sustain Level...")
        ic(value)
        self.__pipe_sustain_spin.setValue(value)
        ic("Pipe Sustain Level Set.")

    #==========================================================================
    # Release Time - Pipe
    #==========================================================================
    @property
    def release_time_pipe(self) -> int:
        ic("Getting Pipe Release Time...")
        value: int = self.__pipe_release_spin.value()
        ic(value)
        ic("Pipe Release Time Retrieved.")
        return value

    @release_time_pipe.setter
    def release_time_pipe(self, value: int) -> None:
        ic("Setting Pipe Release Time...")
        ic(value)
        self.__pipe_release_spin.setValue(value)
        ic("Pipe Release Time Set.")


#******************************************************************************
# Main
#******************************************************************************
def main() -> None:
    app: QApplication = QApplication([])
    window: StopEditor = StopEditor()
    window.show()
    app.exec()


###############################################################################
# Executable
###############################################################################
if __name__ == "__main__":
    main()
