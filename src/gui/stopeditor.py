"""Stop Editor"""
from typing import Callable
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QWidget,
    QScrollArea,
    QScrollBar,
    QGroupBox,
    #QTabWidget,
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


class StopEditor(QFrame):
    def __init__(self) -> None:
        super().__init__()
        self.__init_ui()
        self.__ui_settings()
        self.__ui_layout()
        self.__rank_harmonics_checked()
        self.__rank_adsr_checked()
        self.__pipe_harmonics_checked()
        self.__pipe_adsr_checked()

    #**************************************************************************
    # Widgets
    #**************************************************************************
    def __init_ui(self) -> None:
        self.__init_ui_header()
        self.__init_ui_editor()
        self.__init_ui_options()

    #==========================================================================
    # Header
    #==========================================================================
    def __init_ui_header(self) -> None:
        self.header_widget: QWidget = QWidget()
        self.__header_label: QLabel = QLabel("Stop:")
        self.__header_edit: QLineEdit = QLineEdit()

    #==========================================================================
    # Editor
    #==========================================================================    
    def __init_ui_editor(self) -> None:
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

    #--------------------------------------------------------------------------
    # Stop Settings
    #--------------------------------------------------------------------------
    def __init_ui_stop_settings(self) -> None:
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
        self.__numranks_label: QLabel = QLabel("Number of Rank:")
        self.__numranks_spin: QSpinBox = QSpinBox()
        # Rank Series
        self.__rankseries_label: QLabel = QLabel("Rank Series:")
        self.__rankseries_combo: QComboBox = QComboBox()

    #--------------------------------------------------------------------------
    # Rank Settings
    #--------------------------------------------------------------------------
    def __init_ui_rank_settings(self) -> None:
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
        
    def __init_ui_rank_harmonics_settings(self) -> None:
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

    def __init_ui_rank_harmonic_adsr_settings(self) -> None:
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

    def __init_ui_rank_adsr_settings(self) -> None:
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

    #--------------------------------------------------------------------------
    # Pipe Settings
    #--------------------------------------------------------------------------
    def __init_ui_pipe_settings(self) -> None:
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

    def __init_ui_pipe_harmonics_settings(self) -> None:
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

    def __init_ui_pipe_harmonic_adsr_settings(self) -> None:
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
        # Edit ADSR Option

    def __init_ui_pipe_adsr_settings(self) -> None:
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

    #==========================================================================
    # Options
    #==========================================================================
    def __init_ui_options(self) -> None:
        self.__load_button: QPushButton = QPushButton("Load Stop")
        self.__clear_button: QPushButton = QPushButton("Clear Changes")
        self.__save_button: QPushButton = QPushButton("Save Stop")

    #**************************************************************************
    # Settings
    #**************************************************************************
    def __ui_settings(self) -> None:
        self.setWindowTitle("pyOrgan - Stop Editor")
        self.__ui_settings_header()
        self.__ui_settings_editor()

    #==========================================================================
    # Header
    #==========================================================================
    def __ui_settings_header(self) -> None:
        self.__header_edit.setReadOnly(True)
        self.__header_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

    #==========================================================================
    # Editor
    #==========================================================================
    def __ui_settings_editor(self) -> None:
        self.__ui_settings_editor_groupboxes()
        self.__ui_settings_editor_labels()
        self.__ui_settings_editor_comboboxes()
        self.__ui_settings_editor_spinboxes()
        self.__ui_settings_editor_checkboxes()

    def __ui_settings_editor_groupboxes(self) -> None:
        group_boxes: tuple[QGroupBox, str] = (
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
        top_level: tuple[QGroupBox] = (
            self.__stop_settings,
            self.__rank_settings,
            self.__pipe_settings
        )
        for group_box in top_level:
            group_box.setFixedWidth(270)

    def __ui_settings_editor_labels(self) -> None:
        labels: tuple[QLabel] = (
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

    def __ui_settings_editor_comboboxes(self) -> None:
        comboboxes: tuple[QComboBox] = (
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
            edit = widget.lineEdit()
            edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
            if widget == self.__stopname_combo:
                edit.setReadOnly(False)
            else:
                edit.setReadOnly(True)

    def __ui_settings_editor_spinboxes(self) -> None:
        spin_boxes: tuple[QSpinBox] = (
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

    def __ui_settings_editor_checkboxes(self) -> None:
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

    #**************************************************************************
    # Layout
    #**************************************************************************
    def __ui_layout(self) -> None:
        self.__ui_layout_header()
        self.__ui_layout_editor()

    #==========================================================================
    # Header
    #==========================================================================
    def __ui_layout_header(self) -> None:
        header_layout: QHBoxLayout = QHBoxLayout()
        widgets: tuple[QWidget] = (
            self.__header_label,
            self.__header_edit
        )
        for widget in widgets:
            header_layout.addWidget(widget)
        self.header_widget.setLayout(header_layout)
    #==========================================================================
    # Editor Forms
    #==========================================================================
    def __ui_layout_editor(self) -> None:
        self.__ui_layout_stop_settings()
        self.__ui_layout_rank_settings()
        self.__ui_layout_pipe_settings()

    #--------------------------------------------------------------------------
    # Stop Settings
    #--------------------------------------------------------------------------
    def __ui_layout_stop_settings(self) -> None:
        stopsettings_layout: QFormLayout = QFormLayout()
        stopsettings_widgets: tuple[QLabel, QWidget] = (
            (self.__stopname_label, self.__stopname_combo),
            (self.__stopfamily_label, self.__stopfamily_combo),
            (self.__organdivision_label, self.__organdivision_combo),
            (self.__numranks_label, self.__numranks_spin),
            (self.__rankseries_label, self.__rankseries_combo)
        )
        for label, widget in stopsettings_widgets:
            stopsettings_layout.addRow(label, widget)
        self.__stop_settings.setLayout(stopsettings_layout)
    
    #======================================================================
    # Rank Settings
    #======================================================================
    def __ui_layout_rank_settings(self) -> None:
        self.__ui_layout_rank_harmonic()
        self.__ui_layout_rank_harmonics_adsr()
        ranksettings_layout: QVBoxLayout = QVBoxLayout()
        ranksettings_widgets: tuple[QWidget] = (
            self.__ui_layout_rank_header(),
            self.__ui_layout_rank_harmonic_settings(),
            self.__ui_layout_rank_adsr()
        )
        for widget in ranksettings_widgets:
            ranksettings_layout.addWidget(widget)
            ranksettings_layout.addSpacing(10)
        self.__rank_settings.setLayout(ranksettings_layout)

    #----------------------------------------------------------------------
    # Rank Header
    #----------------------------------------------------------------------
    def __ui_layout_rank_header(self) -> QWidget:
        rankheader_widget: QWidget = QWidget()
        rankheader_layout: QFormLayout = QFormLayout()
        rankheader_widgets: tuple[QLabel, QWidget] = (
            (self.__ranknum_label, self.__ranknum_spin),
            (self.__ranksize_label, self.__ranksize_combo),
            (self.__numpipes_label, self.__numpipes_spin),
            (self.__pipetype_label, self.__pipetype_combo),
            (self.__startnote_label, self.__startnote_combo),
            (self.__freqoffset_label, self.__freqoffset_spin),
            (self.__numharmonics_label, self.__numharmonics_spin)
        )
        for label, widget in rankheader_widgets:
            rankheader_layout.addRow(label, widget)
        rankheader_widget.setLayout(rankheader_layout)
        return rankheader_widget

    #----------------------------------------------------------------------
    # Rank Harmonics Settings
    #----------------------------------------------------------------------
    def __ui_layout_rank_harmonic_settings(self) -> QWidget:
        rankharmonicsettings_widget: QWidget = QWidget()
        rankharmonicsettings_layout: QVBoxLayout = QVBoxLayout()
        rankharmonicsettings_layout.addWidget(self.__rank_harmonics_button)
        rankharmonicsettings_layout.addWidget(self.__rank_harmonic)
        rankharmonicsettings_widget.setLayout(rankharmonicsettings_layout)
        return rankharmonicsettings_widget

    def __ui_layout_rank_harmonics_widget(self) -> QWidget:
        rankharmonics_widget: QWidget = QWidget()
        rankharmonics_layout: QFormLayout = QFormLayout()
        rankharmonics_widgets: tuple[QLabel, QWidget] = (
            (self.__rank_harmonicnum_label, self.__rank_harmonicnum_spin),
            (self.__rank_amplitude_label, self.__rank_amplitude_spin)
        )
        for label, widget in rankharmonics_widgets:
            rankharmonics_layout.addRow(label, widget)
        rankharmonics_widget.setLayout(rankharmonics_layout)
        return rankharmonics_widget

    def __ui_layout_rank_harmonics_adsr(self) -> None:
        rankharmonicsadsr_layout: QFormLayout = QFormLayout()
        rankharmonicsadsr_widgets: tuple[QLabel, QWidget] = (
            (self.__rankharm_attack_label, self.__rankharm_attack_spin),
            (self.__rankharm_decay_label, self.__rankharm_decay_spin),
            (self.__rankharm_sustain_label, self.__rankharm_sustain_spin),
            (self.__rankharm_release_label, self.__rankharm_release_spin)
        )
        for label, widget in rankharmonicsadsr_widgets:
            rankharmonicsadsr_layout.addRow(label, widget)
        self.__rankharm_adsr.setLayout(rankharmonicsadsr_layout)

    def __ui_layout_rank_harmonic(self) -> None:
        rankharmonic_layout: QVBoxLayout = QVBoxLayout()
        rankharmonic_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        rankharmonic_layout.addWidget(self.__ui_layout_rank_harmonics_widget())
        rankharmonic_layout.addSpacing(10)
        rankharmonic_layout.addWidget(self.__rankharm_adsr_button)
        rankharmonic_layout.addWidget(self.__rankharm_adsr)
        self.__rank_harmonic.setLayout(rankharmonic_layout)
        #----------------------------------------------------------------------

    #--------------------------------------------------------------------------
    # Rank ADSR Settings
    #--------------------------------------------------------------------------
    def __ui_layout_rank_adsr(self) -> QWidget:
        rankadsr_widget: QWidget = QWidget()
        rankadsr_layout: QVBoxLayout = QVBoxLayout()
        rankadsr_form_layout: QFormLayout = QFormLayout()
        rankadsr_widgets: tuple[QLabel, QSpinBox] = (
            (self.__rank_attack_label, self.__rank_attack_spin),
            (self.__rank_decay_label, self.__rank_decay_spin),
            (self.__rank_sustain_label, self.__rank_sustain_spin),
            (self.__rank_release_label, self.__rank_release_spin)
        )
        for label, widget in rankadsr_widgets:
            rankadsr_form_layout.addRow(label, widget)
        self.__rank_adsr.setLayout(rankadsr_form_layout)
        rankadsr_layout.addWidget(self.__rank_adsr_button)
        rankadsr_layout.addWidget(self.__rank_adsr)
        rankadsr_widget.setLayout(rankadsr_layout)
        return rankadsr_widget

    #==========================================================================
    # Pipe Settings
    #==========================================================================
    def __ui_layout_pipe_settings(self) -> None:
        pipesettings_layout: QVBoxLayout = QVBoxLayout()
        #----------------------------------------------------------------------
        # Pipe Header Widget
        #----------------------------------------------------------------------
        pipeheader_widget: QWidget = QWidget()
        pipeheader_layout: QFormLayout = QFormLayout()
        pipeheader_widgets: tuple[QLabel, QWidget] = (
            (self.__ranknum_pipe_label, self.__ranknum_pipe_spin),
            (self.__pipenum_label, self.__pipenum_spin),        
            (self.__note_label, self.__note_combo),
            (self.__relnote_label, self.__relnote_combo)
        )
        for label, widget in pipeheader_widgets:
            pipeheader_layout.addRow(label, widget)
        pipeheader_widget.setLayout(pipeheader_layout)
        #----------------------------------------------------------------------
        # Pipe Harmonics Settings Widget
        #----------------------------------------------------------------------
        pipeharmonicsettings_widget: QWidget = QWidget()
        pipeharmonicsettings_layout: QVBoxLayout = QVBoxLayout()
        pipeharmonic_layout: QVBoxLayout = QVBoxLayout()
        pipeharmonics_widget: QWidget = QWidget()
        pipeharmonics_layout: QFormLayout = QFormLayout()
        pipeharmonics_widgets: tuple[QLabel, QWidget] = (
            (self.__pipe_harmonicnum_label, self.__pipe_harmonicnum_spin),
            (self.__pipe_amplitude_label, self.__pipe_amplitude_spin)
        )
        for label, widget in pipeharmonics_widgets:
            pipeharmonics_layout.addRow(label, widget)
        pipeharmonics_widget.setLayout(pipeharmonics_layout)
        pipeharmonicsadsr_layout: QFormLayout = QFormLayout()
        pipeharmonicsadsr_widgets: tuple[QLabel, QWidget] = (
            (self.__pipeharm_attack_label, self.__pipeharm_attack_spin),
            (self.__pipeharm_decay_label, self.__pipeharm_decay_spin),
            (self.__pipeharm_sustain_label, self.__pipeharm_sustain_spin),
            (self.__pipeharm_release_label, self.__pipeharm_release_spin)
        )
        for label, widget in pipeharmonicsadsr_widgets:
            pipeharmonicsadsr_layout.addRow(label, widget)
        self.__pipeharm_adsr.setLayout(pipeharmonicsadsr_layout)
        pipeharmonic_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        pipeharmonic_layout.addWidget(pipeharmonics_widget)
        pipeharmonic_layout.addSpacing(10)
        pipeharmonic_layout.addWidget(self.__pipeharm_adsr_button)
        pipeharmonic_layout.addWidget(self.__pipeharm_adsr)
        self.__pipe_harmonic.setLayout(pipeharmonic_layout)
        pipeharmonicsettings_layout.addWidget(self.__pipe_harmonics_button)
        pipeharmonicsettings_layout.addWidget(self.__pipe_harmonic)
        pipeharmonicsettings_widget.setLayout(pipeharmonicsettings_layout)
        #----------------------------------------------------------------------
        # Pipe ADSR Widget
        #----------------------------------------------------------------------
        pipeadsr_widget: QWidget = QWidget()
        pipeadsr_layout: QVBoxLayout = QVBoxLayout()
        pipeadsr_form_layout: QFormLayout = QFormLayout()
        pipeadsr_widgets: tuple[QLabel, QSpinBox] = (
            (self.__pipe_attack_label, self.__pipe_attack_spin),
            (self.__pipe_decay_label, self.__pipe_decay_spin),
            (self.__pipe_sustain_label, self.__pipe_sustain_spin),
            (self.__pipe_release_label, self.__pipe_release_spin)
        )
        for label, widget in pipeadsr_widgets:
            pipeadsr_form_layout.addRow(label, widget)
        self.__pipe_adsr.setLayout(pipeadsr_form_layout)
        pipeadsr_layout.addWidget(self.__pipe_adsr_button)
        pipeadsr_layout.addWidget(self.__pipe_adsr)
        pipeadsr_widget.setLayout(pipeadsr_layout)
        #----------------------------------------------------------------------
        # Pipe Settings Layout
        #----------------------------------------------------------------------
        pipesettings_widgets: tuple[QWidget] = (
            pipeheader_widget,
            pipeharmonicsettings_widget,
            pipeadsr_widget
        )
        for widget in pipesettings_widgets:
            pipesettings_layout.addWidget(widget)
            pipesettings_layout.addSpacing(10)
        self.__pipe_settings.setLayout(pipesettings_layout)
        #======================================================================
        # Editor Layout
        #======================================================================
        editor_scroll: QScrollArea = QScrollArea()
        editor_scroll.setVerticalScrollBar(QScrollBar())
        editor_scroll.setWidgetResizable(True)
        editor_scroll.setFixedWidth(310)
        editor_layout: QVBoxLayout = QVBoxLayout()
        editor_widgets: tuple[QWidget] = (
            self.__stop_settings,
            self.__rank_settings,
            self.__pipe_settings
        )
        for widget in editor_widgets:
            editor_layout.addWidget(widget)
        self.__editor.setLayout(editor_layout)
        editor_scroll.setWidget(self.__editor)
        #**********************************************************************
        # Button Widget
        #**********************************************************************
        button_widget: QWidget = QWidget()
        button_layout: QVBoxLayout = QVBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        buttons: tuple[QPushButton] = (
            self.__load_button,
            self.__clear_button,
            self.__save_button
        )
        for button in buttons:
            button_layout.addWidget(button)
        button_widget.setLayout(button_layout)
        #**********************************************************************
        # Form Widget
        #**********************************************************************
        form_widget: QWidget = QWidget()
        form_layout: QVBoxLayout = QVBoxLayout()
        form_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        form_widgets: tuple[QWidget] = (
            self.header_widget,
            editor_scroll
        )
        for widget in form_widgets:
            form_layout.addWidget(widget)
        form_widget.setLayout(form_layout)
        #**********************************************************************
        # Main Layout
        #**********************************************************************
        main_layout: QHBoxLayout = QHBoxLayout()
        widgets: tuple[QWidget] = (
            form_widget,
            button_widget
        )
        for widget in widgets:
            main_layout.addWidget(widget)
        self.setLayout(main_layout)

    #**************************************************************************
    # Actions
    #**************************************************************************
    #==========================================================================
    # Widget Manipulation
    #==========================================================================
    def __rank_harmonics_checked(self) -> None:
        widgets: tuple[QWidget] = (
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

    def __rankharm_adsr_checked(self) -> None:
        widgets = (
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

    def __rank_adsr_checked(self) -> None:
        widgets = (
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

    def __pipe_harmonics_checked(self) -> None:
        widgets: tuple[QWidget] = (
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

    def __pipeharm_adsr_checked(self) -> None:
        spins = (
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

    def __pipe_adsr_checked(self) -> None:
        spins = (
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

    #==========================================================================
    # Widget Data
    #==========================================================================
    def stop_names_populate(self, stop_names: tuple[str]) -> None:
        self.__stopname_combo.addItems(stop_names)

    def stop_families_populate(self, stop_families: tuple[str]) -> None:
        self.__stopfamily_combo.addItems(stop_families)

    def organ_divisions_populate(self, divisions: tuple[str]) -> None:
        self.__organdivision_combo.addItems(divisions)

    def number_ranks_set_minimum(self, min: int) -> None:
        self.__numranks_spin.setMinimum(min)

    def number_ranks_set_maximum(self, max: int) -> None:
        self.__numranks_spin.setMaximum(max)

    def rank_series_populate(self, rank_series: tuple[str]) -> None:
        self.__rankseries_combo.addItems(rank_series)

    def rank_number_set_minimum(self, min: int) -> None:
        self.__ranknum_spin.setMinimum(min)

    def rank_number_set_maximum(self, max: int) -> None:
        self.__ranknum_spin.setMaximum(max)

    def rank_size_populate(self, rank_sizes: tuple[str]) -> None:
        self.__ranksize_combo.addItems(rank_sizes)

    def number_pipes_set_minimum(self, min: int) -> None:
        self.__numpipes_spin.setMinimum(min)

    def number_pipes_set_maximum(self, max: int) -> None:
        self.__numpipes_spin.setMaximum(max)

    def pipe_types_populate(self, pipe_types: tuple[str]) -> None:
        self.__pipetype_combo.addItems(pipe_types)

    def starting_note_populate(self, starting_notes: tuple[str]) -> None:
        self.__startnote_combo.addItems(starting_notes)

    def frequency_offset_set_minimum(self, min: int) -> None:
        self.__freqoffset_spin.setMinimum(min)

    def frequency_offset_set_maximum(self, max: int) -> None:
        self.__freqoffset_spin.setMaximum(max)

    def number_harmonics_set_minimum(self, min: int) -> None:
        self.__numharmonics_spin.setMinimum(min)

    def number_harmonics_set_maximum(self, max: int) -> None:
        self.__numharmonics_spin.setMaximum(max)

    def harmonic_number_rank_set_minimum(self, min: int) -> None:
        self.__rank_harmonicnum_spin.setMinimum(min)

    def harmonic_number_rank_set_maximum(self, max: int) -> None:
        self.__rank_harmonicnum_spin.setMaximum(max)

    def amplitude_rank_set_minimum(self, min: int) -> None:
        self.__rank_amplitude_spin.setMinimum(min)

    def amplitude_rank_set_maximum(self, max: int) -> None:
        self.__rank_amplitude_spin.setMaximum(max)

    def attack_time_rank_harmonic_set_minimum(self, min: int) -> None:
        self.__rankharm_attack_spin.setMinimum(min)

    def attack_time_rank_harmonic_set_maximum(self, max: int) -> None:
        self.__rankharm_attack_spin.setMaximum(max)

    def decay_time_rank_harmonic_set_minimum(self, min: int) -> None:
        self.__rankharm_decay_spin.setMinimum(min)

    def decay_time_rank_harmonic_set_maximum(self, max: int) -> None:
        self.__rankharm_decay_spin.setMaximum(max)

    def sustain_level_rank_harmonic_set_minimum(self, min: int) -> None:
        self.__rankharm_sustain_spin.setMinimum(min)

    def sustain_level_rank_harmonic_set_maximum(self, max: int) -> None:
        self.__rankharm_sustain_spin.setMaximum(max)

    def release_time_rank_harmonic_set_minimum(self, min: int) -> None:
        self.__rankharm_release_spin.setMinimum(min)

    def release_time_rank_harmonic_set_maximum(self, max: int) -> None:
        self.__rankharm_release_spin.setMaximum(max)

    def attack_time_rank_set_minimum(self, min: int) -> None:
        self.__rank_attack_spin.setMinimum(min)

    def attack_time_rank_set_maximum(self, max: int) -> None:
        self.__rank_attack_spin.setMaximum(max)

    def decay_time_rank_set_minimum(self, min: int) -> None:
        self.__rank_decay_spin.setMinimum(min)

    def decay_time_rank_set_maximum(self, max: int) -> None:
        self.__rank_decay_spin.setMaximum(max)

    def sustain_level_rank_set_minimum(self, min: int) -> None:
        self.__rank_sustain_spin.setMinimum(min)

    def sustain_level_rank_set_maximum(self, max: int) -> None:
        self.__rank_sustain_spin.setMaximum(max)

    def release_time_rank_set_minimum(self, min: int) -> None:
        self.__rank_release_spin.setMinimum(min)

    def release_time_rank_set_maximum(self, max: int) -> None:
        self.__rank_release_spin.setMaximum(max)

    def rank_number_pipe_set_minimum(self, min: int) -> None:
        self.__ranknum_pipe_spin.setMinimum(min)

    def rank_number_pipe_set_maximum(self, max: int) -> None:
        self.__ranknum_pipe_spin.setMaximum(max)

    def pipe_number_set_minimum(self, min: int) -> None:
        self.__pipenum_spin.setMinimum(min)

    def pipe_number_set_maximum(self, max: int) -> None:
        self.__pipenum_spin.setMaximum(max)

    def note_populate(self, notes: tuple[str]) -> None:
        self.__note_combo.addItems(notes)

    def relative_note_populate(self, notes: tuple[str]) -> None:
        self.__relnote_combo.addItems(notes)

    def harmonic_number_pipe_set_minimum(self, min: int) -> None:
        self.__pipe_harmonicnum_spin.setMinimum(min)

    def harmonic_number_pipe_set_maximum(self, max: int) -> None:
        self.__pipe_harmonicnum_spin.setMaximum(max)

    def amplitude_pipe_set_minimum(self, min: int) -> None:
        self.__pipe_amplitude_spin.setMinimum(min)

    def amplitude_pipe_set_maximum(self, max: int) -> None:
        self.__pipe_amplitude_spin.setMaximum(max)

    def attack_time_pipe_harmonic_set_minimum(self, min: int) -> None:
        self.__pipeharm_attack_spin.setMinimum(min)

    def attack_time_pipe_harmonic_set_maximum(self, max: int) -> None:
        self.__pipeharm_attack_spin.setMaximum(max)

    def decay_time_pipe_harmonic_set_minimum(self, min: int) -> None:
        self.__pipeharm_decay_spin.setMinimum(min)

    def decay_time_pipe_harmonic_set_maximum(self, max: int) -> None:
        self.__pipeharm_decay_spin.setMaximum(max)

    def sustain_level_pipe_harmonic_set_minimum(self, min: int) -> None:
        self.__pipeharm_sustain_spin.setMinimum(min)

    def sustain_level_pipe_harmonic_set_maximum(self, max: int) -> None:
        self.__pipeharm_sustain_spin.setMaximum(max)

    def release_time_pipe_harmonic_set_minimum(self, min: int) -> None:
        self.__pipeharm_release_spin.setMinimum(min)

    def release_time_pipe_harmonic_set_maximum(self, max: int) -> None:
        self.__pipeharm_release_spin.setMaximum(max)

    def attack_time_pipe_set_minimum(self, min: int) -> None:
        self.__pipe_attack_spin.setMinimum(min)

    def attack_time_pipe_set_maximum(self, max: int) -> None:
        self.__pipe_attack_spin.setMaximum(max)

    def decay_time_pipe_set_minimum(self, min: int) -> None:
        self.__pipe_decay_spin.setMinimum(min)

    def decay_time_pipe_set_maximum(self, max: int) -> None:
        self.__pipe_decay_spin.setMaximum(max)

    def sustain_level_pipe_set_minimum(self, min: int) -> None:
        self.__pipe_sustain_spin.setMinimum(min)

    def sustain_level_pipe_set_maximum(self, max: int) -> None:
        self.__pipe_sustain_spin.setMaximum(max)

    def release_time_pipe_set_minimum(self, min: int) -> None:
        self.__pipe_release_spin.setMinimum(min)

    def release_time_pipe_set_maximum(self, max: int) -> None:
        self.__pipe_release_spin.setMaximum(max)

    #==========================================================================
    # Data Manipulation
    #==========================================================================
    def update_stop_header(self) -> None:
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
        self.__header_edit.setText(stop_name)

    def stop_name_change(self, action: Callable) -> None:
        self.__stopname_combo.currentTextChanged.connect(action)

    def stop_family_change(self, action: Callable) -> None:
        self.__stopfamily_combo.currentTextChanged.connect(action)

    def organ_division_change(self, action: Callable) -> None:
        self.__organdivision_combo.currentTextChanged.connect(action)

    def number_ranks_change(self, action: Callable) -> None:
        self.__numranks_spin.valueChanged.connect(action)

    def rank_series_change(self, action: Callable) -> None:
        self.__rankseries_combo.currentTextChanged.connect(action)

    def rank_number_change(self, action: Callable) -> None:
        self.__ranknum_spin.valueChanged.connect(action)

    def rank_size_change(self, action: Callable) -> None:
        self.__ranksize_combo.currentTextChanged.connect(action)

    def number_pipes_change(self, action: Callable) -> None:
        self.__numpipes_spin.valueChanged.connect(action)

    def pipe_type_change(self, action: Callable) -> None:
        self.__pipetype_combo.currentTextChanged.connect(action)

    def starting_note_change(self, action: Callable) -> None:
        self.__startnote_combo.currentTextChanged.connect(action)

    def frequency_offset_change(self, action: Callable) -> None:
        self.__freqoffset_spin.valueChanged.connect(action)

    def number_harmonics_change(self, action: Callable) -> None:
        self.__numharmonics_spin.valueChanged.connect(action)

    def harmonic_number_rank_change(self, action: Callable) -> None:
        self.__rank_harmonicnum_spin.valueChanged.connect(action)

    def amplitude_rank_change(self, action: Callable) -> None:
        self.__rank_amplitude_spin.valueChanged.connect(action)

    def attack_time_rank_harmonic_change(self, action: Callable) -> None:
        self.__rankharm_attack_spin.valueChanged.connect(action)

    def decay_time_rank_harmonic_change(self, action: Callable) -> None:
        self.__rankharm_decay_spin.valueChanged.connect(action)

    def sustain_level_rank_harmonic_change(self, action: Callable) -> None:
        self.__rankharm_sustain_spin.valueChanged.connect(action)

    def release_time_rank_harmonic_change(self, action: Callable) -> None:
        self.__rankharm_release_spin.valueChanged.connect(action)

    def attack_time_rank_change(self, action: Callable) -> None:
        self.__rank_attack_spin.valueChanged.connect(action)

    def decay_time_rank_change(self, action: Callable) -> None:
        self.__rank_decay_spin.valueChanged.connect(action)

    def sustain_level_rank_change(self, action: Callable) -> None:
        self.__rank_sustain_spin.valueChanged.connect(action)

    def release_time_rank_change(self, action: Callable) -> None:
        self.__rank_release_spin.valueChanged.connect(action)

    def rank_number_pipe_change(self, action: Callable) -> None:
        self.__ranknum_pipe_spin.valueChanged.connect(action)

    def pipe_number_change(self, action: Callable) -> None:
        self.__pipenum_spin.valueChanged.connect(action)

    def note_change(self, action: Callable) -> None:
        self.__note_combo.currentTextChanged.connect(action)

    def relative_note_change(self, action: Callable) -> None:
        self.__relnote_combo.currentTextChanged.connect(action)

    def harmonic_number_pipe_change(self, action: Callable) -> None:
        self.__pipe_harmonicnum_spin.valueChanged.connect(action)

    def amplitude_pipe_change(self, action: Callable) -> None:
        self.__pipe_amplitude_spin.valueChanged.connect(action)

    def attack_time_pipe_harmonic_change(self, action: Callable) -> None:
        self.__pipeharm_attack_spin.valueChanged.connect(action)

    def decay_time_pipe_harmonic_change(self, action: Callable) -> None:
        self.__pipeharm_decay_spin.valueChanged.connect(action)

    def sustain_level_pipe_harmonic_change(self, action: Callable) -> None:
        self.__pipeharm_sustain_spin.valueChanged.connect(action)

    def release_time_pipe_harmonic_change(self, action: Callable) -> None:
        self.__pipeharm_release_spin.valueChanged.connect(action)

    def attack_time_pipe_change(self, action: Callable) -> None:
        self.__pipe_attack_spin.valueChanged.connect(action)

    def decay_time_pipe_change(self, action: Callable) -> None:
        self.__pipe_decay_spin.valueChanged.connect(action)

    def sustain_level_pipe_change(self, action: Callable) -> None:
        self.__pipe_sustain_spin.valueChanged.connect(action)

    def release_time_pipe_change(self, action: Callable) -> None:
        self.__pipe_release_spin.valueChanged.connect(action)

    #**************************************************************************
    # Properties
    #**************************************************************************
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
        self.__freqoffset_spin.value()

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
