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
    QButtonGroup,
    QPushButton,
    QRadioButton,
    QFormLayout,
    QHBoxLayout,
    QVBoxLayout
)
from PySide6.QtGui import Qt
from PySide6 import QtCore
#------------------------------------------------------------------------------


class StopEditor(QFrame):
    def __init__(self):
        super().__init__()
        self.__init_ui()
        self.__ui_settings()
        self.__ui_layout()
        self.harmonic_option_general.toggle()
        self.adsroption_rank.toggle()

    #--------------------------------------------------------------------------
    # Widgets
    #--------------------------------------------------------------------------
    def __init_ui(self):
        self.__init_ui_header()
        self.__init_ui_editor()
        self.__init_ui_options()

    def __init_ui_header(self):
        self.header = QHBoxLayout()
        self.header_label = QLabel("Stop:")
        self.header_edit = QLineEdit()

    def __init_ui_editor(self):
        self.editor = QTabWidget()
        self.__init_ui_editor_stopinfo()
        self.__init_ui_editor_rankinfo()
        self.__init_ui_editor_pipeinfo()
        self.__init_ui_editor_harmonicinfo()
        self.__init_ui_editor_adsrinfo()

    def __init_ui_editor_stopinfo(self):
        self.stop_settings = QFormLayout()
        # Stop Name
        self.stopname_label = QLabel("Stop Name:")
        self.stopname_combo = QComboBox()
        # Stop Family
        self.stopfamily_label = QLabel("Stop Family:")
        self.stopfamily_combo = QComboBox()
        # Organ Division
        self.organdivision_label = QLabel("Organ Division:")
        self.organdivision_combo = QComboBox()
        # Number of Ranks
        self.numranks_label = QLabel("Number of Rank:")
        self.numranks_spin = QSpinBox()
        # Rank Series
        self.rankseries_label = QLabel("Rank Series:")
        self.rankseries_combo = QComboBox()

    def __init_ui_editor_rankinfo(self):
        self.rank_settings = QFormLayout()
        # Rank #
        self.ranknum_label = QLabel("Rank #:")
        self.ranknum_spin = QSpinBox()
        # Rank Size
        self.ranksize_label = QLabel("Rank Size:")
        self.ranksize_combo = QComboBox()
        # Number of Pipes
        self.numpipes_label = QLabel("Number of Pipes:")
        self.numpipes_spin = QSpinBox()
        # Starting Note
        self.startnote_label = QLabel("Starting Note:")
        self.startnote_combo = QComboBox()
        # Pipe Type
        self.pipetype_label = QLabel("PipeType:")
        self.pipetype_combo = QComboBox()
        # Frequency Offset
        self.freqoffset_label = QLabel("Frequency Offset (Hz):")
        self.freqoffset_spin = QSpinBox()
        # Number of Harmonics
        self.numharmonics_label = QLabel("Number of Harmonics:")
        self.numharmonics_spin = QSpinBox()

    def __init_ui_editor_pipeinfo(self):
        self.pipe_settings = QFormLayout()
        # Rank #
        self.ranknum_label = QLabel("Rank #:")
        self.ranknum_spin = QSpinBox()
        # Pipe #
        self.pipenum_label = QLabel("Pipe #:")
        self.pipenum_spin = QSpinBox()        
        # Note
        self.note_label = QLabel("Note:")
        self.note_combo = QComboBox()
        # Relative Note
        self.relnote_label = QLabel("Relative Note:")
        self.relnote_combo = QComboBox()

    def __init_ui_editor_harmonicinfo(self):
        self.harmonic_settings = QVBoxLayout()
        self.__init_ui_editor_harmonicinfo_options()
        self.__init_ui_editor_harmonicinfo_form()

    def __init_ui_editor_harmonicinfo_options(self):
        self.harmonicoptions = QVBoxLayout()
        self.harmonic_options = QButtonGroup()
        self.harmonic_option_general = QRadioButton()
        self.harmonic_option_specific = QRadioButton()

    def __init_ui_editor_harmonicinfo_form(self):
        self.harmonicsettings = QGroupBox()
        # Rank #
        self.harmonic_ranknum_label = QLabel("Rank #:")
        self.harmonic_ranknum_spin = QSpinBox()
        # Pipe #
        self.harmonic_pipenum_label = QLabel("Pipe #:")
        self.harmonic_pipenum_spin = QSpinBox()
        # Harmonic #
        self.harmonicnum_label = QLabel("Harmonic #:")
        self.harmonicnum_spin = QSpinBox()
        # Amplitude
        self.amplitude_label = QLabel("Amplitude (%):")
        self.amplitude_spin = QSpinBox()

    def __init_ui_editor_adsrinfo(self):
        self.adsr_settings = QVBoxLayout()
        self.__init_ui_editor_adsrinfo_options()
        self.__init_ui_editor_adsrinfo_form()

    def __init_ui_editor_adsrinfo_options(self):
        self.adsroptions = QVBoxLayout()
        self.adsroptions_group = QButtonGroup()
        self.adsroption_rank = QRadioButton()
        self.adsroption_pipe = QRadioButton()
        self.adsroption_harmonic = QRadioButton()

    def __init_ui_editor_adsrinfo_form(self):
        self.adsrsettings = QGroupBox()
        # Rank #
        self.adsr_ranknum_label = QLabel("Rank #:")
        self.adsr_ranknum_spin = QSpinBox()
        # Pipe #
        self.adsr_pipenum_label = QLabel("Pipe #:")
        self.adsr_pipenum_spin = QSpinBox()
        # Harmonic #
        self.adsr_harmonicnum_label = QLabel("Harmonic #:")
        self.adsr_harmonicnum_spin = QSpinBox()
        # Attack
        self.attack_label = QLabel("Attack Time (ms)")
        self.attack_spin = QSpinBox()
        # Decay
        self.decay_label = QLabel("Decay Time (ms):")
        self.decay_spin = QSpinBox()
        # Sustain
        self.sustain_label = QLabel("Sustain Level (%):")
        self.sustain_spin = QSpinBox()
        # Release
        self.release_label = QLabel("Release Time (ms):")
        self.release_spin = QSpinBox()

    def __init_ui_options(self):
        self.options = QVBoxLayout()
        self.load_button = QPushButton("Load Stop")
        self.clear_button = QPushButton("Clear Changes")
        self.save_button = QPushButton("Save Stop")

    #--------------------------------------------------------------------------
    # Settings
    #--------------------------------------------------------------------------
    def __ui_settings(self):
        self.setWindowTitle("pyOrgan - Stop Editor")
        #self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.__ui_settings_header()
        self.__ui_settings_editor()
        self.__ui_settings_options()
    
    def __ui_settings_header(self):
        self.header_edit.setReadOnly(True)
        self.header_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def __ui_settings_editor(self):
        self.editor.setFixedWidth(500)
        self.__ui_settings_editor_labels()
        self.__ui_settings_editor_groupboxes()
        self.__ui_settings_editor_comboboxes()
        self.__ui_settings_editor_spinboxes()
        self.__ui_settings_editor_radiobuttons()

    def __ui_settings_editor_labels(self):
        labels = (
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

    def __ui_settings_editor_groupboxes(self):
        group_boxes =  (
            (self.harmonicsettings, "Harmonic Settings"),
            (self.adsrsettings, "ADSR Settings")
        )
        for group_box in group_boxes:
            group_box[0].setTitle(group_box[1])
            group_box[0].setAlignment(
                Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft
            )
            group_box[0].setFixedWidth(465)

    def __ui_settings_editor_comboboxes(self):
        widgets = (
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
        for widget in widgets:
            widget.setEditable(True)
            edit = widget.lineEdit()
            edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
            widget.setFixedWidth(300)
            if widget == self.stopname_combo:
                edit.setReadOnly(False)
            else:
                edit.setReadOnly(True)

    def __ui_settings_editor_spinboxes(self):
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

    def __ui_settings_editor_radiobuttons(self):
        radio_buttons = (
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
        self.harmonic_option_general.toggled.connect(
            lambda: self.harmonic_pipenum_visibility(False)
        )
        self.harmonic_option_specific.toggled.connect(
            lambda: self.harmonic_pipenum_visibility(True)
        )
        #----------------------------------------------------------------------
        self.adsroption_rank.toggled.connect(
            self.adsroption_rank_toggled
        )
        self.adsroption_pipe.toggled.connect(
            self.adsroption_pipe_toggled
        )
        self.adsroption_harmonic.toggled.connect(
            self.adsroption_harmonic_toggled
        )

    def __ui_settings_options(self):
        self.options.setAlignment(Qt.AlignmentFlag.AlignTop)

    #--------------------------------------------------------------------------
    # Layout
    #--------------------------------------------------------------------------
    def __ui_layout(self):
        self.__ui_layout_header()
        self.__ui_layout_editor()
        self.__ui_layout_options()
        self.__ui_layout_final()

    def __ui_layout_header(self):
        widgets = (
            self.header_label,
            self.header_edit
        )
        for widget in widgets:
            self.header.addWidget(widget)
        #self.header.setLayout(layout)

    def __ui_layout_editor(self):
        layouts = (
            (self.stop_settings, "Stop Settings"),
            (self.rank_settings, "Rank Settings"),
            (self.pipe_settings, "Pipe Settings"),
            (self.harmonic_settings, "Harmonic Settings"),
            (self.adsr_settings, "ADSR Settings")
        )

        for layout in layouts:
            tabwidget = QWidget()
            tabwidget.setLayout(layout[0])
            self.editor.addTab(tabwidget, layout[1])
        self.__ui_layout_editor_stopsettings()
        self.__ui_layout_editor_ranksettings()
        self.__ui_layout_editor_pipesettings()
        self.__ui_layout_editor_harmonicsettings()
        self.__ui_layout_editor_adsrsettings()

    def __ui_layout_editor_stopsettings(self):
        widgets = (
            (self.stopname_label, self.stopname_combo),
            (self.stopfamily_label, self.stopfamily_combo),
            (self.organdivision_label, self.organdivision_combo),
            (self.numranks_label, self.numranks_spin),
            (self.rankseries_label, self.rankseries_combo)
        )
        for widget in widgets:
            self.stop_settings.addRow(widget[0], widget[1])

    def __ui_layout_editor_ranksettings(self):
        widgets = (
            (self.ranknum_label, self.ranknum_spin),
            (self.ranksize_label, self.ranksize_combo),
            (self.numpipes_label, self.numpipes_spin),
            (self.pipetype_label, self.pipetype_combo),
            (self.startnote_label, self.startnote_combo),
            (self.freqoffset_label, self.freqoffset_spin),
            (self.numharmonics_label, self.numharmonics_spin)
        )
        for widget in widgets:
            self.rank_settings.addRow(widget[0], widget[1])

    def __ui_layout_editor_pipesettings(self):
        widgets = (
            (self.ranknum_label, self.ranknum_spin),
            (self.pipenum_label, self.pipenum_spin),
            (self.note_label, self.note_combo),
            (self.relnote_label, self.relnote_combo)
        )
        for widget in widgets:
            self.pipe_settings.addRow(widget[0], widget[1])

    def __ui_layout_editor_harmonicsettings(self):
        widgets = (
            self.harmonic_option_general,
            self.harmonic_option_specific
        )
        for widget in widgets:
            self.harmonicoptions.addWidget(widget)
            self.harmonic_options.addButton(widget)
        form_layout = QFormLayout()
        widgets = (
            (self.harmonic_ranknum_label, self.harmonic_ranknum_spin),
            (self.harmonic_pipenum_label, self.harmonic_pipenum_spin),
            (self.harmonicnum_label, self.harmonicnum_spin),
            (self.amplitude_label, self.amplitude_spin)
        )
        for widget in widgets:
            form_layout.addRow(widget[0], widget[1])
        self.harmonicsettings.setLayout(form_layout)
        self.harmonic_settings.addLayout(self.harmonicoptions)
        self.harmonic_settings.addWidget(self.harmonicsettings)

    def __ui_layout_editor_adsrsettings(self):
        widgets = (
            self.adsroption_rank,
            self.adsroption_pipe,
            self.adsroption_harmonic
        )
        for widget in widgets:
            self.adsroptions.addWidget(widget)
            self.adsroptions_group.addButton(widget)
        form_layout = QFormLayout()
        widgets = (
            (self.adsr_ranknum_label, self.adsr_ranknum_spin),
            (self.adsr_pipenum_label, self.adsr_pipenum_spin),
            (self.adsr_harmonicnum_label, self.adsr_harmonicnum_spin),
            (self.attack_label, self.attack_spin),
            (self.decay_label, self.decay_spin),
            (self.sustain_label, self.sustain_spin),
            (self.release_label, self.release_spin)
        )
        for widget in widgets:
            form_layout.addRow(widget[0], widget[1])
        self.adsrsettings.setLayout(form_layout)
        self.adsr_settings.addLayout(self.adsroptions)
        self.adsr_settings.addWidget(self.adsrsettings)

    def __ui_layout_options(self):
        widgets = (
            self.load_button,
            self.clear_button,
            self.save_button
        )
        for widget in widgets:
            self.options.addWidget(widget)

    def __ui_layout_final(self):
        layout_body = QHBoxLayout()
        layout_body.addWidget(self.editor)
        layout_body.addLayout(self.options)
        main_layout = QVBoxLayout()
        main_layout.addSpacing(10)
        layouts = (
            self.header,
            layout_body
        )
        for layout in layouts:
            main_layout.addLayout(layout)
            main_layout.addSpacing(10)
        self.setLayout(main_layout)

    #--------------------------------------------------------------------------
    # Actions
    #--------------------------------------------------------------------------
    def harmonic_pipenum_visibility(self, visible: bool):
        widgets = (
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

    def adsroption_rank_toggled(self):
        shown_widgets = (
            self.adsr_ranknum_label,
            self.adsr_ranknum_spin
        )
        for widget in shown_widgets:
            widget.show()
        #----------------------------------------------------------------------
        hidden_widgets = (
            self.adsr_pipenum_label,
            self.adsr_pipenum_spin,
            self.adsr_harmonicnum_label,
            self.adsr_harmonicnum_spin
        )
        for widget in hidden_widgets:
            widget.hide()

    def adsroption_pipe_toggled(self):
        shown_widgets = (
            self.adsr_ranknum_label,
            self.adsr_ranknum_spin,
            self.adsr_pipenum_label,
            self.adsr_pipenum_spin
        )
        for widget in shown_widgets:
            widget.show()
        #----------------------------------------------------------------------
        hidden_widgets = (
            self.adsr_harmonicnum_label,
            self.adsr_harmonicnum_spin
        )
        for widget in hidden_widgets:
            widget.hide()

    def adsroption_harmonic_toggled(self):
        widgets = (
            self.adsr_ranknum_label,
            self.adsr_ranknum_spin,
            self.adsr_pipenum_label,
            self.adsr_pipenum_spin,
            self.adsr_harmonicnum_label,
            self.adsr_harmonicnum_spin
        )
        for widget in widgets:
            widget.show()


def main():
    app = QApplication([])
    window = StopEditor()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
