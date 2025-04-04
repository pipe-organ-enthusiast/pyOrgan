"""UI Class"""
from gui import StopEditor
from organ import organlib
from config_editors import StopConfig
import log_file  # type: ignore
#-----------------------------------------------------------------------------------------------------------------------
from PySide6.QtWidgets import QApplication, QFileDialog
from icecream import ic  # type: ignore


#=======================================================================================================================
# Stop Editor
#=======================================================================================================================
class StopEditorUI:
    def __init__(self) -> None:
        ic("Initializing Stop Editor UI...")
        self.editor: StopEditor = StopEditor()
        self.config: StopConfig = StopConfig()
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
        self.config.init_default_config()
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
        self.editor.stop_name = self.config.stop_name_get()
        self.editor.stop_family = self.config.stop_family_get()
        self.editor.organ_division = self.config.organ_division_get()
        self.editor.number_ranks = self.config.number_ranks_get()
        self.editor.rank_series = self.config.rank_series_get()
        rank_number: int = self.editor.rank_number
        self.editor.rank_size = self.config.rank_size_get(rank_number)
        self.editor.number_pipes = self.config.number_pipes_get(rank_number)
        self.editor.pipe_type = self.config.pipe_type_get(rank_number)
        self.editor.starting_note = self.config.starting_note_get(rank_number)
        self.editor.frequency_offset = self.config.frequency_offset_get(rank_number)
        self.editor.number_harmonics = self.config.number_harmonics_get(rank_number)
        harmonic_number: int = self.editor.harmonic_number_rank
        self.editor.amplitude_rank = self.config.rank_harmonic_amplitude_get(
            rank_number, harmonic_number
        )
        self.editor.attack_time_harmonic_rank = self.config.rank_harmonic_attack_time_get(
            rank_number, harmonic_number
        )
        self.editor.decay_time_harmonic_rank = self.config.rank_harmonic_decay_time_get(
            rank_number, harmonic_number
        )
        self.editor.sustain_level_harmonic_rank = self.config.rank_harmonic_sustain_level_get(
            rank_number, harmonic_number
        )
        self.editor.release_time_harmonic_rank = self.config.rank_harmonic_release_time_get(
            rank_number, harmonic_number
        )
        self.editor.attack_time_rank = self.config.rank_attack_time_get(rank_number)
        self.editor.decay_time_rank = self.config.rank_decay_time_get(rank_number)
        self.editor.sustain_level_rank = self.config.rank_sustain_level_get(rank_number)
        self.editor.release_time_rank = self.config.rank_release_time_get(rank_number)
        pipe_number: int = self.editor.pipe_number
        self.editor.note = self.config.note_get(
            rank_number, pipe_number
        )
        self.editor.relative_note = self.config.relative_note_get(
            rank_number, pipe_number
        )
        self.editor.amplitude_pipe = self.config.pipe_harmonic_amplitude_get(
            rank_number, pipe_number, harmonic_number
        )
        self.editor.attack_time_harmonic_pipe = self.config.pipe_harmonic_attack_time_get(
            rank_number, pipe_number, harmonic_number
        )
        self.editor.decay_time_harmonic_pipe = self.config.pipe_harmonic_decay_time_get(
            rank_number, pipe_number, harmonic_number
        )
        self.editor.sustain_level_harmonic_pipe = self.config.pipe_harmonic_sustain_level_get(
            rank_number, pipe_number, harmonic_number
        )
        self.editor.release_time_harmonic_pipe = self.config.pipe_harmonic_release_time_get(
            rank_number, pipe_number, harmonic_number
        )
        self.editor.attack_time_pipe = self.config.pipe_attack_time_get(
            rank_number, pipe_number
        )
        self.editor.decay_time_pipe = self.config.pipe_decay_time_get(
            rank_number, pipe_number
        )
        self.editor.sustain_level_pipe = self.config.pipe_sustain_level_get(
            rank_number, pipe_number
        )
        self.editor.release_time_pipe = self.config.pipe_release_time_get(
            rank_number, pipe_number
        )
        ic("UI Editor Data Loaded.")

    #*******************************************************************************************************************
    # Initialize UI Configuration
    #*******************************************************************************************************************
    def __init_ui(self) -> None:
        ic("Initializing UI...")
        self.editor.stop_name_change_connect(self.__update_stop_name)
        self.editor.stop_family_change_connect(self.__update_stop_family)
        self.editor.organ_division_change_connect(self.__update_organ_division)
        self.editor.number_ranks_change_connect(self.__update_number_ranks)
        self.editor.rank_series_change_connect(self.__update_rank_series)
        self.editor.rank_number_change_connect(self.__update_rank_number)
        self.editor.rank_size_change_connect(self.__update_rank_size)
        self.editor.number_pipes_change_connect(self.__update_number_pipes)
        self.editor.pipe_type_change_connection(self.__update_pipe_type)
        self.editor.starting_note_change_connection(self.__update_starting_note)
        self.editor.frequency_offset_change_connection(self.__update_frequency_offset)
        self.editor.number_harmonics_change_connection(self.__update_number_harmonics)
        self.editor.harmonic_number_rank_change_connect(self.__update_harmonic_number_rank)
        self.editor.amplitude_rank_change_connect(self.__update_rank_amplitude)
        self.editor.attack_time_rank_harmonic_change_connect(self.__update_rank_harmonic_attack)
        self.editor.decay_time_rank_harmonic_change_connect(self.__update_rank_harmonic_decay)
        self.editor.sustain_level_rank_harmonic_change_connect(self.__update_rank_harmonic_sustain)
        self.editor.release_time_rank_harmonic_change_connect(self.__update_rank_harmonic_release)
        self.editor.attack_time_rank_change_connect(self.__update_rank_attack)
        self.editor.decay_time_rank_change_connect(self.__update_rank_decay)
        self.editor.sustain_level_rank_change_connect(self.__update_rank_sustain)
        self.editor.release_time_rank_change_connect(self.__update_rank_release)
        self.editor.rank_number_pipe_change_connect(self.__update_rank_number_pipe)
        self.editor.pipe_number_change_connect(self.__update_pipe_number)
        self.editor.note_change_connect(self.__update_note)
        self.editor.relative_note_change_connect(self.__update_relative_note)
        self.editor.harmonic_number_pipe_change_connect(self.__update_harmonic_number_pipe)
        self.editor.amplitude_pipe_change_connect(self.__update_pipe_amplitude)
        self.editor.attack_time_pipe_harmonic_change_connect(self.__update_pipe_harmonic_attack)
        self.editor.decay_time_pipe_harmonic_change_connect(self.__update_pipe_harmonic_decay)
        self.editor.sustain_level_pipe_harmonic_change_connect(self.__update_pipe_harmonic_sustain)
        self.editor.release_time_pipe_harmonic_change_connect(self.__update_pipe_harmonic_release)
        self.editor.attack_time_pipe_change_connect(self.__update_pipe_attack)
        self.editor.decay_time_pipe_change_connect(self.__update_pipe_decay)
        self.editor.sustain_level_pipe_change_connect(self.__update_pipe_sustain)
        self.editor.release_time_pipe_change_connect(self.__update_pipe_release)
        self.editor.load_stop_action_connect(self.__load_stop)
        self.editor.cancel_changes_action_connect(self.__cancel_changes)
        self.editor.save_stop_action_connect(self.__save_stop)
        ic("UI Initialized.")

    #===================================================================================================================
    # Actions
    #===================================================================================================================
    def __update_stop_name(self) -> None:
        ic("Updating Stop Name...")
        stop_name: str = self.editor.stop_name
        self.config.stop_name_set(stop_name)
        self.editor.update_stop_header()
        ic("Stop Name Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_stop_family(self) -> None:
        ic("Updating Stop Family...")
        stop_family: str = self.editor.stop_family
        self.config.stop_family_set(stop_family)
        ic("Stop Family Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_organ_division(self) -> None:
        ic("Updating Organ Division...")
        organ_division: str = self.editor.organ_division
        self.config.organ_division_set(organ_division)
        ic("Organ Division Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_number_ranks(self) -> None:
        ic("Updating Number of Ranks...")
        number_ranks: int = self.editor.number_ranks
        self.config.number_ranks_set(number_ranks)
        self.editor.update_number_ranks()
        self.editor.update_stop_header()
        ic("Number of Ranks Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_series(self) -> None:
        ic("Updating Rank Series...")
        rank_series: str = self.editor.rank_series
        self.config.rank_series_set(rank_series)
        self.editor.update_rank_sizes()
        ic("Rank Series Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_number_general(self) -> None:
        ic("Updating Rank Settings...")
        rank_number: int = self.editor.rank_number
        self.editor.rank_size = self.config.rank_size_get(rank_number)
        self.editor.number_pipes = self.config.number_pipes_get(rank_number)
        self.editor.pipe_type = self.config.pipe_type_get(rank_number)
        self.editor.starting_note = self.config.starting_note_get(rank_number)
        self.editor.frequency_offset = self.config.frequency_offset_get(rank_number)
        self.editor.number_harmonics = self.config.number_harmonics_get(rank_number)
        self.editor.harmonic_number_rank = 1
        self.__update_harmonic_number()
        self.editor.attack_time_rank = self.config.rank_attack_time_get(rank_number)
        self.editor.decay_time_rank = self.config.rank_decay_time_get(rank_number)
        self.editor.sustain_level_rank = self.config.rank_sustain_level_get(rank_number)
        self.editor.release_time_rank = self.config.rank_release_time_get(rank_number)
        self.editor.pipe_number = 1
        self.__update_pipe_number()
        ic("Rank Settings Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_number(self) -> None:
        ic("Updating Rank Number...")
        self.editor.update_rank_number()
        self.__update_rank_number_general()
        ic("Rank Number Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_size(self) -> None:
        ic("Updating Rank Size...")

        self.config.rank_size_set(
            self.editor.rank_number, self.editor.rank_size
        )
        ic("Rank Size Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_number_pipes(self) -> None:
        ic("Updating Number of Pipes...")
        self.config.number_pipes_set(
            self.editor.rank_number, self.editor.number_pipes
        )
        self.editor.update_number_pipes()
        ic("Number of Pipes Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_type(self) -> None:
        ic("Updating Pipe Type...")
        self.config.pipe_type_set(
            self.editor.rank_number, self.editor.pipe_type
        )
        ic("Pipe Type Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_starting_note(self) -> None:
        ic("Updating Starting Note...")
        self.config.starting_note_set(
            self.editor.rank_number, self.editor.starting_note
        )
        ic("Starting Note Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_frequency_offset(self) -> None:
        ic("Updating Frequency Offset...")
        self.config.frequency_offset_set(
            self.editor.rank_number, self.editor.frequency_offset
        )
        ic("Frequency Offset Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_number_harmonics(self) -> None:
        ic("Updating Number of Harmonics...")
        self.config.number_harmonics_set(
            self.editor.rank_number, self.editor.number_harmonics
        )
        self.editor.update_number_harmonics()
        ic("Number of Harmonics Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_harmonic_number(self) -> None:
        ic("Updating Harmonic Settings...")
        self.editor.amplitude_rank = self.config.rank_harmonic_amplitude_get(
            self.editor.rank_number, self.editor.harmonic_number_rank
        )
        self.editor.attack_time_harmonic_rank = self.config.rank_harmonic_attack_time_get(
            self.editor.rank_number, self.editor.harmonic_number_rank
        )
        self.editor.decay_time_harmonic_rank = self.config.rank_harmonic_decay_time_get(
            self.editor.rank_number, self.editor.harmonic_number_rank
        )
        self.editor.sustain_level_harmonic_rank = self.config.rank_harmonic_sustain_level_get(
            self.editor.rank_number, self.editor.harmonic_number_rank
        )
        self.editor.release_time_harmonic_rank = self.config.rank_harmonic_release_time_get(
            self.editor.rank_number, self.editor.harmonic_number_rank
        )
        self.editor.amplitude_pipe = self.config.pipe_harmonic_amplitude_get(
            self.editor.rank_number, self.editor.pipe_number, self.editor.harmonic_number_pipe
        )
        self.editor.attack_time_harmonic_pipe = self.config.pipe_harmonic_attack_time_get(
            self.editor.rank_number, self.editor.pipe_number, self.editor.harmonic_number_pipe
        )
        self.editor.decay_time_harmonic_pipe = self.config.pipe_harmonic_decay_time_get(
            self.editor.rank_number, self.editor.pipe_number, self.editor.harmonic_number_pipe
        )
        self.editor.sustain_level_harmonic_pipe = self.config.pipe_harmonic_sustain_level_get(
            self.editor.rank_number, self.editor.pipe_number, self.editor.harmonic_number_pipe
        )
        self.editor.release_time_harmonic_pipe = self.config.pipe_harmonic_release_time_get(
            self.editor.rank_number, self.editor.pipe_number, self.editor.harmonic_number_pipe
        )
        ic("Harmonic Settings Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_harmonic_number_rank(self) -> None:
        ic("Updating Harmonic Number Rank...")
        self.editor.update_harmonic_number_rank()
        self.__update_harmonic_number()
        ic("Harmonic Number Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_amplitude(self) -> None:
        ic("Updating Amplitude Rank...")
        self.config.rank_harmonic_amplitude_set(
            self.editor.rank_number, self.editor.harmonic_number_rank, self.editor.amplitude_rank
        )
        ic("Amplitude Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_harmonic_attack(self) -> None:
        ic("Updating Attack Harmonic Rank...")
        self.config.rank_harmonic_attack_time_set(
            self.editor.rank_number, self.editor.harmonic_number_rank, self.editor.attack_time_harmonic_rank
        )
        ic("Attack Harmonic Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_harmonic_decay(self) -> None:
        ic("Updating Decay Harmonic Rank...")
        self.config.rank_harmonic_decay_time_set(
            self.editor.rank_number, self.editor.harmonic_number_rank, self.editor.decay_time_harmonic_rank
        )
        ic("Decay Harmonic Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_harmonic_sustain(self) -> None:
        ic("Updating Sustain Harmonic Rank...")
        self.config.rank_harmonic_sustain_level_set(
            self.editor.rank_number, self.editor.harmonic_number_rank, self.editor.sustain_level_harmonic_rank
        )
        ic("Sustain Harmonic Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_harmonic_release(self) -> None:
        ic("Updating Release Harmonic Rank...")
        self.config.rank_harmonic_release_time_set(
            self.editor.rank_number, self.editor.harmonic_number_rank, self.editor.release_time_harmonic_rank
        )
        ic("Release Harmonic Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_attack(self) -> None:
        ic("Updating Attack Rank...")
        self.config.rank_attack_time_set(
            self.editor.rank_number, self.editor.attack_time_rank
        )
        ic("Attack Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_decay(self) -> None:
        ic("Updating Decay Rank...")
        self.config.rank_decay_time_set(
            self.editor.rank_number, self.editor.decay_time_rank
        )
        ic("Decay Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_sustain(self) -> None:
        ic("Updating Sustain Rank...")
        self.config.rank_sustain_level_set(
            self.editor.rank_number, self.editor.sustain_level_rank
        )
        ic("Sustain Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_release(self) -> None:
        ic("Updating Release Rank...")
        self.config.rank_release_time_set(
            self.editor.rank_number, self.editor.release_time_rank
        )
        ic("Release Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_number_pipe(self) -> None:
        ic("Updating Rank Number Pipe...")
        self.editor.update_rank_number_pipe()
        self.__update_rank_number_general()
        ic("Rank Number Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_number(self) -> None:
        ic("Updating Pipe Settings...")
        self.editor.note = self.config.note_get(self.editor.rank_number, self.editor.pipe_number)
        self.editor.relative_note = self.config.relative_note_get(
            self.editor.rank_number, self.editor.pipe_number
        )
        self.harmonic_number_pipe_editor = 1
        self.__update_harmonic_number()
        self.editor.attack_time_pipe = self.config.pipe_attack_time_get(
            self.editor.rank_number, self.editor.pipe_number
        )
        self.editor.decay_time_pipe = self.config.pipe_decay_time_get(
            self.editor.rank_number, self.editor.pipe_number
        )
        self.editor.sustain_level_pipe = self.config.pipe_sustain_level_get(
            self.editor.rank_number, self.editor.pipe_number
        )
        self.editor.release_time_pipe = self.config.pipe_release_time_get(
            self.editor.rank_number, self.editor.pipe_number
        )
        ic("Pipe Settings Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_note(self) -> None:
        ic("Updating Note...")
        self.config.note_set(
            self.editor.rank_number, self.editor.pipe_number, self.editor.note
        )
        ic("Note Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_relative_note(self) -> None:
        ic("Updating Relative Note...")
        note_index = organlib.NOTES.index(self.editor.note)
        ic(note_index)
        notes: tuple[str, ...] = organlib.NOTES[note_index:]
        ic(notes)
        self.config.update_relative_notes(
            self.editor.rank_number, self.editor.pipe_number, notes
        )
        ic("Relative Note Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_harmonic_number_pipe(self) -> None:
        ic("Updating Harmonic Number Pipe...")
        self.editor.update_harmonic_number_pipe()
        self.__update_harmonic_number()
        ic("Harmonic Number Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_amplitude(self) -> None:
        ic("Updating Amplitude Pipe...")
        rank_number: int = self.editor.rank_number
        pipe_number: int = self.editor.pipe_number
        harmonic_number: int = self.editor.harmonic_number_pipe
        amplitude: float = self.editor.amplitude_pipe
        self.config.pipe_harmonic_amplitude_set(
            rank_number, pipe_number, harmonic_number, amplitude
        )
        ic("Amplitude Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_attack(self) -> None:
        ic("Updating Attack Pipe...")
        rank_number: int = self.editor.rank_number
        pipe_number: int = self.editor.pipe_number
        attack_time: float = self.editor.attack_time_pipe
        self.config.pipe_attack_time_set(
            rank_number, pipe_number, attack_time
        )
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
        self.config.load_file(self.config_file)
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
        stop_header: str = self.editor.stop_header
        if stop_header != "":
            self.config_file = f"src/config/stops/{stop_header}.json"
            self.config.save_file(self.config_file)
            ic("Stop Saved.")
        else:
            ic("Stop Header is empty. Cannot save stop.")
        ic("Finished Saving Stop.")

        ic("Setting Release Pipe Config...")
        ic(value)
        rank_number: int = self.rank_number_editor
        pipe_number: int = self.pipe_number_editor
        self.config.pipe_release_time_set(rank_number, pipe_number, value)
        ic("Release Pipe Config Set.")

#=======================================================================================================================
# Executable
#=======================================================================================================================
if __name__ == "__main__":
    log_file.start_logging()
    app = QApplication([])
    ic(app)
    stop_editor_ui = StopEditorUI()
    stop_editor_ui.editor.show()
    app.exec()
