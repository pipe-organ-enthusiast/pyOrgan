"""Stop Editor"""
from typing import Callable
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
#------------------------------------------------------------------------------
from icecream import ic  # type: ignore


class StopEditor(QFrame):
    def __init__(self) -> None:
        print("Initializing Stop Editor...")
        ic()
        super().__init__()
        self.__init_ui()
        self.__ui_settings()
        self.__ui_layout()
        self.__rank_harmonics_checked()
        self.__rank_adsr_checked()
        self.__pipe_harmonics_checked()
        self.__pipe_adsr_checked()
        print("Stop Editor Initialized.")

    #**************************************************************************
    # Widgets
    #**************************************************************************
    def __init_ui(self) -> None:
        print("Initializing Widgets...")
        ic()
        self.__init_ui_header()
        self.__init_ui_editor()
        self.__init_ui_options()
        print("Widgets Initialized.")

    #==========================================================================
    # Header
    #==========================================================================
    def __init_ui_header(self) -> None:
        print("Initializing Header...")
        ic()
        self.header_widget: QWidget = QWidget()
        self.__header_label: QLabel = QLabel("Stop:")
        self.__header_edit: QLineEdit = QLineEdit()
        print("Header Initialized.")

    #==========================================================================
    # Editor
    #==========================================================================    
    def __init_ui_editor(self) -> None:
        print("Initializing Editor...")
        ic()
        self.__editor = QWidget()
        self.__init_ui_stop_settings()
        self.__init_ui_rank_settings()
        self.__init_ui_rank_harmonics_settings()
        self.__init_ui_rank_harmonic_adsr_settings()
        self.__init_ui_rank_adsr_settings()
        self.__init_ui_pipe_settings()
        self.__init_ui_pipe_harmonics_settings()
        self.__init_ui_pipe_harmonic_adsr_settings()
        self.__init_ui_pipe_adsr_settings()
        print("Editor Initialized.")

    #--------------------------------------------------------------------------
    # Stop Settings
    #--------------------------------------------------------------------------
    def __init_ui_stop_settings(self) -> None:
        print("Initializing Stop Settings...")
        ic()
        self.__stop_settings: QGroupBox = QGroupBox("Stop Settings")
        # Stop Name
        self.__stopname_label: QLabel = QLabel("Stop Name:")
        self.__stopname_combo: QComboBox = QComboBox()
        # Stop Family
        self.__stopfamily_label: QLabel = QLabel("Stop Family:")
        self.__stopfamily_combo = QComboBox()
        # Organ Division
        self.__organdivision_label: QLabel = QLabel("Organ Division:")
        self.__organdivision_combo: QComboBox = QComboBox()
        # Number of Ranks
        self.__numranks_label: QLabel = QLabel("Number of Ranks:")
        self.__numranks_spin: QSpinBox = QSpinBox()
        # Rank Series
        self.__rankseries_label: QLabel = QLabel("Rank Series:")
        self.__rankseries_combo: QComboBox = QComboBox()
        print("Stop Settings Initialized.")

    #--------------------------------------------------------------------------
    # Rank Settings
    #--------------------------------------------------------------------------
    def __init_ui_rank_settings(self) -> None:
        print("Initializing Rank Settings...")
        ic()
        self.__rank_settings: QGroupBox = QGroupBox("Rank Settings")
        # Rank #
        self.__ranknum_label: QLabel = QLabel("Rank #:")
        self.__ranknum_spin: QSpinBox = QSpinBox()
        # Rank Size
        self.__ranksize_label: QLabel = QLabel("Rank Size:")
        self.__ranksize_combo = QComboBox()
        # Number of Pipes
        self.__numpipes_label: QLabel = QLabel("Number of Pipes:")
        self.__numpipes_spin: QSpinBox = QSpinBox()
        # Pipe Type
        self.__pipetype_label: QLabel = QLabel("PipeType:")
        self.__pipetype_combo: QComboBox = QComboBox()
        # Starting Note
        self.__startnote_label: QLabel = QLabel("Starting Note:")
        self.__startnote_combo: QComboBox = QComboBox()
        # Frequency Offset
        self.__freqoffset_label: QLabel = QLabel("Frequency Offset (Hz):")
        self.__freqoffset_spin: QSpinBox = QSpinBox()
        # Number of Harmonics
        self.__numharmonics_label: QLabel = QLabel("Number of Harmonics:")
        self.__numharmonics_spin: QSpinBox = QSpinBox()
        print("Rank Settings Initialized.")

    def __init_ui_rank_harmonics_settings(self) -> None:
        print("Initializing Rank Harmonics Settings...")
        ic()
        # Edit Harmonics Option
        self.__rank_harmonics_button: QCheckBox = QCheckBox("Edit Harmonics")
        # Harmonic Group
        self.__rank_harmonic: QGroupBox = QGroupBox("Harmonic Settings - Rank")
        # Harmonic #
        self.__rank_harmonicnum_label: QLabel = QLabel("Harmonic #:")
        self.__rank_harmonicnum_spin: QSpinBox = QSpinBox()
        # Amplitude
        self.__rank_amplitude_label: QLabel = QLabel("Amplitude (%):")
        self.__rank_amplitude_spin: QSpinBox = QSpinBox()
        print("Rank Harmonics Settings Initialized.")

    def __init_ui_rank_harmonic_adsr_settings(self) -> None:
        print("Initializing Rank Harmonic ADSR Settings...")
        ic()
        # Edit Harmonic ADSR Option
        self.__rankharm_adsr_button: QCheckBox = QCheckBox(
            "Edit Harmonics ADSR"
        )
        # Harmonic ADSR Group
        groupbox_text = "Harmonic ADSR Settings - Rank"
        self.__rankharm_adsr: QGroupBox = QGroupBox(groupbox_text)
        # Attack
        self.__rankharm_attack_label: QLabel = QLabel("Attack Time (ms):")
        self.__rankharm_attack_spin: QSpinBox = QSpinBox()
        # Decay
        self.__rankharm_decay_label: QLabel = QLabel("Decay Time (ms):")
        self.__rankharm_decay_spin: QSpinBox = QSpinBox()
        # Sustain
        self.__rankharm_sustain_label: QLabel = QLabel("Sustain Level (%):")
        self.__rankharm_sustain_spin: QSpinBox = QSpinBox()
        # Release
        self.__rankharm_release_label: QLabel = QLabel("Release Time (ms):")
        self.__rankharm_release_spin: QSpinBox = QSpinBox()
        print("Rank Harmonic ADSR Settings Initialized.")

    def __init_ui_rank_adsr_settings(self) -> None:
        print("Initializing Rank ADSR Settings...")
        ic()
        # Edit ADSR Option
        self.__rank_adsr_button: QCheckBox = QCheckBox("Edit ADSR")
        # ADSR Group
        self.__rank_adsr: QGroupBox = QGroupBox("ADSR Settings - Rank")
        # Attack
        self.__rank_attack_label: QLabel = QLabel("Attack Time (ms):")
        self.__rank_attack_spin: QSpinBox = QSpinBox()
        # Decay
        self.__rank_decay_label: QLabel = QLabel("Decay Time (ms):")
        self.__rank_decay_spin: QSpinBox = QSpinBox()
        # Sustain
        self.__rank_sustain_label: QLabel = QLabel("Sustain Level (%):")
        self.__rank_sustain_spin: QSpinBox = QSpinBox()
        # Release
        self.__rank_release_label: QLabel = QLabel("Release Time (ms):")
        self.__rank_release_spin: QSpinBox = QSpinBox()
        print("Rank ADSR Settings Initialized.")

    #--------------------------------------------------------------------------
    # Pipe Settings
    #--------------------------------------------------------------------------
    def __init_ui_pipe_settings(self) -> None:
        print("Initializing Pipe Settings...")
        ic()
        self.__pipe_settings: QGroupBox = QGroupBox("Pipe Settings")
        # Rank #
        self.__ranknum_pipe_label: QLabel = QLabel("Rank #:")
        self.__ranknum_pipe_spin: QSpinBox = QSpinBox()
        # Pipe #
        self.__pipenum_label: QLabel = QLabel("Pipe #:")
        self.__pipenum_spin: QSpinBox = QSpinBox()        
        # Note
        self.__note_label: QLabel = QLabel("Note:")
        self.__note_combo: QComboBox = QComboBox()
        # Relative Note
        self.__relnote_label: QLabel = QLabel("Relative Note:")
        self.__relnote_combo: QComboBox = QComboBox()
        print("Pipe Settings Initialized.")

    def __init_ui_pipe_harmonics_settings(self) -> None:
        print("Initializing Pipe Harmonics Settings...")
        ic()
        # Edit Harmonics Option
        self.__pipe_harmonics_button: QCheckBox = QCheckBox("Edit Harmonics")
        # Harmonic Group
        self.__pipe_harmonic: QGroupBox = QGroupBox("Harmonic Settings - Pipe")
        # Harmonic #
        self.__pipe_harmonicnum_label: QLabel = QLabel("Harmonic #:")
        self.__pipe_harmonicnum_spin: QSpinBox = QSpinBox()
        # Amplitude
        self.__pipe_amplitude_label: QLabel = QLabel("Amplitude (%):")
        self.__pipe_amplitude_spin: QSpinBox = QSpinBox()
        print("Pipe Harmonics Settings Initialized.")

    def __init_ui_pipe_harmonic_adsr_settings(self) -> None:
        print("Initializing Pipe Harmonic ADSR Settings...")
        ic()
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
        self.__pipeharm_attack_spin: QSpinBox = QSpinBox()
        # Decay
        self.__pipeharm_decay_label: QLabel = QLabel("Decay Time (ms):")
        self.__pipeharm_decay_spin: QSpinBox = QSpinBox()
        # Sustain
        self.__pipeharm_sustain_label: QLabel = QLabel("Sustain Level (%):")
        self.__pipeharm_sustain_spin: QSpinBox = QSpinBox()
        # Release
        self.__pipeharm_release_label: QLabel = QLabel("Release Time (ms):")
        self.__pipeharm_release_spin: QSpinBox = QSpinBox()
        print("Pipe Harmonic ADSR Settings Initialized.")

    def __init_ui_pipe_adsr_settings(self) -> None:
        print("Initializing Pipe ADSR Settings...")
        ic()
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
        print("Pipe ADSR Settings Initialized.")

    #==========================================================================
    # Options
    #==========================================================================
    def __init_ui_options(self) -> None:
        print("Initializing Options...")
        ic()
        self.__options: QWidget = QWidget()
        self.__load_button: QPushButton = QPushButton("Load Stop")
        self.__cancel_button: QPushButton = QPushButton("Cancel Changes")
        self.__save_button: QPushButton = QPushButton("Save Stop")
        print("Options Initialized.")

    #**************************************************************************
    # Settings
    #**************************************************************************
    def __ui_settings(self) -> None:
        print("Setting Up Widgets...")
        ic()
        self.setWindowTitle("pyOrgan - Stop Editor")
        self.__ui_settings_header()
        self.__ui_settings_editor()
        print("Widgets Settings Complete.")

    #==========================================================================
    # Header
    #==========================================================================
    def __ui_settings_header(self) -> None:
        print("Setting Up Header...")
        ic()
        self.__header_edit.setReadOnly(True)
        self.__header_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        print("Header Settings Complete.")

    #==========================================================================
    # Editor
    #==========================================================================
    def __ui_settings_editor(self) -> None:
        print("Setting Up Editor...")
        ic()
        self.__ui_settings_editor_groupboxes()
        self.__ui_settings_editor_labels()
        self.__ui_settings_editor_comboboxes()
        self.__ui_settings_editor_spinboxes()
        self.__ui_settings_editor_checkboxes()
        print("Editor Settings Complete.")

    def __ui_settings_editor_groupboxes(self) -> None:
        print("Setting Up Group Boxes...")
        ic()
        group_boxes: tuple[QGroupBox, ...] = (
            self.__stop_settings,
            self.__rank_settings,
            self.__pipe_settings,
            self.__rank_harmonic,
            self.__pipe_harmonic,
            self.__rankharm_adsr,
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
        print("Group Boxes Settings Complete.")

    def __ui_settings_editor_labels(self) -> None:
        print("Setting Up Labels...")
        ic()
        labels: tuple[QLabel, ...] = (
            self.__stopname_label,
            self.__stopfamily_label,
            self.__organdivision_label,
            self.__numranks_label,
            self.__rankseries_label,
            self.__ranknum_label,
            self.__ranksize_label,
            self.__numpipes_label,
            self.__startnote_label,
            self.__pipetype_label,
            self.__freqoffset_label,
            self.__numharmonics_label,
            self.__rank_harmonicnum_label,
            self.__rank_amplitude_label,
            self.__rankharm_attack_label,
            self.__rankharm_decay_label,
            self.__rankharm_sustain_label,
            self.__rankharm_release_label,
            self.__rank_attack_label,
            self.__rank_decay_label,
            self.__rank_sustain_label,
            self.__rank_release_label,
            self.__ranknum_pipe_label,
            self.__pipenum_label,
            self.__note_label,
            self.__relnote_label,
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
        print("Labels Settings Complete.")

    def __ui_settings_editor_comboboxes(self) -> None:
        print("Setting Up Combo Boxes...")
        ic()
        comboboxes: tuple[QComboBox, ...] = (
            self.__stopname_combo,
            self.__stopfamily_combo,
            self.__organdivision_combo,
            self.__rankseries_combo,
            self.__ranksize_combo,
            self.__pipetype_combo,
            self.__startnote_combo,
            self.__note_combo,
            self.__relnote_combo,
        )
        for widget in comboboxes:
            widget.setEditable(True)
            edit: QLineEdit = widget.lineEdit() # type: ignore
            edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
            if widget == self.__stopname_combo:
                edit.setReadOnly(False)
            else:
                edit.setReadOnly(True)
        self.__note_combo.setEnabled(False)
        print("Combo Boxes Settings Complete.")

    def __ui_settings_editor_spinboxes(self) -> None:
        print("Setting Up Spin Boxes...")
        ic()
        spin_boxes: tuple[QSpinBox, ...] = (
            self.__numranks_spin,
            self.__ranknum_spin,
            self.__numpipes_spin,
            self.__freqoffset_spin,
            self.__numharmonics_spin,
            self.__rank_harmonicnum_spin,
            self.__rank_amplitude_spin,
            self.__rankharm_attack_spin,
            self.__rankharm_decay_spin,
            self.__rankharm_sustain_spin,
            self.__rankharm_release_spin,
            self.__rank_attack_spin,
            self.__rank_decay_spin,
            self.__rank_sustain_spin,
            self.__rank_release_spin,
            self.__ranknum_pipe_spin,
            self.__pipenum_spin,
            self.__pipe_harmonicnum_spin,
            self.__pipe_amplitude_spin,
            self.__pipeharm_attack_spin,
            self.__pipeharm_decay_spin,
            self.__pipeharm_sustain_spin,
            self.__pipeharm_release_spin,
            self.__pipe_attack_spin,
            self.__pipe_decay_spin,
            self.__pipe_sustain_spin,
            self.__pipe_release_spin
        )
        for spin_box in spin_boxes:
            spin_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        print("Spin Boxes Settings Complete.")

    def __ui_settings_editor_checkboxes(self) -> None:
        print("Setting Up Check Boxes...")
        ic()
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
        print("Check Boxes Settings Complete.")

    #**************************************************************************
    # Layout
    #**************************************************************************
    def __ui_layout(self) -> None:
        print("Setting Up Layout...")
        ic()
        self.__ui_layout_header()
        self.__ui_layout_editor()
        self.__ui_layout_options()
        self.__ui_layout_main()
        print("Layout Complete.")

    #==========================================================================
    # Header
    #==========================================================================
    def __ui_layout_header(self) -> None:
        print("Laying Out Header...")
        ic()
        header_layout: QHBoxLayout = QHBoxLayout()
        widgets: tuple[QWidget, ...] = (
            self.__header_label,
            self.__header_edit
        )
        for widget in widgets:
            header_layout.addWidget(widget)
        self.header_widget.setLayout(header_layout)
        print("Header Layout Complete.")
    #==========================================================================
    # Editor Forms
    #==========================================================================
    def __ui_layout_editor(self) -> None:
        print("Laying Out Editor...")
        ic()
        self.__ui_layout_stop_settings()
        self.__ui_layout_rank_settings()
        self.__ui_layout_pipe_settings()
        print("Editor Layout Complete.")

    #--------------------------------------------------------------------------
    # Stop Settings
    #--------------------------------------------------------------------------
    def __ui_layout_stop_settings(self) -> None:
        print("Laying Out Stop Settings...")
        ic()
        stopsettings_layout: QFormLayout = QFormLayout()
        stopsettings_widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__stopname_label, self.__stopname_combo),
            (self.__stopfamily_label, self.__stopfamily_combo),
            (self.__organdivision_label, self.__organdivision_combo),
            (self.__numranks_label, self.__numranks_spin),
            (self.__rankseries_label, self.__rankseries_combo)
        )
        for label, widget in stopsettings_widgets:
            stopsettings_layout.addRow(label, widget)
        self.__stop_settings.setLayout(stopsettings_layout)
        print("Stop Settings Layout Complete.")
 
    #==========================================================================
    # Rank Settings
    #==========================================================================
    def __ui_layout_rank_settings(self) -> None:
        print("Laying Out Rank Settings...")
        ic()
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
        print("Rank Settings Layout Complete.")

    #--------------------------------------------------------------------------
    # Rank Header
    #--------------------------------------------------------------------------
    def __ui_layout_rank_header(self) -> QWidget:
        print("Laying Out Rank Header...")
        ic()
        rankheader_widget: QWidget = QWidget()
        rankheader_layout: QFormLayout = QFormLayout()
        rankheader_widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__ranknum_label, self.__ranknum_spin),
            (self.__ranksize_label, self.__ranksize_combo),
            (self.__pipetype_label, self.__pipetype_combo),
            (self.__startnote_label, self.__startnote_combo),
            (self.__freqoffset_label, self.__freqoffset_spin),
            (self.__numpipes_label, self.__numpipes_spin),
            (self.__numharmonics_label, self.__numharmonics_spin)
        )
        for label, widget in rankheader_widgets:
            rankheader_layout.addRow(label, widget)
        rankheader_widget.setLayout(rankheader_layout)
        print("Rank Header Layout Complete.")
        return rankheader_widget

    #--------------------------------------------------------------------------
    # Rank Harmonics Settings
    #--------------------------------------------------------------------------
    def __ui_layout_rank_harmonic_settings(self) -> QWidget:
        print("Laying Out Rank Harmonics Settings...")
        ic()
        rankharmonicsettings_widget: QWidget = QWidget()
        rankharmonicsettings_layout: QVBoxLayout = QVBoxLayout()
        rankharmonicsettings_layout.addWidget(self.__rank_harmonics_button)
        rankharmonicsettings_layout.addWidget(self.__rank_harmonic)
        rankharmonicsettings_widget.setLayout(rankharmonicsettings_layout)
        print("Rank Harmonics Settings Layout Complete.")
        return rankharmonicsettings_widget

    def __ui_layout_rank_harmonics_widget(self) -> QWidget:
        print("Laying Out Rank Harmonics Widget...")
        ic()
        rankharmonics_widget: QWidget = QWidget()
        rankharmonics_layout: QFormLayout = QFormLayout()
        rankharmonics_widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__rank_harmonicnum_label, self.__rank_harmonicnum_spin),
            (self.__rank_amplitude_label, self.__rank_amplitude_spin)
        )
        for label, widget in rankharmonics_widgets:
            rankharmonics_layout.addRow(label, widget)
        rankharmonics_widget.setLayout(rankharmonics_layout)
        print("Rank Harmonics Widget Layout Complete.")
        return rankharmonics_widget

    def __ui_layout_rank_harmonics_adsr(self) -> None:
        print("Laying Out Rank Harmonics ADSR...")
        ic()
        rankharmonicsadsr_layout: QFormLayout = QFormLayout()
        rankharmonicsadsr_widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__rankharm_attack_label, self.__rankharm_attack_spin),
            (self.__rankharm_decay_label, self.__rankharm_decay_spin),
            (self.__rankharm_sustain_label, self.__rankharm_sustain_spin),
            (self.__rankharm_release_label, self.__rankharm_release_spin)
        )
        for label, widget in rankharmonicsadsr_widgets:
            rankharmonicsadsr_layout.addRow(label, widget)
        self.__rankharm_adsr.setLayout(rankharmonicsadsr_layout)
        print("Rank Harmonics ADSR Layout Complete.")

    def __ui_layout_rank_harmonic(self) -> None:
        print("Laying Out Rank Harmonic...")
        ic()
        rankharmonic_layout: QVBoxLayout = QVBoxLayout()
        rankharmonic_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        rankharmonic_layout.addWidget(self.__ui_layout_rank_harmonics_widget())
        rankharmonic_layout.addSpacing(10)
        rankharmonic_layout.addWidget(self.__rankharm_adsr_button)
        rankharmonic_layout.addWidget(self.__rankharm_adsr)
        self.__rank_harmonic.setLayout(rankharmonic_layout)
        print("Rank Harmonic Layout Complete.")

    #--------------------------------------------------------------------------
    # Rank ADSR Settings
    #--------------------------------------------------------------------------
    def __ui_layout_rank_adsr(self) -> QWidget:
        print("Laying Out Rank ADSR...")
        ic()
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
        print("Rank ADSR Layout Complete.")
        return rankadsr_widget

    #==========================================================================
    # Pipe Settings
    #==========================================================================
    def __ui_layout_pipe_settings(self) -> None:
        print("Laying Out Pipe Settings...")
        ic()
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
        print("Pipe Settings Layout Complete.")

    def __ui_layout_pipe_header(self) -> QWidget:
        print("Laying Out Pipe Header...")
        ic()
        pipeheader_widget: QWidget = QWidget()
        pipeheader_layout: QFormLayout = QFormLayout()
        pipeheader_widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__ranknum_pipe_label, self.__ranknum_pipe_spin),
            (self.__pipenum_label, self.__pipenum_spin),        
            (self.__note_label, self.__note_combo),
            (self.__relnote_label, self.__relnote_combo)
        )
        for label, widget in pipeheader_widgets:
            pipeheader_layout.addRow(label, widget)
        pipeheader_widget.setLayout(pipeheader_layout)
        print("Pipe Header Layout Complete.")
        return pipeheader_widget

    #--------------------------------------------------------------------------
    # Pipe Harmonics Settings
    #--------------------------------------------------------------------------
    def __ui_layout_pipe_harmonic_settings(self) -> QWidget:
        print("Laying Out Pipe Harmonic Settings...")
        ic()
        pipeharmonicsettings_widget: QWidget = QWidget()
        pipeharmonicsettings_layout: QVBoxLayout = QVBoxLayout()
        pipeharmonicsettings_layout.addWidget(self.__pipe_harmonics_button)
        pipeharmonicsettings_layout.addWidget(self.__pipe_harmonic)
        pipeharmonicsettings_widget.setLayout(pipeharmonicsettings_layout)
        print("Pipe Harmonic Settings Layout Complete.")
        return pipeharmonicsettings_widget

    def __ui_layout_pipe_harmonics_widget(self) -> QWidget:
        print("Laying Out Pipe Harmonics Widget...")
        ic()
        pipeharmonics_widget: QWidget = QWidget()
        pipeharmonics_layout: QFormLayout = QFormLayout()
        pipeharmonics_widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__pipe_harmonicnum_label, self.__pipe_harmonicnum_spin),
            (self.__pipe_amplitude_label, self.__pipe_amplitude_spin)
        )
        for label, widget in pipeharmonics_widgets:
            pipeharmonics_layout.addRow(label, widget)
        pipeharmonics_widget.setLayout(pipeharmonics_layout)
        print("Pipe Harmonics Widget Layout Complete.")
        return pipeharmonics_widget

    def __ui_layout_pipe_harmonics_adsr(self) -> None:
        print("Laying Out Pipe Harmonics ADSR...")
        ic()
        pipeharmonicsadsr_layout: QFormLayout = QFormLayout()
        pipeharmonicsadsr_widgets: tuple[tuple[QLabel, QWidget], ...] = (
            (self.__pipeharm_attack_label, self.__pipeharm_attack_spin),
            (self.__pipeharm_decay_label, self.__pipeharm_decay_spin),
            (self.__pipeharm_sustain_label, self.__pipeharm_sustain_spin),
            (self.__pipeharm_release_label, self.__pipeharm_release_spin)
        )
        for label, widget in pipeharmonicsadsr_widgets:
            pipeharmonicsadsr_layout.addRow(label, widget)
        self.__pipeharm_adsr.setLayout(pipeharmonicsadsr_layout)
        print("Pipe Harmonics ADSR Layout Complete.")

    def __ui_layout_pipe_harmonic(self) -> None:
        print("Laying Out Pipe Harmonic...")
        ic()
        pipeharmonic_layout: QVBoxLayout = QVBoxLayout()
        pipeharmonic_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        pipeharmonic_layout.addWidget(self.__ui_layout_pipe_harmonics_widget())
        pipeharmonic_layout.addSpacing(10)
        pipeharmonic_layout.addWidget(self.__pipeharm_adsr_button)
        pipeharmonic_layout.addWidget(self.__pipeharm_adsr)
        self.__pipe_harmonic.setLayout(pipeharmonic_layout)
        print("Pipe Harmonic Layout Complete.")

    #--------------------------------------------------------------------------
    # Pipe ADSR Settings
    #--------------------------------------------------------------------------
    def __ui_layout_pipe_adsr(self) -> QWidget:
        print("Laying Out Pipe ADSR...")
        ic()
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
        print("Pipe ADSR Layout Complete.")
        return pipeadsr_widget
        
    #==========================================================================
    # Editor Layout
    #==========================================================================
    def __ui_layout_editor_scroll(self) -> QScrollArea:
        print("Laying Out Editor Scroll...")
        ic()
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
        print("Editor Scroll Layout Complete.")
        return editor_scroll

    #**************************************************************************
    # Options
    #**************************************************************************
    def __ui_layout_options(self) -> None:
        print("Laying Out Options...")
        ic()
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
        print("Options Layout Complete.")

    #**************************************************************************
    # Main Layout
    #**************************************************************************
    def __ui_layout_main(self) -> None:
        print("Laying Out Main Layout...")
        ic()
        main_layout: QHBoxLayout = QHBoxLayout()
        widgets: tuple[QWidget, ...] = (
            self.__ui_layout_form(),
            self.__options
        )
        for widget in widgets:
            main_layout.addWidget(widget)
        self.setLayout(main_layout)
        print("Main Layout Complete.")

    def __ui_layout_form(self) -> QWidget:
        print("Laying Out Form...")
        ic()
        form_widget: QWidget = QWidget()
        form_layout: QVBoxLayout = QVBoxLayout()
        form_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        form_widgets: tuple[QWidget, ...] = (
            self.header_widget,
            self.__ui_layout_editor_scroll(),
        )
        for widget in form_widgets:
            form_layout.addWidget(widget)
        form_widget.setLayout(form_layout)
        print("Form Layout Complete.")
        return form_widget

    #**************************************************************************
    # Actions
    #**************************************************************************
    #==========================================================================
    # Widget Manipulation
    #==========================================================================
    def __rank_harmonics_checked(self) -> None:
        print("Initiating Rank Harmonics CheckBox Clicked...")
        ic()
        widgets: tuple[QWidget, ...] = (
            self.__rank_harmonic,
            self.__rank_harmonicnum_label,
            self.__rank_harmonicnum_spin,
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
        print("Rank Harmonics CheckBox Clicked Complete.")

    def __rankharm_adsr_checked(self) -> None:
        print("Initiating Rank Harmonic ADSR CheckBox Clicked...")
        ic()
        widgets: tuple[QWidget, ...] = (
            self.__rankharm_adsr,
            self.__rankharm_attack_label,
            self.__rankharm_attack_spin,
            self.__rankharm_decay_label,
            self.__rankharm_decay_spin,
            self.__rankharm_sustain_label,
            self.__rankharm_sustain_spin,
            self.__rankharm_release_label,
            self.__rankharm_release_spin
        )
        match self.__rankharm_adsr_button.isChecked():
            case True:
                for widget in widgets:
                    widget.setEnabled(True)
            case False:
                for widget in widgets:
                    widget.setEnabled(False)
        print("Rank Harmonic ADSR CheckBox Clicked Complete.")

    def __rank_adsr_checked(self) -> None:
        print("Initiating Rank ADSR CheckBox Clicked...")
        ic()
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
        print("Rank ADSR CheckBox Clicked Complete.")

    def __pipe_harmonics_checked(self) -> None:
        print("Initiating Pipe Harmonics CheckBox Clicked...")
        widgets: tuple[QWidget, ...] = (
            self.__pipe_harmonic,
            self.__pipe_harmonicnum_label,
            self.__pipe_harmonicnum_spin,
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
        print("Pipe Harmonics CheckBox Clicked Complete.")

    def __pipeharm_adsr_checked(self) -> None:
        print("Initiating Pipe Harmonic ADSR CheckBox Clicked...")
        spins: tuple[QWidget, ...] = (
            self.__pipeharm_adsr,
            self.__pipeharm_attack_label,
            self.__pipeharm_attack_spin,
            self.__pipeharm_decay_label,
            self.__pipeharm_decay_spin,
            self.__pipeharm_sustain_label,
            self.__pipeharm_sustain_spin,
            self.__pipeharm_release_label,
            self.__pipeharm_release_spin
        )
        match self.__pipeharm_adsr_button.isChecked():
            case True:
                for spin in spins:
                    spin.setEnabled(True)
            case False:
                for spin in spins:
                    spin.setEnabled(False)
        print("Pipe Harmonic ADSR CheckBox Clicked Complete.")

    def __pipe_adsr_checked(self) -> None:
        print("Initiating Pipe ADSR CheckBox Clicked...")
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
        print("Pipe ADSR CheckBox Clicked Complete.")

    #==========================================================================
    # Widget Data
    #==========================================================================
    def stop_names_populate(self, stop_names: tuple[str, ...]) -> None:
        print("Populating Stop Names...")
        ic()
        ic(stop_names)
        self.__stopname_combo.clear()
        self.__stopname_combo.addItems(stop_names)
        print("Stop Names Populated.")

    def stop_families_populate(self, stop_families: tuple[str, ...]) -> None:
        print("Populating Stop Families...")
        ic()
        ic(stop_families)
        self.__stopfamily_combo.clear()
        self.__stopfamily_combo.addItems(stop_families)
        print("Stop Families Populated.")

    def organ_divisions_populate(self, divisions: tuple[str, ...]) -> None:
        print("Populating Organ Divisions...")
        ic()
        ic(divisions)
        self.__organdivision_combo.clear()
        self.__organdivision_combo.addItems(divisions)
        print("Organ Divisions Populated.")

    def number_ranks_set_minimum(self, min: int) -> None:
        print("Setting Minimum Number of Ranks...")
        ic()
        ic(min)
        self.__numranks_spin.setMinimum(min)
        print("Minimum Number of Ranks Set.")

    def number_ranks_set_maximum(self, max: int) -> None:
        print("Setting Maximum Number of Ranks...")
        ic()
        ic(max)
        self.__numranks_spin.setMaximum(max)
        print("Maximum Number of Ranks Set.")

    def rank_series_populate(self, rank_series: tuple[str, ...]) -> None:
        print("Populating Rank Series...")
        ic()
        ic(rank_series)
        self.__rankseries_combo.clear()
        self.__rankseries_combo.addItems(rank_series)
        print("Rank Series Populated.")

    def rank_number_set_minimum(self, min: int) -> None:
        print("Setting Minimum Rank Number...")
        ic()
        ic(min)
        self.__ranknum_spin.setMinimum(min)
        print("Minimum Rank Number Set.")

    def rank_number_set_maximum(self, max: int) -> None:
        print("Setting Maximum Rank Number...")
        ic()
        ic(max)
        self.__ranknum_spin.setMaximum(max)
        print("Maximum Rank Number Set.")

    def rank_size_populate(self, rank_sizes: tuple[str, ...]) -> None:
        print("Populating Rank Sizes...")
        ic()
        ic(rank_sizes)
        self.__ranksize_combo.clear()
        self.__ranksize_combo.addItems(rank_sizes)
        print("Rank Sizes Populated.")

    def number_pipes_set_minimum(self, min: int) -> None:
        print("Setting Minimum Number of Pipes...")
        ic()
        ic(min)
        self.__numpipes_spin.setMinimum(min)
        print("Minimum Number of Pipes Set.")

    def number_pipes_set_maximum(self, max: int) -> None:
        print("Setting Maximum Number of Pipes...")
        ic()
        ic(max)
        self.__numpipes_spin.setMaximum(max)
        print("Maximum Number of Pipes Set.")

    def pipe_types_populate(self, pipe_types: tuple[str, ...]) -> None:
        print("Populating Pipe Types...")
        ic()
        ic(pipe_types)
        self.__pipetype_combo.addItems(pipe_types)
        print("Pipe Types Populated.")

    def starting_note_populate(self, starting_notes: tuple[str, ...]) -> None:
        print("Populating Starting Notes...")
        ic()
        ic(starting_notes)
        self.__startnote_combo.addItems(starting_notes)
        print("Starting Notes Populated.")

    def frequency_offset_set_minimum(self, min: int) -> None:
        print("Setting Minimum Frequency Offset...")
        ic()
        ic(min)
        self.__freqoffset_spin.setMinimum(min)
        print("Minimum Frequency Offset Set.")

    def frequency_offset_set_maximum(self, max: int) -> None:
        print("Setting Maximum Frequency Offset...")
        ic()
        ic(max)
        self.__freqoffset_spin.setMaximum(max)
        print("Maximum Frequency Offset Set.")

    def number_harmonics_set_minimum(self, min: int) -> None:
        print("Setting Minimum Number of Harmonics...")
        ic()
        ic(min)
        self.__numharmonics_spin.setMinimum(min)
        print("Minimum Number of Harmonics Set.")

    def number_harmonics_set_maximum(self, max: int) -> None:
        print("Setting Maximum Number of Harmonics...")
        ic()
        ic(max)
        self.__numharmonics_spin.setMaximum(max)
        print("Maximum Number of Harmonics Set.")

    def harmonic_number_rank_set_minimum(self, min: int) -> None:
        print("Setting Minimum Harmonic Number...")
        ic()
        ic(min)
        self.__rank_harmonicnum_spin.setMinimum(min)
        print("Minimum Harmonic Number Set.")

    def harmonic_number_rank_set_maximum(self, max: int) -> None:
        print("Setting Maximum Harmonic Number...")
        ic()
        ic(max)
        self.__rank_harmonicnum_spin.setMaximum(max)
        print("Maximum Harmonic Number Set.")

    def amplitude_rank_set_minimum(self, min: int) -> None:
        print("Setting Minimum Rank Amplitude...")
        ic()
        ic(min)
        self.__rank_amplitude_spin.setMinimum(min)
        print("Minimum Rank Amplitude Set.")

    def amplitude_rank_set_maximum(self, max: int) -> None:
        print("Setting Maximum Rank Amplitude...")
        ic()
        ic(max)
        self.__rank_amplitude_spin.setMaximum(max)
        print("Maximum Rank Amplitude Set.")

    def attack_time_rank_harmonic_set_minimum(self, min: int) -> None:
        print("Setting Minimum Rank Harmonic Attack Time...")
        ic()
        ic(min)
        self.__rankharm_attack_spin.setMinimum(min)
        print("Minimum Rank Harmonic Attack Time Set.")

    def attack_time_rank_harmonic_set_maximum(self, max: int) -> None:
        print("Setting Maximum Rank Harmonic Attack Time...")
        ic()
        ic(max)
        self.__rankharm_attack_spin.setMaximum(max)
        print("Maximum Rank Harmonic Attack Time Set.")

    def decay_time_rank_harmonic_set_minimum(self, min: int) -> None:
        print("Setting Minimum Rank Harmonic Decay Time...")
        ic()
        ic(min)
        self.__rankharm_decay_spin.setMinimum(min)
        print("Minimum Rank Harmonic Decay Time Set.")

    def decay_time_rank_harmonic_set_maximum(self, max: int) -> None:
        print("Setting Maximum Rank Harmonic Decay Time...")
        ic()
        ic(max)
        self.__rankharm_decay_spin.setMaximum(max)
        print("Maximum Rank Harmonic Decay Time Set.")

    def sustain_level_rank_harmonic_set_minimum(self, min: int) -> None:
        print("Setting Minimum Rank Harmonic Sustain Level...")
        ic()
        ic(min)
        self.__rankharm_sustain_spin.setMinimum(min)
        print("Minimum Rank Harmonic Sustain Level Set.")

    def sustain_level_rank_harmonic_set_maximum(self, max: int) -> None:
        print("Setting Maximum Rank Harmonic Sustain Level...")
        ic()
        ic(max)
        self.__rankharm_sustain_spin.setMaximum(max)
        print("Maximum Rank Harmonic Sustain Level Set.")

    def release_time_rank_harmonic_set_minimum(self, min: int) -> None:
        print("Setting Minimum Rank Harmonic Release Time...")
        ic()
        ic(min)
        self.__rankharm_release_spin.setMinimum(min)
        print("Minimum Rank Harmonic Release Time Set.")

    def release_time_rank_harmonic_set_maximum(self, max: int) -> None:
        print("Setting Maximum Rank Harmonic Release Time...")
        ic()
        ic(max)
        self.__rankharm_release_spin.setMaximum(max)
        print("Maximum Rank Harmonic Release Time Set.")

    def attack_time_rank_set_minimum(self, min: int) -> None:
        print("Setting Minimum Rank Attack Time...")
        ic()
        ic(min)
        self.__rank_attack_spin.setMinimum(min)
        print("Minimum Rank Attack Time Set.")

    def attack_time_rank_set_maximum(self, max: int) -> None:
        print("Setting Maximum Rank Attack Time...")
        ic()
        ic(max)
        self.__rank_attack_spin.setMaximum(max)
        print("Maximum Rank Attack Time Set.")

    def decay_time_rank_set_minimum(self, min: int) -> None:
        print("Setting Minimum Rank Decay Time...")
        ic()
        ic(min)
        self.__rank_decay_spin.setMinimum(min)
        print("Minimum Rank Decay Time Set.")

    def decay_time_rank_set_maximum(self, max: int) -> None:
        print("Setting Maximum Rank Decay Time...")
        ic()
        ic(max)
        self.__rank_decay_spin.setMaximum(max)
        print("Maximum Rank Decay Time Set.")

    def sustain_level_rank_set_minimum(self, min: int) -> None:
        print("Setting Minimum Rank Sustain Level...")
        ic()
        ic(min)
        self.__rank_sustain_spin.setMinimum(min)
        print("Minimum Rank Sustain Level Set.")

    def sustain_level_rank_set_maximum(self, max: int) -> None:
        print("Setting Maximum Rank Sustain Level...")
        ic()
        ic(max)
        self.__rank_sustain_spin.setMaximum(max)
        print("Maximum Rank Sustain Level Set.")

    def release_time_rank_set_minimum(self, min: int) -> None:
        print("Setting Minimum Rank Release Time...")
        ic()
        ic(min)
        self.__rank_release_spin.setMinimum(min)
        print("Minimum Rank Release Time Set.")

    def release_time_rank_set_maximum(self, max: int) -> None:
        print("Setting Maximum Rank Release Time...")
        ic()
        ic(max)
        self.__rank_release_spin.setMaximum(max)
        print("Maximum Rank Release Time Set.")

    def rank_number_pipe_set_minimum(self, min: int) -> None:
        print("Setting Minimum Rank Number...")
        ic()
        ic(min)
        self.__ranknum_pipe_spin.setMinimum(min)
        print("Minimum Rank Number Set.")

    def rank_number_pipe_set_maximum(self, max: int) -> None:
        print("Setting Maximum Rank Number...")
        ic()
        ic(max)
        self.__ranknum_pipe_spin.setMaximum(max)
        print("Maximum Rank Number Set.")

    def pipe_number_set_minimum(self, min: int) -> None:
        print("Setting Minimum Pipe Number...")
        ic()
        ic(min)
        self.__pipenum_spin.setMinimum(min)
        print("Minimum Pipe Number Set.")

    def pipe_number_set_maximum(self, max: int) -> None:
        print("Setting Maximum Pipe Number...")
        ic()
        ic(max)
        self.__pipenum_spin.setMaximum(max)
        print("Maximum Pipe Number Set.")

    def note_populate(self, notes: tuple[str, ...]) -> None:
        print("Populating Notes...")
        ic()
        ic(notes)
        self.__note_combo.addItems(notes)
        print("Notes Populated.")

    def relative_note_populate(self, notes: tuple[str, ...]) -> None:
        print("Populating Relative Notes...")
        ic()
        ic(notes)
        self.__relnote_combo.addItems(notes)
        print("Relative Notes Populated.")

    def harmonic_number_pipe_set_minimum(self, min: int) -> None:
        print("Setting Minimum Pipe Harmonic Number...")
        ic()
        ic(min)
        self.__pipe_harmonicnum_spin.setMinimum(min)
        print("Minimum Pipe Harmonic Number Set.")

    def harmonic_number_pipe_set_maximum(self, max: int) -> None:
        print("Setting Maximum Pipe Harmonic Number...")
        ic()
        ic(max)
        self.__pipe_harmonicnum_spin.setMaximum(max)
        print("Maximum Pipe Harmonic Number Set.")

    def amplitude_pipe_set_minimum(self, min: int) -> None:
        print("Setting Minimum Pipe Amplitude...")
        ic()
        ic(min)
        self.__pipe_amplitude_spin.setMinimum(min)
        print("Minimum Pipe Amplitude Set.")

    def amplitude_pipe_set_maximum(self, max: int) -> None:
        print("Setting Maximum Pipe Amplitude...")
        ic()
        ic(max)
        self.__pipe_amplitude_spin.setMaximum(max)
        print("Maximum Pipe Amplitude Set.")

    def attack_time_pipe_harmonic_set_minimum(self, min: int) -> None:
        print("Setting Minimum Pipe Harmonic Attack Time...")
        ic()
        ic(min)
        self.__pipeharm_attack_spin.setMinimum(min)
        print("Minimum Pipe Harmonic Attack Time Set.")

    def attack_time_pipe_harmonic_set_maximum(self, max: int) -> None:
        print("Setting Maximum Pipe Harmonic Attack Time...")
        ic()
        ic(max)
        self.__pipeharm_attack_spin.setMaximum(max)
        print("Maximum Pipe Harmonic Attack Time Set.")

    def decay_time_pipe_harmonic_set_minimum(self, min: int) -> None:
        print("Setting Minimum Pipe Harmonic Decay Time...")
        ic()
        ic(min)
        self.__pipeharm_decay_spin.setMinimum(min)
        print("Minimum Pipe Harmonic Decay Time Set.")

    def decay_time_pipe_harmonic_set_maximum(self, max: int) -> None:
        print("Setting Maximum Pipe Harmonic Decay Time...")
        ic()
        ic(max)
        self.__pipeharm_decay_spin.setMaximum(max)
        print("Maximum Pipe Harmonic Decay Time Set.")

    def sustain_level_pipe_harmonic_set_minimum(self, min: int) -> None:
        print("Setting Minimum Pipe Harmonic Sustain Level...")
        ic()
        ic(min)
        self.__pipeharm_sustain_spin.setMinimum(min)
        print("Minimum Pipe Harmonic Sustain Level Set.")

    def sustain_level_pipe_harmonic_set_maximum(self, max: int) -> None:
        print("Setting Maximum Pipe Harmonic Sustain Level...")
        ic()
        ic(max)
        self.__pipeharm_sustain_spin.setMaximum(max)
        print("Maximum Pipe Harmonic Sustain Level Set.")

    def release_time_pipe_harmonic_set_minimum(self, min: int) -> None:
        print("Setting Minimum Pipe Harmonic Release Time...")
        ic()
        ic(min)
        self.__pipeharm_release_spin.setMinimum(min)
        print("Minimum Pipe Harmonic Release Time Set.")

    def release_time_pipe_harmonic_set_maximum(self, max: int) -> None:
        print("Setting Maximum Pipe Harmonic Release Time...")
        ic()
        ic(max)
        self.__pipeharm_release_spin.setMaximum(max)
        print("Maximum Pipe Harmonic Release Time Set.")

    def attack_time_pipe_set_minimum(self, min: int) -> None:
        print("Setting Minimum Pipe Attack Time...")
        ic()
        ic(min)
        self.__pipe_attack_spin.setMinimum(min)
        print("Minimum Pipe Attack Time Set.")

    def attack_time_pipe_set_maximum(self, max: int) -> None:
        print("Setting Maximum Pipe Attack Time...")
        ic()
        ic(max)
        self.__pipe_attack_spin.setMaximum(max)
        print("Maximum Pipe Attack Time Set.")

    def decay_time_pipe_set_minimum(self, min: int) -> None:
        print("Setting Minimum Pipe Decay Time...")
        ic()
        ic(min)
        self.__pipe_decay_spin.setMinimum(min)
        print("Minimum Pipe Decay Time Set.")

    def decay_time_pipe_set_maximum(self, max: int) -> None:
        print("Setting Maximum Pipe Decay Time...")
        ic()
        ic(max)
        self.__pipe_decay_spin.setMaximum(max)
        print("Maximum Pipe Decay Time Set.")

    def sustain_level_pipe_set_minimum(self, min: int) -> None:
        print("Setting Minimum Pipe Sustain Level...")
        ic()
        ic(min)
        self.__pipe_sustain_spin.setMinimum(min)
        print("Minimum Pipe Sustain Level Set.")

    def sustain_level_pipe_set_maximum(self, max: int) -> None:
        print("Setting Maximum Pipe Sustain Level...")
        ic()
        ic(max)
        self.__pipe_sustain_spin.setMaximum(max)
        print("Maximum Pipe Sustain Level Set.")

    def release_time_pipe_set_minimum(self, min: int) -> None:
        print("Setting Minimum Pipe Release Time...")
        ic()
        ic(min)
        self.__pipe_release_spin.setMinimum(min)
        print("Minimum Pipe Release Time Set.")

    def release_time_pipe_set_maximum(self, max: int) -> None:
        print("Setting Maximum Pipe Release Time...")
        ic()
        ic(max)
        self.__pipe_release_spin.setMaximum(max)
        print("Maximum Pipe Release Time Set.")

    #==========================================================================
    # Data Manipulation
    #==========================================================================
    def update_stop_header(self) -> None:
        print("Updating Stop Header...")
        ic()
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
        print("Stop Header Updated.")

    def stop_name_change(
        self,
        action: Callable[[], None]
    ) -> None:
        print("Initiating Stop Name Change...")
        ic()
        ic(action)
        self.__stopname_combo.currentTextChanged.connect(action)
        print("Stop Name Change Complete.")

    def stop_family_change(
        self,
        action: Callable[[], None]
    ) -> None:
        print("Initiating Stop Family Change...")
        ic()
        ic(action)
        self.__stopfamily_combo.currentTextChanged.connect(action)
        print("Stop Family Change Complete.")

    def organ_division_change(
        self,
        action: Callable[[], None]
    ) -> None:
        print("Initiating Organ Division Change...")
        ic()
        ic(action)
        self.__organdivision_combo.currentTextChanged.connect(action)
        print("Organ Division Change Complete.")

    def number_ranks_change(
        self,
        action: Callable[[], None]
    ) -> None:
        print("Initiating Number of Ranks Change...")
        ic()
        ic(action)
        self.__numranks_spin.valueChanged.connect(action)
        print("Number of Ranks Change Complete.")

    def rank_series_change(
        self,
        action: Callable[[], None]
    ) -> None:
        print("Initiating Rank Series Change...")
        ic()
        self.__rankseries_combo.currentTextChanged.connect(action)
        print("Rank Series Change Complete.")

    def rank_number_change(
        self,
        action: Callable[[], None]
    ) -> None:
        print("Initiating Rank Number Change...")
        ic()
        ic(action)
        self.__ranknum_spin.valueChanged.connect(action)
        print("Rank Number Change Complete.")

    def rank_size_change(
        self,
        action: Callable[[], None]
    ) -> None:
        print("Initiating Rank Size Change...")
        ic()
        ic(action)
        self.__ranksize_combo.currentTextChanged.connect(action)
        print("Rank Size Change Complete.")

    def number_pipes_change(
        self,
        action: Callable[[], None]
    ) -> None:
        print("Initiating Number of Pipes Change...")
        ic()
        ic(action)
        self.__numpipes_spin.valueChanged.connect(action)
        print("Number of Pipes Change Complete.")

    def pipe_type_change(
        self,
        action: Callable[[], None]
    ) -> None:
        print("Initiating Pipe Type Change...")
        ic()
        ic(action)
        self.__pipetype_combo.currentTextChanged.connect(action)
        print("Pipe Type Change Complete.")

    def starting_note_change(
        self,
        action: Callable[[], None]
    ) -> None:
        print("Initiating Starting Note Change...")
        ic()
        ic(action)
        self.__startnote_combo.currentTextChanged.connect(action)
        print("Starting Note Change Complete.")

    def frequency_offset_change(
        self,
        action: Callable[[], None]
    ) -> None:
        print("Initiating Frequency Offset Change...")
        ic()
        ic(action)
        self.__freqoffset_spin.valueChanged.connect(action)
        print("Frequency Offset Change Complete.")

    def number_harmonics_change(
        self,
        action: Callable[[], None]
    ) -> None:
        print("Initiating Number of Harmonics Change...")
        ic()
        ic(action)
        self.__numharmonics_spin.valueChanged.connect(action)
        print("Number of Harmonics Change Complete.")

    def harmonic_number_rank_change(
        self,
        action: Callable[[], None]
    ) -> None:
        print("Initiating Harmonic Number Change...")
        ic()
        ic(action)
        self.__rank_harmonicnum_spin.valueChanged.connect(action)
        print("Harmonic Number Change Complete.")

    def amplitude_rank_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Rank Amplitude Change...")
        ic()
        ic(action)
        self.__rank_amplitude_spin.valueChanged.connect(action)
        print("Rank Amplitude Change Complete.")

    def attack_time_rank_harmonic_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Rank Harmonic Attack Time Change...")
        ic()
        ic(action)
        self.__rankharm_attack_spin.valueChanged.connect(action)
        print("Rank Harmonic Attack Time Change Complete.")

    def decay_time_rank_harmonic_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Rank Harmonic Decay Time Change...")
        ic()
        ic(action)
        self.__rankharm_decay_spin.valueChanged.connect(action)
        print("Rank Harmonic Decay Time Change Complete.")

    def sustain_level_rank_harmonic_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Rank Harmonic Sustain Level Change...")
        ic()
        ic(action)
        self.__rankharm_sustain_spin.valueChanged.connect(action)
        print("Rank Harmonic Sustain Level Change Complete.")

    def release_time_rank_harmonic_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Rank Harmonic Release Time Change...")
        ic()
        ic(action)
        self.__rankharm_release_spin.valueChanged.connect(action)
        print("Rank Harmonic Release Time Change Complete.")

    def attack_time_rank_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Rank Attack Time Change...")
        ic()
        ic(action)
        self.__rank_attack_spin.valueChanged.connect(action)
        print("Rank Attack Time Change Complete.")

    def decay_time_rank_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Rank Decay Time Change...")
        ic()
        ic(action)
        self.__rank_decay_spin.valueChanged.connect(action)
        print("Rank Decay Time Change Complete.")

    def sustain_level_rank_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Rank Sustain Level Change...")
        ic()
        ic(action)
        self.__rank_sustain_spin.valueChanged.connect(action)
        print("Rank Sustain Level Change Complete.")

    def release_time_rank_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Rank Release Time Change...")
        ic()
        ic(action)
        self.__rank_release_spin.valueChanged.connect(action)
        print("Rank Release Time Change Complete.")

    def rank_number_pipe_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Rank Number Change...")
        ic()
        ic(action)
        self.__ranknum_pipe_spin.valueChanged.connect(action)
        print("Rank Number Change Complete.")

    def pipe_number_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Pipe Number Change...")
        ic()
        ic(action)
        self.__pipenum_spin.valueChanged.connect(action)
        print("Pipe Number Change Complete.")

    def note_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Note Change...")
        ic()
        ic(action)
        self.__note_combo.currentTextChanged.connect(action)
        print("Note Change Complete.")

    def relative_note_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Relative Note Change...")
        ic()
        ic(action)
        self.__relnote_combo.currentTextChanged.connect(action)
        print("Relative Note Change Complete.")

    def harmonic_number_pipe_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Pipe Harmonic Number Change...")
        ic()
        ic(action)
        self.__pipe_harmonicnum_spin.valueChanged.connect(action)
        print("Pipe Harmonic Number Change Complete.")

    def amplitude_pipe_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Pipe Amplitude Change...")
        ic()
        ic(action)
        self.__pipe_amplitude_spin.valueChanged.connect(action)
        print("Pipe Amplitude Change Complete.")

    def attack_time_pipe_harmonic_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Pipe Harmonic Attack Time Change...")
        ic()
        ic(action)
        self.__pipeharm_attack_spin.valueChanged.connect(action)
        print("Pipe Harmonic Attack Time Change Complete.")

    def decay_time_pipe_harmonic_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Pipe Harmonic Decay Time Change...")
        ic()
        ic(action)
        self.__pipeharm_decay_spin.valueChanged.connect(action)
        print("Pipe Harmonic Decay Time Change Complete.")

    def sustain_level_pipe_harmonic_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Pipe Harmonic Sustain Level Change...")
        ic()
        ic(action)
        self.__pipeharm_sustain_spin.valueChanged.connect(action)
        print("Pipe Harmonic Sustain Level Change Complete.")

    def release_time_pipe_harmonic_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Pipe Harmonic Release Time Change...")
        ic()
        ic(action)
        self.__pipeharm_release_spin.valueChanged.connect(action)
        print("Pipe Harmonic Release Time Change Complete.")

    def attack_time_pipe_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Pipe Attack Time Change...")
        ic()
        ic(action)
        self.__pipe_attack_spin.valueChanged.connect(action)
        print("Pipe Attack Time Change Complete.")

    def decay_time_pipe_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Pipe Decay Time Change...")
        ic()
        ic(action)
        self.__pipe_decay_spin.valueChanged.connect(action)
        print("Pipe Decay Time Change Complete.")

    def sustain_level_pipe_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Pipe Sustain Level Change...")
        ic()
        ic(action)
        self.__pipe_sustain_spin.valueChanged.connect(action)
        print("Pipe Sustain Level Change Complete.")

    def release_time_pipe_change(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Pipe Release Time Change...")
        ic()
        ic(action)
        self.__pipe_release_spin.valueChanged.connect(action)
        print("Pipe Release Time Change Complete.")

    def load_stop_action(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Load Stop Action...")
        ic()
        ic(action)
        self.__load_button.clicked.connect(action)
        print("Load Stop Action Complete.")

    def cancel_changes_action(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Cancel Changes Action...")
        ic()
        ic(action)
        self.__cancel_button.clicked.connect(action)
        print("Cancel Changes Action Complete.")

    def save_stop_action(
            self,
            action: Callable[[], None]
    ) -> None:
        print("Initiating Save Stop Action...")
        ic()
        ic(action)
        self.__save_button.clicked.connect(action)
        print("Save Stop Action Complete.")

    #**************************************************************************
    # Properties
    #**************************************************************************
    #==========================================================================
    # Stop Header
    #==========================================================================
    @property
    def stop_header(self) -> str:
        print("Getting Stop Header...")
        ic()
        ic(self.__header_edit.text())
        print("Stop Header Retrieved.")
        return self.__header_edit.text()

    #==========================================================================
    # Stop Name
    #==========================================================================
    @property
    def stop_name(self) -> str:
        return self.__stopname_combo.currentText()

    @stop_name.setter
    def stop_name(self, n: str) -> None:
        self.__stopname_combo.setCurrentText(n)

    #==========================================================================
    # Stop Family
    #==========================================================================
    @property
    def stop_family(self) -> str:
        return self.__stopfamily_combo.currentText()

    @stop_family.setter
    def stop_family(self, f: str) -> None:
        self.__stopfamily_combo.setCurrentText(f)

    #==========================================================================
    # Organ Division
    #==========================================================================
    @property
    def organ_division(self) -> str:
        return self.__organdivision_combo.currentText()

    @organ_division.setter
    def organ_division(self, d: str) -> None:
        self.__organdivision_combo.setCurrentText(d)

    #==========================================================================
    # Number of Ranks
    #==========================================================================
    @property
    def number_ranks(self) -> int:
        return self.__numranks_spin.value()

    @number_ranks.setter
    def number_ranks(self, n: int) -> None:
        self.__numranks_spin.setValue(n)

    #==========================================================================
    # Rank Series
    #==========================================================================
    @property
    def rank_series(self) -> str:
        return self.__rankseries_combo.currentText()

    @rank_series.setter
    def rank_series(self, r: str) -> None:
        self.__rankseries_combo.setCurrentText(r)

    #==========================================================================
    # Rank Number
    #==========================================================================
    @property
    def rank_number(self) -> int:
        return self.__ranknum_spin.value()

    @rank_number.setter
    def rank_number(self, n: int) -> None:
        self.__ranknum_spin.setValue(n)

    #==========================================================================
    # Rank Size
    #==========================================================================
    @property
    def rank_size(self) -> str:
        return self.__ranksize_combo.currentText()

    @rank_size.setter
    def rank_size(self, s: str) -> None:
        self.__ranksize_combo.setCurrentText(s)

    #==========================================================================
    # Number of Pipes
    #==========================================================================
    @property
    def number_pipes(self) -> int:
        return self.__numpipes_spin.value()

    @number_pipes.setter
    def number_pipes(self, n: int) -> None:
        self.__numpipes_spin.setValue(n)

    #==========================================================================
    # Pipe Type
    #==========================================================================
    @property
    def pipe_type(self) -> str:
        return self.__pipetype_combo.currentText()

    @pipe_type.setter
    def pipe_type(self, t: str) -> None:
        self.__pipetype_combo.setCurrentText(t)

    #==========================================================================
    # Starting Note
    #==========================================================================
    @property
    def starting_note(self) -> str:
        return self.__startnote_combo.currentText()

    @starting_note.setter
    def starting_note(self, n: str) -> None:
        self.__startnote_combo.setCurrentText(n)

    #==========================================================================
    # Frequency Offset
    #==========================================================================
    @property
    def frequency_offset(self) -> int:
        return self.__freqoffset_spin.value()

    @frequency_offset.setter
    def frequency_offset(self, f: int) -> None:
        self.__freqoffset_spin.setValue(f)

    #==========================================================================
    # Number of Harmonics
    #==========================================================================
    @property
    def number_harmonics(self) -> int:
        return self.__numharmonics_spin.value()

    @number_harmonics.setter
    def number_harmonics(self, n: int) -> None:
        self.__numharmonics_spin.setValue(n)

    #==========================================================================
    # Harmonic Number - Rank
    #==========================================================================
    @property
    def harmonic_number_rank(self) -> int:
        return self.__rank_harmonicnum_spin.value()

    @harmonic_number_rank.setter
    def harmonic_number_rank(self, n: int) -> None:
        self.__rank_harmonicnum_spin.setValue(n)

    #==========================================================================
    # Amplitude - Rank
    #==========================================================================
    @property
    def amplitude_rank(self) -> int:
        return self.__rank_amplitude_spin.value()

    @amplitude_rank.setter
    def amplitude_rank(self, a: int) -> None:
        self.__rank_amplitude_spin.setValue(a)

    #==========================================================================
    # Attack Time - Harmonic - Rank
    #==========================================================================
    @property
    def attack_time_harmonic_rank(self) -> int:
        return self.__rankharm_attack_spin.value()

    @attack_time_harmonic_rank.setter
    def attack_time_harmonic_rank(self, a: int) -> None:
        self.__rankharm_attack_spin.setValue(a)

    #==========================================================================
    # Decay Time - Harmonic - Rank
    #==========================================================================
    @property
    def decay_time_harmonic_rank(self) -> int:
        return self.__rankharm_decay_spin.value()

    @decay_time_harmonic_rank.setter
    def decay_time_harmonic_rank(self, d: int) -> None:
        self.__rankharm_decay_spin.setValue(d)

    #==========================================================================
    # Sustain Level - Harmonic - Rank
    #==========================================================================
    @property
    def sustain_level_harmonic_rank(self) -> int:
        return self.__rankharm_sustain_spin.value()

    @sustain_level_harmonic_rank.setter
    def sustain_level_harmonic_rank(self, s: int) -> None:
        self.__rankharm_sustain_spin.setValue(s)

    #==========================================================================
    # Release Time - Harmonic - Rank
    #==========================================================================
    @property
    def release_time_harmonic_rank(self) -> int:
        return self.__rankharm_release_spin.value()

    @release_time_harmonic_rank.setter
    def release_time_harmonic_rank(self, r: int) -> None:
        self.__rankharm_release_spin.setValue(r)

    #==========================================================================
    # Attack Time - Rank
    #==========================================================================
    @property
    def attack_time_rank(self) -> int:
        return self.__rank_attack_spin.value()

    @attack_time_rank.setter
    def attack_time_rank(self, a: int) -> None:
        self.__rank_attack_spin.setValue(a)

    #==========================================================================
    # Decay Time - Rank
    #==========================================================================
    @property
    def decay_time_rank(self) -> int:
        return self.__rank_decay_spin.value()

    @decay_time_rank.setter
    def decay_time_rank(self, d: int) -> None:
        self.__rank_decay_spin.setValue(d)

    #==========================================================================
    # Sustain Level - Rank
    #==========================================================================
    @property
    def sustain_level_rank(self) -> int:
        return self.__rank_sustain_spin.value()

    @sustain_level_rank.setter
    def sustain_level_rank(self, s: int) -> None:
        self.__rank_sustain_spin.setValue(s)

    #==========================================================================
    # Release Time - Rank
    #==========================================================================
    @property
    def release_time_rank(self) -> int:
        return self.__rank_release_spin.value()

    @release_time_rank.setter
    def release_time_rank(self, r: int) -> None:
        self.__rank_release_spin.setValue(r)

    #==========================================================================
    # Rank Number - Pipe
    #==========================================================================
    @property
    def rank_number_pipe(self) -> int:
        return self.__ranknum_pipe_spin.value()

    @rank_number_pipe.setter
    def rank_number_pipe(self, n: int) -> None:
        self.__ranknum_pipe_spin.setValue(n)

    #==========================================================================
    # Pipe Number
    #==========================================================================
    @property
    def pipe_number(self) -> int:
        return self.__pipenum_spin.value()

    @pipe_number.setter
    def pipe_number(self, n: int) -> None:
        self.__pipenum_spin.setValue(n)

    #==========================================================================
    # Note
    #==========================================================================
    @property
    def note(self) -> str:
        return self.__note_combo.currentText()

    @note.setter
    def note(self, n: str) -> None:
        self.__note_combo.setCurrentText(n)

    #==========================================================================
    # Relative Note
    #==========================================================================
    @property
    def relative_note(self) -> str:
        return self.__relnote_combo.currentText()

    @relative_note.setter
    def relative_note(self, n: str) -> None:
        self.__relnote_combo.setCurrentText(n)

    #==========================================================================
    # Harmonic Number - Pipe
    #==========================================================================
    @property
    def harmonic_number_pipe(self) -> int:
        return self.__pipe_harmonicnum_spin.value()

    @harmonic_number_pipe.setter
    def harmonic_number_pipe(self, n: int) -> None:
        self.__pipe_harmonicnum_spin.setValue(n)

    #==========================================================================
    # Amplitude - Pipe
    #==========================================================================
    @property
    def amplitude_pipe(self) -> int:
        return self.__pipe_amplitude_spin.value()

    @amplitude_pipe.setter
    def amplitude_pipe(self, a: int) -> None:
        self.__pipe_amplitude_spin.setValue(a)

    #==========================================================================
    # Attack Time - Harmonic - Pipe
    #==========================================================================
    @property
    def attack_time_harmonic_pipe(self) -> int:
        return self.__pipeharm_attack_spin.value()

    @attack_time_harmonic_pipe.setter
    def attack_time_harmonic_pipe(self, a: int) -> None:
        self.__pipeharm_attack_spin.setValue(a)

    #==========================================================================
    # Decay Time - Harmonic - Pipe
    #==========================================================================
    @property
    def decay_time_harmonic_pipe(self) -> int:
        return self.__pipeharm_decay_spin.value()

    @decay_time_harmonic_pipe.setter
    def decay_time_harmonic_pipe(self, d: int) -> None:
        self.__pipeharm_decay_spin.setValue(d)

    #==========================================================================
    # Sustain Level - Harmonic - Pipe
    #==========================================================================
    @property
    def sustain_level_harmonic_pipe(self) -> int:
        return self.__pipeharm_sustain_spin.value()

    @sustain_level_harmonic_pipe.setter
    def sustain_level_harmonic_pipe(self, s: int) -> None:
        self.__pipeharm_sustain_spin.setValue(s)

    #==========================================================================
    # Release Time - Harmonic - Pipe
    #==========================================================================
    @property
    def release_time_harmonic_pipe(self) -> int:
        return self.__pipeharm_release_spin.value()

    @release_time_harmonic_pipe.setter
    def release_time_harmonic_pipe(self, r: int) -> None:
        self.__pipeharm_release_spin.setValue(r)

    #==========================================================================
    # Attack Time - Pipe
    #==========================================================================
    @property
    def attack_time_pipe(self) -> int:
        return self.__pipe_attack_spin.value()

    @attack_time_pipe.setter
    def attack_time_pipe(self, a: int) -> None:
        self.__pipe_attack_spin.setValue(a)

    #==========================================================================
    # Decay Time - Pipe
    #==========================================================================
    @property
    def decay_time_pipe(self) -> int:
        return self.__pipe_decay_spin.value()

    @decay_time_pipe.setter
    def decay_time_pipe(self, d: int) -> None:
        self.__pipe_decay_spin.setValue(d)

    #==========================================================================
    # Sustain Level - Pipe
    #==========================================================================
    @property
    def sustain_level_pipe(self) -> int:
        return self.__pipe_sustain_spin.value()

    @sustain_level_pipe.setter
    def sustain_level_pipe(self, s: int) -> None:
        self.__pipe_sustain_spin.setValue(s)

    #==========================================================================
    # Release Time - Pipe
    #==========================================================================
    @property
    def release_time_pipe(self) -> int:
        return self.__pipe_release_spin.value()

    @release_time_pipe.setter
    def release_time_pipe(self, r: int) -> None:
        self.__pipe_release_spin.setValue(r)


def main() -> None:
    app: QApplication = QApplication([])
    window: StopEditor = StopEditor()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
