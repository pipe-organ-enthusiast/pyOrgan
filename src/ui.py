from gui import MainWindow, StopEditor
from organ import organlib
#------------------------------------------------------------------------------
from PySide6.QtWidgets import QApplication
#------------------------------------------------------------------------------
from typing import Callable


#******************************************************************************
# Stop Editor
#******************************************************************************
class StopEditorUI(StopEditor):
    def __init__(self) -> None:
        super().__init__()
        self.__config_ui()

    def __config_ui(self) -> None:
        #**********************************************************************
        # Stop Name
        #**********************************************************************
        stop_name: tuple[str] = ("",) + organlib.STOP_NAMES
        self.stop_names_populate(stop_name)
        self.stop_name_change(self.__update_stop_name)
        #**********************************************************************
        # Stop Family
        #**********************************************************************
        stop_families: tuple[str] = ("",) + organlib.STOP_FAMILIES
        self.stop_families_populate(stop_families)
        self.stop_family_change(self.__update_stop_family)
        #**********************************************************************
        # Organ Division
        #**********************************************************************
        organ_divisions: tuple[str] = ("",) + organlib.ORGAN_DIVISIONS
        self.organ_divisions_populate(organ_divisions)
        self.organ_division_change(self.__update_organ_division)
        #**********************************************************************
        # Number of Ranks
        #**********************************************************************
        self.number_ranks_set_minimum(1)
        self.number_ranks_set_maximum(10)
        self.number_ranks_change(self.__update_number_ranks)
        #**********************************************************************
        # Rank Series
        #**********************************************************************
        rank_series: tuple[str] = ("",) + organlib.RANK_SERIES
        self.rank_series_populate(rank_series)
        self.rank_series_change(self.__update_rank_series)
        #**********************************************************************
        # Rank Number
        #**********************************************************************
        self.rank_number_set_minimum(1)
        self.rank_number_set_maximum(self.number_ranks)
        self.rank_number_change(self.__update_rank_number)
        #**********************************************************************
        # Rank Size
        #**********************************************************************
        self.__update_rank_series()
        self.rank_size_change(self.__update_rank_size)
        #**********************************************************************
        # Number of Pipes
        #**********************************************************************
        self.number_pipes_set_minimum(1)
        self.number_pipes_set_maximum(61)
        self.number_pipes_change(self.__update_number_pipes)
        #**********************************************************************
        # Pipe Type
        #**********************************************************************
        pipe_types: tuple[str] = ("",) + organlib.PIPE_TYPES
        self.pipe_types_populate(pipe_types)
        self.pipe_type_change(self.__update_pipe_type)
        #**********************************************************************
        # Starting None
        #**********************************************************************
        notes: tuple[str] = ("",) + organlib.NOTES
        self.starting_note_populate(notes)
        self.starting_note_change(self.__update_starting_note)
        #**********************************************************************
        # Frequency Offset
        #**********************************************************************
        self.frequency_offset_set_minimum(-7)
        self.frequency_offset_set_maximum(7)
        self.frequency_offset_change(self.__update_frequency_offset)
        #**********************************************************************
        # Number of Harmonics
        #**********************************************************************
        self.number_harmonics_set_minimum(1)
        self.number_harmonics_set_maximum(20)
        self.number_harmonics_change(self.__update_number_harmonics)
        #**********************************************************************
        # Harmonic Number - Rank
        #**********************************************************************
        self.harmonic_number_rank_set_minimum(1)
        self.harmonic_number_rank_set_maximum(self.number_harmonics)
        self.harmonic_number_rank_change(self.__update_harmonic_number_rank)
        #**********************************************************************
        # Amplitude - Rank
        #**********************************************************************
        self.amplitude_rank_set_minimum(0)
        self.amplitude_rank_set_maximum(100)
        self.amplitude_rank_change(self.__update_amplitude_rank)
        #**********************************************************************
        # Attack Time - Harmonic - Rank
        #**********************************************************************
        self.attack_time_rank_harmonic_set_minimum(0)
        self.attack_time_rank_harmonic_set_maximum(1000)
        self.attack_time_rank_harmonic_change(
            self.__update_attack_time_rank_harmonic
        )
        #**********************************************************************
        # Decay Time - Harmonic - Rank
        #**********************************************************************
        self.decay_time_rank_harmonic_set_minimum(0)
        self.decay_time_rank_harmonic_set_maximum(1000)
        self.decay_time_rank_harmonic_change(
            self.__update_decay_time_rank_harmonic
        )
        #**********************************************************************
        # Sustain Level - Harmonic - Rank
        #**********************************************************************
        self.sustain_level_rank_harmonic_set_minimum(0)
        self.sustain_level_rank_harmonic_set_maximum(100)
        self.sustain_level_rank_harmonic_change(
            self.__update_sustain_level_rank_harmonic
        )
        #**********************************************************************
        # Release Time - Harmonic - Rank
        #**********************************************************************
        self.release_time_rank_harmonic_set_minimum(0)
        self.release_time_rank_harmonic_set_maximum(2000)
        self.release_time_rank_harmonic_change(
            self.__update_release_time_rank_harmonic
        )
        #**********************************************************************
        # Attack Time - Rank
        #**********************************************************************
        self.attack_time_rank_set_minimum(0)
        self.attack_time_rank_set_maximum(1000)
        self.attack_time_rank_change(self.__update_attack_time_rank)
        #**********************************************************************
        # Decay Time - Rank
        #**********************************************************************
        self.decay_time_rank_set_minimum(0)
        self.decay_time_rank_set_maximum(1000)
        self.decay_time_rank_change(self.__update_decay_time_rank)
        #**********************************************************************
        # Sustain Level - Rank
        #**********************************************************************
        self.sustain_level_rank_set_minimum(0)
        self.sustain_level_rank_set_maximum(100)
        self.sustain_level_rank_change(self.__update_sustain_level_rank)
        #**********************************************************************
        # Release Time - Rank
        #**********************************************************************
        self.release_time_rank_set_minimum(0)
        self.release_time_rank_set_maximum(2000)
        self.release_time_rank_change(self.__update_release_time_rank)
        #**********************************************************************
        # Rank Number - Pipe
        #**********************************************************************
        self.rank_number_pipe_set_minimum(1)
        self.rank_number_pipe_set_maximum(self.number_ranks)
        self.rank_number_pipe_change(self.__update_rank_number_pipe)
        #**********************************************************************
        # Pipe Number
        #**********************************************************************
        self.pipe_number_set_minimum(1)
        self.pipe_number_set_maximum(self.number_pipes)
        self.pipe_number_change(self.__update_pipe_number)
        #**********************************************************************
        # Note
        #**********************************************************************
        self.note_populate(notes)
        self.note_change(self.__update_note)
        #**********************************************************************
        # Relative Note
        #**********************************************************************
        self.relative_note_populate(notes)
        self.relative_note_change(self.__update_relative_note)
        #**********************************************************************
        # Harmonic Number - Pipe
        #**********************************************************************
        self.harmonic_number_pipe_set_minimum(1)
        self.harmonic_number_pipe_set_maximum(self.number_harmonics)
        self.harmonic_number_pipe_change(self.__update_harmonic_number_pipe)
        #**********************************************************************
        # Amplitude - Pipe
        #**********************************************************************
        self.amplitude_pipe_set_minimum(0)
        self.amplitude_pipe_set_maximum(100)
        self.amplitude_pipe_change(self.__update_amplitude_pipe)
        #**********************************************************************
        # Attack Time - Harmonic - Pipe
        #**********************************************************************
        self.attack_time_pipe_harmonic_set_minimum(0)
        self.attack_time_pipe_harmonic_set_maximum(1000)
        self.attack_time_pipe_harmonic_change(
            self.__update_attack_time_pipe_harmonic
        )
        #**********************************************************************
        # Decay Time - Harmonic - Pipe
        #**********************************************************************
        self.decay_time_pipe_harmonic_set_minimum(0)
        self.decay_time_pipe_harmonic_set_maximum(1000)
        self.decay_time_pipe_harmonic_change(
            self.__update_decay_time_pipe_harmonic
        )
        #**********************************************************************
        # Sustain Level - Harmonic - Pipe
        #**********************************************************************
        self.sustain_level_pipe_harmonic_set_minimum(0)
        self.sustain_level_pipe_harmonic_set_maximum(100)
        self.sustain_level_pipe_harmonic_change(
            self.__update_sustain_level_pipe_harmonic
        )
        #**********************************************************************
        # Release Time - Harmonic - Pipe
        #**********************************************************************
        self.release_time_pipe_harmonic_set_minimum(0)
        self.release_time_pipe_harmonic_set_maximum(2000)
        self.release_time_pipe_harmonic_change(
            self.__update_release_time_pipe_harmonic
        )
        #**********************************************************************
        # Attack Time - Pipe
        #**********************************************************************
        self.attack_time_pipe_set_minimum(0)
        self.attack_time_pipe_set_maximum(1000)
        self.attack_time_pipe_change(self.__update_attack_time_pipe)
        #**********************************************************************
        # Decay Time - Pipe
        #**********************************************************************
        self.decay_time_pipe_set_minimum(0)
        self.decay_time_pipe_set_maximum(1000)
        self.decay_time_pipe_change(self.__update_decay_time_pipe)
        #**********************************************************************
        # Sustain Level - Pipe
        #**********************************************************************
        self.sustain_level_pipe_set_minimum(0)
        self.sustain_level_pipe_set_maximum(100)
        self.sustain_level_pipe_change(self.__update_sustain_level_pipe)
        #**********************************************************************
        # Release Time - Pipe
        #**********************************************************************
        self.release_time_pipe_set_minimum(0)
        self.release_time_pipe_set_maximum(2000)
        self.release_time_pipe_change(self.__update_release_time_pipe)

    #**************************************************************************
    # Actions
    #**************************************************************************
    def __update_stop_name(self) -> None:
        self.update_stop_header()
        #TODO: Add functionality for use with config files

    def __update_stop_family(self) -> None:
        ...
        #TODO: Add functionality for use with config files

    def __update_organ_division(self) -> None:
        ...
        #TODO: Add functionality for use with config files

    def __update_number_ranks(self) -> None:
        methods: tuple[Callable] = (
            self.rank_number_set_maximum,
            self.rank_number_pipe_set_maximum
        )
        for method in methods:
            method(self.number_ranks)
        #TODO: Add functionality for use with config files

    def __update_rank_series(self) -> None:
        match self.rank_series:
            case "64' Series":
                ranks = organlib.RANK_SERIES_64
            case "32' Series":
                ranks = organlib.RANK_SERIES_32
            case "16' Series":
                ranks = organlib.RANK_SERIES_16
            case "8' Series":
                ranks = organlib.RANK_SERIES_8
            case "4' Series":
                ranks = organlib.RANK_SERIES_4
            case _:
                ranks = organlib.RANK_SIZES
        self.rank_series_populate(ranks)
        #TODO: Add functionality for use with config files

    def __update_rank_number(self) -> None:
        ...
        #TODO: Add functionality for use with config files

    def __update_rank_size(self) -> None:
        ...
        #TODO: Add functionality for use with config files

    def __update_number_pipes(self) -> None:
        self.pipe_number_set_maximum(self.number_pipes)
        #TODO: Add functionality for use with config files

    def __update_pipe_type(self) -> None:
        ...
        #TODO: Add functionality for use with config files

    def __update_starting_note(self) -> None:
        ...
        #TODO: Add functionality for use with config files

    def __update_frequency_offset(self) -> None:
        ...
        #TODO: Add functionality for use with config files

    def __update_number_harmonics(self) -> None:
        methods: tuple[Callable] = (
            self.harmonic_number_rank_set_maximum,
            self.harmonic_number_pipe_set_maximum
        )
        for method in methods:
            method(self.number_harmonics)
        #TODO: add functionality for use with config files

    def __update_harmonic_number_rank(self) -> None:
        ...
        #TODO: add functionality for use with config files

    def __update_amplitude_rank(self) -> None:
        ...
        #TODO: add functionality for use with config files

    def __update_attack_time_rank_harmonic(self) -> None:
        ...
        #TODO: add functionality for use with config files

    def __update_decay_time_rank_harmonic(self) -> None:
        ...
        #TODO: add functionality for use with config files

    def __update_sustain_level_rank_harmonic(self) -> None:
        ...
        #TODO: add functionality for use with config files

    def __update_release_time_rank_harmonic(self) -> None:
        ...
        #TODO: add functionality for use with config files

    def __update_attack_time_rank(self) -> None:
        ...
        #TODO: add functionality for use with config files

    def __update_decay_time_rank(self) -> None:
        ...
        #TODO: add functionality for use with config files

    def __update_sustain_level_rank(self) -> None:
        ...
        #TODO: add functionality for use with config files

    def __update_release_time_rank(self) -> None:
        ...
        #TODO: add functionality for use with config files

    def __update_rank_number_pipe(self) -> None:
        ...
        #TODO: Add functionality for use with config files

    def __update_pipe_number(self) -> None:
        ...
        #TODO: Add functionality for use with config files

    def __update_note(self) -> None:
        ...
        #TODO: Add functionality for use with config files

    def __update_relative_note(self) -> None:
        ...
        #TODO: Add functionality for use with config files

    def __update_harmonic_number_pipe(self) -> None:
        ...
        #TODO: Add functionality for use with config files

    def __update_amplitude_pipe(self) -> None:
        ...
        #TODO: add functionality for use with config files

    def __update_attack_time_pipe_harmonic(self) -> None:
        ...
        #TODO: add functionality for use with config files

    def __update_decay_time_pipe_harmonic(self) -> None:
        ...
        #TODO: add functionality for use with config files

    def __update_sustain_level_pipe_harmonic(self) -> None:
        ...
        #TODO: add functionality for use with config files

    def __update_release_time_pipe_harmonic(self) -> None:
        ...
        #TODO: add functionality for use with config files

    def __update_attack_time_pipe(self) -> None:
        ...
        #TODO: add functionality for use with config files

    def __update_decay_time_pipe(self) -> None:
        ...
        #TODO: add functionality for use with config files

    def __update_sustain_level_pipe(self) -> None:
        ...
        #TODO: add functionality for use with config files

    def __update_release_time_pipe(self) -> None:
        ...
        #TODO: add functionality for use with config files


def test_stop_editor():
    app = QApplication([])
    window = StopEditorUI()
    window.show()
    app.exec()


if __name__ == "__main__":
    test_stop_editor()
