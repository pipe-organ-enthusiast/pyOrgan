from gui import MainWindow, StopEditor
from organ import organlib
from config_editors import StopConfig
#------------------------------------------------------------------------------
from PySide6.QtWidgets import QApplication
#------------------------------------------------------------------------------
from typing import Callable


#******************************************************************************
# Stop Editor
#******************************************************************************
class StopEditorUI:
    def __init__(self) -> None:
        super().__init__()
        self.stop_editor: StopEditor = StopEditor()
        self.old_number_ranks: int = self.stop_editor.number_ranks
        self.config_editor: StopConfig = StopConfig()
        self.__init_properties()
        self.__config_ui()

    def __init_properties(self) -> None:
        editor: StopEditor = self.stop_editor
        self.stop_name: str = editor.stop_name
        self.stop_family: str = editor.stop_family
        self.organ_division: str = editor.organ_division
        self.rank_series: str = editor.rank_series
        self.rank_number: int = editor.rank_number
        self.rank_size: str = editor.rank_size
        self.number_pipes: int = editor.number_pipes
        self.pipe_type: str = editor.pipe_type
        self.starting_note: str = editor.starting_note
        self.frequency_offset: int = editor.frequency_offset
        self.number_harmonics: int = editor.number_harmonics
        self.harmonic_number_rank: int = editor.harmonic_number_rank
        self.amplitude_rank: int = editor.amplitude_rank
        self.attack_harmonic_rank: int = editor.attack_time_harmonic_rank
        self.decay_harmonic_rank: int = editor.decay_time_harmonic_rank
        self.sustain_harmonic_rank: int = editor.sustain_level_harmonic_rank
        self.release_harmonic_rank: int = editor.release_time_harmonic_rank
        self.attack_rank: int = editor.attack_time_rank
        self.decay_rank: int = editor.decay_time_rank
        self.sustain_rank: int = editor.sustain_level_rank
        self.release_rank: int = editor.release_time_rank
        self.rank_number_pipe: int = editor.rank_number_pipe
        self.pipe_number: int = editor.pipe_number
        self.note: str = editor.note
        self.relative_note: str = editor.relative_note
        self.harmonic_number_pipe: int = editor.harmonic_number_pipe
        self.amplitude_pipe: int = editor.amplitude_pipe
        self.attack_harmonic_pipe: int = editor.attack_time_harmonic_pipe
        self.decay_harmonic_pipe: int = editor.decay_time_harmonic_pipe
        self.sustain_harmonic_pipe: int = editor.sustain_level_harmonic_pipe
        self.release_harmonic_pipe: int = editor.release_time_harmonic_pipe
        self.attack_pipe: int = editor.attack_time_pipe
        self.decay_pipe: int = editor.decay_time_pipe
        self.sustain_pipe: int = editor.sustain_level_pipe
        self.release_pipe: int = editor.release_time_pipe

    #**************************************************************************
    # Configuration
    #**************************************************************************
    def __config_ui(self) -> None:
        self.__config_ui_config_editor()
        self.__config_ui_stop_editor()

    #==========================================================================
    # Stop Editor
    #==========================================================================
    def __config_ui_stop_editor(self) -> None:
        self.__config_ui_stop_editor_stop_name()
        self.__config_ui_stop_editor_stop_families()
        self.__config_ui_stop_editor_organ_division()
        self.__config_ui_stop_editor_number_ranks()
        self.__config_ui_stop_editor_rank_series()
        self.__config_ui_stop_editor_rank_number()
        self.__config_ui_stop_editor_rank_size()
        self.__config_ui_stop_editor_number_pipes()
        self.__config_ui_stop_editor_pipe_types()
        self.__config_ui_stop_editor_starting_note()
        self.__config_ui_stop_editor_frequency_offset()
        self.__config_ui_stop_editor_number_harmonics()
        self.__config_ui_stop_editor_harmonic_number_rank()
        self.__config_ui_stop_editor_amplitude_rank()
        self.__config_ui_stop_editor_attack_rank_harmonic()
        self.__config_ui_stop_editor_decay_rank_harmonic()
        self.__config_ui_stop_editor_sustain_rank_harmonic()
        self.__config_ui_stop_editor_release_rank_harmonic()
        self.__config_ui_stop_editor_attack_rank()
        self.__config_ui_stop_editor_decay_rank()
        self.__config_ui_stop_editor_sustain_rank()
        self.__config_ui_stop_editor_release_rank()
        self.__config_ui_stop_editor_rank_number_pipe()
        self.__config_ui_stop_editor_pipe_number()
        self.__config_ui_stop_editor_note()
        self.__config_ui_stop_editor_relative_note()
        self.__config_ui_stop_editor_harmonic_number_pipe()
        self.__config_ui_stop_editor_amplitude_pipe()
        self.__config_ui_stop_editor_attack_pipe_harmonic()
        self.__config_ui_stop_editor_decay_pipe_harmonic()
        self.__config_ui_stop_editor_sustain_pipe_harmonic()
        self.__config_ui_stop_editor_release_pipe_harmonic()
        self.__config_ui_stop_editor_attack_pipe()
        self.__config_ui_stop_editor_decay_pipe()
        self.__config_ui_stop_editor_sustain_pipe()
        self.__config_ui_stop_editor_release_pipe()

    def __config_ui_stop_editor_stop_name(self) -> None:
        editor: StopEditor = self.stop_editor
        stop_name: tuple[str] = ("",) + organlib.STOP_NAMES
        editor.stop_names_populate(stop_name)
        editor.stop_name_change(self.__update_stop_name)

    def __config_ui_stop_editor_stop_families(self) -> None:
        editor: StopEditor = self.stop_editor
        stop_families: tuple[str] = ("",) + organlib.STOP_FAMILIES
        editor.stop_families_populate(stop_families)
        editor.stop_family_change(self.__update_stop_family)

    def __config_ui_stop_editor_organ_division(self) -> None:
        editor: StopEditor = self.stop_editor
        organ_divisions: tuple[str] = ("",) + organlib.ORGAN_DIVISIONS
        editor.organ_divisions_populate(organ_divisions)
        editor.organ_division_change(self.__update_organ_division)

    def __config_ui_stop_editor_number_ranks(self) -> None:
        editor: StopEditor = self.stop_editor
        editor.number_ranks_set_minimum(0)
        editor.number_ranks_set_maximum(10)
        editor.number_ranks_change(self.__update_number_ranks)
    
    def __config_ui_stop_editor_rank_series(self) -> None:
        editor: StopEditor = self.stop_editor
        rank_series: tuple[str] = ("",) + organlib.RANK_SERIES
        editor.rank_series_populate(rank_series)
        editor.rank_series_change(self.__update_rank_series)

    def __config_ui_stop_editor_rank_number(self) -> None:
        editor: StopEditor = self.stop_editor
        editor.rank_number_set_minimum(1)
        editor.rank_number_set_maximum(editor.number_ranks)
        editor.rank_number_change(self.__update_rank_number)
    
    def __config_ui_stop_editor_rank_size(self) -> None:
        editor: StopEditor = self.stop_editor
        self.__update_rank_series()
        editor.rank_size_change(self.__update_rank_size)

    def __config_ui_stop_editor_number_pipes(self) -> None:
        editor: StopEditor = self.stop_editor
        editor.number_pipes_set_minimum(0)
        editor.number_pipes_set_maximum(61)
        editor.number_pipes_change(self.__update_number_pipes)

    def __config_ui_stop_editor_pipe_types(self) -> None:
        editor: StopEditor = self.stop_editor
        pipe_types: tuple[str] = ("",) + organlib.PIPE_TYPES
        editor.pipe_types_populate(pipe_types)
        editor.pipe_type_change(self.__update_pipe_type)
        
    def __config_ui_stop_editor_starting_note(self) -> None:
        editor: StopEditor = self.stop_editor
        notes: tuple[str] = ("",) + organlib.NOTES
        editor.starting_note_populate(notes)
        editor.starting_note_change(self.__update_starting_note)

    def __config_ui_stop_editor_frequency_offset(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.frequency_offset_set_minimum(-7)
        editor.frequency_offset_set_maximum(7)
        editor.frequency_offset_change(self.__update_frequency_offset)

    def __config_ui_stop_editor_number_harmonics(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.number_harmonics_set_minimum(0)
        editor.number_harmonics_set_maximum(20)
        editor.number_harmonics_change(self.__update_number_harmonics)

    def __config_ui_stop_editor_harmonic_number_rank(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.harmonic_number_rank_set_minimum(0)
        editor.harmonic_number_rank_set_maximum(editor.number_harmonics)
        editor.harmonic_number_rank_change(self.__update_harmonic_number_rank)

    def __config_ui_stop_editor_amplitude_rank(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.amplitude_rank_set_minimum(0)
        editor.amplitude_rank_set_maximum(100)
        editor.amplitude_rank_change(self.__update_amplitude_rank)

    def __config_ui_stop_editor_attack_rank_harmonic(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.attack_time_rank_harmonic_set_minimum(0)
        editor.attack_time_rank_harmonic_set_maximum(1000)
        editor.attack_time_rank_harmonic_change(
            self.__update_attack_time_rank_harmonic
        )

    def __config_ui_stop_editor_decay_rank_harmonic(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.decay_time_rank_harmonic_set_minimum(0)
        editor.decay_time_rank_harmonic_set_maximum(1000)
        editor.decay_time_rank_harmonic_change(
            self.__update_decay_time_rank_harmonic
        )

    def __config_ui_stop_editor_sustain_rank_harmonic(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.sustain_level_rank_harmonic_set_minimum(0)
        editor.sustain_level_rank_harmonic_set_maximum(100)
        editor.sustain_level_rank_harmonic_change(
            self.__update_sustain_level_rank_harmonic
        )

    def __config_ui_stop_editor_release_rank_harmonic(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.release_time_rank_harmonic_set_minimum(0)
        editor.release_time_rank_harmonic_set_maximum(2000)
        editor.release_time_rank_harmonic_change(
            self.__update_release_time_rank_harmonic
        )

    def __config_ui_stop_editor_attack_rank(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.attack_time_rank_set_minimum(0)
        editor.attack_time_rank_set_maximum(1000)
        editor.attack_time_rank_change(self.__update_attack_time_rank)

    def __config_ui_stop_editor_decay_rank(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.decay_time_rank_set_minimum(0)
        editor.decay_time_rank_set_maximum(1000)
        editor.decay_time_rank_change(self.__update_decay_time_rank)

    def __config_ui_stop_editor_sustain_rank(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.sustain_level_rank_set_minimum(0)
        editor.sustain_level_rank_set_maximum(100)
        editor.sustain_level_rank_change(self.__update_sustain_level_rank)

    def __config_ui_stop_editor_release_rank(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.release_time_rank_set_minimum(0)
        editor.release_time_rank_set_maximum(2000)
        editor.release_time_rank_change(self.__update_release_time_rank)

    def __config_ui_stop_editor_rank_number_pipe(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.rank_number_pipe_set_minimum(0)
        editor.rank_number_pipe_set_maximum(editor.number_ranks)
        editor.rank_number_pipe_change(self.__update_rank_number_pipe)

    def __config_ui_stop_editor_pipe_number(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.pipe_number_set_minimum(0)
        editor.pipe_number_set_maximum(editor.number_pipes)
        editor.pipe_number_change(self.__update_pipe_number)

    def __config_ui_stop_editor_note(self) -> None:
        editor: StopConfig = self.stop_editor
        notes: tuple[str] = ("",) + organlib.NOTES
        editor.note_populate(notes)
        editor.note_change(self.__update_note)

    def __config_ui_stop_editor_relative_note(self) -> None:
        editor: StopConfig = self.stop_editor
        notes: tuple[str] = ("",) + organlib.NOTES
        editor.relative_note_populate(notes)
        editor.relative_note_change(self.__update_relative_note)

    def __config_ui_stop_editor_harmonic_number_pipe(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.harmonic_number_pipe_set_minimum(0)
        editor.harmonic_number_pipe_set_maximum(editor.number_harmonics)
        editor.harmonic_number_pipe_change(self.__update_harmonic_number_pipe)

    def __config_ui_stop_editor_amplitude_pipe(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.amplitude_pipe_set_minimum(0)
        editor.amplitude_pipe_set_maximum(100)
        editor.amplitude_pipe_change(self.__update_amplitude_pipe)

    def __config_ui_stop_editor_attack_pipe_harmonic(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.attack_time_pipe_harmonic_set_minimum(0)
        editor.attack_time_pipe_harmonic_set_maximum(1000)
        editor.attack_time_pipe_harmonic_change(
            self.__update_attack_time_pipe_harmonic
        )

    def __config_ui_stop_editor_decay_pipe_harmonic(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.decay_time_pipe_harmonic_set_minimum(0)
        editor.decay_time_pipe_harmonic_set_maximum(1000)
        editor.decay_time_pipe_harmonic_change(
            self.__update_decay_time_pipe_harmonic
        )

    def __config_ui_stop_editor_sustain_pipe_harmonic(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.sustain_level_pipe_harmonic_set_minimum(0)
        editor.sustain_level_pipe_harmonic_set_maximum(100)
        editor.sustain_level_pipe_harmonic_change(
            self.__update_sustain_level_pipe_harmonic
        )

    def __config_ui_stop_editor_release_pipe_harmonic(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.release_time_pipe_harmonic_set_minimum(0)
        editor.release_time_pipe_harmonic_set_maximum(2000)
        editor.release_time_pipe_harmonic_change(
            self.__update_release_time_pipe_harmonic
        )

    def __config_ui_stop_editor_attack_pipe(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.attack_time_pipe_set_minimum(0)
        editor.attack_time_pipe_set_maximum(1000)
        editor.attack_time_pipe_change(self.__update_attack_time_pipe)

    def __config_ui_stop_editor_decay_pipe(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.decay_time_pipe_set_minimum(0)
        editor.decay_time_pipe_set_maximum(1000)
        editor.decay_time_pipe_change(self.__update_decay_time_pipe)

    def __config_ui_stop_editor_sustain_pipe(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.sustain_level_pipe_set_minimum(0)
        editor.sustain_level_pipe_set_maximum(100)
        editor.sustain_level_pipe_change(self.__update_sustain_level_pipe)

    def __config_ui_stop_editor_release_pipe(self) -> None:
        editor: StopConfig = self.stop_editor
        editor.release_time_pipe_set_minimum(0)
        editor.release_time_pipe_set_maximum(2000)
        editor.release_time_pipe_change(self.__update_release_time_pipe)

    def __config_ui_config_editor(self) -> None:
        self.config_editor.init_stopsettings()

    #**************************************************************************
    # Actions
    #**************************************************************************
    def __update_stop_header(self) -> None:
        if self.rank_size != "" or self.number_ranks > 1:
            self.stop_editor.update_stop_header()
    
    def __update_stop_name(self) -> None:
        stop_editor: StopEditor = self.stop_editor
        methods: tuple[Callable] = (
            stop_editor.number_ranks_set_minimum,
            stop_editor.rank_number_set_minimum,
            stop_editor.number_pipes_set_minimum,
            stop_editor.number_harmonics_set_minimum,
            stop_editor.harmonic_number_rank_set_minimum,
            stop_editor.pipe_number_set_minimum,
            stop_editor.harmonic_number_pipe_set_minimum,
        )
        if self.stop_name == "":
            for method in methods:
                method(0)
        else:
            for method in methods:
                method(1)
        self.__update_stop_header()
        self.__update_number_ranks()
        self.__update_rank_number()
        self.config_editor.stop_name_set(self.stop_name)

    def __update_stop_family(self) -> None:
        self.stop_family = self.stop_editor.stop_family
        self.config_editor.stop_family_set(self.stop_family)

    def __update_organ_division(self) -> None:
        self.config_editor.organ_division_set(self.organ_division)

    def __update_number_ranks(self) -> None:
        number_ranks: int = self.number_ranks
        self.__set_maximum_rank_number(number_ranks)
        self.__update_number_ranks_config_editor(number_ranks)
        self.old_number_ranks = number_ranks

    def __set_maximum_rank_number(self, number_ranks: int) -> None:
        stop_editor: StopEditor = self.stop_editor
        methods: tuple[Callable] = (
            stop_editor.rank_number_set_maximum,
            stop_editor.rank_number_pipe_set_maximum
        )
        for method in methods:
            method(number_ranks)

    def __update_number_ranks_config_editor(self, number_ranks):
        self.config_editor.number_ranks_set(number_ranks)
        if number_ranks < self.old_number_ranks:
            for rank in range(number_ranks, self.old_number_ranks):
                self.config_editor.del_rank_settings(rank)
        else:
            for rank in range(self.old_number_ranks, number_ranks):
                self.config_editor.init_rank_settings(rank)

    def __update_rank_series(self) -> None:
        self.rank_series = self.stop_editor.rank_series
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
        self.stop_editor.rank_series_populate(ranks)
        self.config_editor.rank_series_set(self.rank_series)

    def __update_rank_number(self) -> None:
        stop_editor = self.stop_editor
        config_editor = self.config_editor
        rank_number = stop_editor.rank_number
        stop_editor.rank_size = config_editor.rank_size_get(rank_number)
        stop_editor.number_pipes = config_editor.number_pipes_get(rank_number)
        stop_editor.pipe_type = config_editor.pipe_type_get(rank_number)
        stop_editor.starting_note = config_editor.starting_note_get(
            rank_number
        )
        stop_editor.frequency_offset = config_editor.frequency_offset_get(
            rank_number
        )
        stop_editor.number_harmonics = config_editor.number_harmonics_get(
            rank_number
        )

    def __update_rank_size(self) -> None:
        self.rank_size = self.stop_editor.rank_size
        self.config_editor.rank_size_set(self.rank_number, self.rank_size)

    def __update_number_pipes(self) -> None:
        self.number_pipes = self.stop_editor.number_pipes
        self.stop_editor.pipe_number_set_maximum(self.number_pipes)
        self.config_editor.number_pipes_set(
            rank_number=self.rank_number,
            number_pipes=self.number_pipes
        )

    def __update_pipe_type(self) -> None:
        self.pipe_type = self.stop_editor.pipe_type
        self.config_editor.pipe_type_set(
            rank_number=self.rank_number,
            pipe_type=self.pipe_type
        )

    def __update_starting_note(self) -> None:
        self.starting_note = self.stop_editor.starting_note
        self.config_editor.starting_note_set(
            rank_number=self.rank_number,
            starting_note=self.starting_note
        )

    def __update_frequency_offset(self) -> None:
        self.frequency_offset = self.stop_editor.frequency_offset

    def __update_number_harmonics(self) -> None:
        editor: StopEditor = self.stop_editor
        methods: tuple[Callable] = (
            editor.harmonic_number_rank_set_maximum,
            editor.harmonic_number_pipe_set_maximum
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

    #**************************************************************************
    # Properties
    #**************************************************************************
    #==========================================================================
    # Stop Name
    #==========================================================================
    @property
    def stop_name(self) -> str:
        return self.stop_editor.stop_name

    @stop_name.setter
    def stop_name(self, stop_name: str) -> None:
        self.stop_editor.stop_name = stop_name

    #==========================================================================
    # Stop Family
    #==========================================================================
    @property
    def stop_family(self) -> str:
        return self.stop_editor.stop_family

    @stop_family.setter
    def stop_family(self, stop_family: str) -> None:
        self.stop_editor.stop_family = stop_family

    #==========================================================================
    # Organ Division
    #==========================================================================
    @property
    def organ_division(self) -> str:
        return self.stop_editor.organ_division

    @organ_division.setter
    def organ_division(self, organ_division: str) -> None:
        self.stop_editor.organ_division = organ_division

    #==========================================================================
    # Number of Ranks
    #==========================================================================
    @property
    def number_ranks(self) -> int:
        return self.stop_editor.number_ranks

    @number_ranks.setter
    def number_ranks(self, number_ranks: int) -> None:
        self.stop_editor.number_ranks = number_ranks

    #==========================================================================
    # Rank Series
    #==========================================================================


def test_stop_editor():
    app = QApplication([])
    window = StopEditorUI()
    window.stop_editor.show()
    app.exec()


if __name__ == "__main__":
    test_stop_editor()
