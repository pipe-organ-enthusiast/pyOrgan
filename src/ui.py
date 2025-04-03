"""UI Class"""
from gui import StopEditor
from organ import organlib
from config_editors import StopConfig
import log_file
#-----------------------------------------------------------------------------------------------------------------------
from PySide6.QtWidgets import QApplication, QFileDialog
from icecream import ic  # type: ignore


#=======================================================================================================================
# Stop Editor
#=======================================================================================================================
class StopEditorUI:
    def __init__(self) -> None:
        ic("Initializing Stop Editor UI...")
        self.stop_editor: StopEditor = StopEditor()
        self.stop_config: StopConfig = StopConfig()
        self.config_file: str = ""
        ic(self.config_file)
        self.__default_ui_editor_data()
        self.__init_ui()
        ic("Stop Editor UI Initialized.")

    #===================================================================================================================
    # Configuration
    #===================================================================================================================
    #*******************************************************************************************************************
    # Default Data
    #*******************************************************************************************************************
    def __default_ui_editor_data(self) -> None:
        ic("Loading Default UI Editor Data...")
        self.__init_setting_numbers()
        self.stop_config.init_default_config()
        self.__load_ui_editor_data()
        self.__update_number_ranks()
        self.__update_number_pipes()
        self.__update_number_harmonics()
        ic("Default UI Editor Data Loaded.")

    #-------------------------------------------------------------------------------------------------------------------
    def __init_setting_numbers(self) -> None:
        ic("Initializing Setting Numbers...")
        self.rank_number_editor = 1
        self.harmonic_number_rank_editor = 1
        self.rank_number_pipe_editor = 1
        self.pipe_number_editor = 1
        self.harmonic_number_pipe_editor = 1
        ic("Setting Numbers Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
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

    #*******************************************************************************************************************
    # Initialize UI Configuration
    #*******************************************************************************************************************
    def __init_ui(self) -> None:
        ic("Initializing UI...")
        self.stop_editor.stop_name_change_connect(self.__update_stop_name)
        self.stop_editor.stop_family_change_connect(self.__update_stop_family)
        self.stop_editor.organ_division_change_connect(self.__update_organ_division)
        self.stop_editor.number_ranks_change_connect(self.__update_number_ranks)
        self.stop_editor.rank_series_change_connect(self.__update_rank_series)
        self.stop_editor.rank_number_change_connect(self.__update_rank_number)
        self.stop_editor.rank_size_change_connect(self.__update_rank_size)
        self.stop_editor.number_pipes_change_connect(self.__update_number_pipes)
        self.stop_editor.pipe_type_change_connection(self.__update_pipe_type)
        self.stop_editor.starting_note_change_connection(self.__update_starting_note)
        self.stop_editor.frequency_offset_change_connection(self.__update_frequency_offset)
        self.stop_editor.number_harmonics_change_connection(self.__update_number_harmonics)
        self.stop_editor.harmonic_number_rank_change_connect(self.__update_harmonic_number_rank)
        self.stop_editor.amplitude_rank_change_connect(self.__update_rank_amplitude)
        self.stop_editor.attack_time_rank_harmonic_change_connect(self.__update_rank_harmonic_attack)
        self.stop_editor.decay_time_rank_harmonic_change_connect(self.__update_rank_harmonic_decay)
        self.stop_editor.sustain_level_rank_harmonic_change_connect(self.__update_rank_harmonic_sustain)
        self.stop_editor.release_time_rank_harmonic_change_connect(self.__update_rank_harmonic_release)
        self.stop_editor.attack_time_rank_change_connect(self.__update_rank_attack)
        self.stop_editor.decay_time_rank_change_connect(self.__update_rank_decay)
        self.stop_editor.sustain_level_rank_change_connect(self.__update_rank_sustain)
        self.stop_editor.release_time_rank_change_connect(self.__update_rank_release)
        self.stop_editor.rank_number_pipe_change_connect(self.__update_rank_number_pipe)
        self.stop_editor.pipe_number_change_connect(self.__update_pipe_number)
        self.stop_editor.note_change_connect(self.__update_note)
        self.stop_editor.relative_note_change_connect(self.__update_relative_note)
        self.stop_editor.harmonic_number_pipe_change_connect(self.__update_harmonic_number_pipe)
        self.stop_editor.amplitude_pipe_change_connect(self.__update_pipe_amplitude)
        self.stop_editor.attack_time_pipe_harmonic_change_connect(self.__update_pipe_harmonic_attack)
        self.stop_editor.decay_time_pipe_harmonic_change_connect(self.__update_pipe_harmonic_decay)
        self.stop_editor.sustain_level_pipe_harmonic_change_connect(self.__update_pipe_harmonic_sustain)
        self.stop_editor.release_time_pipe_harmonic_change_connect(self.__update_pipe_harmonic_release)
        self.stop_editor.attack_time_pipe_change_connect(self.__update_pipe_attack)
        self.stop_editor.decay_time_pipe_change_connect(self.__update_pipe_decay)
        self.stop_editor.sustain_level_pipe_change_connect(self.__update_pipe_sustain)
        self.stop_editor.release_time_pipe_change_connect(self.__update_pipe_release)
        self.stop_editor.load_stop_action_connect(self.__load_stop)
        self.stop_editor.cancel_changes_action_connect(self.__cancel_changes)
        self.stop_editor.save_stop_action_connect(self.__save_stop)
        ic("UI Initialized.")

    #===================================================================================================================
    # Actions
    #===================================================================================================================
    def __update_stop_name(self) -> None:
        ic("Updating Stop Name...")
        self.stop_name_config = self.stop_name_editor
        self.stop_editor.update_stop_header()
        ic("Stop Name Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_stop_family(self) -> None:
        ic("Updating Stop Family...")
        self.stop_family_config = self.stop_family_editor
        ic("Stop Family Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_organ_division(self) -> None:
        ic("Updating Organ Division...")
        self.organ_division_config = self.organ_division_editor
        ic("Organ Division Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_number_ranks(self) -> None:
        ic("Updating Number of Ranks...")
        self.number_ranks_config = self.number_ranks_editor
        self.stop_editor.update_number_ranks()
        self.stop_editor.update_stop_header()
        ic("Number of Ranks Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_series(self) -> None:
        ic("Updating Rank Series...")
        self.rank_series_config = self.rank_series_editor
        self.stop_editor.update_rank_sizes()
        ic("Rank Series Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_number_general(self) -> None:
        ic("Updating Rank Settings...")
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
        ic("Rank Settings Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_number(self) -> None:
        ic("Updating Rank Number...")
        self.stop_editor.update_rank_number()
        self.__update_rank_number_general()
        ic("Rank Number Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_size(self) -> None:
        ic("Updating Rank Size...")
        self.rank_size_config = self.rank_size_editor
        ic("Rank Size Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_number_pipes(self) -> None:
        ic("Updating Number of Pipes...")
        self.number_pipes_config = self.number_pipes_editor
        self.stop_editor.update_number_pipes()
        ic("Number of Pipes Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_type(self) -> None:
        ic("Updating Pipe Type...")
        self.pipe_type_config = self.pipe_type_editor
        ic("Pipe Type Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_starting_note(self) -> None:
        ic("Updating Starting Note...")
        self.starting_note_config = self.starting_note_editor
        ic("Starting Note Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_frequency_offset(self) -> None:
        ic("Updating Frequency Offset...")
        self.frequency_offset_config = self.frequency_offset_editor
        ic("Frequency Offset Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_number_harmonics(self) -> None:
        ic("Updating Number of Harmonics...")
        self.number_harmonics_config = self.number_harmonics_editor
        self.stop_editor.update_number_harmonics()
        ic("Number of Harmonics Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_harmonic_number(self) -> None:
        ic("Updating Harmonic Settings...")
        self.amplitude_rank_editor = self.amplitude_rank_config
        self.attack_harmonic_rank_editor = self.attack_harmonic_rank_config
        self.decay_harmonic_rank_editor = self.decay_harmonic_rank_config
        self.sustain_harmonic_rank_editor = self.sustain_harmonic_rank_config
        self.release_harmonic_rank_editor = self.release_harmonic_rank_config
        self.amplitude_pipe_editor = self.amplitude_pipe_config
        self.attack_harmonic_pipe_editor = self.attack_harmonic_pipe_config
        self.decay_harmonic_pipe_editor = self.decay_harmonic_pipe_config
        self.sustain_harmonic_pipe_editor = self.sustain_harmonic_pipe_config
        self.release_harmonic_pipe_editor = self.release_harmonic_pipe_config
        ic("Harmonic Settings Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_harmonic_number_rank(self) -> None:
        ic("Updating Harmonic Number Rank...")
        self.stop_editor.update_harmonic_number_rank()
        self.__update_harmonic_number()
        ic("Harmonic Number Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_amplitude(self) -> None:
        ic("Updating Amplitude Rank...")
        self.amplitude_rank_config = self.amplitude_rank_editor
        ic("Amplitude Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_harmonic_attack(self) -> None:
        ic("Updating Attack Harmonic Rank...")
        self.attack_harmonic_rank_config = self.attack_harmonic_rank_editor
        ic("Attack Harmonic Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_harmonic_decay(self) -> None:
        ic("Updating Decay Harmonic Rank...")
        self.decay_harmonic_rank_config = self.decay_harmonic_rank_editor
        ic("Decay Harmonic Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_harmonic_sustain(self) -> None:
        ic("Updating Sustain Harmonic Rank...")
        self.sustain_harmonic_rank_config = self.sustain_harmonic_rank_editor
        ic("Sustain Harmonic Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_harmonic_release(self) -> None:
        ic("Updating Release Harmonic Rank...")
        self.release_harmonic_rank_config = self.release_harmonic_rank_editor
        ic("Release Harmonic Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_attack(self) -> None:
        ic("Updating Attack Rank...")
        self.attack_rank_config = self.attack_rank_editor
        ic("Attack Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_decay(self) -> None:
        ic("Updating Decay Rank...")
        self.decay_rank_config = self.decay_rank_editor
        ic("Decay Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_sustain(self) -> None:
        ic("Updating Sustain Rank...")
        self.sustain_rank_config = self.sustain_rank_editor
        ic("Sustain Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_release(self) -> None:
        ic("Updating Release Rank...")
        self.release_rank_config = self.release_rank_editor
        ic("Release Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_number_pipe(self) -> None:
        ic("Updating Rank Number Pipe...")
        self.stop_editor.update_rank_number_pipe()
        self.__update_rank_number_general()
        ic("Rank Number Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_number(self) -> None:
        ic("Updating Pipe Settings...")
        self.note_editor = self.note_config
        self.relative_note_editor = self.relative_note_config
        self.harmonic_number_pipe_editor = 1
        self.__update_harmonic_number()
        self.attack_pipe_editor = self.attack_pipe_config
        self.decay_pipe_editor = self.decay_pipe_config
        self.sustain_pipe_editor = self.sustain_pipe_config
        self.release_pipe_editor = self.release_pipe_config
        ic("Pipe Settings Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_note(self) -> None:
        ic("Updating Note...")
        self.note_config = self.note_editor
        ic("Note Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_relative_note(self) -> None:
        ic("Updating Relative Note...")
        note_index = organlib.NOTES.index(self.relative_note_editor)
        ic(note_index)
        notes: tuple[str, ...] = organlib.NOTES[note_index:]
        ic(notes)
        self.stop_config.update_relative_notes(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            notes=notes
        )
        ic("Relative Note Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_harmonic_number_pipe(self) -> None:
        ic("Updating Harmonic Number Pipe...")
        self.stop_editor.update_harmonic_number_pipe()
        self.__update_harmonic_number()
        ic("Harmonic Number Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_amplitude(self) -> None:
        ic("Updating Amplitude Pipe...")
        self.amplitude_pipe_config = self.amplitude_pipe_editor
        ic("Amplitude Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_attack(self) -> None:
        ic("Updating Attack Pipe...")
        self.attack_pipe_config = self.attack_pipe_editor
        ic("Attack Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_decay(self) -> None:
        ic("Updating Decay Pipe...")
        self.decay_pipe_config = self.decay_pipe_editor
        ic("Decay Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_sustain(self) -> None:
        ic("Updating Sustain Pipe...")
        self.sustain_pipe_config = self.sustain_pipe_editor
        ic("Sustain Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_release(self) -> None:
        ic("Updating Release Pipe...")
        self.release_pipe_config = self.release_pipe_editor
        ic("Release Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_harmonic_attack(self) -> None:
        ic("Updating Attack Harmonic Pipe...")
        self.attack_harmonic_pipe_config = self.attack_harmonic_pipe_editor
        ic("Attack Harmonic Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_harmonic_decay(self) -> None:
        ic("Updating Decay Harmonic Pipe...")
        self.decay_harmonic_pipe_config = self.decay_harmonic_pipe_editor
        ic("Decay Harmonic Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_harmonic_sustain(self) -> None:
        ic("Updating Sustain Harmonic Pipe...")
        self.sustain_harmonic_pipe_config = self.sustain_harmonic_pipe_editor
        ic("Sustain Harmonic Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_harmonic_release(self) -> None:
        ic("Updating Release Harmonic Pipe...")
        self.release_harmonic_pipe_config = self.release_harmonic_pipe_editor
        ic("Release Harmonic Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __load_config(self) -> None:
        ic("Loading Config...")
        self.stop_config.load_file(self.config_file)
        self.__init_setting_numbers()
        self.__load_ui_editor_data()
        ic("Config Loaded.")

    #-------------------------------------------------------------------------------------------------------------------
    def __load_stop(self) -> None:
        ic("Loading Stop...")
        file_dialog: QFileDialog = QFileDialog()
        ic(file_dialog)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        ic(file_dialog.fileMode())
        file_dialog.setNameFilter("JSON Files (*.json)")
        ic(file_dialog.nameFilters)
        file_dialog.setViewMode(QFileDialog.ViewMode.Detail)
        ic(file_dialog.viewMode())
        file_dialog.setDirectory("src/config/stops")
        ic(file_dialog.directory())
        self.config_file = file_dialog.getOpenFileName()[0]
        ic(self.config_file)
        self.__load_config()
        ic("Stop Loaded.")

    #-------------------------------------------------------------------------------------------------------------------
    def __cancel_changes(self) -> None:
        ic("Cancelling Changes...")
        ic(self.config_file)
        if self.config_file == "":
            self.__default_ui_editor_data()
        else:
            self.__load_config()
        ic("Changes Cancelled.")

    def __save_stop(self) -> None:
        ic("Saving Stop...")
        stop_header: str = self.stop_header_editor
        if stop_header != "":
            self.config_file = f"src/config/stops/{stop_header}.json"
            self.stop_config.save_file(self.config_file)
            ic("Stop Saved.")
        else:
            ic("Stop Header is empty. Cannot save stop.")
        ic("Finished Saving Stop.")

    #===================================================================================================================
    # Properties
    #===================================================================================================================
    #*******************************************************************************************************************
    # Stop Editor
    #*******************************************************************************************************************
    @property
    def stop_header_editor(self) -> str:
        ic("Getting Stop Header Editor...")
        stop_header: str = self.stop_editor.stop_header
        ic("Stop Header Editor Retrieved.")
        return stop_header

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Stop Name
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def stop_name_editor(self) -> str:
        ic("Getting Stop Name Editor...")
        stop_name: str = self.stop_editor.stop_name
        ic("Stop Name Editor Retrieved.")
        return stop_name

    #-------------------------------------------------------------------------------------------------------------------
    @stop_name_editor.setter
    def stop_name_editor(self, value: str) -> None:
        ic("Setting Stop Name Editor...")
        ic(value)
        self.stop_editor.stop_name = value
        ic("Stop Name Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Stop Family
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def stop_family_editor(self) -> str:
        ic("Getting Stop Family Editor...")
        stop_family: str = self.stop_editor.stop_family
        ic("Stop Family Editor Retrieved.")
        return stop_family

    #-------------------------------------------------------------------------------------------------------------------
    @stop_family_editor.setter
    def stop_family_editor(self, value: str) -> None:
        ic("Setting Stop Family Editor...")
        ic(value)
        self.stop_editor.stop_family = value
        ic("Stop Family Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Organ Division
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def organ_division_editor(self) -> str:
        ic("Getting Organ Division Editor...")
        organ_division: str = self.stop_editor.organ_division
        ic("Organ Division Editor Retrieved.")
        return organ_division

    #-------------------------------------------------------------------------------------------------------------------
    @organ_division_editor.setter
    def organ_division_editor(self, value: str) -> None:
        ic("Setting Organ Division Editor...")
        ic(value)
        self.stop_editor.organ_division = value
        ic("Organ Division Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Number of Ranks
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def number_ranks_editor(self) -> int:
        ic("Getting Number of Ranks Editor...")
        number_ranks: int = self.stop_editor.number_ranks
        ic("Number of Ranks Editor Retrieved.")
        return number_ranks

    #-------------------------------------------------------------------------------------------------------------------
    @number_ranks_editor.setter
    def number_ranks_editor(self, value: int) -> None:
        ic("Setting Number of Ranks Editor...")
        ic(value)
        self.stop_editor.number_ranks = value
        ic("Number of Ranks Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Rank Series
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def rank_series_editor(self) -> str:
        ic("Getting Rank Series Editor...")
        rank_series: str = self.stop_editor.rank_series
        ic("Rank Series Editor Retrieved.")
        return rank_series

    #-------------------------------------------------------------------------------------------------------------------
    @rank_series_editor.setter
    def rank_series_editor(self, value: str) -> None:
        ic("Setting Rank Series Editor...")
        ic(value)
        self.stop_editor.rank_series = value
        ic("Rank Series Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Rank Number
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def rank_number_editor(self) -> int:
        ic("Getting Rank Number Editor...")
        rank_number: int = self.stop_editor.rank_number
        ic("Rank Number Editor Retrieved.")
        return rank_number

    #-------------------------------------------------------------------------------------------------------------------
    @rank_number_editor.setter
    def rank_number_editor(self, value: int) -> None:
        ic("Setting Rank Number Editor...")
        ic(value)
        self.stop_editor.rank_number = value
        ic("Rank Number Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Rank Size
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def rank_size_editor(self) -> str:
        ic("Getting Rank Size Editor...")
        rank_size: str = self.stop_editor.rank_size
        ic("Rank Size Editor Retrieved.")
        return rank_size

    #-------------------------------------------------------------------------------------------------------------------
    @rank_size_editor.setter
    def rank_size_editor(self, value: str) -> None:
        ic("Setting Rank Size Editor...")
        ic(value)
        self.stop_editor.rank_size = value
        ic("Rank Size Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Number of Pipes
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def number_pipes_editor(self) -> int:
        ic("Getting Number of Pipes Editor...")
        number_pipes: int = self.stop_editor.number_pipes
        ic("Number of Pipes Editor Retrieved.")
        return number_pipes

    #-------------------------------------------------------------------------------------------------------------------
    @number_pipes_editor.setter
    def number_pipes_editor(self, value: int) -> None:
        ic("Setting Number of Pipes Editor...")
        ic(value)
        self.stop_editor.number_pipes = value
        ic("Number of Pipes Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Pipe Type
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def pipe_type_editor(self) -> str:
        ic("Getting Pipe Type Editor...")
        pipe_type: str = self.stop_editor.pipe_type
        ic("Pipe Type Editor Retrieved.")
        return pipe_type

    #-------------------------------------------------------------------------------------------------------------------
    @pipe_type_editor.setter
    def pipe_type_editor(self, value: str) -> None:
        ic("Setting Pipe Type Editor...")
        ic(value)
        self.stop_editor.pipe_type = value
        ic("Pipe Type Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Starting Note
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def starting_note_editor(self) -> str:
        ic("Getting Starting Note Editor...")
        starting_note: str = self.stop_editor.starting_note
        ic("Starting Note Editor Retrieved.")
        return starting_note

    #-------------------------------------------------------------------------------------------------------------------
    @starting_note_editor.setter
    def starting_note_editor(self, value: str) -> None:
        ic("Setting Starting Note Editor...")
        ic(value)
        self.stop_editor.starting_note = value
        ic("Starting Note Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Frequency Offset
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def frequency_offset_editor(self) -> int:
        ic("Getting Frequency Offset Editor...")
        frequency_offset: int = self.stop_editor.frequency_offset
        ic("Frequency Offset Editor Retrieved.")
        return frequency_offset

    #-------------------------------------------------------------------------------------------------------------------
    @frequency_offset_editor.setter
    def frequency_offset_editor(self, value: int) -> None:
        ic("Setting Frequency Offset Editor...")
        ic(value)
        self.stop_editor.frequency_offset = value
        ic("Frequency Offset Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Number of Harmonics
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def number_harmonics_editor(self) -> int:
        ic("Getting Number of Harmonics Editor...")
        number_harmonics: int = self.stop_editor.number_harmonics
        ic("Number of Harmonics Editor Retrieved.")
        return number_harmonics

    #-------------------------------------------------------------------------------------------------------------------
    @number_harmonics_editor.setter
    def number_harmonics_editor(self, value: int) -> None:
        ic("Setting Number of Harmonics Editor...")
        ic(value)
        self.stop_editor.number_harmonics = value
        ic("Number of Harmonics Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Harmonic Number - Rank
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def harmonic_number_rank_editor(self) -> int:
        ic("Getting Harmonic Number Rank Editor...")
        harmonic_number_rank: int = self.stop_editor.harmonic_number_rank
        ic("Harmonic Number Rank Editor Retrieved.")
        return harmonic_number_rank

    #-------------------------------------------------------------------------------------------------------------------
    @harmonic_number_rank_editor.setter
    def harmonic_number_rank_editor(self, value: int) -> None:
        ic("Setting Harmonic Number Rank Editor...")
        ic(value)
        self.stop_editor.harmonic_number_rank = value
        ic("Harmonic Number Rank Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Amplitude - Rank
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def amplitude_rank_editor(self) -> int:
        ic("Getting Amplitude Rank Editor...")
        amplitude_rank: int = self.stop_editor.amplitude_rank
        ic("Amplitude Rank Editor Retrieved.")
        return amplitude_rank

    #-------------------------------------------------------------------------------------------------------------------
    @amplitude_rank_editor.setter
    def amplitude_rank_editor(self, value: int) -> None:
        ic("Setting Amplitude Rank Editor...")
        ic(value)
        self.stop_editor.amplitude_rank = value
        ic("Amplitude Rank Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Attack Time - Harmonic - Rank
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def attack_harmonic_rank_editor(self) -> int:
        ic("Getting Attack Harmonic Rank Editor...")
        attack_time_harmonic_rank: int = self.stop_editor.attack_time_harmonic_rank
        ic("Attack Harmonic Rank Editor Retrieved.")
        return attack_time_harmonic_rank

    #-------------------------------------------------------------------------------------------------------------------
    @attack_harmonic_rank_editor.setter
    def attack_harmonic_rank_editor(self, value: int) -> None:
        ic("Setting Attack Harmonic Rank Editor...")
        ic(value)
        self.stop_editor.attack_time_harmonic_rank = value
        ic("Attack Harmonic Rank Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Decay Time - Harmonic - Rank
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def decay_harmonic_rank_editor(self) -> int:
        ic("Getting Decay Harmonic Rank Editor...")
        decay_time_harmonic_rank: int = self.stop_editor.decay_time_harmonic_rank
        ic("Decay Harmonic Rank Editor Retrieved.")
        return decay_time_harmonic_rank

    #-------------------------------------------------------------------------------------------------------------------
    @decay_harmonic_rank_editor.setter
    def decay_harmonic_rank_editor(self, value: int) -> None:
        ic("Setting Decay Harmonic Rank Editor...")
        ic(value)
        self.stop_editor.decay_time_harmonic_rank = value
        ic("Decay Harmonic Rank Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Sustain Level - Harmonic - Rank
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def sustain_harmonic_rank_editor(self) -> int:
        ic("Getting Sustain Harmonic Rank Editor...")
        sustain_level_harmonic_rank: int = self.stop_editor.sustain_level_harmonic_rank
        ic("Sustain Harmonic Rank Editor Retrieved.")
        return sustain_level_harmonic_rank

    #-------------------------------------------------------------------------------------------------------------------
    @sustain_harmonic_rank_editor.setter
    def sustain_harmonic_rank_editor(self, value: int) -> None:
        ic("Setting Sustain Harmonic Rank Editor...")
        ic(value)
        self.stop_editor.sustain_level_harmonic_rank = value
        ic("Sustain Harmonic Rank Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Release Time - Harmonic - Rank
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def release_harmonic_rank_editor(self) -> int:
        ic("Getting Release Harmonic Rank Editor...")
        release_time_harmonic_rank: int = self.stop_editor.release_time_harmonic_rank
        ic("Release Harmonic Rank Editor Retrieved.")
        return release_time_harmonic_rank

    #-------------------------------------------------------------------------------------------------------------------
    @release_harmonic_rank_editor.setter
    def release_harmonic_rank_editor(self, value: int) -> None:
        ic("Setting Release Harmonic Rank Editor...")
        ic(value)
        self.stop_editor.release_time_harmonic_rank = value
        ic("Release Harmonic Rank Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Attack Time - Rank
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def attack_rank_editor(self) -> int:
        ic("Getting Attack Rank Editor...")
        attack_time_rank: int = self.stop_editor.attack_time_rank
        ic("Attack Rank Editor Retrieved.")
        return attack_time_rank

    #-------------------------------------------------------------------------------------------------------------------
    @attack_rank_editor.setter
    def attack_rank_editor(self, value: int) -> None:
        ic("Setting Attack Rank Editor...")
        ic(value)
        self.stop_editor.attack_time_rank = value
        ic("Attack Rank Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Decay Time - Rank
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def decay_rank_editor(self) -> int:
        ic("Getting Decay Rank Editor...")
        decay_time_rank: int = self.stop_editor.decay_time_rank
        ic("Decay Rank Editor Retrieved.")
        return decay_time_rank

    #-------------------------------------------------------------------------------------------------------------------
    @decay_rank_editor.setter
    def decay_rank_editor(self, value: int) -> None:
        ic("Setting Decay Rank Editor...")
        ic(value)
        self.stop_editor.decay_time_rank = value
        ic("Decay Rank Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Sustain Level - Rank
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def sustain_rank_editor(self) -> int:
        ic("Getting Sustain Rank Editor...")
        sustain_level_rank: int = self.stop_editor.sustain_level_rank
        ic("Sustain Rank Editor Retrieved.")
        return sustain_level_rank

    #-------------------------------------------------------------------------------------------------------------------
    @sustain_rank_editor.setter
    def sustain_rank_editor(self, value: int) -> None:
        ic("Setting Sustain Rank Editor...")
        ic(value)
        self.stop_editor.sustain_level_rank = value
        ic("Sustain Rank Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Release Time - Rank
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def release_rank_editor(self) -> int:
        ic("Getting Release Rank Editor...")
        release_time_rank: int = self.stop_editor.release_time_rank
        ic("Release Rank Editor Retrieved.")
        return release_time_rank

    #-------------------------------------------------------------------------------------------------------------------
    @release_rank_editor.setter
    def release_rank_editor(self, value: int) -> None:
        ic("Setting Release Rank Editor...")
        ic(value)
        self.stop_editor.release_time_rank = value
        ic("Release Rank Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Rank Number - Pipe
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def rank_number_pipe_editor(self) -> int:
        ic("Getting Rank Number Pipe Editor...")
        rank_number_pipe: int = self.stop_editor.rank_number_pipe
        ic("Rank Number Pipe Editor Retrieved.")
        return rank_number_pipe

    #-------------------------------------------------------------------------------------------------------------------
    @rank_number_pipe_editor.setter
    def rank_number_pipe_editor(self, value: int) -> None:
        ic("Setting Rank Number Pipe Editor...")
        ic(value)
        self.stop_editor.rank_number_pipe = value
        ic("Rank Number Pipe Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Pipe Number
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def pipe_number_editor(self) -> int:
        ic("Getting Pipe Number Editor...")
        pipe_number: int = self.stop_editor.pipe_number
        ic("Pipe Number Editor Retrieved.")
        return pipe_number

    #-------------------------------------------------------------------------------------------------------------------
    @pipe_number_editor.setter
    def pipe_number_editor(self, value: int) -> None:
        ic("Setting Pipe Number Editor...")
        ic(value)
        self.stop_editor.pipe_number = value
        ic("Pipe Number Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Note
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def note_editor(self) -> str:
        ic("Getting Note Editor...")
        note: str = self.stop_editor.note
        ic("Note Editor Retrieved.")
        return note

    #-------------------------------------------------------------------------------------------------------------------
    @note_editor.setter
    def note_editor(self, value: str) -> None:
        ic("Setting Note Editor...")
        ic(value)
        self.stop_editor.note = value
        ic("Note Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Relative Note
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def relative_note_editor(self) -> str:
        ic("Getting Relative Note Editor...")
        relative_note: str = self.stop_editor.relative_note
        ic("Relative Note Editor Retrieved.")
        return relative_note

    #-------------------------------------------------------------------------------------------------------------------
    @relative_note_editor.setter
    def relative_note_editor(self, value: str) -> None:
        ic("Setting Relative Note Editor...")
        ic(value)
        self.stop_editor.relative_note = value
        ic("Relative Note Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Harmonic Number - Pipe
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def harmonic_number_pipe_editor(self) -> int:
        ic("Getting Harmonic Number Pipe Editor...")
        harmonic_number_pipe: int = self.stop_editor.harmonic_number_pipe
        ic("Harmonic Number Pipe Editor Retrieved.")
        return harmonic_number_pipe

    #-------------------------------------------------------------------------------------------------------------------
    @harmonic_number_pipe_editor.setter
    def harmonic_number_pipe_editor(self, value: int) -> None:
        ic("Setting Harmonic Number Pipe Editor...")
        ic(value)
        self.stop_editor.harmonic_number_pipe = value
        ic("Harmonic Number Pipe Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Amplitude - Pipe
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def amplitude_pipe_editor(self) -> int:
        ic("Getting Amplitude Pipe Editor...")
        amplitude_pipe: int = self.stop_editor.amplitude_pipe
        ic("Amplitude Pipe Editor Retrieved.")
        return amplitude_pipe

    #-------------------------------------------------------------------------------------------------------------------
    @amplitude_pipe_editor.setter
    def amplitude_pipe_editor(self, value: int) -> None:
        ic("Setting Amplitude Pipe Editor...")
        ic(value)
        self.stop_editor.amplitude_pipe = value
        ic("Amplitude Pipe Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Attack Time - Harmonic - Pipe
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def attack_harmonic_pipe_editor(self) -> int:
        ic("Getting Attack Harmonic Pipe Editor...")
        attack_time_harmonic_pipe: int = self.stop_editor.attack_time_harmonic_pipe
        ic("Attack Harmonic Pipe Editor Retrieved.")
        return attack_time_harmonic_pipe

    #-------------------------------------------------------------------------------------------------------------------
    @attack_harmonic_pipe_editor.setter
    def attack_harmonic_pipe_editor(self, value: int) -> None:
        ic("Setting Attack Harmonic Pipe Editor...")
        ic(value)
        self.stop_editor.attack_time_harmonic_pipe = value
        ic("Attack Harmonic Pipe Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Decay Time - Harmonic - Pipe
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def decay_harmonic_pipe_editor(self) -> int:
        ic("Getting Decay Harmonic Pipe Editor...")
        decay_time_harmonic_pipe: int = self.stop_editor.decay_time_harmonic_pipe
        ic("Decay Harmonic Pipe Editor Retrieved.")
        return decay_time_harmonic_pipe

    #-------------------------------------------------------------------------------------------------------------------
    @decay_harmonic_pipe_editor.setter
    def decay_harmonic_pipe_editor(self, value: int) -> None:
        ic("Setting Decay Harmonic Pipe Editor...")
        ic(value)
        self.stop_editor.decay_time_harmonic_pipe = value
        ic("Decay Harmonic Pipe Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Sustain Level - Harmonic - Pipe
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def sustain_harmonic_pipe_editor(self) -> int:
        ic("Getting Sustain Harmonic Pipe Editor...")
        sustain_level_harmonic_pipe: int = self.stop_editor.sustain_level_harmonic_pipe
        ic("Sustain Harmonic Pipe Editor Retrieved.")
        return sustain_level_harmonic_pipe

    #-------------------------------------------------------------------------------------------------------------------
    @sustain_harmonic_pipe_editor.setter
    def sustain_harmonic_pipe_editor(self, value: int) -> None:
        ic("Setting Sustain Harmonic Pipe Editor...")
        ic(value)
        self.stop_editor.sustain_level_harmonic_pipe = value
        ic("Sustain Harmonic Pipe Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Release Time - Harmonic - Pipe
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def release_harmonic_pipe_editor(self) -> int:
        ic("Getting Release Harmonic Pipe Editor...")
        release_time_harmonic_pipe: int = self.stop_editor.release_time_harmonic_pipe
        ic("Release Harmonic Pipe Editor Retrieved.")
        return release_time_harmonic_pipe

    #-------------------------------------------------------------------------------------------------------------------
    @release_harmonic_pipe_editor.setter
    def release_harmonic_pipe_editor(self, value: int) -> None:
        ic("Setting Release Harmonic Pipe Editor...")
        ic(value)
        self.stop_editor.release_time_harmonic_pipe = value
        ic("Release Harmonic Pipe Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Attack Time - Pipe
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def attack_pipe_editor(self) -> int:
        ic("Getting Attack Pipe Editor...")
        attack_time_pipe: int = self.stop_editor.attack_time_pipe
        ic("Attack Pipe Editor Retrieved.")
        return attack_time_pipe

    #-------------------------------------------------------------------------------------------------------------------
    @attack_pipe_editor.setter
    def attack_pipe_editor(self, value: int) -> None:
        ic("Setting Attack Pipe Editor...")
        ic(value)
        self.stop_editor.attack_time_pipe = value
        ic("Attack Pipe Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Decay Time - Pipe
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def decay_pipe_editor(self) -> int:
        ic("Getting Decay Pipe Editor...")
        decay_time_pipe: int = self.stop_editor.decay_time_pipe
        ic("Decay Pipe Editor Retrieved.")
        return decay_time_pipe

    #-------------------------------------------------------------------------------------------------------------------
    @decay_pipe_editor.setter
    def decay_pipe_editor(self, value: int) -> None:
        ic("Setting Decay Pipe Editor...")
        ic(value)
        self.stop_editor.decay_time_pipe = value
        ic("Decay Pipe Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Sustain Level - Pipe
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def sustain_pipe_editor(self) -> int:
        ic("Getting Sustain Pipe Editor...")
        sustain_level_pipe: int = self.stop_editor.sustain_level_pipe
        ic("Sustain Pipe Editor Retrieved.")
        return sustain_level_pipe

    #-------------------------------------------------------------------------------------------------------------------
    @sustain_pipe_editor.setter
    def sustain_pipe_editor(self, value: int) -> None:
        ic("Setting Sustain Pipe Editor...")
        ic(value)
        self.stop_editor.sustain_level_pipe = value
        ic("Sustain Pipe Editor Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Release Time - Pipe
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def release_pipe_editor(self) -> int:
        ic("Getting Release Pipe Editor...")
        release_time_pipe: int = self.stop_editor.release_time_pipe
        ic("Release Pipe Editor Retrieved.")
        return release_time_pipe

    #-------------------------------------------------------------------------------------------------------------------
    @release_pipe_editor.setter
    def release_pipe_editor(self, value: int) -> None:
        ic("Setting Release Pipe Editor...")
        ic(value)
        self.stop_editor.release_time_pipe = value
        ic("Release Pipe Editor Set.")

    #*******************************************************************************************************************
    # Stop Config
    #*******************************************************************************************************************
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Stop Name
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def stop_name_config(self) -> str:
        ic("Getting Stop Name Config...")
        stop_name: str = self.stop_config.stop_name_get()
        ic("Stop Name Config Retrieved.")
        return stop_name

    #-------------------------------------------------------------------------------------------------------------------
    @stop_name_config.setter
    def stop_name_config(self, value: str):
        ic("Setting Stop Name Config...")
        ic(value)
        self.stop_config.stop_name_set(value)
        ic("Stop Name Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Stop Family
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def stop_family_config(self) -> str:
        ic("Getting Stop Family Config...")
        stop_family: str = self.stop_config.stop_family_get()
        ic("Stop Family Config Retrieved.")
        return stop_family

    #-------------------------------------------------------------------------------------------------------------------
    @stop_family_config.setter
    def stop_family_config(self, value: str):
        ic("Setting Stop Family Config...")
        ic(value)
        self.stop_config.stop_family_set(value)
        ic("Stop Family Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Organ Division
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def organ_division_config(self) -> str:
        ic("Getting Organ Division Config...")
        organ_division: str = self.stop_config.organ_division_get()
        ic("Organ Division Config Retrieved.")
        return organ_division

    #-------------------------------------------------------------------------------------------------------------------
    @organ_division_config.setter
    def organ_division_config(self, value: str):
        ic("Setting Organ Division Config...")
        ic(value)
        self.stop_config.organ_division_set(value)
        ic("Organ Division Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Number of Ranks
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def number_ranks_config(self) -> int:
        ic("Getting Number of Ranks Config...")
        number_ranks: int = self.stop_config.number_ranks_get()
        ic("Number of Ranks Config Retrieved.")
        return number_ranks

    #-------------------------------------------------------------------------------------------------------------------
    @number_ranks_config.setter
    def number_ranks_config(self, value: int):
        ic("Setting Number of Ranks Config...")
        ic(value)
        self.stop_config.number_ranks_set(value)
        ic("Number of Ranks Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Rank Series
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def rank_series_config(self) -> str:
        ic("Getting Rank Series Config...")
        rank_series: str = self.stop_config.rank_series_get()
        ic("Rank Series Config Retrieved.")
        return rank_series

    #-------------------------------------------------------------------------------------------------------------------
    @rank_series_config.setter
    def rank_series_config(self, value: str):
        ic("Setting Rank Series Config...")
        ic(value)
        self.stop_config.rank_series_set(value)
        ic("Rank Series Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Rank Size
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def rank_size_config(self) -> str:
        ic("Getting Rank Size Config...")
        rank_number: int = self.rank_number_editor
        rank_size: str = self.stop_config.rank_size_get(rank_number)
        ic("Rank Size Config Retrieved.")
        return rank_size

    #-------------------------------------------------------------------------------------------------------------------
    @rank_size_config.setter
    def rank_size_config(self, value: str):
        ic("Setting Rank Size Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        self.stop_config.rank_size_set(rank_number, value)
        ic("Rank Size Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Number of Pipes
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def number_pipes_config(self) -> int:
        ic("Getting Number of Pipes Config...")
        rank_number: int = self.rank_number_editor
        number_pipes: int = self.stop_config.number_pipes_get(rank_number)
        ic("Number of Pipes Config Retrieved.")
        return number_pipes

    #-------------------------------------------------------------------------------------------------------------------
    @number_pipes_config.setter
    def number_pipes_config(self, value: int):
        ic("Setting Number of Pipes Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        self.stop_config.number_pipes_set(rank_number, value)
        ic("Number of Pipes Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Pipe Type
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def pipe_type_config(self) -> str:
        ic("Getting Pipe Type Config...")
        pipe_type: str = self.stop_config.pipe_type_get(self.rank_number_editor)
        ic("Pipe Type Config Retrieved.")
        return pipe_type

    #-------------------------------------------------------------------------------------------------------------------
    @pipe_type_config.setter
    def pipe_type_config(self, value: str):
        ic("Setting Pipe Type Config...")
        ic(value)
        self.stop_config.pipe_type_set(self.rank_number_editor, value)
        ic("Pipe Type Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Starting Note
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def starting_note_config(self) -> str:
        ic("Getting Starting Note Config...")
        rank_number: int = self.rank_number_editor
        starting_note: str = self.stop_config.starting_note_get(rank_number)
        ic("Starting Note Config Retrieved.")
        return starting_note

    #-------------------------------------------------------------------------------------------------------------------
    @starting_note_config.setter
    def starting_note_config(self, value: str):
        ic("Setting Starting Note Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        self.stop_config.starting_note_set(rank_number, value)
        ic("Starting Note Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Frequency Offset
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def frequency_offset_config(self) -> int:
        ic("Getting Frequency Offset Config...")
        rank_number: int = self.rank_number_editor
        frequency_offset: int = self.stop_config.frequency_offset_get(rank_number)
        ic("Frequency Offset Config Retrieved.")
        return frequency_offset

    #-------------------------------------------------------------------------------------------------------------------
    @frequency_offset_config.setter
    def frequency_offset_config(self, value: int):
        ic("Setting Frequency Offset Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        self.stop_config.frequency_offset_set(rank_number, value)

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Number of Harmonics
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def number_harmonics_config(self) -> int:
        ic("Getting Number of Harmonics Config...")
        rank_number: int = self.rank_number_editor
        number_harmonics: int = self.stop_config.number_harmonics_get(rank_number)
        ic("Number of Harmonics Config Retrieved.")
        return number_harmonics

    #-------------------------------------------------------------------------------------------------------------------
    @number_harmonics_config.setter
    def number_harmonics_config(self, value: int):
        ic("Setting Number of Harmonics Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        self.stop_config.number_harmonics_set(rank_number, value)
        ic("Number of Harmonics Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Amplitude - Rank
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def amplitude_rank_config(self) -> int:
        ic("Getting Amplitude Rank Config...")
        rank_number: int = self.rank_number_editor
        harmonic_number: int = self.harmonic_number_rank_editor
        amplitude: int = self.stop_config.rank_harmonic_amplitude_get(rank_number, harmonic_number)
        ic("Amplitude Rank Config Retrieved.")
        return amplitude

    #-------------------------------------------------------------------------------------------------------------------
    @amplitude_rank_config.setter
    def amplitude_rank_config(self, value: int):
        ic("Setting Amplitude Rank Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        harmonic_number: int = self.harmonic_number_rank_editor
        self.stop_config.rank_harmonic_amplitude_set(rank_number, harmonic_number, value)
        ic("Amplitude Rank Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Attack Time - Harmonic - Rank
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def attack_harmonic_rank_config(self) -> int:
        ic("Getting Attack Harmonic Rank Config...")
        rank_number: int = self.rank_number_editor
        harmonic_number: int = self.harmonic_number_rank_editor
        attack_time: int = self.stop_config.rank_harmonic_attack_time_get(rank_number, harmonic_number)
        ic("Attack Harmonic Rank Config Retrieved.")
        return attack_time

    #-------------------------------------------------------------------------------------------------------------------
    @attack_harmonic_rank_config.setter
    def attack_harmonic_rank_config(self, value: int):
        ic("Setting Attack Harmonic Rank Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        harmonic_number: int = self.harmonic_number_rank_editor
        self.stop_config.rank_harmonic_attack_time_set(rank_number, harmonic_number, value)
        ic("Attack Harmonic Rank Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Decay Time - Harmonic - Rank
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def decay_harmonic_rank_config(self) -> int:
        ic("Getting Decay Harmonic Rank Config...")
        rank_number: int = self.rank_number_editor
        harmonic_number: int = self.harmonic_number_rank_editor
        decay_time: int = self.stop_config.rank_harmonic_decay_time_get(rank_number, harmonic_number)
        ic("Decay Harmonic Rank Config Retrieved.")
        return decay_time

    #-------------------------------------------------------------------------------------------------------------------
    @decay_harmonic_rank_config.setter
    def decay_harmonic_rank_config(self, value: int):
        ic("Setting Decay Harmonic Rank Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        harmonic_number: int = self.harmonic_number_rank_editor
        self.stop_config.rank_harmonic_decay_time_set(rank_number, harmonic_number, value)
        ic("Decay Harmonic Rank Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Sustain Level - Harmonic - Rank
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def sustain_harmonic_rank_config(self) -> int:
        ic("Getting Sustain Harmonic Rank Config...")
        rank_number: int = self.rank_number_editor
        harmonic_number: int = self.harmonic_number_rank_editor
        sustain_level: int = self.stop_config.rank_harmonic_sustain_level_get(rank_number, harmonic_number)
        ic("Sustain Harmonic Rank Config Retrieved.")
        return sustain_level

    #-------------------------------------------------------------------------------------------------------------------
    @sustain_harmonic_rank_config.setter
    def sustain_harmonic_rank_config(self, value: int):
        ic("Setting Sustain Harmonic Rank Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        harmonic_number: int = self.harmonic_number_rank_editor
        self.stop_config.rank_harmonic_sustain_level_set(rank_number, harmonic_number, value)
        ic("Sustain Harmonic Rank Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Release Time - Harmonic - Rank
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def release_harmonic_rank_config(self) -> int:
        ic("Getting Release Harmonic Rank Config...")
        rank_number: int = self.rank_number_editor
        harmonic_number: int = self.harmonic_number_rank_editor
        release_time: int = self.stop_config.rank_harmonic_release_time_get(rank_number, harmonic_number)
        ic("Release Harmonic Rank Config Retrieved.")
        return release_time

    #-------------------------------------------------------------------------------------------------------------------
    @release_harmonic_rank_config.setter
    def release_harmonic_rank_config(self, value: int):
        ic("Setting Release Harmonic Rank Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        harmonic_number: int = self.harmonic_number_rank_editor
        self.stop_config.rank_harmonic_release_time_set(rank_number, harmonic_number, value)

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Attack Time - Rank
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def attack_rank_config(self) -> int:
        ic("Getting Attack Rank Config...")
        rank_number: int = self.rank_number_editor
        attack_time: int = self.stop_config.rank_attack_time_get(rank_number)
        ic("Attack Rank Config Retrieved.")
        return attack_time

    #-------------------------------------------------------------------------------------------------------------------
    @attack_rank_config.setter
    def attack_rank_config(self, value: int):
        ic("Setting Attack Rank Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        self.stop_config.rank_attack_time_set(rank_number, value)
        ic("Attack Rank Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Decay Time - Rank
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def decay_rank_config(self) -> int:
        ic("Getting Decay Rank Config...")
        rank_number: int = self.rank_number_editor
        decay_time: int = self.stop_config.rank_decay_time_get(rank_number)
        ic("Decay Rank Config Retrieved.")
        return decay_time

    #-------------------------------------------------------------------------------------------------------------------
    @decay_rank_config.setter
    def decay_rank_config(self, value: int):
        ic("Setting Decay Rank Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        self.stop_config.rank_decay_time_set(rank_number, value)

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Sustain Level - Rank
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def sustain_rank_config(self) -> int:
        ic("Getting Sustain Rank Config...")
        rank_number: int = self.rank_number_editor
        sustain_level: int = self.stop_config.rank_sustain_level_get(rank_number)
        ic("Sustain Rank Config Retrieved.")
        return sustain_level

    #-------------------------------------------------------------------------------------------------------------------
    @sustain_rank_config.setter
    def sustain_rank_config(self, value: int):
        ic("Setting Sustain Rank Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        self.stop_config.rank_sustain_level_set(rank_number, value)
        ic("Sustain Rank Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Release Time - Rank
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def release_rank_config(self) -> int:
        ic("Getting Release Rank Config...")
        rank_number: int = self.rank_number_editor
        release_time: int = self.stop_config.rank_release_time_get(rank_number)
        ic("Release Rank Config Retrieved.")
        return release_time

    #-------------------------------------------------------------------------------------------------------------------
    @release_rank_config.setter
    def release_rank_config(self, value: int):
        ic("Setting Release Rank Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        self.stop_config.rank_release_time_set(rank_number, value)
        ic("Release Rank Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Note
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def note_config(self) -> str:
        ic("Getting Note Config...")
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        note: str = self.stop_config.note_get(rank_number, pipe_number)
        ic("Note Config Retrieved.")
        return note

    #-------------------------------------------------------------------------------------------------------------------
    @note_config.setter
    def note_config(self, value: str):
        ic("Setting Note Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        self.stop_config.note_set(rank_number, pipe_number, value)
        ic("Note Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Relative Note
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def relative_note_config(self) -> str:
        ic("Getting Relative Note Config...")
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        relative_note: str = self.stop_config.relative_note_get(rank_number, pipe_number)
        ic("Relative Note Config Retrieved.")
        return relative_note

    #-------------------------------------------------------------------------------------------------------------------
    @relative_note_config.setter
    def relative_note_config(self, value: str):
        ic("Setting Relative Note Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        self.stop_config.relative_note_set(rank_number, pipe_number, value)
        ic("Relative Note Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Amplitude - Pipe
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def amplitude_pipe_config(self) -> int:
        ic("Getting Amplitude Pipe Config...")
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        harmonic_number: int = self.harmonic_number_pipe_editor
        amplitude: int = self.stop_config.pipe_harmonic_amplitude_get(rank_number, pipe_number, harmonic_number)
        ic("Amplitude Pipe Config Retrieved.")
        return amplitude

    #-------------------------------------------------------------------------------------------------------------------
    @amplitude_pipe_config.setter
    def amplitude_pipe_config(self, value: int):
        ic("Setting Amplitude Pipe Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        harmonic_number: int = self.harmonic_number_pipe_editor
        self.stop_config.pipe_harmonic_amplitude_set(rank_number, pipe_number, harmonic_number, value)
        ic("Amplitude Pipe Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Attack Time - Harmonic - Pipe
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def attack_harmonic_pipe_config(self) -> int:
        ic("Getting Attack Harmonic Pipe Config...")
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        harmonic_number: int = self.harmonic_number_pipe_editor
        attack_time: int = self.stop_config.pipe_harmonic_attack_time_get(rank_number, pipe_number, harmonic_number)
        ic("Attack Harmonic Pipe Config Retrieved.")
        return attack_time

    #-------------------------------------------------------------------------------------------------------------------
    @attack_harmonic_pipe_config.setter
    def attack_harmonic_pipe_config(self, value: int):
        ic("Setting Attack Harmonic Pipe Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        harmonic_number: int = self.harmonic_number_pipe_editor
        self.stop_config.pipe_harmonic_attack_time_set(rank_number, pipe_number, harmonic_number, value)
        ic("Attack Harmonic Pipe Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Decay Time - Harmonic - Pipe
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def decay_harmonic_pipe_config(self) -> int:
        ic("Getting Decay Harmonic Pipe Config...")
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        harmonic_number: int = self.harmonic_number_pipe_editor
        decay_time: int = self.stop_config.pipe_harmonic_decay_time_get(rank_number, pipe_number, harmonic_number)
        ic("Decay Harmonic Pipe Config Retrieved.")
        return decay_time

    #-------------------------------------------------------------------------------------------------------------------
    @decay_harmonic_pipe_config.setter
    def decay_harmonic_pipe_config(self, value: int):
        ic("Setting Decay Harmonic Pipe Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        harmonic_number: int = self.harmonic_number_pipe_editor
        self.stop_config.pipe_harmonic_decay_time_set(rank_number, pipe_number, harmonic_number, value)
        ic("Decay Harmonic Pipe Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Sustain Level - Harmonic - Pipe
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def sustain_harmonic_pipe_config(self) -> int:
        ic("Getting Sustain Harmonic Pipe Config...")
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        harmonic_number: int = self.harmonic_number_pipe_editor
        sustain_level: int = self.stop_config.pipe_harmonic_sustain_level_get(rank_number, pipe_number, harmonic_number)
        ic("Sustain Harmonic Pipe Config Retrieved.")
        return sustain_level

    #-------------------------------------------------------------------------------------------------------------------
    @sustain_harmonic_pipe_config.setter
    def sustain_harmonic_pipe_config(self, value: int):
        ic("Setting Sustain Harmonic Pipe Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        harmonic_number: int = self.harmonic_number_pipe_editor
        self.stop_config.pipe_harmonic_sustain_level_set(rank_number, pipe_number, harmonic_number, value)
        ic("Sustain Harmonic Pipe Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Release Time - Harmonic - Pipe
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def release_harmonic_pipe_config(self) -> int:
        ic("Getting Release Harmonic Pipe Config...")
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        harmonic_number: int = self.harmonic_number_pipe_editor
        release_time: int = self.stop_config.pipe_harmonic_release_time_get(rank_number, pipe_number, harmonic_number)
        ic("Release Harmonic Pipe Config Retrieved.")
        return release_time

    #-------------------------------------------------------------------------------------------------------------------
    @release_harmonic_pipe_config.setter
    def release_harmonic_pipe_config(self, value: int):
        ic("Setting Release Harmonic Pipe Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        harmonic_number: int = self.harmonic_number_pipe_editor
        self.stop_config.pipe_harmonic_release_time_set(rank_number, pipe_number, harmonic_number, value)
        ic("Release Harmonic Pipe Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Attack Time - Pipe
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def attack_pipe_config(self) -> int:
        ic("Getting Attack Pipe Config...")
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        attack_time: int = self.stop_config.pipe_attack_time_get(rank_number, pipe_number)
        ic("Attack Pipe Config Retrieved.")
        return attack_time

    #-------------------------------------------------------------------------------------------------------------------
    @attack_pipe_config.setter
    def attack_pipe_config(self, value: int):
        ic("Setting Attack Pipe Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        self.stop_config.pipe_attack_time_set(rank_number, pipe_number, value)
        ic("Attack Pipe Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Decay Time - Pipe
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def decay_pipe_config(self) -> int:
        ic("Getting Decay Pipe Config...")
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        decay_time: int = self.stop_config.pipe_decay_time_get(rank_number, pipe_number)
        ic("Decay Pipe Config Retrieved.")
        return decay_time

    #-------------------------------------------------------------------------------------------------------------------
    @decay_pipe_config.setter
    def decay_pipe_config(self, value: int):
        ic("Setting Decay Pipe Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        self.stop_config.pipe_decay_time_set(rank_number, pipe_number, value)
        ic("Decay Pipe Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Sustain Level - Pipe
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def sustain_pipe_config(self) -> int:
        ic("Getting Sustain Pipe Config...")
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        sustain_level: int = self.stop_config.pipe_sustain_level_get(rank_number, pipe_number)
        ic("Sustain Pipe Config Retrieved.")
        return sustain_level

    #-------------------------------------------------------------------------------------------------------------------
    @sustain_pipe_config.setter
    def sustain_pipe_config(self, value: int):
        ic("Setting Sustain Pipe Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        self.stop_config.pipe_sustain_level_set(rank_number, pipe_number, value)
        ic("Sustain Pipe Config Set.")

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Release Time - Pipe
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    @property
    def release_pipe_config(self) -> int:
        ic("Getting Release Pipe Config...")
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        release_time: int = self.stop_config.pipe_release_time_get(rank_number, pipe_number)
        ic("Release Pipe Config Retrieved.")
        return release_time

    #-------------------------------------------------------------------------------------------------------------------
    @release_pipe_config.setter
    def release_pipe_config(self, value: int):
        ic("Setting Release Pipe Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        self.stop_config.pipe_release_time_set(rank_number, pipe_number, value)
        ic("Release Pipe Config Set.")


if __name__ == "__main__":
    log_file.start_logging()
    app = QApplication([])
    ic(app)
    stop_editor_ui = StopEditorUI()
    stop_editor_ui.stop_editor.show()
    app.exec()
