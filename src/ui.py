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
        #---------------------------------------------------------------------------------------------------------------
        # Rank Number
        #---------------------------------------------------------------------------------------------------------------
        self.editor.rank_number_spin_signal_blocking()
        self.editor.rank_number = 1
        self.editor.rank_number_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Harmonic Number - Rank
        #---------------------------------------------------------------------------------------------------------------
        self.editor.harmonic_number_rank_spin_signal_blocking()
        self.editor.harmonic_number_rank = 1
        self.editor.harmonic_number_rank_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Rank Number - Pipe
        #---------------------------------------------------------------------------------------------------------------
        self.editor.rank_number_pipe_spin_signal_blocking()
        self.editor.rank_number_pipe = 1
        self.editor.rank_number_pipe_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Pipe Number
        #---------------------------------------------------------------------------------------------------------------
        self.editor.pipe_number_spin_signal_blocking()
        self.editor.pipe_number = 1
        self.editor.pipe_number_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Harmonic Number - Pipe
        #---------------------------------------------------------------------------------------------------------------
        self.editor.harmonic_number_pipe_spin_signal_blocking()
        self.editor.harmonic_number_pipe = 1
        self.editor.harmonic_number_pipe_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        ic("Setting Numbers Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def __load_ui_editor_data(self) -> None:
        ic("Loading UI Editor Data...")
        #---------------------------------------------------------------------------------------------------------------
        # Stop Name
        #---------------------------------------------------------------------------------------------------------------
        self.editor.stop_name_combo_signal_blocking()
        self.editor.stop_name = self.config.stop_name_get()
        self.editor.stop_name_combo_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Stop Family
        #---------------------------------------------------------------------------------------------------------------
        self.editor.stop_family_combo_signal_blocking()
        self.editor.stop_family = self.config.stop_family_get()
        self.editor.stop_family_combo_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Organ Division
        #---------------------------------------------------------------------------------------------------------------
        self.editor.organ_division_combo_signal_blocking()
        self.editor.organ_division = self.config.organ_division_get()
        self.editor.organ_division_combo_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Number of Ranks
        #---------------------------------------------------------------------------------------------------------------
        self.editor.number_ranks_spin_signal_blocking()
        self.editor.number_ranks = self.config.number_ranks_get()
        self.editor.number_ranks_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Rank Series
        #---------------------------------------------------------------------------------------------------------------
        self.editor.rank_series_combo_signal_blocking()
        self.editor.rank_series = self.config.rank_series_get()
        self.editor.rank_series_combo_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        rank_number: int = self.editor.rank_number
        #---------------------------------------------------------------------------------------------------------------
        # Rank Size
        #---------------------------------------------------------------------------------------------------------------
        self.editor.rank_size_combo_signal_blocking()
        self.editor.rank_size = self.config.rank_size_get(rank_number)
        self.editor.rank_size_combo_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Number of Pipes
        #---------------------------------------------------------------------------------------------------------------
        self.editor.number_pipes_spin_signal_blocking()
        self.editor.number_pipes = self.config.number_pipes_get(rank_number)
        self.editor.number_pipes_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Pipe Type
        #---------------------------------------------------------------------------------------------------------------
        self.editor.pipe_type_combo_signal_blocking()
        self.editor.pipe_type = self.config.pipe_type_get(rank_number)
        self.editor.pipe_type_combo_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Starting Note
        #---------------------------------------------------------------------------------------------------------------
        self.editor.starting_note_combo_signal_blocking()
        self.editor.starting_note = self.config.starting_note_get(rank_number)
        self.editor.starting_note_combo_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Frequency Offset
        #---------------------------------------------------------------------------------------------------------------
        self.editor.frequency_offset_spin_signal_blocking()
        self.editor.frequency_offset = self.config.frequency_offset_get(rank_number)
        self.editor.frequency_offset_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Number of Harmonics
        #---------------------------------------------------------------------------------------------------------------
        self.editor.number_harmonics_spin_signal_blocking()
        self.editor.number_harmonics = self.config.number_harmonics_get(rank_number)
        self.editor.number_harmonics_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        harmonic_number: int = self.editor.harmonic_number_rank
        #---------------------------------------------------------------------------------------------------------------
        # Amplitude - Rank
        #---------------------------------------------------------------------------------------------------------------
        self.editor.amplitude_rank_spin_signal_blocking()
        self.editor.amplitude_rank = self.config.rank_harmonic_amplitude_get(
            rank_number, harmonic_number
        )
        self.editor.amplitude_rank_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Attack Time - Rank Harmonic
        #---------------------------------------------------------------------------------------------------------------
        self.editor.attack_time_rank_harmonic_spin_signal_blocking()
        self.editor.attack_time_rank_harmonic = self.config.rank_harmonic_attack_time_get(
            rank_number, harmonic_number
        )
        self.editor.attack_time_rank_harmonic_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Decay Time - Rank Harmonic
        #---------------------------------------------------------------------------------------------------------------
        self.editor.decay_time_rank_harmonic_spin_signal_blocking()
        self.editor.decay_time_rank_harmonic = self.config.rank_harmonic_decay_time_get(
            rank_number, harmonic_number
        )
        self.editor.decay_time_rank_harmonic_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Sustain Level - Rank Harmonic
        #---------------------------------------------------------------------------------------------------------------
        self.editor.sustain_level_rank_harmonic_spin_signal_blocking()
        self.editor.sustain_level_rank_harmonic = self.config.rank_harmonic_sustain_level_get(
            rank_number, harmonic_number
        )
        self.editor.sustain_level_rank_harmonic_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Release Time - Rank Harmonic
        #---------------------------------------------------------------------------------------------------------------
        self.editor.release_time_rank_harmonic_spin_signal_blocking()
        self.editor.release_time_rank_harmonic = self.config.rank_harmonic_release_time_get(
            rank_number, harmonic_number
        )
        self.editor.release_time_rank_harmonic_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Attack Time - Pipe
        #---------------------------------------------------------------------------------------------------------------
        self.editor.attack_time_rank_spin_signal_blocking()
        self.editor.attack_time_rank = self.config.rank_attack_time_get(rank_number)
        self.editor.attack_time_rank_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Decay Time - Pipe
        #---------------------------------------------------------------------------------------------------------------
        self.editor.decay_time_rank_spin_signal_blocking()
        self.editor.decay_time_rank = self.config.rank_decay_time_get(rank_number)
        self.editor.decay_time_rank_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Sustain Level - Pipe
        #---------------------------------------------------------------------------------------------------------------
        self.editor.sustain_level_rank_spin_signal_blocking()
        self.editor.sustain_level_rank = self.config.rank_sustain_level_get(rank_number)
        self.editor.sustain_level_rank_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Release Time - Pipe
        #---------------------------------------------------------------------------------------------------------------
        self.editor.release_time_rank_spin_signal_blocking()
        self.editor.release_time_rank = self.config.rank_release_time_get(rank_number)
        self.editor.release_time_rank_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Rank Number Pipe
        #---------------------------------------------------------------------------------------------------------------
        self.editor.rank_number_pipe_spin_signal_blocking()
        self.editor.rank_number_pipe = self.editor.rank_number
        self.editor.rank_number_pipe_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        pipe_number: int = self.editor.pipe_number
        #---------------------------------------------------------------------------------------------------------------
        # Note
        #---------------------------------------------------------------------------------------------------------------
        self.editor.note_combo_signal_blocking()
        self.editor.note = self.config.note_get(
            rank_number, pipe_number
        )
        self.editor.note_combo_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Relative Note
        #---------------------------------------------------------------------------------------------------------------
        self.editor.relative_note_combo_signal_blocking()
        self.editor.relative_note = self.config.relative_note_get(
            rank_number, pipe_number
        )
        self.editor.relative_note_combo_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Amplitude - Pipe
        #---------------------------------------------------------------------------------------------------------------
        self.editor.amplitude_pipe_spin_signal_blocking()
        self.editor.amplitude_pipe = self.config.pipe_harmonic_amplitude_get(
            rank_number, pipe_number, harmonic_number
        )
        self.editor.amplitude_pipe_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Attack Time - Pipe Harmonic
        #---------------------------------------------------------------------------------------------------------------
        self.editor.attack_time_pipe_harmonic_spin_signal_blocking()
        self.editor.attack_time_pipe_harmonics = self.config.pipe_harmonic_attack_time_get(
            rank_number, pipe_number, harmonic_number
        )
        self.editor.attack_time_pipe_harmonic_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Decay Time - Pipe Harmonic
        #---------------------------------------------------------------------------------------------------------------
        self.editor.decay_time_pipe_harmonic_spin_signal_blocking()
        self.editor.decay_time_pipe_harmonics = self.config.pipe_harmonic_decay_time_get(
            rank_number, pipe_number, harmonic_number
        )
        self.editor.decay_time_pipe_harmonic_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Sustain Level - Pipe Harmonic
        #---------------------------------------------------------------------------------------------------------------
        self.editor.sustain_level_pipe_harmonic_spin_signal_blocking()
        self.editor.sustain_level_pipe_harmonics = self.config.pipe_harmonic_sustain_level_get(
            rank_number, pipe_number, harmonic_number
        )
        self.editor.sustain_level_pipe_harmonic_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Release Time - Pipe Harmonic
        #---------------------------------------------------------------------------------------------------------------
        self.editor.release_time_pipe_harmonics = self.config.pipe_harmonic_release_time_get(
            rank_number, pipe_number, harmonic_number
        )
        self.editor.release_time_pipe_harmonic_spin_signal_blocking()
        #---------------------------------------------------------------------------------------------------------------
        # Attack Time - Pipe
        #---------------------------------------------------------------------------------------------------------------
        self.editor.attack_time_pipe_spin_signal_blocking()
        self.editor.attack_time_pipe = self.config.pipe_attack_time_get(
            rank_number, pipe_number
        )
        self.editor.attack_time_pipe_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Decay Time - Pipe
        #---------------------------------------------------------------------------------------------------------------
        self.editor.decay_time_pipe_spin_signal_blocking()
        self.editor.decay_time_pipe = self.config.pipe_decay_time_get(
            rank_number, pipe_number
        )
        self.editor.decay_time_pipe_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Sustain Level - Pipe
        #---------------------------------------------------------------------------------------------------------------
        self.editor.sustain_level_pipe_spin_signal_blocking()
        self.editor.sustain_level_pipe = self.config.pipe_sustain_level_get(
            rank_number, pipe_number
        )
        self.editor.sustain_level_pipe_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Release Time - Pipe
        #---------------------------------------------------------------------------------------------------------------
        self.editor.release_time_pipe_spin_signal_blocking()
        self.editor.release_time_pipe = self.config.pipe_release_time_get(
            rank_number, pipe_number
        )
        self.editor.release_time_pipe_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
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
        #---------------------------------------------------------------------------------------------------------------
        rank_number: int = self.editor.rank_number
        #---------------------------------------------------------------------------------------------------------------
        # Rank Size
        #---------------------------------------------------------------------------------------------------------------
        self.editor.rank_size_combo_signal_blocking()
        self.editor.rank_size = self.config.rank_size_get(rank_number)
        self.editor.rank_size_combo_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Number of Pipes
        #---------------------------------------------------------------------------------------------------------------
        self.editor.number_pipes_spin_signal_blocking()
        self.editor.number_pipes = self.config.number_pipes_get(rank_number)
        self.editor.number_pipes_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Pipe Type
        #---------------------------------------------------------------------------------------------------------------
        self.editor.pipe_type_combo_signal_blocking()
        self.editor.pipe_type = self.config.pipe_type_get(rank_number)
        self.editor.pipe_type_combo_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Starting Note
        #---------------------------------------------------------------------------------------------------------------
        self.editor.starting_note_combo_signal_blocking()
        self.editor.starting_note = self.config.starting_note_get(rank_number)
        self.editor.starting_note_combo_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Frequency Offset
        #---------------------------------------------------------------------------------------------------------------
        self.editor.frequency_offset_spin_signal_blocking()
        self.editor.frequency_offset = self.config.frequency_offset_get(rank_number)
        self.editor.frequency_offset_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Number of Harmonics
        #---------------------------------------------------------------------------------------------------------------
        self.editor.number_harmonics_spin_signal_blocking()
        self.editor.number_harmonics = self.config.number_harmonics_get(rank_number)
        self.editor.number_harmonics_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Harmonic Number
        #---------------------------------------------------------------------------------------------------------------
        self.editor.harmonic_number_rank_spin_signal_blocking()
        self.editor.harmonic_number_rank = 1
        self.editor.harmonic_number_rank_spin_signal_unblocking()
        self.__update_harmonic_number()
        #---------------------------------------------------------------------------------------------------------------
        # Attack Time
        #---------------------------------------------------------------------------------------------------------------
        self.editor.attack_time_rank_spin_signal_blocking()
        self.editor.attack_time_rank = self.config.rank_attack_time_get(rank_number)
        self.editor.attack_time_rank_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Decay Time
        #---------------------------------------------------------------------------------------------------------------
        self.editor.decay_time_rank_spin_signal_blocking()
        self.editor.decay_time_rank = self.config.rank_decay_time_get(rank_number)
        self.editor.decay_time_rank_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Sustain Level
        #---------------------------------------------------------------------------------------------------------------
        self.editor.sustain_level_rank_spin_signal_blocking()
        self.editor.sustain_level_rank = self.config.rank_sustain_level_get(rank_number)
        self.editor.sustain_level_rank_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Release Time
        #---------------------------------------------------------------------------------------------------------------
        self.editor.release_time_rank_spin_signal_blocking()
        self.editor.release_time_rank = self.config.rank_release_time_get(rank_number)
        self.editor.release_time_rank_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        self.editor.pipe_number = 1
        self.__update_pipe_number()
        #---------------------------------------------------------------------------------------------------------------
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
        rank_number: int = self.editor.rank_number
        rank_size: str = self.editor.rank_size
        self.config.rank_size_set(rank_number, rank_size)
        ic("Rank Size Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_number_pipes(self) -> None:
        ic("Updating Number of Pipes...")
        rank_number: int = self.editor.rank_number
        number_pipes: int = self.editor.number_pipes
        self.config.number_pipes_set(rank_number, number_pipes)
        self.editor.update_number_pipes()
        ic("Number of Pipes Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_type(self) -> None:
        ic("Updating Pipe Type...")
        rank_number: int = self.editor.rank_number
        pipe_type: str = self.editor.pipe_type
        self.config.pipe_type_set(rank_number, pipe_type)
        ic("Pipe Type Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_starting_note(self) -> None:
        ic("Updating Starting Note...")
        rank_number: int = self.editor.rank_number
        starting_note: str = self.editor.starting_note
        self.config.starting_note_set(rank_number, starting_note)
        ic("Starting Note Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_frequency_offset(self) -> None:
        ic("Updating Frequency Offset...")
        rank_number: int = self.editor.rank_number
        frequency_offset: float = self.editor.frequency_offset
        self.config.frequency_offset_set(rank_number, frequency_offset)
        ic("Frequency Offset Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_number_harmonics(self) -> None:
        ic("Updating Number of Harmonics...")
        rank_number: int = self.editor.rank_number
        number_harmonics: int = self.editor.number_harmonics
        self.config.number_harmonics_set(rank_number, number_harmonics)
        self.editor.update_number_harmonics()
        ic("Number of Harmonics Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_harmonic_number(self) -> None:
        ic("Updating Harmonic Settings...")
        #===============================================================================================================
        rank_number: int = self.editor.rank_number
        pipe_number: int = self.editor.pipe_number
        harmonic_number: int = self.editor.harmonic_number_rank
        #===============================================================================================================
        # Rank
        #===============================================================================================================
        #---------------------------------------------------------------------------------------------------------------
        # Amplitude
        #---------------------------------------------------------------------------------------------------------------
        self.editor.amplitude_rank_spin_signal_blocking()
        self.editor.amplitude_rank = self.config.rank_harmonic_amplitude_get(
            rank_number, harmonic_number
        )
        self.editor.amplitude_rank_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Attack Time
        #---------------------------------------------------------------------------------------------------------------
        self.editor.attack_time_rank_harmonic_spin_signal_blocking()
        self.editor.attack_time_rank_harmonic = self.config.rank_harmonic_attack_time_get(
            rank_number, harmonic_number
        )
        self.editor.attack_time_rank_harmonic_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Decay Time
        #---------------------------------------------------------------------------------------------------------------
        self.editor.decay_time_rank_harmonic_spin_signal_blocking()
        self.editor.decay_time_rank_harmonic = self.config.rank_harmonic_decay_time_get(
            rank_number, harmonic_number
        )
        self.editor.decay_time_rank_harmonic_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Sustain Level
        #---------------------------------------------------------------------------------------------------------------
        self.editor.sustain_level_rank_harmonic_spin_signal_blocking()
        self.editor.sustain_level_rank_harmonic = self.config.rank_harmonic_sustain_level_get(
            rank_number, harmonic_number
        )
        self.editor.sustain_level_rank_harmonic_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Release Time
        #---------------------------------------------------------------------------------------------------------------
        self.editor.release_time_rank_harmonic_spin_signal_blocking()
        self.editor.release_time_rank_harmonic = self.config.rank_harmonic_release_time_get(
            rank_number, harmonic_number
        )
        self.editor.release_time_rank_harmonic_spin_signal_unblocking()
        #===============================================================================================================
        # Pipe
        #===============================================================================================================
        #---------------------------------------------------------------------------------------------------------------
        # Amplitude
        #---------------------------------------------------------------------------------------------------------------
        self.editor.amplitude_pipe_spin_signal_blocking()
        self.editor.amplitude_pipe = self.config.pipe_harmonic_amplitude_get(
            rank_number, pipe_number, harmonic_number
        )
        self.editor.amplitude_pipe_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Attack Time
        #---------------------------------------------------------------------------------------------------------------
        self.editor.attack_time_pipe_harmonic_spin_signal_blocking()
        self.editor.attack_time_pipe_harmonics = self.config.pipe_harmonic_attack_time_get(
            rank_number, pipe_number, harmonic_number
        )
        self.editor.attack_time_pipe_harmonic_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Decay Time
        #---------------------------------------------------------------------------------------------------------------
        self.editor.decay_time_pipe_harmonic_spin_signal_blocking()
        self.editor.decay_time_pipe_harmonics = self.config.pipe_harmonic_decay_time_get(
            rank_number, pipe_number, harmonic_number
        )
        self.editor.decay_time_pipe_harmonic_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Sustain Level
        #---------------------------------------------------------------------------------------------------------------
        self.editor.sustain_level_pipe_harmonic_spin_signal_blocking()
        self.editor.sustain_level_pipe_harmonics = self.config.pipe_harmonic_sustain_level_get(
            rank_number, pipe_number, harmonic_number
        )
        self.editor.sustain_level_pipe_harmonic_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Release Time
        #---------------------------------------------------------------------------------------------------------------
        self.editor.release_time_pipe_harmonic_spin_signal_blocking()
        self.editor.release_time_pipe_harmonics = self.config.pipe_harmonic_release_time_get(
            rank_number, pipe_number, harmonic_number
        )
        self.editor.release_time_pipe_harmonic_spin_signal_unblocking()
        #===============================================================================================================
        ic("Harmonic Settings Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_harmonic_number_rank(self) -> None:
        ic("Updating Harmonic Number Rank...")
        self.editor.harmonic_number_pipe_spin_signal_blocking()
        self.editor.update_harmonic_number_rank()
        self.editor.harmonic_number_pipe_spin_signal_unblocking()
        self.__update_harmonic_number()
        ic("Harmonic Number Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_amplitude(self) -> None:
        ic("Updating Amplitude Rank...")
        rank_number: int = self.editor.rank_number
        pipe_number: int = self.editor.pipe_number
        harmonic_number: int = self.editor.harmonic_number_rank
        amplitude: float = self.editor.amplitude_rank
        self.config.update_amplitudes(
            rank_number, harmonic_number, amplitude
        )
        self.editor.amplitude_pipe_spin_signal_blocking()
        self.editor.amplitude_pipe = self.config.pipe_harmonic_amplitude_get(
            rank_number, pipe_number, harmonic_number
        )
        self.editor.amplitude_pipe_spin_signal_unblocking()
        ic("Amplitude Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_harmonic_attack(self) -> None:
        ic("Updating Attack Time Rank Harmonic...")
        rank_number: int = self.editor.rank_number
        pipe_number: int = self.editor.pipe_number
        harmonic_number: int = self.editor.harmonic_number_rank
        attack_time: float = self.editor.attack_time_rank_harmonic
        self.config.update_attack_times(
            rank_number, harmonic_number, attack_time
        )
        self.editor.attack_time_pipe_harmonic_spin_signal_blocking()
        self.editor.attack_time_pipe_harmonics = self.config.pipe_harmonic_attack_time_get(
            rank_number, pipe_number, harmonic_number
        )
        self.editor.attack_time_pipe_harmonic_spin_signal_unblocking()
        ic("Attack Time Rank Harmonic Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_harmonic_decay(self) -> None:
        ic("Updating Decay Harmonic Rank...")
        rank_number: int = self.editor.rank_number
        pipe_number: int = self.editor.pipe_number
        harmonic_number: int = self.editor.harmonic_number_rank
        decay_time: float = self.editor.decay_time_rank_harmonic
        self.config.update_decay_times(
            rank_number, harmonic_number, decay_time
        )
        self.editor.decay_time_pipe_harmonic_spin_signal_blocking()
        self.editor.decay_time_pipe_harmonics = self.config.pipe_harmonic_decay_time_get(
            rank_number, pipe_number, harmonic_number
        )
        self.editor.decay_time_pipe_harmonic_spin_signal_unblocking()
        ic("Decay Harmonic Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_harmonic_sustain(self) -> None:
        ic("Updating Sustain Harmonic Rank...")
        rank_number: int = self.editor.rank_number
        pipe_number: int = self.editor.pipe_number
        harmonic_number: int = self.editor.harmonic_number_rank
        sustain_level: float = self.editor.sustain_level_rank_harmonic
        self.config.update_sustain_levels(
            rank_number, harmonic_number, sustain_level
        )
        self.editor.sustain_level_pipe_harmonic_spin_signal_blocking()
        self.editor.sustain_level_pipe_harmonics = self.config.pipe_harmonic_sustain_level_get(
            rank_number, pipe_number, harmonic_number
        )
        self.editor.sustain_level_pipe_harmonic_spin_signal_unblocking()
        ic("Sustain Harmonic Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_harmonic_release(self) -> None:
        ic("Updating Release Harmonic Rank...")
        rank_number: int = self.editor.rank_number
        pipe_number: int = self.editor.pipe_number
        harmonic_number: int = self.editor.harmonic_number_rank
        release_time: float = self.editor.release_time_rank_harmonic
        self.config.update_release_times(
            rank_number, harmonic_number, release_time
        )
        self.editor.release_time_pipe_harmonic_spin_signal_blocking()
        self.editor.release_time_pipe_harmonics = self.config.pipe_harmonic_release_time_get(
            rank_number, pipe_number, harmonic_number
        )
        self.editor.release_time_pipe_harmonic_spin_signal_unblocking()
        ic("Release Harmonic Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_attack(self) -> None:
        ic("Updating Attack Rank...")
        rank_number: int = self.editor.rank_number
        attack_time: float = self.editor.attack_time_rank
        self.config.rank_attack_time_set(rank_number, attack_time)
        ic("Attack Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_decay(self) -> None:
        ic("Updating Decay Rank...")
        rank_number: int = self.editor.rank_number
        decay_time: float = self.editor.decay_time_rank
        self.config.rank_decay_time_set(rank_number, decay_time)
        ic("Decay Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_sustain(self) -> None:
        ic("Updating Sustain Rank...")
        rank_number: int = self.editor.rank_number
        sustain_level: float = self.editor.sustain_level_rank
        self.config.rank_sustain_level_set(rank_number, sustain_level)
        ic("Sustain Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_release(self) -> None:
        ic("Updating Release Rank...")
        rank_number: int = self.editor.rank_number
        release_time: float = self.editor.release_time_rank
        self.config.rank_release_time_set(rank_number, release_time)
        ic("Release Rank Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_rank_number_pipe(self) -> None:
        ic("Updating Rank Number Pipe...")
        self.editor.rank_number_spin_signal_blocking()
        self.editor.update_rank_number_pipe()
        self.editor.rank_number_spin_signal_unblocking()
        self.__update_rank_number_general()
        ic("Rank Number Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_number(self) -> None:
        ic("Updating Pipe Settings...")
        rank_number: int = self.editor.rank_number
        pipe_number: int = self.editor.pipe_number
        #---------------------------------------------------------------------------------------------------------------
        # Note
        #---------------------------------------------------------------------------------------------------------------
        self.editor.note_combo_signal_blocking()
        self.editor.note = self.config.note_get(rank_number, pipe_number)
        self.editor.note_combo_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Relative Note
        #---------------------------------------------------------------------------------------------------------------
        self.editor.relative_note_combo_signal_blocking()
        self.editor.relative_note = self.config.relative_note_get(rank_number, pipe_number)
        self.editor.relative_note_combo_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Harmonic Number - Pipe
        #---------------------------------------------------------------------------------------------------------------
        self.editor.harmonic_number_pipe_spin_signal_blocking()
        self.harmonic_number_pipe_editor = 1
        self.editor.harmonic_number_pipe_spin_signal_unblocking()
        self.__update_harmonic_number()
        #---------------------------------------------------------------------------------------------------------------
        # Attack Time - Pipe
        #---------------------------------------------------------------------------------------------------------------
        self.editor.attack_time_pipe_spin_signal_blocking()
        self.editor.attack_time_pipe = self.config.pipe_attack_time_get(rank_number, pipe_number)
        self.editor.attack_time_pipe_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Decay Time - Pipe
        #---------------------------------------------------------------------------------------------------------------
        self.editor.decay_time_pipe_spin_signal_blocking()
        self.editor.decay_time_pipe = self.config.pipe_decay_time_get(rank_number, pipe_number)
        self.editor.decay_time_pipe_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Sustain Level - Pipe
        #---------------------------------------------------------------------------------------------------------------
        self.editor.sustain_level_pipe_spin_signal_blocking()
        self.editor.sustain_level_pipe = self.config.pipe_sustain_level_get(rank_number, pipe_number)
        self.editor.sustain_level_pipe_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        # Release Time - Pipe
        #---------------------------------------------------------------------------------------------------------------
        self.editor.release_time_pipe_spin_signal_blocking()
        self.editor.release_time_pipe = self.config.pipe_release_time_get(rank_number, pipe_number)
        self.editor.release_time_pipe_spin_signal_unblocking()
        #---------------------------------------------------------------------------------------------------------------
        ic("Pipe Settings Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_note(self) -> None:
        ic("Updating Note...")
        rank_number: int = self.editor.rank_number
        pipe_number: int = self.editor.pipe_number
        note: str = self.editor.note
        self.config.note_set(rank_number, pipe_number, note)
        ic("Note Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_relative_note(self) -> None:
        ic("Updating Relative Note...")
        rank_number: int = self.editor.rank_number
        pipe_number: int = self.editor.pipe_number
        note: str = self.editor.relative_note
        note_index = organlib.NOTES.index(note)
        notes: tuple[str, ...] = organlib.NOTES[note_index:]
        self.config.update_relative_notes(rank_number, pipe_number, notes)
        ic("Relative Note Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_harmonic_number_pipe(self) -> None:
        ic("Updating Harmonic Number Pipe...")
        self.editor.harmonic_number_rank_spin_signal_blocking()
        self.editor.update_harmonic_number_pipe()
        self.editor.harmonic_number_rank_spin_signal_unblocking()
        self.__update_harmonic_number()
        ic("Harmonic Number Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_amplitude(self) -> None:
        ic("Updating Amplitude Pipe...")
        rank_number: int = self.editor.rank_number
        pipe_number: int = self.editor.pipe_number
        harmonic_number: int = self.editor.harmonic_number_pipe
        amplitude: float = self.editor.amplitude_pipe
        self.config.pipe_harmonic_amplitude_set(rank_number, pipe_number, harmonic_number, amplitude)
        ic("Amplitude Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_attack(self) -> None:
        ic("Updating Attack Pipe...")
        rank_number: int = self.editor.rank_number
        pipe_number: int = self.editor.pipe_number
        attack_time: float = self.editor.attack_time_pipe
        self.config.pipe_attack_time_set(rank_number, pipe_number, attack_time)
        ic("Attack Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_decay(self) -> None:
        ic("Updating Decay Pipe...")
        rank_number: int = self.editor.rank_number
        pipe_number: int = self.editor.pipe_number
        decay_time: float = self.editor.decay_time_pipe
        self.config.pipe_decay_time_set(rank_number, pipe_number, decay_time)
        ic("Decay Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_sustain(self) -> None:
        ic("Updating Sustain Pipe...")
        rank_number: int = self.editor.rank_number
        pipe_number: int = self.editor.pipe_number
        sustain_level: float = self.editor.sustain_level_pipe
        self.config.pipe_sustain_level_set(rank_number, pipe_number, sustain_level)
        ic("Sustain Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_release(self) -> None:
        ic("Updating Release Pipe...")
        rank_number: int = self.editor.rank_number
        pipe_number: int = self.editor.pipe_number
        release_time: float = self.editor.release_time_pipe
        self.config.pipe_release_time_set(rank_number, pipe_number, release_time)
        ic("Release Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_harmonic_attack(self) -> None:
        ic("Updating Attack Harmonic Pipe...")
        rank_number: int = self.editor.rank_number
        pipe_number: int = self.editor.pipe_number
        harmonic_number: int = self.editor.harmonic_number_pipe
        attack_time: float = self.editor.attack_time_pipe_harmonics
        self.config.pipe_harmonic_attack_time_set(rank_number, pipe_number, harmonic_number, attack_time)
        ic("Attack Harmonic Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_harmonic_decay(self) -> None:
        ic("Updating Decay Harmonic Pipe...")
        rank_number: int = self.editor.rank_number
        pipe_number: int = self.editor.pipe_number
        harmonic_number: int = self.editor.harmonic_number_pipe
        decay_time: float = self.editor.decay_time_pipe_harmonics
        self.config.pipe_harmonic_decay_time_set(rank_number, pipe_number, harmonic_number, decay_time)
        ic("Decay Harmonic Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_harmonic_sustain(self) -> None:
        ic("Updating Sustain Harmonic Pipe...")
        rank_number: int = self.editor.rank_number
        pipe_number: int = self.editor.pipe_number
        harmonic_number: int = self.editor.harmonic_number_pipe
        sustain_level: float = self.editor.sustain_level_pipe_harmonics
        self.config.pipe_harmonic_sustain_level_set(rank_number, pipe_number, harmonic_number, sustain_level)
        ic("Sustain Harmonic Pipe Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_harmonic_release(self) -> None:
        ic("Updating Release Harmonic Pipe...")
        rank_number: int = self.editor.rank_number
        pipe_number: int = self.editor.pipe_number
        harmonic_number: int = self.editor.harmonic_number_pipe
        release_time: float = self.editor.release_time_pipe_harmonics
        self.config.pipe_harmonic_release_time_set(rank_number, pipe_number, harmonic_number, release_time)
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
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("JSON Files (*.json)")
        file_dialog.setViewMode(QFileDialog.ViewMode.Detail)
        file_dialog.setDirectory("src/config/stops")
        self.config_file = file_dialog.getOpenFileName()[0]
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

    #-------------------------------------------------------------------------------------------------------------------
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


#=======================================================================================================================
# Executable
#=======================================================================================================================
if __name__ == "__main__":
    log_file.start_logging_to_file()
    app = QApplication([])
    stop_editor_ui = StopEditorUI()
    stop_editor_ui.editor.show()
    app.exec()
