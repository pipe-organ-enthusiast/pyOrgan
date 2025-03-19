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
        self.old_number_pipes: int = self.stop_editor.number_pipes
        self.old_number_harmonics: int = self.stop_editor.number_harmonics
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

    #--------------------------------------------------------------------------
    def __update_number_ranks(self) -> None:
        self.__set_maximum_rank_number()
        self.__update_number_ranks_config_editor()
        self.old_number_ranks = self.number_ranks

    def __set_maximum_rank_number(self) -> None:
        methods: tuple[Callable] = (
            self.stop_editor.rank_number_set_maximum,
            self.stop_editor.rank_number_pipe_set_maximum
        )
        for method in methods:
            method(self.number_ranks)

    def __update_number_ranks_config_editor(self) -> None:
        self.config_editor.number_ranks_set(self.number_ranks)
        if self.number_ranks < self.old_number_ranks:
            for rank in range(self.number_ranks, self.old_number_ranks):
                self.config_editor.del_rank_settings(rank)
        else:
            for rank in range(self.old_number_ranks, self.number_ranks):
                self.config_editor.init_rank_settings(rank)

    #--------------------------------------------------------------------------
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
        ce: StopConfig = self.config_editor
        self.rank_size = ce.rank_size_get(self.rank_number)
        self.number_pipes = ce.number_pipes_get(self.rank_number)
        self.pipe_type = ce.pipe_type_get(self.rank_number)
        self.starting_note = ce.starting_note_get(self.rank_number)
        self.frequency_offset = ce.frequency_offset_get(self.rank_number)
        self.number_harmonics = ce.number_harmonics_get(self.rank_number)
        self.harmonic_number_rank = 1
        self.__update_harmonic_number_rank()

    def __update_rank_size(self) -> None:
        self.rank_size = self.stop_editor.rank_size
        self.config_editor.rank_size_set(self.rank_number, self.rank_size)

    def __update_number_pipes(self) -> None:
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
        self.config_editor.frequency_offset_set(
            rank_number=self.rank_number,
            frequency_offset=self.frequency_offset
        )

    #--------------------------------------------------------------------------
    def __update_number_harmonics(self) -> None:
        self.__set_maximum_harmonic_number()
        self.__update_number_harmonics_config_editor()
        self.old_number_harmonics = self.number_harmonics
    
    def __set_maximum_harmonic_number(self) -> None:
        methods: tuple[Callable] = (
            self.stop_editor.harmonic_number_rank_set_maximum,
            self.stop_editor.harmonic_number_pipe_set_maximum
        )
        for method in methods:
            method(self.number_harmonics)
    
    def __update_number_harmonics_config_editor(self) -> None:
        self.config_editor.number_harmonics_set(
            rank_number=self.rank_number,
            number_harmonics=self.number_harmonics
        )
        if self.number_harmonics < self.old_number_harmonics:
            for harmonic in range(
                self.number_harmonics,
                self.old_number_harmonics
            ):
                self.config_editor.del_harmonic_settings(
                    rank_number=self.rank_number,
                    harmonic_number=harmonic
                )
        else:
            for harmonic in range(
                self.old_number_harmonics,
                self.number_harmonics
            ):
                self.config_editor.init_harmonic_settings(
                    rank_number=self.rank_number,
                    harmonic_number=harmonic
                )

    #--------------------------------------------------------------------------
    def __update_harmonic_number_rank(self) -> None:
        ce: StopConfig = self.config_editor
        self.amplitude_rank = ce.amplitude_rank_get(
            rank_number=self.rank_number,
            harmonic_number=self.harmonic_number_rank
        )
        self.attack_harmonic_rank = ce.attack_time_rank_harmonic_get(
            rank_number=self.rank_number,
            harmonic_number=self.harmonic_number_rank
        )
        self.decay_harmonic_rank = ce.decay_time_rank_harmonic_get(
            rank_number=self.rank_number,
            harmonic_number=self.harmonic_number_rank
        )
        self.sustain_harmonic_rank = ce.sustain_level_rank_harmonic_get(
            rank_number=self.rank_number,
            harmonic_number=self.harmonic_number_rank
        )
        self.release_harmonic_rank = ce.release_time_rank_harmonic_get(
            rank_number=self.rank_number,
            harmonic_number=self.harmonic_number_rank
        )

    def __update_amplitude_rank(self) -> None:
        self.config_editor.amplitude_rank_set(
            rank_number=self.rank_number,
            harmonic_number=self.harmonic_number_rank,
            amplitude=self.amplitude_rank
        )

    def __update_attack_time_rank_harmonic(self) -> None:
        self.config_editor.attack_time_rank_harmonic_set(
            rank_number=self.rank_number,
            harmonic_number=self.harmonic_number_rank,
            attack_time=self.attack_harmonic_rank
        )

    def __update_decay_time_rank_harmonic(self) -> None:
        self.config_editor.decay_time_rank_harmonic_set(
            rank_number=self.rank_number,
            harmonic_number=self.harmonic_number_rank,
            decay_time=self.decay_harmonic_rank
        )

    def __update_sustain_level_rank_harmonic(self) -> None:
        self.config_editor.sustain_level_rank_harmonic_set(
            rank_number=self.rank_number,
            harmonic_number=self.harmonic_number_rank,
            sustain_level=self.sustain_harmonic_rank
        )

    def __update_release_time_rank_harmonic(self) -> None:
        self.config_editor.release_time_rank_harmonic_set(
            rank_number=self.rank_number,
            harmonic_number=self.harmonic_number_rank,
            release_time=self.release_harmonic_rank
        )

    def __update_attack_time_rank(self) -> None:
        self.config_editor.attack_time_rank_set(
            rank_number=self.rank_number,
            attack_time=self.attack_rank
        )

    def __update_decay_time_rank(self) -> None:
        self.config_editor.decay_time_rank_set(
            rank_number=self.rank_number,
            decay_time=self.decay_rank
        )

    def __update_sustain_level_rank(self) -> None:
        self.config_editor.sustain_level_rank_set(
            rank_number=self.rank_number,
            sustain_level=self.sustain_rank
        )

    def __update_release_time_rank(self) -> None:
        self.config_editor.release_time_rank_set(
            rank_number=self.rank_number,
            release_time=self.release_rank
        )

    def __update_rank_number_pipe(self) -> None:
        self.pipe_number = 1
        self.__update_pipe_number()

    def __update_pipe_number(self) -> None:
        self.note = self.config_editor.note_get(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number
        )
        self.relative_note = self.config_editor.relative_note_get(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number
        )
        self.harmonic_number_pipe = 1
        self.__update_harmonic_number_pipe()
        self.attack_pipe = self.config_editor.attack_time_pipe_get(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number
        )
        self.decay_pipe = self.config_editor.decay_time_pipe_get(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number
        )
        self.sustain_pipe = self.config_editor.sustain_level_pipe_get(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number
        )
        self.release_pipe = self.config_editor.release_time_pipe_get(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number
        )

    def __update_note(self) -> None:
        self.config_editor.note_set(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number,
            note=self.note
        )

    def __update_relative_note(self) -> None:
        self.config_editor.relative_note_set(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number,
            relative_note=self.relative_note
        )

    def __update_harmonic_number_pipe(self) -> None:
        ce: StopConfig = self.config_editor
        self.amplitude_pipe = ce.amplitude_pipe_get(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number,
            harmonic_number=self.harmonic_number_pipe
        )
        self.attack_harmonic_pipe = ce.attack_time_pipe_harmonic_get(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number,
            harmonic_number=self.harmonic_number_pipe
        )
        self.decay_harmonic_pipe = ce.decay_time_pipe_harmonic_get(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number,
            harmonic_number=self.harmonic_number_pipe
        )
        self.sustain_harmonic_pipe = ce.sustain_level_pipe_harmonic_get(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number,
            harmonic_number=self.harmonic_number_pipe
        )
        self.release_harmonic_pipe = ce.release_time_pipe_harmonic_get(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number,
            harmonic_number=self.harmonic_number_pipe
        )

    def __update_amplitude_pipe(self) -> None:
        self.config_editor.amplitude_pipe_set(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number,
            harmonic_number=self.harmonic_number_pipe,
            amplitude=self.amplitude_pipe
        )

    def __update_attack_time_pipe_harmonic(self) -> None:
        self.config_editor.attack_time_pipe_harmonic_set(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number,
            harmonic_number=self.harmonic_number_pipe,
            attack_time=self.attack_harmonic_pipe
        )

    def __update_decay_time_pipe_harmonic(self) -> None:
        self.config_editor.decay_time_pipe_harmonic_set(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number,
            harmonic_number=self.harmonic_number_pipe,
            decay_time=self.decay_harmonic_pipe
        )

    def __update_sustain_level_pipe_harmonic(self) -> None:
        self.config_editor.sustain_level_pipe_harmonic_set(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number,
            harmonic_number=self.harmonic_number_pipe,
            sustain_level=self.sustain_harmonic_pipe
        )

    def __update_release_time_pipe_harmonic(self) -> None:
        self.config_editor.release_time_pipe_harmonic_set(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number,
            harmonic_number=self.harmonic_number_pipe,
            release_time=self.release_harmonic_pipe
        )

    def __update_attack_time_pipe(self) -> None:
        self.config_editor.attack_time_pipe_set(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number,
            attack_time=self.attack_pipe
        )

    def __update_decay_time_pipe(self) -> None:
        self.config_editor.decay_time_pipe_set(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number,
            decay_time=self.decay_pipe
        )

    def __update_sustain_level_pipe(self) -> None:
        self.config_editor.sustain_level_pipe_set(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number,
            sustain_level=self.sustain_pipe
        )

    def __update_release_time_pipe(self) -> None:
        self.config_editor.release_time_pipe_set(
            rank_number=self.rank_number_pipe,
            pipe_number=self.pipe_number,
            release_time=self.release_pipe
        )

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
    @property
    def rank_series(self) -> str:
        return self.stop_editor.rank_series

    @rank_series.setter
    def rank_series(self, rank_series: str) -> None:
        self.stop_editor.rank_series = rank_series

    #==========================================================================
    # Rank Number
    #==========================================================================
    @property
    def rank_number(self) -> int:
        return self.stop_editor.rank_number

    @rank_number.setter
    def rank_number(self, rank_number: int) -> None:
        self.stop_editor.rank_number = rank_number

    #==========================================================================
    # Rank Size
    #==========================================================================
    @property
    def rank_size(self) -> str:
        return self.stop_editor.rank_size

    @rank_size.setter
    def rank_size(self, rank_size: str) -> None:
        self.stop_editor.rank_size = rank_size

    #==========================================================================
    # Number of Pipes
    #==========================================================================
    @property
    def number_pipes(self) -> int:
        return self.stop_editor.number_pipes

    @number_pipes.setter
    def number_pipes(self, number_pipes: int) -> None:
        self.stop_editor.number_pipes = number_pipes

    #==========================================================================
    # Pipe Type
    #==========================================================================
    @property
    def pipe_type(self) -> str:
        return self.stop_editor.pipe_type

    @pipe_type.setter
    def pipe_type(self, pipe_type: str) -> None:
        self.stop_editor.pipe_type = pipe_type

    #==========================================================================
    # Starting Note
    #==========================================================================
    @property
    def starting_note(self) -> str:
        return self.stop_editor.starting_note

    @starting_note.setter
    def starting_note(self, starting_note: str) -> None:
        self.stop_editor.starting_note = starting_note

    #==========================================================================
    # Frequency Offset
    #==========================================================================
    @property
    def frequency_offset(self) -> int:
        return self.stop_editor.frequency_offset

    @frequency_offset.setter
    def frequency_offset(self, frequency_offset: int) -> None:
        self.stop_editor.frequency_offset = frequency_offset

    #==========================================================================
    # Number of Harmonics
    #==========================================================================
    @property
    def number_harmonics(self) -> int:
        return self.stop_editor.number_harmonics

    @number_harmonics.setter
    def number_harmonics(self, number_harmonics: int) -> None:
        self.stop_editor.number_harmonics = number_harmonics

    #==========================================================================
    # Harmonic Number - Rank
    #==========================================================================
    @property
    def harmonic_number_rank(self) -> int:
        return self.stop_editor.harmonic_number_rank

    @harmonic_number_rank.setter
    def harmonic_number_rank(self, harmonic_number_rank: int) -> None:
        self.stop_editor.harmonic_number_rank = harmonic_number_rank

    #==========================================================================
    # Amplitude - Rank
    #==========================================================================
    @property
    def amplitude_rank(self) -> int:
        return self.stop_editor.amplitude_rank

    @amplitude_rank.setter
    def amplitude_rank(self, amplitude_rank: int) -> None:
        self.stop_editor.amplitude_rank = amplitude_rank

    #==========================================================================
    # Attack Time - Rank Harmonic
    #==========================================================================
    @property
    def attack_harmonic_rank(self) -> int:
        return self.stop_editor.attack_time_harmonic_rank

    @attack_harmonic_rank.setter
    def attack_harmonic_rank(self, attack_harmonic_rank: int) -> None:
        self.stop_editor.attack_time_harmonic_rank = attack_harmonic_rank

    #==========================================================================
    # Decay Time - Rank Harmonic
    #==========================================================================
    @property
    def decay_harmonic_rank(self) -> int:
        return self.stop_editor.decay_time_harmonic_rank

    @decay_harmonic_rank.setter
    def decay_harmonic_rank(self, decay_harmonic_rank: int) -> None:
        self.stop_editor.decay_time_harmonic_rank = decay_harmonic_rank

    #==========================================================================
    # Sustain Level - Rank Harmonic
    #==========================================================================
    @property
    def sustain_harmonic_rank(self) -> int:
        return self.stop_editor.sustain_level_harmonic_rank

    @sustain_harmonic_rank.setter
    def sustain_harmonic_rank(self, sustain_harmonic_rank: int) -> None:
        self.stop_editor.sustain_level_harmonic_rank = sustain_harmonic_rank

    #==========================================================================
    # Release Time - Rank Harmonic
    #==========================================================================
    @property
    def release_harmonic_rank(self) -> int:
        return self.stop_editor.release_time_harmonic_rank

    @release_harmonic_rank.setter
    def release_harmonic_rank(self, release_harmonic_rank: int) -> None:
        self.stop_editor.release_time_harmonic_rank = release_harmonic_rank

    #==========================================================================
    # Attack Time - Rank
    #==========================================================================
    @property
    def attack_rank(self) -> int:
        return self.stop_editor.attack_time_rank

    @attack_rank.setter
    def attack_rank(self, attack_rank: int) -> None:
        self.stop_editor.attack_time_rank = attack_rank

    #==========================================================================
    # Decay Time - Rank
    #==========================================================================
    @property
    def decay_rank(self) -> int:
        return self.stop_editor.decay_time_rank

    @decay_rank.setter
    def decay_rank(self, decay_rank: int) -> None:
        self.stop_editor.decay_time_rank = decay_rank

    #==========================================================================
    # Sustain Level - Rank
    #==========================================================================
    @property
    def sustain_rank(self) -> int:
        return self.stop_editor.sustain_level_rank

    @sustain_rank.setter
    def sustain_rank(self, sustain_rank: int) -> None:
        self.stop_editor.sustain_level_rank = sustain_rank

    #==========================================================================
    # Release Time - Rank
    #==========================================================================
    @property
    def release_rank(self) -> int:
        return self.stop_editor.release_time_rank

    @release_rank.setter
    def release_rank(self, release_rank: int) -> None:
        self.stop_editor.release_time_rank = release_rank

    #==========================================================================
    # Rank Number - Pipe
    #==========================================================================
    @property
    def rank_number_pipe(self) -> int:
        return self.stop_editor.rank_number_pipe

    @rank_number_pipe.setter
    def rank_number_pipe(self, rank_number_pipe: int) -> None:
        self.stop_editor.rank_number_pipe = rank_number_pipe

    #==========================================================================
    # Pipe Number
    #==========================================================================
    @property
    def pipe_number(self) -> int:
        return self.stop_editor.pipe_number

    @pipe_number.setter
    def pipe_number(self, pipe_number: int) -> None:
        self.stop_editor.pipe_number = pipe_number

    #==========================================================================
    # Note
    #==========================================================================
    @property
    def note(self) -> str:
        return self.stop_editor.note

    @note.setter
    def note(self, note: str) -> None:
        self.stop_editor.note = note

    #==========================================================================
    # Relative Note
    #==========================================================================
    @property
    def relative_note(self) -> str:
        return self.stop_editor.relative_note

    @relative_note.setter
    def relative_note(self, relative_note: str) -> None:
        self.stop_editor.relative_note = relative_note

    #==========================================================================
    # Harmonic Number - Pipe
    #==========================================================================
    @property
    def harmonic_number_pipe(self) -> int:
        return self.stop_editor.harmonic_number_pipe

    @harmonic_number_pipe.setter
    def harmonic_number_pipe(self, harmonic_number_pipe: int) -> None:
        self.stop_editor.harmonic_number_pipe = harmonic_number_pipe

    #==========================================================================
    # Amplitude - Pipe
    #==========================================================================
    @property
    def amplitude_pipe(self) -> int:
        return self.stop_editor.amplitude_pipe

    @amplitude_pipe.setter
    def amplitude_pipe(self, amplitude_pipe: int) -> None:
        self.stop_editor.amplitude_pipe = amplitude_pipe

    #==========================================================================
    # Attack Time - Pipe Harmonic
    #==========================================================================
    @property
    def attack_harmonic_pipe(self) -> int:
        return self.stop_editor.attack_time_harmonic_pipe

    @attack_harmonic_pipe.setter
    def attack_harmonic_pipe(self, attack_harmonic_pipe: int) -> None:
        self.stop_editor.attack_time_harmonic_pipe = attack_harmonic_pipe

    #==========================================================================
    # Decay Time - Pipe Harmonic
    #==========================================================================
    @property
    def decay_harmonic_pipe(self) -> int:
        return self.stop_editor.decay_time_harmonic_pipe

    @decay_harmonic_pipe.setter
    def decay_harmonic_pipe(self, decay_harmonic_pipe: int) -> None:
        self.stop_editor.decay_time_harmonic_pipe = decay_harmonic_pipe

    #==========================================================================
    # Sustain Level - Pipe Harmonic
    #==========================================================================
    @property
    def sustain_harmonic_pipe(self) -> int:
        return self.stop_editor.sustain_level_harmonic_pipe

    @sustain_harmonic_pipe.setter
    def sustain_harmonic_pipe(self, sustain_harmonic_pipe: int) -> None:
        self.stop_editor.sustain_level_harmonic_pipe = sustain_harmonic_pipe

    #==========================================================================
    # Release Time - Pipe Harmonic
    #==========================================================================
    @property
    def release_harmonic_pipe(self) -> int:
        return self.stop_editor.release_time_harmonic_pipe

    @release_harmonic_pipe.setter
    def release_harmonic_pipe(self, release_harmonic_pipe: int) -> None:
        self.stop_editor.release_time_harmonic_pipe = release_harmonic_pipe

    #==========================================================================
    # Attack Time - Pipe
    #==========================================================================
    @property
    def attack_pipe(self) -> int:
        return self.stop_editor.attack_time_pipe

    @attack_pipe.setter
    def attack_pipe(self, attack_pipe: int) -> None:
        self.stop_editor.attack_time_pipe = attack_pipe

    #==========================================================================
    # Decay Time - Pipe
    #==========================================================================
    @property
    def decay_pipe(self) -> int:
        return self.stop_editor.decay_time_pipe

    @decay_pipe.setter
    def decay_pipe(self, decay_pipe: int) -> None:
        self.stop_editor.decay_time_pipe = decay_pipe

    #==========================================================================
    # Sustain Level - Pipe
    #==========================================================================
    @property
    def sustain_pipe(self) -> int:
        return self.stop_editor.sustain_level_pipe

    @sustain_pipe.setter
    def sustain_pipe(self, sustain_pipe: int) -> None:
        self.stop_editor.sustain_level_pipe = sustain_pipe

    #==========================================================================
    # Release Time - Pipe
    #==========================================================================
    @property
    def release_pipe(self) -> int:
        return self.stop_editor.release_time_pipe

    @release_pipe.setter
    def release_pipe(self, release_pipe: int) -> None:
        self.stop_editor.release_time_pipe = release_pipe


def test_stop_editor():
    app = QApplication([])
    window = StopEditorUI()
    window.stop_editor.show()
    app.exec()


if __name__ == "__main__":
    test_stop_editor()
