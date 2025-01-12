from gui import MainWindow
from organ import organlib
#------------------------------------------------------------------------------
from PySide6.QtWidgets import QApplication


class UI:
    def __init__(self):
        self.__init_ui()
        self.__aliases()
        self.__config()

    def __init_ui(self):
        self.ui = QApplication([])
        self.mainwindow = MainWindow()

    def __aliases(self):
        self.__stop_info = self.mainwindow.stopeditor.editor.stop_info
        self.__rank_info = self.mainwindow.stopeditor.editor.rank_info
        self.__ri_harmonics = self.__rank_info.finetuning.harmonics_info
        self.__ri_h_adsr = self.__ri_harmonics.adsr_info
        self.__ri_adsr = self.__rank_info.finetuning.adsr_info
        __pipe_editor = self.mainwindow.stopeditor.editor.pipe_editor
        self.__pipe_info = __pipe_editor.pipe_info
        self.__pipe_harmonics = __pipe_editor.finetuning.harmonics_info
        self.__p_h_adsr = __pipe_editor.finetuning.harmonics_info.adsr_info
        self.__pipe_adsr = __pipe_editor.finetuning.adsr_info

    #**************************************************************************
    # UI Config
    #**************************************************************************
    def __config(self):
        self.__config_mainwindow_menu()
        self.__config_stopeditor()
    
    def __config_mainwindow_menu(self):
        self.mainwindow.stopeditor_action.triggered.connect(
            self.__run_stopeditor
        )

    #--------------------------------------------------------------------------
    # Stop Editor
    #--------------------------------------------------------------------------
    def __config_stopeditor(self):
        self.__config_stopeditor_stopinfo()
        self.__config_stopeditor_rankinfo()
        self.__config_stopeditor_rankinfo_harmonics()
        self.__config_stopeditor_rankinfo_adsr()
        self.__config_stopeditor_pipeinfo()
        self.__config_stopeditor_pipeharmonics()
        self.__config_stopeditor_pipeadsr()
        self.__set_numranks()
        self.__set_rankseries()
        self.__set_numpipes()
        self.__set_numharmonics()

    def __config_stopeditor_stopinfo(self):
        # Stop Name
        stop_names = ("",) + organlib.STOP_NAMES
        self.__stop_info.stopname_combo.addItems(stop_names)
        #----------------------------------------------------------------------
        # Stop Family
        stop_families = ("",) + organlib.STOP_FAMILIES
        self.__stop_info.stopfamily_combo.addItems(stop_families)
        #----------------------------------------------------------------------
        # Organ Division
        organ_divisions = ("",) + organlib.ORGAN_DIVISIONS
        self.__stop_info.organdivision_combo.addItems(organ_divisions)
        #----------------------------------------------------------------------
        # Number of Ranks
        self.__stop_info.numranks_spin.setMinimum(1)
        self.__stop_info.numranks_spin.setMaximum(10)
        self.__stop_info.numranks_spin.valueChanged.connect(
            self.__set_numranks
        )
        #----------------------------------------------------------------------
        # Rank Series
        rank_series: tuple[str] = ("",) + organlib.RANK_SERIES
        self.__stop_info.rankseries_combo.addItems(rank_series)
        self.__stop_info.rankseries_combo.currentTextChanged.connect(
            self.__set_rankseries
        )

    def __config_stopeditor_rankinfo(self):
        # Rank Number
        self.__rank_info.ranknum_spin.setMinimum(1)
        #----------------------------------------------------------------------
        # Number of Pipes
        self.__rank_info.numpipes_spin.setMinimum(1)
        self.__rank_info.numpipes_spin.setMaximum(61)
        self.__rank_info.numpipes_spin.valueChanged.connect(
            self.__set_numpipes
        )
        #----------------------------------------------------------------------
        # Starting Note
        notes: tuple[str] = organlib.NOTES
        self.__rank_info.startnote_combo.addItems(notes)
        #----------------------------------------------------------------------
        # Pipe Type
        pipe_types: tuple[str] = organlib.PIPE_TYPES
        self.__rank_info.pipetype_combo.addItems(pipe_types)
        #----------------------------------------------------------------------
        # Frequency Offset
        self.__rank_info.freqoffset_spin.setMinimum(-7)
        self.__rank_info.freqoffset_spin.setMaximum(7)
        #----------------------------------------------------------------------
        # Number of Harmonics
        self.__rank_info.numharmonics_spin.setMinimum(1)
        self.__rank_info.numharmonics_spin.setMaximum(20)
        self.__rank_info.numharmonics_spin.valueChanged.connect(
            self.__set_numharmonics
        )

    def __config_stopeditor_rankinfo_harmonics(self):
        # Harmonic Number
        self.__ri_harmonics.harmonicnum_spin.setMinimum(1)
        #----------------------------------------------------------------------
        # Amplitude
        self.__ri_harmonics.amplitude_spin.setMinimum(0)
        self.__ri_harmonics.amplitude_spin.setMaximum(100)
        #----------------------------------------------------------------------
        # Attack Time
        self.__ri_h_adsr.attack_spin.setMinimum(0)
        self.__ri_h_adsr.attack_spin.setMaximum(1000)
        #----------------------------------------------------------------------
        # Decay Time
        self.__ri_h_adsr.decay_spin.setMinimum(0)
        self.__ri_h_adsr.decay_spin.setMaximum(1000)
        #----------------------------------------------------------------------
        # Sustain Level
        self.__ri_h_adsr.sustain_spin.setMinimum(0)
        self.__ri_h_adsr.sustain_spin.setMaximum(100)
        #----------------------------------------------------------------------
        # Release Time
        self.__ri_h_adsr.release_spin.setMinimum(0)
        self.__ri_h_adsr.release_spin.setMaximum(1000)

    def __config_stopeditor_rankinfo_adsr(self):
        # Attack
        self.__ri_adsr.attack_spin.setMinimum(0)
        self.__ri_adsr.attack_spin.setMaximum(1000)
        #----------------------------------------------------------------------
        # Decay
        self.__ri_adsr.decay_spin.setMinimum(0)
        self.__ri_adsr.decay_spin.setMaximum(1000)
        #----------------------------------------------------------------------
        # Sustain
        self.__ri_adsr.sustain_spin.setMinimum(0)
        self.__ri_adsr.sustain_spin.setMaximum(100)
        #----------------------------------------------------------------------
        # Release
        self.__ri_adsr.release_spin.setMinimum(0)
        self.__ri_adsr.release_spin.setMaximum(1000)

    def __config_stopeditor_pipeinfo(self):
        widgets = (
            self.__pipe_info.ranknum_spin,
            self.__pipe_info.pipenum_spin
        )
        for widget in widgets:
            widget.setMinimum(1)
        # Note
        notes = organlib.NOTES
        widgets = (
            self.__pipe_info.note_combo,
            self.__pipe_info.relnote_combo
        )
        for widget in widgets:
            widget.addItems(notes)

    def __config_stopeditor_pipeharmonics(self):
        self.__pipe_harmonics.harmonicnum_spin.setMinimum(1)
        self.__pipe_harmonics.amplitude_spin.setMinimum(0)
        self.__p_h_adsr.attack_spin.setMinimum(0)
        self.__p_h_adsr.attack_spin.setMaximum(1000)
        self.__p_h_adsr.decay_spin.setMinimum(0)
        self.__p_h_adsr.decay_spin.setMaximum(1000)
        self.__p_h_adsr.sustain_spin.setMinimum(0)
        self.__p_h_adsr.sustain_spin.setMaximum(100)
        self.__p_h_adsr.release_spin.setMinimum(0)
        self.__p_h_adsr.release_spin.setMaximum(1000)

    def __config_stopeditor_pipeadsr(self):
        self.__pipe_adsr.attack_spin.setMinimum(0)
        self.__pipe_adsr.attack_spin.setMaximum(1000)
        self.__pipe_adsr.decay_spin.setMinimum(0)
        self.__pipe_adsr.decay_spin.setMaximum(1000)
        self.__pipe_adsr.sustain_spin.setMinimum(0)
        self.__pipe_adsr.sustain_spin.setMaximum(100)
        self.__pipe_adsr.release_spin.setMinimum(0)
        self.__pipe_adsr.release_spin.setMaximum(1000)

    #**************************************************************************
    # Actions
    #**************************************************************************
    def __run_stopeditor(self):
        self.mainwindow.stopeditor.show()

    def __set_numranks(self):
        max_ranknum: int = self.__stop_info.numranks_spin.value()
        widgets = (
            self.__rank_info.ranknum_spin,
            self.__pipe_info.ranknum_spin
        )
        for widget in widgets:
            widget.setMaximum(max_ranknum)

    def __set_rankseries(self):
        match self.__stop_info.rankseries_combo.currentText():
            case "64' Series":
                rank_series: tuple[str] = ("",) + organlib.RANK_SERIES_64
            case "32' Series":
                rank_series: tuple[str] = ("",) + organlib.RANK_SERIES_32
            case "16' Series":
                rank_series: tuple[str] = ("",) + organlib.RANK_SERIES_16
            case "8' Series":
                rank_series: tuple[str] = ("",) + organlib.RANK_SERIES_8
            case "4' Series":
                rank_series: tuple[str] = ("",) + organlib.RANK_SERIES_4
            case "":
                rank_series: tuple[str] = ("",) + organlib.RANK_SIZES
        self.__rank_info.ranksize_combo.addItems(rank_series)

    def __set_numharmonics(self):
        max_harmonics: int = self.__rank_info.numharmonics_spin.value()
        widgets = (
            self.__ri_harmonics.harmonicnum_spin,
            self.__pipe_harmonics.harmonicnum_spin
        )
        for widget in widgets:
            widget.setMaximum(max_harmonics)

    def __set_numpipes(self):
        max_pipes: int = self.__rank_info.numpipes_spin.value()
        self.__pipe_info.pipenum_spin.setMaximum(max_pipes)

    #**************************************************************************
    def run(self):
        self.ui.exec()


if __name__ == "__main__":
    ui = UI()
    ui.run()
