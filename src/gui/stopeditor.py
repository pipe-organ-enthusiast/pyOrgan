"""Stop Editor"""
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QWidget,
    QGroupBox,
    QTabWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QSpinBox,
    QPushButton,
    QRadioButton,
    QLayout,
    QFormLayout,
    QHBoxLayout,
    QVBoxLayout
)
from PySide6.QtGui import Qt
#------------------------------------------------------------------------------


class StopEditor(QFrame):
    def __init__(self) -> None:
        super().__init__()
        self.__init_ui()
        self.__ui_settings()
        self.__ui_layout()

    #--------------------------------------------------------------------------
    # Widgets
    #--------------------------------------------------------------------------
    def __init_ui(self) -> None:
        #**********************************************************************
        # Header
        #**********************************************************************
        self.header_label: QLabel = QLabel("Stop:")
        self.header_edit: QLineEdit = QLineEdit()
        #**********************************************************************
        # Editor
        #**********************************************************************
        self.editor: QTabWidget = QTabWidget()
        #======================================================================
        # Stop Settings
        #======================================================================
        # Stop Name
        self.stopname_label: QLabel = QLabel("Stop Name:")
        self.stopname_combo: QComboBox = QComboBox()
        # Stop Family
        self.stopfamily_label: QLabel = QLabel("Stop Family:")
        self.stopfamily_combo = QComboBox()
        # Organ Division
        self.organdivision_label: QLabel = QLabel("Organ Division:")
        self.organdivision_combo: QComboBox = QComboBox()
        # Number of Ranks
        self.numranks_label: QLabel = QLabel("Number of Rank:")
        self.numranks_spin: QSpinBox = QSpinBox()
        # Rank Series
        self.rankseries_label: QLabel = QLabel("Rank Series:")
        self.rankseries_combo: QComboBox = QComboBox()
        #======================================================================
        # Rank Settings
        #======================================================================
        # Rank #
        self.ranknum_label: QLabel = QLabel("Rank #:")
        self.ranknum_spin: QSpinBox = QSpinBox()
        # Rank Size
        self.ranksize_label: QLabel = QLabel("Rank Size:")
        self.ranksize_combo = QComboBox()
        # Number of Pipes
        self.numpipes_label: QLabel = QLabel("Number of Pipes:")
        self.numpipes_spin: QSpinBox = QSpinBox()
        # Starting Note
        self.startnote_label: QLabel = QLabel("Starting Note:")
        self.startnote_combo: QComboBox = QComboBox()
        # Pipe Type
        self.pipetype_label: QLabel = QLabel("PipeType:")
        self.pipetype_combo: QComboBox = QComboBox()
        # Frequency Offset
        self.freqoffset_label: QLabel = QLabel("Frequency Offset (Hz):")
        self.freqoffset_spin: QSpinBox = QSpinBox()
        # Number of Harmonics
        self.numharmonics_label: QLabel = QLabel("Number of Harmonics:")
        self.numharmonics_spin: QSpinBox = QSpinBox()
        #======================================================================
        # Pipe Settings
        #======================================================================
        # Rank #
        self.ranknum_label: QLabel = QLabel("Rank #:")
        self.ranknum_spin: QSpinBox = QSpinBox()
        # Pipe #
        self.pipenum_label: QLabel = QLabel("Pipe #:")
        self.pipenum_spin: QSpinBox = QSpinBox()        
        # Note
        self.note_label: QLabel = QLabel("Note:")
        self.note_combo: QComboBox = QComboBox()
        # Relative Note
        self.relnote_label: QLabel = QLabel("Relative Note:")
        self.relnote_combo: QComboBox = QComboBox()
        #======================================================================
        # Harmonic Settings
        #======================================================================
        #----------------------------------------------------------------------
        # Harmonic Settings Options
        #----------------------------------------------------------------------
        self.harmonic_option_general: QRadioButton = QRadioButton()
        self.harmonic_option_specific: QRadioButton = QRadioButton()
        #----------------------------------------------------------------------
        # Harmonic Settings Form
        #----------------------------------------------------------------------
        self.harmonicsettings: QGroupBox = QGroupBox()
        # Rank #
        self.harmonic_ranknum_label: QLabel = QLabel("Rank #:")
        self.harmonic_ranknum_spin: QSpinBox = QSpinBox()
        # Pipe #
        self.harmonic_pipenum_label: QLabel = QLabel("Pipe #:")
        self.harmonic_pipenum_spin: QSpinBox = QSpinBox()
        # Harmonic #
        self.harmonicnum_label: QLabel = QLabel("Harmonic #:")
        self.harmonicnum_spin: QSpinBox = QSpinBox()
        # Amplitude
        self.amplitude_label: QLabel = QLabel("Amplitude (%):")
        self.amplitude_spin: QSpinBox = QSpinBox()
        #======================================================================
        # ADSR Settings
        #======================================================================
        #----------------------------------------------------------------------
        # ADSR Settings Options
        #----------------------------------------------------------------------
        self.adsroption_rank: QRadioButton = QRadioButton()
        self.adsroption_pipe: QRadioButton = QRadioButton()
        self.adsroption_harmonic: QRadioButton = QRadioButton()
        #----------------------------------------------------------------------
        # ADSR Settings Form
        #----------------------------------------------------------------------
        self.adsrsettings: QGroupBox = QGroupBox()
        # Rank #
        self.adsr_ranknum_label: QLabel = QLabel("Rank #:")
        self.adsr_ranknum_spin: QSpinBox = QSpinBox()
        # Pipe #
        self.adsr_pipenum_label: QLabel = QLabel("Pipe #:")
        self.adsr_pipenum_spin: QSpinBox = QSpinBox()
        # Harmonic #
        self.adsr_harmonicnum_label: QLabel = QLabel("Harmonic #:")
        self.adsr_harmonicnum_spin: QSpinBox = QSpinBox()
        # Attack
        self.attack_label: QLabel = QLabel("Attack Time (ms)")
        self.attack_spin: QSpinBox = QSpinBox()
        # Decay
        self.decay_label: QLabel = QLabel("Decay Time (ms):")
        self.decay_spin: QSpinBox = QSpinBox()
        # Sustain
        self.sustain_label: QLabel = QLabel("Sustain Level (%):")
        self.sustain_spin: QSpinBox = QSpinBox()
        # Release
        self.release_label: QLabel = QLabel("Release Time (ms):")
        self.release_spin: QSpinBox = QSpinBox()
        #======================================================================
        # Options
        #======================================================================
        self.load_button: QPushButton = QPushButton("Load Stop")
        self.clear_button: QPushButton = QPushButton("Clear Changes")
        self.save_button: QPushButton = QPushButton("Save Stop")

    #--------------------------------------------------------------------------
    # Settings
    #--------------------------------------------------------------------------
    def __ui_settings(self) -> None:
        self.setWindowTitle("pyOrgan - Stop Editor")
        #**********************************************************************
        # Settings - Header
        #**********************************************************************
        self.header_edit.setReadOnly(True)
        self.header_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #**********************************************************************
        # Settings - Editor
        #**********************************************************************
        self.editor.setFixedWidth(500)
        #======================================================================
        # Settings - Editor - Labels
        #======================================================================
        labels: tuple[QLabel] = (
            self.stopname_label,
            self.stopfamily_label,
            self.organdivision_label,
            self.numranks_label,
            self.rankseries_label,
            self.ranknum_label,
            self.ranksize_label,
            self.numpipes_label,
            self.startnote_label,
            self.pipetype_label,
            self.freqoffset_label,
            self.numharmonics_label,
            self.ranknum_label,
            self.pipenum_label,
            self.note_label,
            self.relnote_label,
            self.harmonic_ranknum_label,
            self.harmonic_pipenum_label,
            self.harmonicnum_label,
            self.amplitude_label,
            self.adsr_ranknum_label,
            self.adsr_pipenum_label,
            self.adsr_harmonicnum_label,
            self.attack_label,
            self.decay_label,
            self.sustain_label,
            self.release_label
        )
        for label in labels:
            label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            label.setFixedWidth(130)
        #======================================================================
        # Settings - Editor - GroupBoxes
        #======================================================================
        group_boxes: tuple[QGroupBox, str] =  (
            (self.harmonicsettings, "Harmonic Settings"),
            (self.adsrsettings, "ADSR Settings")
        )
        for group_box in group_boxes:
            group_box[0].setTitle(group_box[1])
            group_box[0].setAlignment(
                Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft
            )
            group_box[0].setFixedWidth(465)
        #======================================================================
        # Settings - Editor - ComboBoxes
        #======================================================================
        comboboxes: tuple[QComboBox] = (
            self.stopname_combo,
            self.stopfamily_combo,
            self.organdivision_combo,
            self.rankseries_combo,
            self.ranksize_combo,
            self.pipetype_combo,
            self.startnote_combo,
            self.note_combo,
            self.relnote_combo,
        )
        for widget in comboboxes:
            widget.setEditable(True)
            edit = widget.lineEdit()
            edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
            widget.setFixedWidth(300)
            if widget == self.stopname_combo:
                edit.setReadOnly(False)
            else:
                edit.setReadOnly(True)
        #======================================================================
        # Settings - Editor - SpinBoxes
        #======================================================================
        spin_boxes: tuple[QSpinBox] = (
            self.numranks_spin,
            self.ranknum_spin,
            self.numpipes_spin,
            self.freqoffset_spin,
            self.numharmonics_spin,
            self.ranknum_spin,
            self.pipenum_spin,
            self.harmonic_ranknum_spin,
            self.harmonic_pipenum_spin,
            self.harmonicnum_spin,
            self.amplitude_spin,
            self.adsr_ranknum_spin,
            self.adsr_pipenum_spin,
            self.adsr_harmonicnum_spin,
            self.attack_spin,
            self.decay_spin,
            self.sustain_spin,
            self.release_spin
        )
        for spin_box in spin_boxes:
            spin_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
            spin_box.setFixedWidth(300)
        #======================================================================
        # Settings - Editor - RadioButtons
        #======================================================================
        radio_buttons: tuple[QRadioButton, str] = (
            (
                self.harmonic_option_general,
                "Harmonic Settings - Rank Wide"
            ),
            (
                self.harmonic_option_specific, 
                "Harmonic Settings - Pipe Specific"
            ),
            (
                self.adsroption_rank,
                "ADSR Settings - Rank Wide"
            ),
            (
                self.adsroption_pipe,
                "ADSR Settings - Pipe Specific"
            ),
            (
                self.adsroption_harmonic,
                "ADSR Settings - Harmonic Specific"
            )
        )
        for radio_button in radio_buttons:
            radio_button[0].setText(radio_button[1])
        #----------------------------------------------------------------------
        # Settings - Editor - RadioButtons - Actions
        #----------------------------------------------------------------------
        self.harmonic_option_general.toggled.connect(
            lambda: self.harmonic_pipenum_visibility(False)
        )
        self.harmonic_option_specific.toggled.connect(
            lambda: self.harmonic_pipenum_visibility(True)
        )
        self.adsroption_rank.toggled.connect(
            self.adsroption_rank_toggled
        )
        self.adsroption_pipe.toggled.connect(
            self.adsroption_pipe_toggled
        )
        self.adsroption_harmonic.toggled.connect(
            self.adsroption_harmonic_toggled
        )
        #----------------------------------------------------------------------
        # Settings - Editor - RadioButtons - Default State
        #----------------------------------------------------------------------
        self.harmonic_option_general.toggle()
        self.adsroption_rank.toggle()

    #--------------------------------------------------------------------------
    # Layout
    #--------------------------------------------------------------------------
    def __ui_layout(self) -> None:
        #**********************************************************************
        # Header Layout
        #**********************************************************************
        header_layout: QHBoxLayout = QHBoxLayout()
        widgets: tuple[QWidget] = (
            self.header_label,
            self.header_edit
        )
        for widget in widgets:
            header_layout.addWidget(widget)
        #**********************************************************************
        # Stop Settings Layout
        #**********************************************************************
        stopsettings_layout: QFormLayout = QFormLayout()
        stopsettings_widgets: tuple[QLabel, QWidget] = (
            (self.stopname_label, self.stopname_combo),
            (self.stopfamily_label, self.stopfamily_combo),
            (self.organdivision_label, self.organdivision_combo),
            (self.numranks_label, self.numranks_spin),
            (self.rankseries_label, self.rankseries_combo)
        )
        for widget in stopsettings_widgets:
            stopsettings_layout.addRow(widget[0], widget[1])
        #**********************************************************************
        # Rank Settings Layout
        #**********************************************************************
        ranksettings_layout: QFormLayout = QFormLayout()
        ranksettings_widgets: tuple[QLabel, QWidget] = (
            (self.ranknum_label, self.ranknum_spin),
            (self.ranksize_label, self.ranksize_combo),
            (self.numpipes_label, self.numpipes_spin),
            (self.pipetype_label, self.pipetype_combo),
            (self.startnote_label, self.startnote_combo),
            (self.freqoffset_label, self.freqoffset_spin),
            (self.numharmonics_label, self.numharmonics_spin)
        )
        for widget in ranksettings_widgets:
            ranksettings_layout.addRow(widget[0], widget[1])
        #**********************************************************************
        # Pipe Settings Layout
        #**********************************************************************
        pipesettings_layout: QFormLayout = QFormLayout()
        pipesettings_widgets: tuple[QLabel, QWidget] = (
            (self.ranknum_label, self.ranknum_spin),
            (self.pipenum_label, self.pipenum_spin),
            (self.note_label, self.note_combo),
            (self.relnote_label, self.relnote_combo)
        )
        for widget in pipesettings_widgets:
            pipesettings_layout.addRow(widget[0], widget[1])
        #**********************************************************************
        # Harmonic Settings Layout
        #**********************************************************************
        harmonicsettings_layout: QVBoxLayout = QVBoxLayout()
        harmonicoptions_widgets: tuple[QRadioButton] = (
            self.harmonic_option_general,
            self.harmonic_option_specific
        )
        for widget in harmonicoptions_widgets:
            harmonicsettings_layout.addWidget(widget)
        harmonicform_layout: QFormLayout = QFormLayout()
        harmonicoptions_widgets: tuple[QLabel, QSpinBox] = (
            (self.harmonic_ranknum_label, self.harmonic_ranknum_spin),
            (self.harmonic_pipenum_label, self.harmonic_pipenum_spin),
            (self.harmonicnum_label, self.harmonicnum_spin),
            (self.amplitude_label, self.amplitude_spin)
        )
        for widget in harmonicoptions_widgets:
            harmonicform_layout.addRow(widget[0], widget[1])
        harmonicsettings_layout.addSpacing(10)
        harmonicsettings_layout.addLayout(harmonicform_layout)
        #**********************************************************************
        # ADSR Settings Layout
        #**********************************************************************
        adsrsettings_layout: QVBoxLayout = QVBoxLayout()
        adsrsettings_widgets: tuple[QRadioButton] = (
            self.adsroption_rank,
            self.adsroption_pipe,
            self.adsroption_harmonic
        )
        for widget in adsrsettings_widgets:
            adsrsettings_layout.addWidget(widget)
        adsrform_layout: QFormLayout = QFormLayout()
        adsrsettings_widgets: tuple[QLabel, QSpinBox] = (
            (self.adsr_ranknum_label, self.adsr_ranknum_spin),
            (self.adsr_pipenum_label, self.adsr_pipenum_spin),
            (self.adsr_harmonicnum_label, self.adsr_harmonicnum_spin),
            (self.attack_label, self.attack_spin),
            (self.decay_label, self.decay_spin),
            (self.sustain_label, self.sustain_spin),
            (self.release_label, self.release_spin)
        )
        for widget in adsrsettings_widgets:
            adsrform_layout.addRow(widget[0], widget[1])
        adsrsettings_layout.addSpacing(10)
        adsrsettings_layout.addLayout(adsrform_layout)
        #**********************************************************************
        # Editor Layout
        #**********************************************************************
        editor_layouts: tuple[QLayout, str] = (
            (stopsettings_layout, "Stop Settings"),
            (ranksettings_layout, "Rank Settings"),
            (pipesettings_layout, "Pipe Settings"),
            (harmonicsettings_layout, "Harmonic Settings"),
            (adsrsettings_layout, "ADSR Settings")
        )
        for layout in editor_layouts:
            tabwidget = QWidget()
            tabwidget.setLayout(layout[0])
            self.editor.addTab(tabwidget, layout[1])
        #**********************************************************************
        # Button Layout
        #**********************************************************************
        button_layout: QVBoxLayout = QVBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        button_widgets: tuple[QPushButton] = (
            self.load_button,
            self.clear_button,
            self.save_button
        )
        for widget in button_widgets:
            button_layout.addWidget(widget)
        #**********************************************************************
        # Main Layout
        #**********************************************************************
        layout_body: QHBoxLayout = QHBoxLayout()
        layout_body.addWidget(self.editor)
        layout_body.addLayout(button_layout)
        main_layout: QVBoxLayout = QVBoxLayout()
        main_layout.addSpacing(10)
        layouts: tuple[QLayout] = (
            header_layout,
            layout_body
        )
        for layout in layouts:
            main_layout.addLayout(layout)
            main_layout.addSpacing(10)
        self.setLayout(main_layout)

    #--------------------------------------------------------------------------
    # Actions
    #--------------------------------------------------------------------------
    def harmonic_pipenum_visibility(self, visible: bool) -> None:
        widgets: tuple[QWidget] = (
            self.harmonic_pipenum_label,
            self.harmonic_pipenum_spin
        )
        match visible:
            case True:
                for widget in widgets:
                    widget.show()
            case False:
                for widget in widgets:
                    widget.hide()

    def adsroption_rank_toggled(self) -> None:
        shown_widgets: tuple[QWidget] = (
            self.adsr_ranknum_label,
            self.adsr_ranknum_spin
        )
        for widget in shown_widgets:
            widget.show()
        #----------------------------------------------------------------------
        hidden_widgets: tuple[QWidget] = (
            self.adsr_pipenum_label,
            self.adsr_pipenum_spin,
            self.adsr_harmonicnum_label,
            self.adsr_harmonicnum_spin
        )
        for widget in hidden_widgets:
            widget.hide()

    def adsroption_pipe_toggled(self) -> None:
        shown_widgets: tuple[QWidget] = (
            self.adsr_ranknum_label,
            self.adsr_ranknum_spin,
            self.adsr_pipenum_label,
            self.adsr_pipenum_spin
        )
        for widget in shown_widgets:
            widget.show()
        #----------------------------------------------------------------------
        hidden_widgets: tuple[QWidget] = (
            self.adsr_harmonicnum_label,
            self.adsr_harmonicnum_spin
        )
        for widget in hidden_widgets:
            widget.hide()

    def adsroption_harmonic_toggled(self) -> None:
        widgets: tuple[QWidget] = (
            self.adsr_ranknum_label,
            self.adsr_ranknum_spin,
            self.adsr_pipenum_label,
            self.adsr_pipenum_spin,
            self.adsr_harmonicnum_label,
            self.adsr_harmonicnum_spin
        )
        for widget in widgets:
            widget.show()


def main() -> None:
    app: QApplication = QApplication([])
    window: StopEditor = StopEditor()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
