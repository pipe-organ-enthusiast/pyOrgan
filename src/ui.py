from gui import StopEditor
from organ import organlib
from config_editors import StopConfig
import log_file
#------------------------------------------------------------------------------
from PySide6.QtWidgets import QApplication, QFileDialog
from icecream import ic  # type: ignore
#------------------------------------------------------------------------------
#from typing import Callable


#******************************************************************************
# Stop Editor
#******************************************************************************
class StopEditorUI:
    def __init__(self) -> None:
        ic("Initializing Stop Editor UI...")
        self.stop_editor: StopEditor = StopEditor()
        self.stop_config: StopConfig = StopConfig()
        self.config_file: str = ""
        self.__init_ui()
        self.__default_ui_editor_data()
        ic("Stop Editor UI Initialized.")

    #**************************************************************************
    # Configuration
    #**************************************************************************
    #==========================================================================
    # Default Data
    #==========================================================================
    def __default_ui_editor_data(self) -> None:
        ic("Loading Default UI Editor Data...")
        self.__init_setting_numbers()
        self.stop_config.init_default_config()
        self.__load_ui_editor_data()
        self.__update_number_ranks()
        self.__update_number_pipes()
        self.__update_number_harmonics()
        ic("Default UI Editor Data Loaded.")

    def __init_setting_numbers(self) -> None:
        ic("Initializing Setting Numbers...")
        self.rank_number_editor = 1
        self.harmonic_number_rank_editor = 1
        self.rank_number_pipe_editor = 1
        self.pipe_number_editor = 1
        self.harmonic_number_pipe_editor = 1
        ic("Setting Numbers Initialized.")

    def __load_ui_editor_data(self) -> None:
        ic("Loading UI Editor Data...")
        self.stop_name_editor = self.stop_name_config
        self.stop_family_editor = self.stop_family_config
        self.organ_division_editor = self.organ_division_config
        self.number_ranks_editor = self.number_ranks_config
        self.rank_series_editor = self.rank_series_config
        self.rank_size_editor = self.rank_size_config
        self.number_pipes_editor = self.number_pipes_config
        self.pipe_type_editor = self.pipe_type_config
        self.starting_note_editor = self.starting_note_config
        self.frequency_offset_editor = self.frequency_offset_config
        self.number_harmonics_editor = self.number_harmonics_config
        self.amplitude_rank_editor = self.amplitude_rank_config
        self.attack_harmonic_rank_editor = self.attack_harmonic_rank_config
        self.decay_harmonic_rank_editor = self.decay_harmonic_rank_config
        self.sustain_harmonic_rank_editor = self.sustain_harmonic_rank_config
        self.release_harmonic_rank_editor = self.release_harmonic_rank_config
        self.attack_rank_editor = self.attack_rank_config
        self.decay_rank_editor = self.decay_rank_config
        self.sustain_rank_editor = self.sustain_rank_config
        self.release_rank_editor = self.release_rank_config
        self.note_editor = self.note_config
        self.relative_note_editor = self.relative_note_config
        self.amplitude_pipe_editor = self.amplitude_pipe_config
        self.attack_harmonic_pipe_editor = self.attack_harmonic_pipe_config
        self.decay_harmonic_pipe_editor = self.decay_harmonic_pipe_config
        self.sustain_harmonic_pipe_editor = self.sustain_harmonic_pipe_config
        self.release_harmonic_pipe_editor = self.release_harmonic_pipe_config
        self.attack_pipe_editor = self.attack_pipe_config
        self.decay_pipe_editor = self.decay_pipe_config
        self.sustain_pipe_editor = self.sustain_pipe_config
        self.release_pipe_editor = self.release_pipe_config
        ic("UI Editor Data Loaded.")

    #==========================================================================
    # Initialize UI Configuration
    #==========================================================================
    def __init_ui(self) -> None:
        ic("Initializing UI...")
        self.stop_editor.stop_name_change_connect(self.__update_stop_name)
        self.stop_editor.stop_family_change_connect(self.__update_stop_family)
        self.stop_editor.organ_division_change_connect(self.__update_organ_division)
        self.stop_editor.number_ranks_change_connect(self.__update_number_ranks)
        self.stop_editor.rank_series_change_connect(self.__update_rank_series)
        self.stop_editor.rank_number_change_connect(self.__update_rank_number)
        self.stop_editor.rank_size_change(self.__update_rank_size)
        self.stop_editor.number_pipes_change(self.__update_number_pipes)
        self.stop_editor.pipe_type_change(self.__update_pipe_type)
        self.stop_editor.starting_note_change(self.__update_starting_note)
        self.stop_editor.frequency_offset_change(self.__update_frequency_offset)
        self.stop_editor.number_harmonics_change(self.__update_number_harmonics)
        self.stop_editor.harmonic_number_rank_change(self.__update_harmonic_number_rank)
        self.stop_editor.amplitude_rank_change(self.__update_rank_amplitude)
        self.stop_editor.attack_time_rank_harmonic_change(self.__update_rank_harmonic_attack)
        self.stop_editor.decay_time_rank_harmonic_change(self.__update_rank_harmonic_decay)
        self.stop_editor.sustain_level_rank_harmonic_change(self.__update_rank_harmonic_sustain)
        self.stop_editor.release_time_rank_harmonic_change(self.__update_rank_harmonic_release)
        self.stop_editor.attack_time_rank_change(self.__update_rank_attack)
        self.stop_editor.decay_time_rank_change(self.__update_rank_decay)
        self.stop_editor.sustain_level_rank_change(self.__update_rank_sustain)
        self.stop_editor.release_time_rank_change(self.__update_rank_release)
        self.stop_editor.rank_number_pipe_change(self.__update_rank_number_pipe)
        self.stop_editor.pipe_number_change(self.__update_pipe_number)
        self.stop_editor.note_change(self.__update_note)
        self.stop_editor.relative_note_change(self.__update_relative_note)
        self.stop_editor.harmonic_number_pipe_change(self.__update_harmonic_number_pipe)
        self.stop_editor.amplitude_pipe_change(self.__update_pipe_amplitude)
        self.stop_editor.attack_time_pipe_harmonic_change(self.__update_pipe_harmonic_attack)
        self.stop_editor.decay_time_pipe_harmonic_change(self.__update_pipe_harmonic_decay)
        self.stop_editor.sustain_level_pipe_harmonic_change(self.__update_pipe_harmonic_sustain)
        self.stop_editor.release_time_pipe_harmonic_change(self.__update_pipe_harmonic_release)
        self.stop_editor.attack_time_pipe_change(self.__update_pipe_attack)
        self.stop_editor.decay_time_pipe_change(self.__update_pipe_decay)
        self.stop_editor.sustain_level_pipe_change(self.__update_pipe_sustain)
        self.stop_editor.release_time_pipe_change(self.__update_pipe_release)
        self.stop_editor.load_stop_action(self.__load_stop)
        self.stop_editor.cancel_changes_action(self.__cancel_changes)
        self.stop_editor.save_stop_action(self.__save_stop)
        ic("UI Initialized.")

    #**************************************************************************
    # Actions
    #**************************************************************************
#    def __set_maximum_number(
#            self,
#            number: int,
#            *methods: Callable[[int], None]
#    ) -> None:
#        ic()
#        for method in methods:
#            method(number)

    def __update_stop_name(self) -> None:
        ic()
        self.stop_editor.update_stop_header()
        self.stop_name_config = self.stop_name_editor

    def __update_stop_family(self) -> None:
        ic()
        self.stop_family_config = self.stop_family_editor

    def __update_organ_division(self) -> None:
        ic()
        self.organ_division_config = self.organ_division_editor

    def __update_number_ranks(self) -> None:
        ic()
        self.number_ranks_config = self.number_ranks_editor
        self.stop_editor.update_number_ranks()
        self.stop_editor.update_stop_header()

    def __update_rank_series(self) -> None:
        #TODO: Transfer to gui/stop_editor.py
        ic()
        rank_sizes: tuple[str, ...] = ("",)
        match self.rank_series_editor:
            case "64' Series":
                rank_sizes += organlib.RANK_SERIES_64
            case "32' Series":
                rank_sizes += organlib.RANK_SERIES_32
            case "16' Series":
                rank_sizes += organlib.RANK_SERIES_16
            case "8' Series":
                rank_sizes += organlib.RANK_SERIES_8
            case "4' Series":
                rank_sizes += organlib.RANK_SERIES_4
            case _:
                rank_sizes += organlib.RANK_SIZES
        self.stop_editor.rank_size_populate(rank_sizes)
        #-------------------------------------------------------------------------------------------
        self.rank_series_config = self.rank_series_editor

    def __update_rank_number_general(self) -> None:
        ic()
        self.rank_size_editor = self.rank_size_config
        self.number_pipes_editor = self.number_pipes_config
        self.pipe_type_editor = self.pipe_type_config
        self.starting_note_editor = self.starting_note_config
        self.frequency_offset_editor = self.frequency_offset_config
        self.number_harmonics_editor = self.number_harmonics_config
        self.harmonic_number_rank_editor = 1
        self.__update_harmonic_number()
        self.attack_rank_editor = self.attack_rank_config
        self.decay_rank_editor = self.decay_rank_config
        self.sustain_rank_editor = self.sustain_rank_config
        self.release_rank_editor = self.release_rank_config
        self.pipe_number_editor = 1
        self.__update_pipe_number()

    def __update_rank_number(self) -> None:
        #TODO: Transfer to gui/stop_editor.py
        ic()
        self.rank_number_pipe_editor = self.rank_number_editor
        #-------------------------------------------------------------------------------------------
        self.__update_rank_number_general()

    def __update_rank_size(self) -> None:
        ic()
        self.rank_size_config = self.rank_size_editor

    def __update_number_pipes(self) -> None:
        #TODO: Transfer to gui/stop_editor.py
        ic()
        # Set Maximum Pipe Number
        self.__set_maximum_number(
            self.number_pipes_editor,
            self.stop_editor.pipe_number_set_maximum,
        )
        #-------------------------------------------------------------------------------------------
        self.number_pipes_config = self.number_pipes_editor

    def __update_pipe_type(self) -> None:
        ic()
        self.pipe_type_config = self.pipe_type_editor

    def __update_starting_note(self) -> None:
        ic()
        self.starting_note_config = self.starting_note_editor

    def __update_frequency_offset(self) -> None:
        ic()
        self.frequency_offset_config = self.frequency_offset_editor

    def __update_number_harmonics(self) -> None:
        #TODO: Transfer to gui/stop_editor.py
        ic()
        # Set Maximum Harmonic Number
        self.__set_maximum_number(
            self.number_harmonics_editor,
            self.stop_editor.harmonic_number_rank_set_maximum,
            self.stop_editor.harmonic_number_pipe_set_maximum
        )
        #-------------------------------------------------------------------------------------------
        self.number_harmonics_config = self.number_harmonics_editor

    def __update_harmonic_number(self) -> None:
        ic()
        self.amplitude_rank_editor = self.amplitude_rank_config
        self.attack_harmonic_rank_editor = self.attack_harmonic_rank_config
        self.decay_harmonic_rank_editor = self.decay_harmonic_rank_config
        self.sustain_harmonic_rank_editor = self.sustain_harmonic_rank_config
        self.release_harmonic_rank_editor = self.release_harmonic_rank_config
        self.harmonic_number_pipe_editor = self.harmonic_number_rank_editor  # Deprecate
        self.amplitude_pipe_editor = self.amplitude_pipe_config
        self.attack_harmonic_pipe_editor = self.attack_harmonic_pipe_config
        self.decay_harmonic_pipe_editor = self.decay_harmonic_pipe_config
        self.sustain_harmonic_pipe_editor = self.sustain_harmonic_pipe_config
        self.release_harmonic_pipe_editor = self.release_harmonic_pipe_config
        self.harmonic_number_rank_editor = self.harmonic_number_pipe_editor  # Deprecate

    def __update_harmonic_number_rank(self) -> None:
        ic()
        self.harmonic_number_pipe_editor = self.harmonic_number_rank_editor
        #TODO: Transfer to gui/stop_editor.py
        self.__update_harmonic_number()

    def __update_rank_amplitude(self) -> None:
        ic()
        self.amplitude_rank_config = self.amplitude_rank_editor

    def __update_rank_harmonic_attack(self) -> None:
        ic()
        self.attack_harmonic_rank_config = self.attack_harmonic_rank_editor

    def __update_rank_harmonic_decay(self) -> None:
        ic()
        self.decay_harmonic_rank_config = self.decay_harmonic_rank_editor

    def __update_rank_harmonic_sustain(self) -> None:
        ic()
        self.sustain_harmonic_rank_config = self.sustain_harmonic_rank_editor

    def __update_rank_harmonic_release(self) -> None:
        ic()
        self.release_harmonic_rank_config = self.release_harmonic_rank_editor

    def __update_rank_attack(self) -> None:
        ic()
        self.attack_rank_config = self.attack_rank_editor

    def __update_rank_decay(self) -> None:
        ic()
        self.decay_rank_config = self.decay_rank_editor

    def __update_rank_sustain(self) -> None:
        ic()
        self.sustain_rank_config = self.sustain_rank_editor

    def __update_rank_release(self) -> None:
        ic()
        self.release_rank_config = self.release_rank_editor

    def __update_rank_number_pipe(self) -> None:
        #TODO: Transfer to gui/stop_editor.py
        ic()
        self.rank_number_editor = self.rank_number_pipe_editor
        #-------------------------------------------------------------------------------------------
        self.__update_rank_number_general()

    def __update_pipe_number(self) -> None:
        ic()
        ic(self.note_config)
        ic(self.relative_note_config)
        self.note_editor = self.note_config
        ic(self.note_editor)
        self.relative_note_editor = self.relative_note_config
        ic(self.relative_note_editor)
        self.harmonic_number_pipe_editor = 1
        self.__update_harmonic_number()
        self.attack_pipe_editor = self.attack_pipe_config
        self.decay_pipe_editor = self.decay_pipe_config
        self.sustain_pipe_editor = self.sustain_pipe_config
        self.release_pipe_editor = self.release_pipe_config

    def __update_note(self) -> None:
        ic()
        self.note_config = self.note_editor

    def __update_relative_note(self) -> None:
        #TODO: Transfer to gui/stop_editor.py
        ic()
        note_index = organlib.NOTES.index(self.relative_note_editor)
        notes: tuple[str, ...] = organlib.NOTES[note_index:]
        self.stop_config.update_relative_notes(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            notes=notes
        )

    def __update_harmonic_number_pipe(self) -> None:
        #TODO: Transfer to gui/stop_editor.py
        ic()
        self.harmonic_number_rank_editor = self.harmonic_number_pipe_editor
        #-------------------------------------------------------------------------------------------
        self.__update_harmonic_number()

    def __update_pipe_amplitude(self) -> None:
        ic()
        self.amplitude_pipe_config = self.amplitude_pipe_editor

    def __update_pipe_attack(self) -> None:
        ic()
        self.attack_pipe_config = self.attack_pipe_editor

    def __update_pipe_decay(self) -> None:
        ic()
        self.decay_pipe_config = self.decay_pipe_editor

    def __update_pipe_sustain(self) -> None:
        ic()
        self.sustain_pipe_config = self.sustain_pipe_editor

    def __update_pipe_release(self) -> None:
        ic()
        self.release_pipe_config = self.release_pipe_editor

    def __update_pipe_harmonic_attack(self) -> None:
        ic()
        self.attack_harmonic_pipe_config = self.attack_harmonic_pipe_editor

    def __update_pipe_harmonic_decay(self) -> None:
        ic()
        self.decay_harmonic_pipe_config = self.decay_harmonic_pipe_editor

    def __update_pipe_harmonic_sustain(self) -> None:
        ic()
        self.sustain_harmonic_pipe_config = self.sustain_harmonic_pipe_editor

    def __update_pipe_harmonic_release(self) -> None:
        ic()
        self.release_harmonic_pipe_config = self.release_harmonic_pipe_editor

    def __load_config(self) -> None:
        ic()
        self.stop_config.load_file(self.config_file)
        self.__init_setting_numbers()
        self.__load_ui_editor_data()

    def __load_stop(self) -> None:
        ic()
        file_dialog: QFileDialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("JSON Files (*.json)")
        file_dialog.setViewMode(QFileDialog.ViewMode.Detail)
        file_dialog.setDirectory("src/config/stops")
        self.config_file = file_dialog.getOpenFileName()[0]
        self.__load_config()

    def __cancel_changes(self) -> None:
        ic()
        if self.config_file == "":
            self.__default_ui_editor_data()
        else:
            self.__load_config()

    def __save_stop(self) -> None:
        ic()
        stop_header: str = self.stop_header_editor
        if stop_header != "":
            self.config_file = f"src/config/stops/{stop_header}.json"
            self.stop_config.save_file(self.config_file)

    #**************************************************************************
    # Properties
    #**************************************************************************
    #==========================================================================
    # Stop Editor
    #==========================================================================
    @property
    def stop_header_editor(self) -> str:
        ic()
        return self.stop_editor.stop_header

    #--------------------------------------------------------------------------
    # Stop Name
    #--------------------------------------------------------------------------
    @property
    def stop_name_editor(self) -> str:
        ic()
        return self.stop_editor.stop_name

    @stop_name_editor.setter
    def stop_name_editor(self, value: str) -> None:
        ic()
        self.stop_editor.stop_name = value

    #--------------------------------------------------------------------------
    # Stop Family
    #--------------------------------------------------------------------------
    @property
    def stop_family_editor(self) -> str:
        ic()
        return self.stop_editor.stop_family

    @stop_family_editor.setter
    def stop_family_editor(self, value: str) -> None:
        ic()
        self.stop_editor.stop_family = value

    #--------------------------------------------------------------------------
    # Organ Division
    #--------------------------------------------------------------------------
    @property
    def organ_division_editor(self) -> str:
        ic()
        return self.stop_editor.organ_division

    @organ_division_editor.setter
    def organ_division_editor(self, value: str) -> None:
        ic()
        self.stop_editor.organ_division = value

    #--------------------------------------------------------------------------
    # Number of Ranks
    #--------------------------------------------------------------------------
    @property
    def number_ranks_editor(self) -> int:
        ic()
        return self.stop_editor.number_ranks

    @number_ranks_editor.setter
    def number_ranks_editor(self, value: int) -> None:
        ic()
        self.stop_editor.number_ranks = value

    #--------------------------------------------------------------------------
    # Rank Series
    #--------------------------------------------------------------------------
    @property
    def rank_series_editor(self) -> str:
        ic()
        return self.stop_editor.rank_series

    @rank_series_editor.setter
    def rank_series_editor(self, value: str) -> None:
        ic()
        self.stop_editor.rank_series = value

    #--------------------------------------------------------------------------
    # Rank Number
    #--------------------------------------------------------------------------
    @property
    def rank_number_editor(self) -> int:
        ic()
        return self.stop_editor.rank_number

    @rank_number_editor.setter
    def rank_number_editor(self, value: int) -> None:
        ic()
        self.stop_editor.rank_number = value

    #--------------------------------------------------------------------------
    # Rank Size
    #--------------------------------------------------------------------------
    @property
    def rank_size_editor(self) -> str:
        ic()
        return self.stop_editor.rank_size

    @rank_size_editor.setter
    def rank_size_editor(self, value: str) -> None:
        ic()
        self.stop_editor.rank_size = value

    #--------------------------------------------------------------------------
    # Number of Pipes
    #--------------------------------------------------------------------------
    @property
    def number_pipes_editor(self) -> int:
        ic()
        return self.stop_editor.number_pipes

    @number_pipes_editor.setter
    def number_pipes_editor(self, value: int) -> None:
        ic()
        self.stop_editor.number_pipes = value

    #--------------------------------------------------------------------------
    # Pipe Type
    #--------------------------------------------------------------------------
    @property
    def pipe_type_editor(self) -> str:
        ic()
        return self.stop_editor.pipe_type

    @pipe_type_editor.setter
    def pipe_type_editor(self, value: str) -> None:
        ic()
        self.stop_editor.pipe_type = value

    #--------------------------------------------------------------------------
    # Starting Note
    #--------------------------------------------------------------------------
    @property
    def starting_note_editor(self) -> str:
        ic()
        return self.stop_editor.starting_note

    @starting_note_editor.setter
    def starting_note_editor(self, value: str) -> None:
        ic()
        self.stop_editor.starting_note = value

    #--------------------------------------------------------------------------
    # Frequency Offset
    #--------------------------------------------------------------------------
    @property
    def frequency_offset_editor(self) -> int:
        ic()
        return self.stop_editor.frequency_offset

    @frequency_offset_editor.setter
    def frequency_offset_editor(self, value: int) -> None:
        ic()
        self.stop_editor.frequency_offset = value

    #--------------------------------------------------------------------------
    # Number of Harmonics
    #--------------------------------------------------------------------------
    @property
    def number_harmonics_editor(self) -> int:
        ic()
        return self.stop_editor.number_harmonics

    @number_harmonics_editor.setter
    def number_harmonics_editor(self, value: int) -> None:
        ic()
        self.stop_editor.number_harmonics = value

    #--------------------------------------------------------------------------
    # Harmonic Number - Rank
    #--------------------------------------------------------------------------
    @property
    def harmonic_number_rank_editor(self) -> int:
        ic()
        return self.stop_editor.harmonic_number_rank

    @harmonic_number_rank_editor.setter
    def harmonic_number_rank_editor(self, value: int) -> None:
        ic()
        self.stop_editor.harmonic_number_rank = value

    #--------------------------------------------------------------------------
    # Amplitude - Rank
    #--------------------------------------------------------------------------
    @property
    def amplitude_rank_editor(self) -> int:
        ic()
        return self.stop_editor.amplitude_rank

    @amplitude_rank_editor.setter
    def amplitude_rank_editor(self, value: int) -> None:
        ic()
        self.stop_editor.amplitude_rank = value

    #--------------------------------------------------------------------------
    # Attack Time - Harmonic - Rank
    #--------------------------------------------------------------------------
    @property
    def attack_harmonic_rank_editor(self) -> int:
        ic()
        return self.stop_editor.attack_time_harmonic_rank

    @attack_harmonic_rank_editor.setter
    def attack_harmonic_rank_editor(self, value: int) -> None:
        ic()
        self.stop_editor.attack_time_harmonic_rank = value

    #--------------------------------------------------------------------------
    # Decay Time - Harmonic - Rank
    #--------------------------------------------------------------------------
    @property
    def decay_harmonic_rank_editor(self) -> int:
        ic()
        return self.stop_editor.decay_time_harmonic_rank

    @decay_harmonic_rank_editor.setter
    def decay_harmonic_rank_editor(self, value: int) -> None:
        ic()
        self.stop_editor.decay_time_harmonic_rank = value

    #--------------------------------------------------------------------------
    # Sustain Level - Harmonic - Rank
    #--------------------------------------------------------------------------
    @property
    def sustain_harmonic_rank_editor(self) -> int:
        ic()
        return self.stop_editor.sustain_level_harmonic_rank

    @sustain_harmonic_rank_editor.setter
    def sustain_harmonic_rank_editor(self, value: int) -> None:
        ic()
        self.stop_editor.sustain_level_harmonic_rank = value

    #--------------------------------------------------------------------------
    # Release Time - Harmonic - Rank
    #--------------------------------------------------------------------------
    @property
    def release_harmonic_rank_editor(self) -> int:
        ic()
        return self.stop_editor.release_time_harmonic_rank

    @release_harmonic_rank_editor.setter
    def release_harmonic_rank_editor(self, value: int) -> None:
        ic()
        self.stop_editor.release_time_harmonic_rank = value

    #--------------------------------------------------------------------------
    # Attack Time - Rank
    #--------------------------------------------------------------------------
    @property
    def attack_rank_editor(self) -> int:
        ic()
        return self.stop_editor.attack_time_rank

    @attack_rank_editor.setter
    def attack_rank_editor(self, value: int) -> None:
        ic()
        self.stop_editor.attack_time_rank = value

    #--------------------------------------------------------------------------
    # Decay Time - Rank
    #--------------------------------------------------------------------------
    @property
    def decay_rank_editor(self) -> int:
        ic()
        return self.stop_editor.decay_time_rank

    @decay_rank_editor.setter
    def decay_rank_editor(self, value: int) -> None:
        ic()
        self.stop_editor.decay_time_rank = value

    #--------------------------------------------------------------------------
    # Sustain Level - Rank
    #--------------------------------------------------------------------------
    @property
    def sustain_rank_editor(self) -> int:
        ic()
        return self.stop_editor.sustain_level_rank

    @sustain_rank_editor.setter
    def sustain_rank_editor(self, value: int) -> None:
        ic()
        self.stop_editor.sustain_level_rank = value

    #--------------------------------------------------------------------------
    # Release Time - Rank
    #--------------------------------------------------------------------------
    @property
    def release_rank_editor(self) -> int:
        ic()
        return self.stop_editor.release_time_rank

    @release_rank_editor.setter
    def release_rank_editor(self, value: int) -> None:
        ic()
        self.stop_editor.release_time_rank = value

    #--------------------------------------------------------------------------
    # Rank Number - Pipe
    #--------------------------------------------------------------------------
    @property
    def rank_number_pipe_editor(self) -> int:
        ic()
        return self.stop_editor.rank_number_pipe

    @rank_number_pipe_editor.setter
    def rank_number_pipe_editor(self, value: int) -> None:
        ic()
        self.stop_editor.rank_number_pipe = value

    #--------------------------------------------------------------------------
    # Pipe Number
    #--------------------------------------------------------------------------
    @property
    def pipe_number_editor(self) -> int:
        ic()
        return self.stop_editor.pipe_number

    @pipe_number_editor.setter
    def pipe_number_editor(self, value: int) -> None:
        ic()
        self.stop_editor.pipe_number = value

    #--------------------------------------------------------------------------
    # Note
    #--------------------------------------------------------------------------
    @property
    def note_editor(self) -> str:
        ic()
        return self.stop_editor.note

    @note_editor.setter
    def note_editor(self, value: str) -> None:
        ic()
        self.stop_editor.note = value

    #--------------------------------------------------------------------------
    # Relative Note
    #--------------------------------------------------------------------------
    @property
    def relative_note_editor(self) -> str:
        ic()
        return self.stop_editor.relative_note

    @relative_note_editor.setter
    def relative_note_editor(self, value: str) -> None:
        ic()
        self.stop_editor.relative_note = value

    #--------------------------------------------------------------------------
    # Harmonic Number - Pipe
    #--------------------------------------------------------------------------
    @property
    def harmonic_number_pipe_editor(self) -> int:
        ic()
        return self.stop_editor.harmonic_number_pipe

    @harmonic_number_pipe_editor.setter
    def harmonic_number_pipe_editor(self, value: int) -> None:
        ic()
        self.stop_editor.harmonic_number_pipe = value

    #--------------------------------------------------------------------------
    # Amplitude - Pipe
    #--------------------------------------------------------------------------
    @property
    def amplitude_pipe_editor(self) -> int:
        ic()
        return self.stop_editor.amplitude_pipe

    @amplitude_pipe_editor.setter
    def amplitude_pipe_editor(self, value: int) -> None:
        ic()
        self.stop_editor.amplitude_pipe = value

    #--------------------------------------------------------------------------
    # Attack Time - Harmonic - Pipe
    #--------------------------------------------------------------------------
    @property
    def attack_harmonic_pipe_editor(self) -> int:
        ic()
        return self.stop_editor.attack_time_harmonic_pipe

    @attack_harmonic_pipe_editor.setter
    def attack_harmonic_pipe_editor(self, value: int) -> None:
        ic()
        self.stop_editor.attack_time_harmonic_pipe = value

    #--------------------------------------------------------------------------
    # Decay Time - Harmonic - Pipe
    #--------------------------------------------------------------------------
    @property
    def decay_harmonic_pipe_editor(self) -> int:
        ic()
        return self.stop_editor.decay_time_harmonic_pipe

    @decay_harmonic_pipe_editor.setter
    def decay_harmonic_pipe_editor(self, value: int) -> None:
        ic()
        self.stop_editor.decay_time_harmonic_pipe = value

    #--------------------------------------------------------------------------
    # Sustain Level - Harmonic - Pipe
    #--------------------------------------------------------------------------
    @property
    def sustain_harmonic_pipe_editor(self) -> int:
        ic()
        return self.stop_editor.sustain_level_harmonic_pipe

    @sustain_harmonic_pipe_editor.setter
    def sustain_harmonic_pipe_editor(self, value: int) -> None:
        ic()
        self.stop_editor.sustain_level_harmonic_pipe = value

    #--------------------------------------------------------------------------
    # Release Time - Harmonic - Pipe
    #--------------------------------------------------------------------------
    @property
    def release_harmonic_pipe_editor(self) -> int:
        ic()
        return self.stop_editor.release_time_harmonic_pipe

    @release_harmonic_pipe_editor.setter
    def release_harmonic_pipe_editor(self, value: int) -> None:
        ic()
        self.stop_editor.release_time_harmonic_pipe = value

    #--------------------------------------------------------------------------
    # Attack Time - Pipe
    #--------------------------------------------------------------------------
    @property
    def attack_pipe_editor(self) -> int:
        ic()
        return self.stop_editor.attack_time_pipe

    @attack_pipe_editor.setter
    def attack_pipe_editor(self, value: int) -> None:
        ic()
        self.stop_editor.attack_time_pipe = value

    #--------------------------------------------------------------------------
    # Decay Time - Pipe
    #--------------------------------------------------------------------------
    @property
    def decay_pipe_editor(self) -> int:
        ic()
        return self.stop_editor.decay_time_pipe

    @decay_pipe_editor.setter
    def decay_pipe_editor(self, value: int) -> None:
        ic()
        self.stop_editor.decay_time_pipe = value

    #--------------------------------------------------------------------------
    # Sustain Level - Pipe
    #--------------------------------------------------------------------------
    @property
    def sustain_pipe_editor(self) -> int:
        ic()
        return self.stop_editor.sustain_level_pipe

    @sustain_pipe_editor.setter
    def sustain_pipe_editor(self, value: int) -> None:
        ic()
        self.stop_editor.sustain_level_pipe = value

    #--------------------------------------------------------------------------
    # Release Time - Pipe
    #--------------------------------------------------------------------------
    @property
    def release_pipe_editor(self) -> int:
        ic()
        return self.stop_editor.release_time_pipe

    @release_pipe_editor.setter
    def release_pipe_editor(self, value: int) -> None:
        ic()
        self.stop_editor.release_time_pipe = value

    #==========================================================================
    # Stop Config
    #==========================================================================
    #--------------------------------------------------------------------------
    # Stop Name
    #--------------------------------------------------------------------------
    @property
    def stop_name_config(self) -> str:
        ic()
        return self.stop_config.stop_name_get()

    @stop_name_config.setter
    def stop_name_config(self, value: str):
        ic()
        self.stop_config.stop_name_set(value)

    #--------------------------------------------------------------------------
    # Stop Family
    #--------------------------------------------------------------------------
    @property
    def stop_family_config(self) -> str:
        ic()
        return self.stop_config.stop_family_get()

    @stop_family_config.setter
    def stop_family_config(self, value: str):
        ic()
        self.stop_config.stop_family_set(value)

    #--------------------------------------------------------------------------
    # Organ Division
    #--------------------------------------------------------------------------
    @property
    def organ_division_config(self) -> str:
        ic()
        return self.stop_config.organ_division_get()

    @organ_division_config.setter
    def organ_division_config(self, value: str):
        ic()
        self.stop_config.organ_division_set(value)

    #--------------------------------------------------------------------------
    # Number of Ranks
    #--------------------------------------------------------------------------
    @property
    def number_ranks_config(self) -> int:
        ic()
        return self.stop_config.number_ranks_get()

    @number_ranks_config.setter
    def number_ranks_config(self, value: int):
        ic()
        self.stop_config.number_ranks_set(value)

    #--------------------------------------------------------------------------
    # Rank Series
    #--------------------------------------------------------------------------
    @property
    def rank_series_config(self) -> str:
        ic()
        return self.stop_config.rank_series_get()

    @rank_series_config.setter
    def rank_series_config(self, value: str):
        ic()
        self.stop_config.rank_series_set(value)

    #--------------------------------------------------------------------------
    # Rank Size
    #--------------------------------------------------------------------------
    @property
    def rank_size_config(self) -> str:
        ic()
        return self.stop_config.rank_size_get(
            rank_number=self.rank_number_editor
        )

    @rank_size_config.setter
    def rank_size_config(self, value: str):
        ic()
        self.stop_config.rank_size_set(
            rank_number=self.rank_number_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Number of Pipes
    #--------------------------------------------------------------------------
    @property
    def number_pipes_config(self) -> int:
        ic()
        return self.stop_config.number_pipes_get(
            rank_number=self.rank_number_editor
        )

    @number_pipes_config.setter
    def number_pipes_config(self, value: int):
        ic()
        self.stop_config.number_pipes_set(
            rank_number=self.rank_number_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Pipe Type
    #--------------------------------------------------------------------------
    @property
    def pipe_type_config(self) -> str:
        ic()
        return self.stop_config.pipe_type_get(
            rank_number=self.rank_number_editor,
        )

    @pipe_type_config.setter
    def pipe_type_config(self, value: str):
        ic()
        self.stop_config.pipe_type_set(
            rank_number=self.rank_number_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Starting Note
    #--------------------------------------------------------------------------
    @property
    def starting_note_config(self) -> str:
        ic()
        return self.stop_config.starting_note_get(
            rank_number=self.rank_number_editor
        )

    @starting_note_config.setter
    def starting_note_config(self, value: str):
        ic()
        notes: tuple[str, ...] = organlib.NOTES
        ic(notes)
        starting_note_index: int = notes.index(value)
        ic(starting_note_index)
        revised_notes: tuple[str, ...] = tuple(
            [note for note in notes[starting_note_index:]]
        )
        self.stop_config.starting_note_set(
            rank_number=self.rank_number_editor,
            starting_note=value,
            values=revised_notes
        )

    #--------------------------------------------------------------------------
    # Frequency Offset
    #--------------------------------------------------------------------------
    @property
    def frequency_offset_config(self) -> int:
        ic()
        return self.stop_config.frequency_offset_get(
            rank_number=self.rank_number_editor
        )

    @frequency_offset_config.setter
    def frequency_offset_config(self, value: int):
        ic()
        self.stop_config.frequency_offset_set(
            rank_number=self.rank_number_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Number of Harmonics
    #--------------------------------------------------------------------------
    @property
    def number_harmonics_config(self) -> int:
        ic()
        return self.stop_config.number_harmonics_get(
            rank_number=self.rank_number_editor
        )

    @number_harmonics_config.setter
    def number_harmonics_config(self, value: int):
        ic()
        self.stop_config.number_harmonics_set(
            rank_number=self.rank_number_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Amplitude - Rank
    #--------------------------------------------------------------------------
    @property
    def amplitude_rank_config(self) -> int:
        ic()
        return self.stop_config.rank_harmonic_amplitude_get(
            rank_number=self.rank_number_editor,
            harmonic_number=self.harmonic_number_rank_editor
        )

    @amplitude_rank_config.setter
    def amplitude_rank_config(self, value: int):
        ic()
        self.stop_config.rank_harmonic_amplitude_set(
            rank_number=self.rank_number_editor,
            harmonic_number=self.harmonic_number_rank_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Attack Time - Harmonic - Rank
    #--------------------------------------------------------------------------
    @property
    def attack_harmonic_rank_config(self) -> int:
        ic()
        return self.stop_config.rank_harmonic_attack_time_get(
            rank_number=self.rank_number_editor,
            harmonic_number=self.harmonic_number_rank_editor
        )

    @attack_harmonic_rank_config.setter
    def attack_harmonic_rank_config(self, value: int):
        ic()
        self.stop_config.rank_harmonic_attack_time_set(
            rank_number=self.rank_number_editor,
            harmonic_number=self.harmonic_number_rank_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Decay Time - Harmonic - Rank
    #--------------------------------------------------------------------------
    @property
    def decay_harmonic_rank_config(self) -> int:
        ic()
        return self.stop_config.rank_harmonic_decay_time_get(
            rank_number=self.rank_number_editor,
            harmonic_number=self.harmonic_number_rank_editor
        )

    @decay_harmonic_rank_config.setter
    def decay_harmonic_rank_config(self, value: int):
        ic()
        self.stop_config.rank_harmonic_decay_time_set(
            rank_number=self.rank_number_editor,
            harmonic_number=self.harmonic_number_rank_editor,
             value=value
        )

    #--------------------------------------------------------------------------
    # Sustain Level - Harmonic - Rank
    #--------------------------------------------------------------------------
    @property
    def sustain_harmonic_rank_config(self) -> int:
        ic()
        return self.stop_config.rank_harmonic_sustain_level_get(
            rank_number=self.rank_number_editor,
            harmonic_number=self.harmonic_number_rank_editor
        )

    @sustain_harmonic_rank_config.setter
    def sustain_harmonic_rank_config(self, value: int):
        ic()
        self.stop_config.rank_harmonic_sustain_level_set(
            rank_number=self.rank_number_editor,
            harmonic_number=self.harmonic_number_rank_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Release Time - Harmonic - Rank
    #--------------------------------------------------------------------------
    @property
    def release_harmonic_rank_config(self) -> int:
        ic()
        return self.stop_config.rank_harmonic_release_time_get(
            rank_number=self.rank_number_editor,
            harmonic_number=self.harmonic_number_rank_editor
        )

    @release_harmonic_rank_config.setter
    def release_harmonic_rank_config(self, value: int):
        ic()
        self.stop_config.rank_harmonic_release_time_set(
            rank_number=self.rank_number_editor,
            harmonic_number=self.harmonic_number_rank_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Attack Time - Rank
    #--------------------------------------------------------------------------
    @property
    def attack_rank_config(self) -> int:
        ic()
        return self.stop_config.rank_attack_time_get(
            rank_number=self.rank_number_editor
        )

    @attack_rank_config.setter
    def attack_rank_config(self, value: int):
        ic()
        self.stop_config.rank_attack_time_set(
            rank_number=self.rank_number_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Decay Time - Rank
    #--------------------------------------------------------------------------
    @property
    def decay_rank_config(self) -> int:
        ic()
        return self.stop_config.rank_decay_time_get(
            rank_number=self.rank_number_editor
        )

    @decay_rank_config.setter
    def decay_rank_config(self, value: int):
        ic()
        self.stop_config.rank_decay_time_set(
            rank_number=self.rank_number_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Sustain Level - Rank
    #--------------------------------------------------------------------------
    @property
    def sustain_rank_config(self) -> int:
        ic()
        return self.stop_config.rank_sustain_level_get(
            rank_number=self.rank_number_editor
        )

    @sustain_rank_config.setter
    def sustain_rank_config(self, value: int):
        ic()
        self.stop_config.rank_sustain_level_set(
            rank_number=self.rank_number_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Release Time - Rank
    #--------------------------------------------------------------------------
    @property
    def release_rank_config(self) -> int:
        ic()
        return self.stop_config.rank_release_time_get(
            rank_number=self.rank_number_editor
        )

    @release_rank_config.setter
    def release_rank_config(self, value: int):
        ic()
        self.stop_config.rank_release_time_set(
            rank_number=self.rank_number_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Note
    #--------------------------------------------------------------------------
    @property
    def note_config(self) -> str:
        ic()
        return self.stop_config.note_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor
        )

    @note_config.setter
    def note_config(self, value: str):
        ic()
        self.stop_config.note_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Relative Note
    #--------------------------------------------------------------------------
    @property
    def relative_note_config(self) -> str:
        ic()
        return self.stop_config.relative_note_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor
        )

    @relative_note_config.setter
    def relative_note_config(self, value: str):
        ic()
        self.stop_config.relative_note_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Amplitude - Pipe
    #--------------------------------------------------------------------------
    @property
    def amplitude_pipe_config(self) -> int:
        ic()
        return self.stop_config.pipe_harmonic_amplitude_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            harmonic_number=self.harmonic_number_pipe_editor
        )

    @amplitude_pipe_config.setter
    def amplitude_pipe_config(self, value: int):
        ic()
        self.stop_config.pipe_harmonic_amplitude_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            harmonic_number=self.harmonic_number_pipe_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Attack Time - Harmonic - Pipe
    #--------------------------------------------------------------------------
    @property
    def attack_harmonic_pipe_config(self) -> int:
        ic()
        return self.stop_config.pipe_harmonic_attack_time_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            harmonic_number=self.harmonic_number_pipe_editor
        )

    @attack_harmonic_pipe_config.setter
    def attack_harmonic_pipe_config(self, value: int):
        ic()
        self.stop_config.pipe_harmonic_attack_time_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            harmonic_number=self.harmonic_number_pipe_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Decay Time - Harmonic - Pipe
    #--------------------------------------------------------------------------
    @property
    def decay_harmonic_pipe_config(self) -> int:
        ic()
        return self.stop_config.pipe_harmonic_decay_time_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            harmonic_number=self.harmonic_number_pipe_editor
        )

    @decay_harmonic_pipe_config.setter
    def decay_harmonic_pipe_config(self, value: int):
        ic()
        self.stop_config.pipe_harmonic_decay_time_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            harmonic_number=self.harmonic_number_pipe_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Sustain Level - Harmonic - Pipe
    #--------------------------------------------------------------------------
    @property
    def sustain_harmonic_pipe_config(self) -> int:
        ic()
        return self.stop_config.pipe_harmonic_sustain_level_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            harmonic_number=self.harmonic_number_pipe_editor
        )

    @sustain_harmonic_pipe_config.setter
    def sustain_harmonic_pipe_config(self, value: int):
        ic()
        self.stop_config.pipe_harmonic_sustain_level_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            harmonic_number=self.harmonic_number_pipe_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Release Time - Harmonic - Pipe
    #--------------------------------------------------------------------------
    @property
    def release_harmonic_pipe_config(self) -> int:
        ic()
        return self.stop_config.pipe_harmonic_release_time_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            harmonic_number=self.harmonic_number_pipe_editor
        )

    @release_harmonic_pipe_config.setter
    def release_harmonic_pipe_config(self, value: int):
        ic()
        self.stop_config.pipe_harmonic_release_time_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            harmonic_number=self.harmonic_number_pipe_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Attack Time - Pipe
    #--------------------------------------------------------------------------
    @property
    def attack_pipe_config(self) -> int:
        ic()
        return self.stop_config.pipe_attack_time_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor
        )

    @attack_pipe_config.setter
    def attack_pipe_config(self, value: int):
        ic()
        self.stop_config.pipe_attack_time_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Decay Time - Pipe
    #--------------------------------------------------------------------------
    @property
    def decay_pipe_config(self) -> int:
        ic()
        return self.stop_config.pipe_decay_time_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor
        )

    @decay_pipe_config.setter
    def decay_pipe_config(self, value: int):
        ic()
        self.stop_config.pipe_decay_time_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Sustain Level - Pipe
    #--------------------------------------------------------------------------
    @property
    def sustain_pipe_config(self) -> int:
        ic()
        return self.stop_config.pipe_sustain_level_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor
        )

    @sustain_pipe_config.setter
    def sustain_pipe_config(self, value: int):
        ic()
        self.stop_config.pipe_sustain_level_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            value=value
        )

    #--------------------------------------------------------------------------
    # Release Time - Pipe
    #--------------------------------------------------------------------------
    @property
    def release_pipe_config(self) -> int:
        ic()
        return self.stop_config.pipe_release_time_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor
        )

    @release_pipe_config.setter
    def release_pipe_config(self, value: int):
        ic()
        self.stop_config.pipe_release_time_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            value=value
        )


if __name__ == "__main__":
    log_file.start_logging()
    app = QApplication([])
    ic(app)
    stop_editor_ui = StopEditorUI()
    #log: str = f"{ic.contextDelimiter} {ic(stop_editor_ui)}"
    stop_editor_ui.stop_editor.show()
    #print(log)
    app.exec()
