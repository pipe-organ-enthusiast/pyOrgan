from gui import StopEditor
from organ import organlib
from config_editors import StopConfig
#------------------------------------------------------------------------------
from PySide6.QtWidgets import QApplication, QFileDialog
#------------------------------------------------------------------------------
from typing import Callable


#******************************************************************************
# Stop Editor
#******************************************************************************
class StopEditorUI:
    def __init__(self) -> None:
        print("class: StopEditorUI")
        print("method: __init__")
        self.stop_editor: StopEditor = StopEditor()
        self.stop_config: StopConfig = StopConfig()
        self.config_file: str = ""
        self.__init_ui()
        self.__default_ui_editor_data()

    #**************************************************************************
    # Configuration
    #**************************************************************************
    #==========================================================================
    # Default Data
    #==========================================================================
    def __default_ui_editor_data(self) -> None:
        print("class: StopEditorUI")
        print("method: __default_ui_editor_data")
        self.__init_rank_number()
        self.stop_config.init_default_config()
        self.__load_ui_editor_data()

    def __init_rank_number(self) -> None:
        print("class: StopEditorUI")
        print("method: __init_rank_number")
        self.rank_number_editor = 1
        self.harmonic_number_rank_editor = 1
        self.rank_number_pipe_editor = 1
        self.pipe_number_editor = 1
        self.harmonic_number_pipe_editor = 1
    
    def __load_ui_editor_data(self) -> None:
        print("class: StopEditorUI")
        print("method: __load_ui_editor_data")
        print("setting stop name")
        self.stop_name_editor = self.stop_name_config
        print("setting stop family")
        self.stop_family_editor = self.stop_family_config
        print("setting organ division")
        self.organ_division_editor = self.organ_division_config
        print("setting number of ranks")
        self.number_ranks_editor = self.number_ranks_config
        print("setting rank series")
        self.rank_series_editor = self.rank_series_config
        print("setting rank size")
        self.rank_size_editor = self.rank_size_config
        print("setting number of pipes")
        self.number_pipes_editor = self.number_pipes_config
        print("setting pipe type")
        self.pipe_type_editor = self.pipe_type_config
        print("setting starting note")
        self.starting_note_editor = self.starting_note_config
        print("setting frequency offset")
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
        #print("setting relative note")
        self.relative_note_editor = self.relative_note_config
        #print("setting amplitude pipe")
        self.amplitude_pipe_editor = self.amplitude_pipe_config
        self.attack_harmonic_pipe_editor = self.attack_harmonic_pipe_config
        self.decay_harmonic_pipe_editor = self.decay_harmonic_pipe_config
        self.sustain_harmonic_pipe_editor = self.sustain_harmonic_pipe_config
        self.release_harmonic_pipe_editor = self.release_harmonic_pipe_config
        self.attack_pipe_editor = self.attack_pipe_config
        self.decay_pipe_editor = self.decay_pipe_config
        self.sustain_pipe_editor = self.sustain_pipe_config
        self.release_pipe_editor = self.release_pipe_config

    #==========================================================================
    # Initialize UI Configuration
    #==========================================================================
    def __init_ui(self) -> None:
        print("method: __init_ui")
        self.__stop_name_config()
        self.__stop_family_config()
        self.__organ_division_config()
        self.__number_ranks_config()
        self.__rank_series_config()
        self.__rank_number_config()
        self.__rank_size_config()
        self.__number_pipes_config()
        self.__pipe_type_config()
        self.__starting_note_config()
        self.__frequency_offset_config()
        self.__number_harmonics_config()
        self.__rank_harmonic_number_config()
        self.__rank_amplitude_config()
        self.__rank_harmonic_attack_config()
        self.__rank_harmonic_decay_config()
        self.__rank_harmonic_sustain_config()
        self.__rank_harmonic_release_config()
        self.__rank_attack_config()
        self.__rank_decay_config()
        self.__rank_sustain_config()
        self.__rank_release_config()
        self.__rank_number_pipe_config()
        self.__pipe_number_config()
        self.__note_config()
        self.__relative_note_config()
        self.__harmonic_number_pipe_config()
        self.__amplitude_pipe_config()
        self.__attack_harmonic_pipe_config()
        self.__decay_harmonic_pipe_config()
        self.__sustain_harmonic_pipe_config()
        self.__release_harmonic_pipe_config()
        self.__attack_pipe_config()
        self.__decay_pipe_config()
        self.__sustain_pipe_config()
        self.__release_pipe_config()
        self.__options_config()

    def __stop_name_config(self) -> None:
        print("method: __stop_name_config")
        stop_names: tuple[str, ...] = ("",) + organlib.STOP_NAMES
        self.stop_editor.stop_names_populate(stop_names)
        self.stop_editor.stop_name_change(self.__update_stop_name)

    def __stop_family_config(self) -> None:
        print("method: __stop_family_config")
        stop_families: tuple[str, ...] = ("",) + organlib.STOP_FAMILIES
        self.stop_editor.stop_families_populate(stop_families)
        self.stop_editor.stop_family_change(self.__update_stop_family)

    def __organ_division_config(self) -> None:
        print("method: __organ_division_config")
        organ_divisions: tuple[str, ...] = ("",) + organlib.ORGAN_DIVISIONS
        self.stop_editor.organ_divisions_populate(organ_divisions)
        self.stop_editor.organ_division_change(self.__update_organ_division)

    def __number_ranks_config(self) -> None:
        print("method: __number_ranks_config")
        self.stop_editor.number_ranks_set_minimum(1)
        self.stop_editor.number_ranks_set_maximum(20)
        self.stop_editor.number_ranks_change(self.__update_number_ranks)

    def __rank_series_config(self) -> None:
        print("method: __rank_series_config")
        rank_series: tuple[str, ...] = ("",) + organlib.RANK_SERIES
        self.stop_editor.rank_series_populate(rank_series)
        self.stop_editor.rank_series_change(self.__update_rank_series)

    def __rank_number_config(self) -> None:
        print("method: __rank_number_config")
        self.stop_editor.rank_number_set_minimum(1)
        self.stop_editor.rank_number_change(self.__update_rank_number)

    def __rank_size_config(self) -> None:
        print("method: __rank_size_config")
        rank_sizes: tuple[str, ...] = ("",) + organlib.RANK_SIZES
        self.stop_editor.rank_size_populate(rank_sizes)
        self.stop_editor.rank_size_change(self.__update_rank_size)

    def __number_pipes_config(self) -> None:
        print("method: __number_pipes_config")
        self.stop_editor.number_pipes_set_minimum(1)
        self.stop_editor.number_pipes_set_maximum(61)
        self.stop_editor.number_pipes_change(self.__update_number_pipes)

    def __pipe_type_config(self) -> None:
        print("method: __pipe_type_config")
        pipe_types: tuple[str, ...] = ("",) + organlib.PIPE_TYPES
        self.stop_editor.pipe_types_populate(pipe_types)
        self.stop_editor.pipe_type_change(self.__update_pipe_type)

    def __starting_note_config(self) -> None:
        print("method: __starting_note_config")
        starting_notes: tuple[str, ...] = ("",) + organlib.NOTES
        self.stop_editor.starting_note_populate(starting_notes)
        self.stop_editor.starting_note_change(self.__update_starting_note)

    def __frequency_offset_config(self) -> None:
        print("method: __frequency_offset_config")
        self.stop_editor.frequency_offset_set_minimum(-7)
        self.stop_editor.frequency_offset_set_maximum(7)
        self.stop_editor.frequency_offset_change(
            self.__update_frequency_offset
        )

    def __number_harmonics_config(self) -> None:
        print("method: __number_harmonics_config")
        self.stop_editor.number_harmonics_set_minimum(1)
        self.stop_editor.number_harmonics_set_maximum(20)
        self.stop_editor.number_harmonics_change(
            self.__update_number_harmonics
        )

    def __rank_harmonic_number_config(self) -> None:
        print("method: __rank_harmonic_number_config")
        self.stop_editor.harmonic_number_rank_set_minimum(1)
        self.stop_editor.harmonic_number_rank_change(
            self.__update_harmonic_number_rank
        )

    def __rank_amplitude_config(self) -> None:
        print("method: __rank_amplitude_config")
        self.stop_editor.amplitude_rank_set_minimum(0)
        self.stop_editor.amplitude_rank_set_maximum(100)
        self.stop_editor.amplitude_rank_change(self.__update_rank_amplitude)

    def __rank_harmonic_attack_config(self) -> None:
        print("method: __rank_harmonic_attack_config")
        self.stop_editor.attack_time_rank_harmonic_set_minimum(0)
        self.stop_editor.attack_time_rank_harmonic_set_maximum(1000)
        self.stop_editor.attack_time_rank_harmonic_change(
            self.__update_rank_harmonic_attack
        )

    def __rank_harmonic_decay_config(self) -> None:
        print("method: __rank_harmonic_decay_config")
        self.stop_editor.decay_time_rank_harmonic_set_minimum(0)
        self.stop_editor.decay_time_rank_harmonic_set_maximum(1000)
        self.stop_editor.decay_time_rank_harmonic_change(
            self.__update_rank_harmonic_decay
        )

    def __rank_harmonic_sustain_config(self) -> None:
        print("method: __rank_harmonic_sustain_config")
        self.stop_editor.sustain_level_rank_harmonic_set_minimum(0)
        self.stop_editor.sustain_level_rank_harmonic_set_maximum(100)
        self.stop_editor.sustain_level_rank_harmonic_change(
            self.__update_rank_harmonic_sustain
        )

    def __rank_harmonic_release_config(self) -> None:
        self.stop_editor.release_time_rank_harmonic_set_minimum(0)
        self.stop_editor.release_time_rank_harmonic_set_maximum(1000)
        self.stop_editor.release_time_rank_harmonic_change(
            self.__update_rank_harmonic_release
        )

    def __rank_attack_config(self) -> None:
        self.stop_editor.attack_time_rank_set_minimum(0)
        self.stop_editor.attack_time_rank_set_maximum(1000)
        self.stop_editor.attack_time_rank_change(self.__update_rank_attack)

    def __rank_decay_config(self) -> None:
        self.stop_editor.decay_time_rank_set_minimum(0)
        self.stop_editor.decay_time_rank_set_maximum(1000)
        self.stop_editor.decay_time_rank_change(self.__update_rank_decay)

    def __rank_sustain_config(self) -> None:
        self.stop_editor.sustain_level_rank_set_minimum(0)
        self.stop_editor.sustain_level_rank_set_maximum(100)
        self.stop_editor.sustain_level_rank_change(self.__update_rank_sustain)

    def __rank_release_config(self) -> None:
        self.stop_editor.release_time_rank_set_minimum(0)
        self.stop_editor.release_time_rank_set_maximum(1000)
        self.stop_editor.release_time_rank_change(self.__update_rank_release)

    def __rank_number_pipe_config(self) -> None:
        self.stop_editor.rank_number_pipe_set_minimum(1)
        self.stop_editor.rank_number_pipe_change(
            self.__update_rank_number_pipe
        )

    def __pipe_number_config(self) -> None:
        self.stop_editor.pipe_number_set_minimum(1)
        self.stop_editor.pipe_number_change(self.__update_pipe_number)

    def __note_config(self) -> None:
        notes: tuple[str, ...] = ("",) + organlib.NOTES
        self.stop_editor.note_populate(notes)
        self.stop_editor.note_change(self.__update_note)

    def __relative_note_config(self) -> None:
        notes: tuple[str, ...] = ("",) + organlib.NOTES
        self.stop_editor.relative_note_populate(notes)
        self.stop_editor.relative_note_change(self.__update_relative_note)

    def __harmonic_number_pipe_config(self) -> None:
        self.stop_editor.harmonic_number_pipe_set_minimum(1)
        self.stop_editor.harmonic_number_pipe_change(
            self.__update_harmonic_number_pipe
        )

    def __amplitude_pipe_config(self) -> None:
        self.stop_editor.amplitude_pipe_set_minimum(0)
        self.stop_editor.amplitude_pipe_set_maximum(100)
        self.stop_editor.amplitude_pipe_change(self.__update_pipe_amplitude)

    def __attack_harmonic_pipe_config(self) -> None:
        self.stop_editor.attack_time_pipe_harmonic_set_minimum(0)
        self.stop_editor.attack_time_pipe_harmonic_set_maximum(1000)
        self.stop_editor.attack_time_pipe_harmonic_change(
            self.__update_pipe_harmonic_attack
        )

    def __decay_harmonic_pipe_config(self) -> None:
        self.stop_editor.decay_time_pipe_harmonic_set_minimum(0)
        self.stop_editor.decay_time_pipe_harmonic_set_maximum(1000)
        self.stop_editor.decay_time_pipe_harmonic_change(
            self.__update_pipe_harmonic_decay
        )

    def __sustain_harmonic_pipe_config(self) -> None:
        self.stop_editor.sustain_level_pipe_harmonic_set_minimum(0)
        self.stop_editor.sustain_level_pipe_harmonic_set_maximum(100)
        self.stop_editor.sustain_level_pipe_harmonic_change(
            self.__update_pipe_harmonic_sustain
        )

    def __release_harmonic_pipe_config(self) -> None:
        self.stop_editor.release_time_pipe_harmonic_set_minimum(0)
        self.stop_editor.release_time_pipe_harmonic_set_maximum(1000)
        self.stop_editor.release_time_pipe_harmonic_change(
            self.__update_pipe_harmonic_release
        )

    def __attack_pipe_config(self) -> None:
        self.stop_editor.attack_time_pipe_set_minimum(0)
        self.stop_editor.attack_time_pipe_set_maximum(1000)
        self.stop_editor.attack_time_pipe_change(self.__update_pipe_attack)

    def __decay_pipe_config(self) -> None:
        self.stop_editor.decay_time_pipe_set_minimum(0)
        self.stop_editor.decay_time_pipe_set_maximum(1000)
        self.stop_editor.decay_time_pipe_change(self.__update_pipe_decay)

    def __sustain_pipe_config(self) -> None:
        self.stop_editor.sustain_level_pipe_set_minimum(0)
        self.stop_editor.sustain_level_pipe_set_maximum(100)
        self.stop_editor.sustain_level_pipe_change(self.__update_pipe_sustain)

    def __release_pipe_config(self) -> None:
        self.stop_editor.release_time_pipe_set_minimum(0)
        self.stop_editor.release_time_pipe_set_maximum(1000)
        self.stop_editor.release_time_pipe_change(self.__update_pipe_release)

    def __options_config(self) -> None:
        self.stop_editor.load_stop_action(self.__load_stop)
        self.stop_editor.cancel_changes_action(self.__cancel_changes)
        self.stop_editor.save_stop_action(self.__save_stop)

    #**************************************************************************
    # Actions
    #**************************************************************************
    def __set_maximum_number(
            self,
            editor_number: int,
            *methods: Callable[[int], None]
    ) -> None:
        for method in methods:
            method(editor_number)
    
    def __update_stop_header(self) -> None:
        condition1: bool = self.stop_name_editor != ""
        condition2: bool = self.number_ranks_editor > 1
        condition3: bool = self.rank_size_editor != ""
        condition4: bool = condition2 or condition3
        if condition1 and condition4:
            self.stop_editor.update_stop_header()
    
    def __update_stop_name(self) -> None:
        self.stop_name_config = self.stop_name_editor
        self.__update_stop_header()

    def __update_stop_family(self) -> None:
        self.stop_family_config = self.stop_family_editor

    def __update_organ_division(self) -> None:
        self.organ_division_config = self.organ_division_editor

    def __update_number_ranks(self) -> None:
        # Set Maximum Rank Number
        self.__set_maximum_number(
            self.number_ranks_editor,
            self.stop_editor.rank_number_set_maximum,
            self.stop_editor.number_harmonics_set_maximum
        )
        self.number_ranks_config = self.number_ranks_editor
        self.__update_stop_header()

    def __update_rank_series(self) -> None:
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
        self.rank_series_config = self.rank_series_editor

    def __update_rank_number_general(self) -> None:
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
        self.rank_number_pipe_editor = self.rank_number_editor
        self.__update_rank_number_general()

    def __update_rank_size(self) -> None:
        self.rank_size_config = self.rank_size_editor
        self.__update_stop_header()

    def __update_number_pipes(self) -> None:
        # Set Maximum Pipe Number
        self.__set_maximum_number(
            self.number_pipes_editor,
            self.stop_editor.pipe_number_set_maximum,
        )
        self.number_pipes_config = self.number_pipes_editor

    def __update_pipe_type(self) -> None:
        self.pipe_type_config = self.pipe_type_editor

    def __update_starting_note(self) -> None:
        print("method: __update_starting_note")
        #rank_number = self.rank_number_editor
        #number_pipes = self.number_pipes_editor
        #notes: tuple[str, ...] = organlib.NOTES
        #for num in range(1, number_pipes):
        #    self.stop_config.note_set(
        #        rank_number=rank_number,
        #        pipe_number=num,
        #        note=notes[num]
        #    )
        #    self.stop_config.relative_note_set(
        #        rank_number=rank_number,
        #        pipe_number=num,
        #        relative_note=notes[num]
        #    )
        #self.starting_note_config = self.starting_note_editor

    def __update_frequency_offset(self) -> None:
        self.frequency_offset_config = self.frequency_offset_editor

    def __update_number_harmonics(self) -> None:
        # Set Maximum Harmonic Number
        self.__set_maximum_number(
            self.number_harmonics_editor,
            self.stop_editor.harmonic_number_rank_set_maximum,
            self.stop_editor.harmonic_number_pipe_set_maximum
        )
        self.number_harmonics_config = self.number_harmonics_editor

    def __update_harmonic_number(self) -> None:
        self.amplitude_rank_editor = self.amplitude_rank_config
        self.attack_harmonic_rank_editor = self.attack_harmonic_rank_config
        self.decay_harmonic_rank_editor = self.decay_harmonic_rank_config
        self.sustain_harmonic_rank_editor = self.sustain_harmonic_rank_config
        self.release_harmonic_rank_editor = self.release_harmonic_rank_config
        self.harmonic_number_pipe_editor = self.harmonic_number_rank_editor
        self.amplitude_pipe_editor = self.amplitude_pipe_config
        self.attack_harmonic_pipe_editor = self.attack_harmonic_pipe_config
        self.decay_harmonic_pipe_editor = self.decay_harmonic_pipe_config
        self.sustain_harmonic_pipe_editor = self.sustain_harmonic_pipe_config
        self.release_harmonic_pipe_editor = self.release_harmonic_pipe_config
        self.harmonic_number_rank_editor = self.harmonic_number_pipe_editor

    def __update_harmonic_number_rank(self) -> None:
        self.harmonic_number_pipe_editor = self.harmonic_number_rank_editor
        self.__update_harmonic_number()

    def __update_rank_amplitude(self) -> None:
        self.amplitude_rank_config = self.amplitude_rank_editor

    def __update_rank_harmonic_attack(self) -> None:
        self.attack_harmonic_rank_config = self.attack_harmonic_rank_editor

    def __update_rank_harmonic_decay(self) -> None:
        self.decay_harmonic_rank_config = self.decay_harmonic_rank_editor

    def __update_rank_harmonic_sustain(self) -> None:
        self.sustain_harmonic_rank_config = self.sustain_harmonic_rank_editor

    def __update_rank_harmonic_release(self) -> None:
        self.release_harmonic_rank_config = self.release_harmonic_rank_editor

    def __update_rank_attack(self) -> None:
        self.attack_rank_config = self.attack_rank_editor

    def __update_rank_decay(self) -> None:
        self.decay_rank_config = self.decay_rank_editor

    def __update_rank_sustain(self) -> None:
        self.sustain_rank_config = self.sustain_rank_editor

    def __update_rank_release(self) -> None:
        self.release_rank_config = self.release_rank_editor

    def __update_rank_number_pipe(self) -> None:
        self.rank_number_editor = self.rank_number_pipe_editor
        self.__update_rank_number_general()

    def __update_pipe_number(self) -> None:
        self.note_editor = self.note_config
        self.relative_note_editor = self.relative_note_config
        self.harmonic_number_pipe_editor = 1
        self.__update_harmonic_number()
        self.attack_pipe_editor = self.attack_pipe_config
        self.decay_pipe_editor = self.decay_pipe_config
        self.sustain_pipe_editor = self.sustain_pipe_config
        self.release_pipe_editor = self.release_pipe_config

    def __update_note(self) -> None:
        self.note_config = self.note_editor

    def __update_relative_note(self) -> None:
        #print("updating relative note...")
        self.relative_note_config = self.relative_note_editor
        #starting_pipe: int = self.pipe_number_editor
        #total_pipes: int = self.number_pipes_editor
        #number_pipes: int = len(range(starting_pipe, total_pipes))
        #note: str = self.relative_note_editor
        #notes: tuple[str, ...] = organlib.NOTES
        #note_index: int = notes.index(note)
        #revised_notes: tuple[str, ...] = notes[note_index:]
        #if len(revised_notes) < number_pipes:
        #    number_pipes = len(revised_notes)
        #for num in range(number_pipes):
        #    print(self.rank_number_editor, starting_pipe+num, revised_notes[num])
        #    self.stop_config.relative_note_set(
        #        rank_number=self.rank_number_editor,
        #        pipe_number=starting_pipe+num,
        #        relative_note=revised_notes[num]
        #    )
        #print("Relative Notes updated")

    def __update_harmonic_number_pipe(self) -> None:
        self.harmonic_number_rank_editor = self.harmonic_number_pipe_editor
        self.__update_harmonic_number()

    def __update_pipe_amplitude(self) -> None:
        self.amplitude_pipe_config = self.amplitude_pipe_editor

    def __update_pipe_attack(self) -> None:
        self.attack_pipe_config = self.attack_pipe_editor

    def __update_pipe_decay(self) -> None:
        self.decay_pipe_config = self.decay_pipe_editor

    def __update_pipe_sustain(self) -> None:
        self.sustain_pipe_config = self.sustain_pipe_editor

    def __update_pipe_release(self) -> None:
        self.release_pipe_config = self.release_pipe_editor

    def __update_pipe_harmonic_attack(self) -> None:
        self.attack_harmonic_pipe_config = self.attack_harmonic_pipe_editor

    def __update_pipe_harmonic_decay(self) -> None:
        self.decay_harmonic_pipe_config = self.decay_harmonic_pipe_editor

    def __update_pipe_harmonic_sustain(self) -> None:
        self.sustain_harmonic_pipe_config = self.sustain_harmonic_pipe_editor

    def __update_pipe_harmonic_release(self) -> None:
        self.release_harmonic_pipe_config = self.release_harmonic_pipe_editor

    def __load_config(self) -> None:
        self.stop_config.load_file(self.config_file)
        self.__init_rank_number()
        self.__load_ui_editor_data()

    def __load_stop(self) -> None:
        file_dialog: QFileDialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("JSON Files (*.json)")
        file_dialog.setViewMode(QFileDialog.ViewMode.Detail)
        file_dialog.setDirectory("src/config/stops")
        self.config_file = file_dialog.getOpenFileName()[0]
        self.__load_config()

    def __cancel_changes(self) -> None:
        if self.config_file == "":
            self.__default_ui_editor_data()
        else:
            self.__load_config()

    def __save_stop(self) -> None:
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
        return self.stop_editor.stop_header

    #--------------------------------------------------------------------------
    # Stop Name
    #--------------------------------------------------------------------------
    @property
    def stop_name_editor(self) -> str:
        return self.stop_editor.stop_name

    @stop_name_editor.setter
    def stop_name_editor(self, value: str) -> None:
        self.stop_editor.stop_name = value

    #--------------------------------------------------------------------------
    # Stop Family
    #--------------------------------------------------------------------------
    @property
    def stop_family_editor(self) -> str:
        return self.stop_editor.stop_family

    @stop_family_editor.setter
    def stop_family_editor(self, value: str) -> None:
        self.stop_editor.stop_family = value

    #--------------------------------------------------------------------------
    # Organ Division
    #--------------------------------------------------------------------------
    @property
    def organ_division_editor(self) -> str:
        return self.stop_editor.organ_division

    @organ_division_editor.setter
    def organ_division_editor(self, value: str) -> None:
        self.stop_editor.organ_division = value

    #--------------------------------------------------------------------------
    # Number of Ranks
    #--------------------------------------------------------------------------
    @property
    def number_ranks_editor(self) -> int:
        return self.stop_editor.number_ranks

    @number_ranks_editor.setter
    def number_ranks_editor(self, value: int) -> None:
        self.stop_editor.number_ranks = value

    #--------------------------------------------------------------------------
    # Rank Series
    #--------------------------------------------------------------------------
    @property
    def rank_series_editor(self) -> str:
        return self.stop_editor.rank_series

    @rank_series_editor.setter
    def rank_series_editor(self, value: str) -> None:
        self.stop_editor.rank_series = value

    #--------------------------------------------------------------------------
    # Rank Number
    #--------------------------------------------------------------------------
    @property
    def rank_number_editor(self) -> int:
        return self.stop_editor.rank_number

    @rank_number_editor.setter
    def rank_number_editor(self, value: int) -> None:
        self.stop_editor.rank_number = value

    #--------------------------------------------------------------------------
    # Rank Size
    #--------------------------------------------------------------------------
    @property
    def rank_size_editor(self) -> str:
        return self.stop_editor.rank_size

    @rank_size_editor.setter
    def rank_size_editor(self, value: str) -> None:
        self.stop_editor.rank_size = value

    #--------------------------------------------------------------------------
    # Number of Pipes
    #--------------------------------------------------------------------------
    @property
    def number_pipes_editor(self) -> int:
        return self.stop_editor.number_pipes

    @number_pipes_editor.setter
    def number_pipes_editor(self, value: int) -> None:
        self.stop_editor.number_pipes = value

    #--------------------------------------------------------------------------
    # Pipe Type
    #--------------------------------------------------------------------------
    @property
    def pipe_type_editor(self) -> str:
        return self.stop_editor.pipe_type

    @pipe_type_editor.setter
    def pipe_type_editor(self, value: str) -> None:
        self.stop_editor.pipe_type = value

    #--------------------------------------------------------------------------
    # Starting Note
    #--------------------------------------------------------------------------
    @property
    def starting_note_editor(self) -> str:
        print("method: starting_note_editor (getter)")
        return self.stop_editor.starting_note

    @starting_note_editor.setter
    def starting_note_editor(self, value: str) -> None:
        print("method: starting_note_editor (setter)")
        self.stop_editor.starting_note = value

    #--------------------------------------------------------------------------
    # Frequency Offset
    #--------------------------------------------------------------------------
    @property
    def frequency_offset_editor(self) -> int:
        return self.stop_editor.frequency_offset

    @frequency_offset_editor.setter
    def frequency_offset_editor(self, value: int) -> None:
        self.stop_editor.frequency_offset = value

    #--------------------------------------------------------------------------
    # Number of Harmonics
    #--------------------------------------------------------------------------
    @property
    def number_harmonics_editor(self) -> int:
        return self.stop_editor.number_harmonics

    @number_harmonics_editor.setter
    def number_harmonics_editor(self, value: int) -> None:
        self.stop_editor.number_harmonics = value

    #--------------------------------------------------------------------------
    # Harmonic Number - Rank
    #--------------------------------------------------------------------------
    @property
    def harmonic_number_rank_editor(self) -> int:
        return self.stop_editor.harmonic_number_rank

    @harmonic_number_rank_editor.setter
    def harmonic_number_rank_editor(self, value: int) -> None:
        self.stop_editor.harmonic_number_rank = value

    #--------------------------------------------------------------------------
    # Amplitude - Rank
    #--------------------------------------------------------------------------
    @property
    def amplitude_rank_editor(self) -> int:
        return self.stop_editor.amplitude_rank

    @amplitude_rank_editor.setter
    def amplitude_rank_editor(self, value: int) -> None:
        self.stop_editor.amplitude_rank = value

    #--------------------------------------------------------------------------
    # Attack Time - Harmonic - Rank
    #--------------------------------------------------------------------------
    @property
    def attack_harmonic_rank_editor(self) -> int:
        return self.stop_editor.attack_time_harmonic_rank

    @attack_harmonic_rank_editor.setter
    def attack_harmonic_rank_editor(self, value: int) -> None:
        self.stop_editor.attack_time_harmonic_rank = value

    #--------------------------------------------------------------------------
    # Decay Time - Harmonic - Rank
    #--------------------------------------------------------------------------
    @property
    def decay_harmonic_rank_editor(self) -> int:
        return self.stop_editor.decay_time_harmonic_rank

    @decay_harmonic_rank_editor.setter
    def decay_harmonic_rank_editor(self, value: int) -> None:
        self.stop_editor.decay_time_harmonic_rank = value

    #--------------------------------------------------------------------------
    # Sustain Level - Harmonic - Rank
    #--------------------------------------------------------------------------
    @property
    def sustain_harmonic_rank_editor(self) -> int:
        return self.stop_editor.sustain_level_harmonic_rank

    @sustain_harmonic_rank_editor.setter
    def sustain_harmonic_rank_editor(self, value: int) -> None:
        self.stop_editor.sustain_level_harmonic_rank = value

    #--------------------------------------------------------------------------
    # Release Time - Harmonic - Rank
    #--------------------------------------------------------------------------
    @property
    def release_harmonic_rank_editor(self) -> int:
        return self.stop_editor.release_time_harmonic_rank

    @release_harmonic_rank_editor.setter
    def release_harmonic_rank_editor(self, value: int) -> None:
        self.stop_editor.release_time_harmonic_rank = value

    #--------------------------------------------------------------------------
    # Attack Time - Rank
    #--------------------------------------------------------------------------
    @property
    def attack_rank_editor(self) -> int:
        return self.stop_editor.attack_time_rank

    @attack_rank_editor.setter
    def attack_rank_editor(self, value: int) -> None:
        self.stop_editor.attack_time_rank = value

    #--------------------------------------------------------------------------
    # Decay Time - Rank
    #--------------------------------------------------------------------------
    @property
    def decay_rank_editor(self) -> int:
        return self.stop_editor.decay_time_rank

    @decay_rank_editor.setter
    def decay_rank_editor(self, value: int) -> None:
        self.stop_editor.decay_time_rank = value

    #--------------------------------------------------------------------------
    # Sustain Level - Rank
    #--------------------------------------------------------------------------
    @property
    def sustain_rank_editor(self) -> int:
        return self.stop_editor.sustain_level_rank

    @sustain_rank_editor.setter
    def sustain_rank_editor(self, value: int) -> None:
        self.stop_editor.sustain_level_rank = value

    #--------------------------------------------------------------------------
    # Release Time - Rank
    #--------------------------------------------------------------------------
    @property
    def release_rank_editor(self) -> int:
        return self.stop_editor.release_time_rank

    @release_rank_editor.setter
    def release_rank_editor(self, value: int) -> None:
        self.stop_editor.release_time_rank = value

    #--------------------------------------------------------------------------
    # Rank Number - Pipe
    #--------------------------------------------------------------------------
    @property
    def rank_number_pipe_editor(self) -> int:
        return self.stop_editor.rank_number_pipe

    @rank_number_pipe_editor.setter
    def rank_number_pipe_editor(self, value: int) -> None:
        self.stop_editor.rank_number_pipe = value

    #--------------------------------------------------------------------------
    # Pipe Number
    #--------------------------------------------------------------------------
    @property
    def pipe_number_editor(self) -> int:
        return self.stop_editor.pipe_number

    @pipe_number_editor.setter
    def pipe_number_editor(self, value: int) -> None:
        self.stop_editor.pipe_number = value

    #--------------------------------------------------------------------------
    # Note
    #--------------------------------------------------------------------------
    @property
    def note_editor(self) -> str:
        return self.stop_editor.note

    @note_editor.setter
    def note_editor(self, value: str) -> None:
        self.stop_editor.note = value

    #--------------------------------------------------------------------------
    # Relative Note
    #--------------------------------------------------------------------------
    @property
    def relative_note_editor(self) -> str:
        return self.stop_editor.relative_note

    @relative_note_editor.setter
    def relative_note_editor(self, value: str) -> None:
        self.stop_editor.relative_note = value

    #--------------------------------------------------------------------------
    # Harmonic Number - Pipe
    #--------------------------------------------------------------------------
    @property
    def harmonic_number_pipe_editor(self) -> int:
        return self.stop_editor.harmonic_number_pipe

    @harmonic_number_pipe_editor.setter
    def harmonic_number_pipe_editor(self, value: int) -> None:
        self.stop_editor.harmonic_number_pipe = value

    #--------------------------------------------------------------------------
    # Amplitude - Pipe
    #--------------------------------------------------------------------------
    @property
    def amplitude_pipe_editor(self) -> int:
        return self.stop_editor.amplitude_pipe

    @amplitude_pipe_editor.setter
    def amplitude_pipe_editor(self, value: int) -> None:
        self.stop_editor.amplitude_pipe = value

    #--------------------------------------------------------------------------
    # Attack Time - Harmonic - Pipe
    #--------------------------------------------------------------------------
    @property
    def attack_harmonic_pipe_editor(self) -> int:
        return self.stop_editor.attack_time_harmonic_pipe

    @attack_harmonic_pipe_editor.setter
    def attack_harmonic_pipe_editor(self, value: int) -> None:
        self.stop_editor.attack_time_harmonic_pipe = value

    #--------------------------------------------------------------------------
    # Decay Time - Harmonic - Pipe
    #--------------------------------------------------------------------------
    @property
    def decay_harmonic_pipe_editor(self) -> int:
        return self.stop_editor.decay_time_harmonic_pipe

    @decay_harmonic_pipe_editor.setter
    def decay_harmonic_pipe_editor(self, value: int) -> None:
        self.stop_editor.decay_time_harmonic_pipe = value

    #--------------------------------------------------------------------------
    # Sustain Level - Harmonic - Pipe
    #--------------------------------------------------------------------------
    @property
    def sustain_harmonic_pipe_editor(self) -> int:
        return self.stop_editor.sustain_level_harmonic_pipe

    @sustain_harmonic_pipe_editor.setter
    def sustain_harmonic_pipe_editor(self, value: int) -> None:
        self.stop_editor.sustain_level_harmonic_pipe = value

    #--------------------------------------------------------------------------
    # Release Time - Harmonic - Pipe
    #--------------------------------------------------------------------------
    @property
    def release_harmonic_pipe_editor(self) -> int:
        return self.stop_editor.release_time_harmonic_pipe

    @release_harmonic_pipe_editor.setter
    def release_harmonic_pipe_editor(self, value: int) -> None:
        self.stop_editor.release_time_harmonic_pipe = value

    #--------------------------------------------------------------------------
    # Attack Time - Pipe
    #--------------------------------------------------------------------------
    @property
    def attack_pipe_editor(self) -> int:
        return self.stop_editor.attack_time_pipe

    @attack_pipe_editor.setter
    def attack_pipe_editor(self, value: int) -> None:
        self.stop_editor.attack_time_pipe = value

    #--------------------------------------------------------------------------
    # Decay Time - Pipe
    #--------------------------------------------------------------------------
    @property
    def decay_pipe_editor(self) -> int:
        return self.stop_editor.decay_time_pipe

    @decay_pipe_editor.setter
    def decay_pipe_editor(self, value: int) -> None:
        self.stop_editor.decay_time_pipe = value

    #--------------------------------------------------------------------------
    # Sustain Level - Pipe
    #--------------------------------------------------------------------------
    @property
    def sustain_pipe_editor(self) -> int:
        return self.stop_editor.sustain_level_pipe

    @sustain_pipe_editor.setter
    def sustain_pipe_editor(self, value: int) -> None:
        self.stop_editor.sustain_level_pipe = value

    #--------------------------------------------------------------------------
    # Release Time - Pipe
    #--------------------------------------------------------------------------
    @property
    def release_pipe_editor(self) -> int:
        return self.stop_editor.release_time_pipe

    @release_pipe_editor.setter
    def release_pipe_editor(self, value: int) -> None:
        self.stop_editor.release_time_pipe = value

    #==========================================================================
    # Stop Config
    #==========================================================================
    #--------------------------------------------------------------------------
    # Stop Name
    #--------------------------------------------------------------------------
    @property
    def stop_name_config(self) -> str:
        return self.stop_config.stop_name_get()

    @stop_name_config.setter
    def stop_name_config(self, value: str):
        self.stop_config.stop_name_set(value)

    #--------------------------------------------------------------------------
    # Stop Family
    #--------------------------------------------------------------------------
    @property
    def stop_family_config(self) -> str:
        return self.stop_config.stop_family_get()

    @stop_family_config.setter
    def stop_family_config(self, value: str):
        self.stop_config.stop_family_set(value)

    #--------------------------------------------------------------------------
    # Organ Division
    #--------------------------------------------------------------------------
    @property
    def organ_division_config(self) -> str:
        return self.stop_config.organ_division_get()

    @organ_division_config.setter
    def organ_division_config(self, value: str):
        self.stop_config.organ_division_set(value)

    #--------------------------------------------------------------------------
    # Number of Ranks
    #--------------------------------------------------------------------------
    @property
    def number_ranks_config(self) -> int:
        return self.stop_config.number_ranks_get()

    @number_ranks_config.setter
    def number_ranks_config(self, value: int):
        self.stop_config.number_ranks_set(value)

    #--------------------------------------------------------------------------
    # Rank Series
    #--------------------------------------------------------------------------
    @property
    def rank_series_config(self) -> str:
        return self.stop_config.rank_series_get()

    @rank_series_config.setter
    def rank_series_config(self, value: str):
        self.stop_config.rank_series_set(value)

    #--------------------------------------------------------------------------
    # Rank Size
    #--------------------------------------------------------------------------
    @property
    def rank_size_config(self) -> str:
        return self.stop_config.rank_size_get(
            rank_number=self.rank_number_editor
        )

    @rank_size_config.setter
    def rank_size_config(self, value: str):
        self.stop_config.rank_size_set(
            rank_number=self.rank_number_editor,
            rank_size=value
        )

    #--------------------------------------------------------------------------
    # Number of Pipes
    #--------------------------------------------------------------------------
    @property
    def number_pipes_config(self) -> int:
        return self.stop_config.number_pipes_get(
            rank_number=self.rank_number_editor
        )

    @number_pipes_config.setter
    def number_pipes_config(self, value: int):
        self.stop_config.number_pipes_set(
            rank_number=self.rank_number_editor,
            number_pipes=value
        )

    #--------------------------------------------------------------------------
    # Pipe Type
    #--------------------------------------------------------------------------
    @property
    def pipe_type_config(self) -> str:
        return self.stop_config.pipe_type_get(
            rank_number=self.rank_number_editor,
        )

    @pipe_type_config.setter
    def pipe_type_config(self, value: str):
        self.stop_config.pipe_type_set(
            rank_number=self.rank_number_editor,
            pipe_type=value
        )

    #--------------------------------------------------------------------------
    # Starting Note
    #--------------------------------------------------------------------------
    @property
    def starting_note_config(self) -> str:
        print("method: starting_note_config (getter)")
        return self.stop_config.starting_note_get(
            rank_number=self.rank_number_editor
        )

    @starting_note_config.setter
    def starting_note_config(self, value: str):
        print(f"method: starting_note_config (setter)")
        notes: tuple[str, ...] = organlib.NOTES
        print(notes)
        starting_note_index: int = notes.index(value)
        print(starting_note_index)
        revised_notes: tuple[str, ...] = tuple(
            [note for note in notes[starting_note_index:]]
        )
        self.stop_config.starting_note_set(
            rank_number=self.rank_number_editor,
            starting_note=value,
            notes=revised_notes
        )

    #--------------------------------------------------------------------------
    # Frequency Offset
    #--------------------------------------------------------------------------
    @property
    def frequency_offset_config(self) -> int:
        return self.stop_config.frequency_offset_get(
            rank_number=self.rank_number_editor
        )

    @frequency_offset_config.setter
    def frequency_offset_config(self, value: int):
        self.stop_config.frequency_offset_set(
            rank_number=self.rank_number_editor,
            frequency_offset=value
        )

    #--------------------------------------------------------------------------
    # Number of Harmonics
    #--------------------------------------------------------------------------
    @property
    def number_harmonics_config(self) -> int:
        return self.stop_config.number_harmonics_get(
            rank_number=self.rank_number_editor
        )

    @number_harmonics_config.setter
    def number_harmonics_config(self, value: int):
        self.stop_config.number_harmonics_set(
            rank_number=self.rank_number_editor,
            number_harmonics=value
        )

    #--------------------------------------------------------------------------
    # Amplitude - Rank
    #--------------------------------------------------------------------------
    @property
    def amplitude_rank_config(self) -> int:
        return self.stop_config.rank_harmonic_amplitude_get(
            rank_number=self.rank_number_editor,
            harmonic_number=self.harmonic_number_rank_editor
        )

    @amplitude_rank_config.setter
    def amplitude_rank_config(self, value: int):
        self.stop_config.rank_harmonic_amplitude_set(
            rank_number=self.rank_number_editor,
            harmonic_number=self.harmonic_number_rank_editor,
            amplitude=value
        )

    #--------------------------------------------------------------------------
    # Attack Time - Harmonic - Rank
    #--------------------------------------------------------------------------
    @property
    def attack_harmonic_rank_config(self) -> int:
        return self.stop_config.rank_harmonic_attack_time_get(
            rank_number=self.rank_number_editor,
            harmonic_number=self.harmonic_number_rank_editor
        )

    @attack_harmonic_rank_config.setter
    def attack_harmonic_rank_config(self, value: int):
        self.stop_config.rank_harmonic_attack_time_set(
            rank_number=self.rank_number_editor,
            harmonic_number=self.harmonic_number_rank_editor,
            attack_time=value
        )

    #--------------------------------------------------------------------------
    # Decay Time - Harmonic - Rank
    #--------------------------------------------------------------------------
    @property
    def decay_harmonic_rank_config(self) -> int:
        return self.stop_config.rank_harmonic_decay_time_get(
            rank_number=self.rank_number_editor,
            harmonic_number=self.harmonic_number_rank_editor
        )

    @decay_harmonic_rank_config.setter
    def decay_harmonic_rank_config(self, value: int):
        self.stop_config.rank_harmonic_decay_time_set(
            rank_number=self.rank_number_editor,
            harmonic_number=self.harmonic_number_rank_editor,
            decay_time=value
        )

    #--------------------------------------------------------------------------
    # Sustain Level - Harmonic - Rank
    #--------------------------------------------------------------------------
    @property
    def sustain_harmonic_rank_config(self) -> int:
        return self.stop_config.rank_harmonic_sustain_level_get(
            rank_number=self.rank_number_editor,
            harmonic_number=self.harmonic_number_rank_editor
        )

    @sustain_harmonic_rank_config.setter
    def sustain_harmonic_rank_config(self, value: int):
        self.stop_config.rank_harmonic_sustain_level_set(
            rank_number=self.rank_number_editor,
            harmonic_number=self.harmonic_number_rank_editor,
            sustain_level=value
        )

    #--------------------------------------------------------------------------
    # Release Time - Harmonic - Rank
    #--------------------------------------------------------------------------
    @property
    def release_harmonic_rank_config(self) -> int:
        return self.stop_config.rank_harmonic_release_time_get(
            rank_number=self.rank_number_editor,
            harmonic_number=self.harmonic_number_rank_editor
        )

    @release_harmonic_rank_config.setter
    def release_harmonic_rank_config(self, value: int):
        self.stop_config.rank_harmonic_release_time_set(
            rank_number=self.rank_number_editor,
            harmonic_number=self.harmonic_number_rank_editor,
            release_time=value
        )

    #--------------------------------------------------------------------------
    # Attack Time - Rank
    #--------------------------------------------------------------------------
    @property
    def attack_rank_config(self) -> int:
        return self.stop_config.rank_attack_time_get(
            rank_number=self.rank_number_editor
        )

    @attack_rank_config.setter
    def attack_rank_config(self, value: int):
        self.stop_config.rank_attack_time_set(
            rank_number=self.rank_number_editor,
            attack_time=value
        )

    #--------------------------------------------------------------------------
    # Decay Time - Rank
    #--------------------------------------------------------------------------
    @property
    def decay_rank_config(self) -> int:
        return self.stop_config.rank_decay_time_get(
            rank_number=self.rank_number_editor
        )

    @decay_rank_config.setter
    def decay_rank_config(self, value: int):
        self.stop_config.rank_decay_time_set(
            rank_number=self.rank_number_editor,
            decay_time=value
        )

    #--------------------------------------------------------------------------
    # Sustain Level - Rank
    #--------------------------------------------------------------------------
    @property
    def sustain_rank_config(self) -> int:
        return self.stop_config.rank_sustain_level_get(
            rank_number=self.rank_number_editor
        )

    @sustain_rank_config.setter
    def sustain_rank_config(self, value: int):
        self.stop_config.rank_sustain_level_set(
            rank_number=self.rank_number_editor,
            sustain_level=value
        )

    #--------------------------------------------------------------------------
    # Release Time - Rank
    #--------------------------------------------------------------------------
    @property
    def release_rank_config(self) -> int:
        return self.stop_config.rank_release_time_get(
            rank_number=self.rank_number_editor
        )

    @release_rank_config.setter
    def release_rank_config(self, value: int):
        self.stop_config.rank_release_time_set(
            rank_number=self.rank_number_editor,
            release_time=value
        )

    #--------------------------------------------------------------------------
    # Note
    #--------------------------------------------------------------------------
    @property
    def note_config(self) -> str:
        return self.stop_config.note_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor
        )

    @note_config.setter
    def note_config(self, value: str):
        self.stop_config.note_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            note=value
        )

    #--------------------------------------------------------------------------
    # Relative Note
    #--------------------------------------------------------------------------
    @property
    def relative_note_config(self) -> str:
        return self.stop_config.relative_note_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor
        )

    @relative_note_config.setter
    def relative_note_config(self, value: str):
        self.stop_config.relative_note_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            relative_note=value
        )

    #--------------------------------------------------------------------------
    # Amplitude - Pipe
    #--------------------------------------------------------------------------
    @property
    def amplitude_pipe_config(self) -> int:
        return self.stop_config.pipe_harmonic_amplitude_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            harmonic_number=self.harmonic_number_pipe_editor
        )

    @amplitude_pipe_config.setter
    def amplitude_pipe_config(self, value: int):
        self.stop_config.pipe_harmonic_amplitude_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            harmonic_number=self.harmonic_number_pipe_editor,
            amplitude=value
        )

    #--------------------------------------------------------------------------
    # Attack Time - Harmonic - Pipe
    #--------------------------------------------------------------------------
    @property
    def attack_harmonic_pipe_config(self) -> int:
        return self.stop_config.pipe_harmonic_attack_time_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            harmonic_number=self.harmonic_number_pipe_editor
        )

    @attack_harmonic_pipe_config.setter
    def attack_harmonic_pipe_config(self, value: int):
        self.stop_config.pipe_harmonic_attack_time_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            harmonic_number=self.harmonic_number_pipe_editor,
            attack_time=value
        )

    #--------------------------------------------------------------------------
    # Decay Time - Harmonic - Pipe
    #--------------------------------------------------------------------------
    @property
    def decay_harmonic_pipe_config(self) -> int:
        return self.stop_config.pipe_harmonic_decay_time_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            harmonic_number=self.harmonic_number_pipe_editor
        )

    @decay_harmonic_pipe_config.setter
    def decay_harmonic_pipe_config(self, value: int):
        self.stop_config.pipe_harmonic_decay_time_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            harmonic_number=self.harmonic_number_pipe_editor,
            decay_time=value
        )

    #--------------------------------------------------------------------------
    # Sustain Level - Harmonic - Pipe
    #--------------------------------------------------------------------------
    @property
    def sustain_harmonic_pipe_config(self) -> int:
        return self.stop_config.pipe_harmonic_sustain_level_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            harmonic_number=self.harmonic_number_pipe_editor
        )

    @sustain_harmonic_pipe_config.setter
    def sustain_harmonic_pipe_config(self, value: int):
        self.stop_config.pipe_harmonic_sustain_level_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            harmonic_number=self.harmonic_number_pipe_editor,
            sustain_level=value
        )

    #--------------------------------------------------------------------------
    # Release Time - Harmonic - Pipe
    #--------------------------------------------------------------------------
    @property
    def release_harmonic_pipe_config(self) -> int:
        return self.stop_config.pipe_harmonic_release_time_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            harmonic_number=self.harmonic_number_pipe_editor
        )

    @release_harmonic_pipe_config.setter
    def release_harmonic_pipe_config(self, value: int):
        self.stop_config.pipe_harmonic_release_time_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            harmonic_number=self.harmonic_number_pipe_editor,
            release_time=value
        )

    #--------------------------------------------------------------------------
    # Attack Time - Pipe
    #--------------------------------------------------------------------------
    @property
    def attack_pipe_config(self) -> int:
        return self.stop_config.pipe_attack_time_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor
        )

    @attack_pipe_config.setter
    def attack_pipe_config(self, value: int):
        self.stop_config.pipe_attack_time_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            attack_time=value
        )

    #--------------------------------------------------------------------------
    # Decay Time - Pipe
    #--------------------------------------------------------------------------
    @property
    def decay_pipe_config(self) -> int:
        return self.stop_config.pipe_decay_time_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor
        )

    @decay_pipe_config.setter
    def decay_pipe_config(self, value: int):
        self.stop_config.pipe_decay_time_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            decay_time=value
        )

    #--------------------------------------------------------------------------
    # Sustain Level - Pipe
    #--------------------------------------------------------------------------
    @property
    def sustain_pipe_config(self) -> int:
        return self.stop_config.pipe_sustain_level_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor
        )

    @sustain_pipe_config.setter
    def sustain_pipe_config(self, value: int):
        self.stop_config.pipe_sustain_level_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            sustain_level=value
        )

    #--------------------------------------------------------------------------
    # Release Time - Pipe
    #--------------------------------------------------------------------------
    @property
    def release_pipe_config(self) -> int:
        return self.stop_config.pipe_release_time_get(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor
        )

    @release_pipe_config.setter
    def release_pipe_config(self, value: int):
        self.stop_config.pipe_release_time_set(
            rank_number=self.rank_number_editor,
            pipe_number=self.pipe_number_editor,
            release_time=value
        )


if __name__ == "__main__":
    app = QApplication([])
    stop_editor_ui = StopEditorUI()
    stop_editor_ui.stop_editor.show()
    app.exec()