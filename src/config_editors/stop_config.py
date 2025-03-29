import json
from icecream import ic # type: ignore
#------------------------------------------------------------------------------


class StopConfig:
    def __init__(self) -> None:
        ic("Initializing StopConfig...")
        ic()
        self.config: dict[str, dict[str, str | int]] = {}
        ic(self.config)
        ic("StopConfig Initialized")

    #**************************************************************************
    # File Operations
    #**************************************************************************
    def load_file(
            self,
            file: str
    ) -> None:
        ic("Loading File...")
        ic()
        ic(file)
        with open(file, "r") as config_file:
            self.config = json.load(config_file)
        ic(self.config)
        ic("File Loaded.")

    def save_file(self, file: str) -> None:
        ic("Saving File...")
        ic()
        ic(file)
        with open(file, "w") as config_file:
            json.dump(self.config, config_file, indent=4)
        ic("File Saved.")

    #**************************************************************************
    # Config Creation
    #**************************************************************************
    #==========================================================================
    # Default Config
    #==========================================================================
    def init_default_config(self) -> None:
        ic("Initializing Default Config...")
        ic()
        self.clear_config()
        self.init_stop_config()
        ic(self.config)
        ic("Default Config Initialized.")

    #==========================================================================
    # Stop Config
    #==========================================================================
    def init_stop_config(self) -> None:
        ic("Initializing Stop Config...")
        ic()
        self.init_stop_settings()
        number_ranks: int = self.number_ranks_get()
        ic(number_ranks)
        for rank in range(1, number_ranks+1):
            self.init_rank_config(rank)
        ic("Stop Config Initialized.")

    #==========================================================================
    # Rank Config
    #==========================================================================
    def init_rank_config(self, rank_number: int) -> None:
        ic("Initializing Rank Config...")
        ic()
        ic(rank_number)
        self.init_rank_settings(rank_number)
        self.init_rank_adsr_settings(rank_number)
        self.init_rank_harmonics_config(rank_number)
        number_pipes: int = self.number_pipes_get(rank_number)
        ic(number_pipes)
        pipes: range = range(1, number_pipes+1)
        ic(pipes)
        for pipe in pipes:
            ic(pipe)
            self.init_pipe_config(rank_number, pipe)
        ic("Rank Config Initialized.")

    def init_rank_harmonics_config(self, rank_number: int) -> None:
        ic("Initializing Rank Harmonics Config...")
        ic()
        ic(rank_number)
        number_harmonics: int = self.number_harmonics_get(rank_number)
        ic(number_harmonics)
        harmonics: range = range(1, number_harmonics+1)
        ic(harmonics)
        for harmonic in harmonics:
            ic(harmonic)
            self.init_rank_harmonic_settings(rank_number, harmonic)
            self.init_rank_harmonic_adsr_settings(rank_number, harmonic)
        ic("Rank Harmonics Config Initialized.")

    #==========================================================================
    # Pipe Config
    #==========================================================================
    def init_pipe_config(
            self,
            rank_number: int,
            pipe_number: int
    ) -> None:
        ic("Initializing Pipe Config...")
        ic()
        ic(rank_number)
        ic(pipe_number)
        self.init_pipe_settings(rank_number, pipe_number)
        self.init_pipe_adsr_settings(rank_number, pipe_number)
        number_harmonics: int = self.number_harmonics_get(rank_number)
        ic(number_harmonics)
        harmonics: range = range(1, number_harmonics+1)
        ic(harmonics)
        for harmonic in harmonics:
            ic(harmonic)
            self.init_pipe_harmonic_settings(
                rank_number, pipe_number, harmonic
            )
            self.init_pipe_harmonic_adsr_settings(
                rank_number, pipe_number, harmonic
            )
        ic("Pipe Config Initialized.")

    #==========================================================================
    # Harmonic Config
    #==========================================================================
    def init_harmonic_config(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> None:
        ic("Initializing Harmonic Config...")
        ic()
        ic(rank_number)
        ic(pipe_number)
        ic(harmonic_number)
        self.init_rank_harmonic_settings(
            rank_number, harmonic_number
        )
        self.init_rank_harmonic_adsr_settings(
            rank_number, harmonic_number
        )
        self.init_pipe_harmonic_settings(
            rank_number, pipe_number, harmonic_number
        )
        self.init_pipe_harmonic_adsr_settings(
            rank_number, pipe_number, harmonic_number
        )
        ic("Harmonic Config Initialized.")

    #**************************************************************************
    # Section Initialization
    #**************************************************************************
    #==========================================================================
    # Stop Settings
    #==========================================================================
    def init_stop_settings(self) -> None:
        ic("Initializing Stop Settings...")
        ic()
        section: str = self.stop_settings
        ic(section)
        self.config[section] = {
            "Stop Name": "",
            "Stop Family": "",
            "Organ Division": "",
            "Number of Ranks": 1,
            "Rank Series": ""
        }
        ic(self.config[section])
        ic("Stop Settings Initialized.")

    #==========================================================================
    # Rank Settings
    #==========================================================================
    def init_rank_settings(self, rank_number: int) -> None:
        ic("Initializing Rank Settings...")
        ic()
        ic(rank_number)
        section: str = self.rank_settings(rank_number)
        ic(section)
        self.config[section] = {
            "Rank Size": "",
            "Pipe Type": "",
            "Starting Note": "C2",
            "Frequency Offset": 0,
            "Number of Pipes": 61,
            "Number of Harmonics": 1
        }
        ic(self.config[section])
        ic("Rank Settings Initialized.")

    def init_rank_harmonic_settings(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> None:
        ic("Initializing Rank Harmonic Settings...")
        ic()
        ic(rank_number)
        ic(harmonic_number)
        section: str = self.rank_harmonics_settings(
            rank_number=rank_number,
            harmonic_number=harmonic_number
        )
        ic(section)
        self.config[section] = {
            "Amplitude": 0
        }
        ic(self.config[section])
        ic("Rank Harmonic Settings Initialized.")

    def init_rank_harmonic_adsr_settings(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> None:
        ic("Initializing Rank Harmonic ADSR Settings...")
        ic()
        ic(rank_number)
        ic(harmonic_number)
        section: str = self.rank_harmonics_adsr_settings(
            rank_number=rank_number,
            harmonic_number=harmonic_number
        )
        ic(section)
        self.config[section] = {
            "Attack Time": 0,
            "Decay Time": 0,
            "Sustain Level": 0,
            "Release Time": 0
        }
        ic(self.config[section])
        ic("Rank Harmonic ADSR Settings Initialized.")

    def init_rank_adsr_settings(self, rank_number: int) -> None:
        ic("Initializing Rank ADSR Settings...")
        ic()
        ic(rank_number)
        section: str = self.rank_adsr_settings(rank_number)
        ic(section)
        self.config[section] = {
            "Attack Time": 0,
            "Decay Time": 0,
            "Sustain Level": 0,
            "Release Time": 0
        }
        ic(self.config[section])
        ic("Rank ADSR Settings Initialized.")

    #==========================================================================
    # Pipe Settings
    #==========================================================================
    def init_pipe_settings(
            self,
            rank_number: int,
            pipe_number: int
    ) -> None:
        ic("Initializing Pipe Settings...")
        ic()
        ic(rank_number)
        ic(pipe_number)
        section: str = self.pipe_settings(
            rank_number=rank_number,
            pipe_number=pipe_number
        )
        ic(section)
        self.config[section] = {
            "Note": "",
            "Relative Note": ""
        }
        ic(self.config[section])
        ic("Pipe Settings Initialized.")

    def init_pipe_harmonic_settings(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> None:
        ic("Initializing Pipe Harmonic Settings...")
        ic()
        ic(rank_number)
        ic(pipe_number)
        ic(harmonic_number)
        section: str = self.pipe_harmonics_settings(
            rank_number=rank_number,
            pipe_number=pipe_number,
            harmonic_number=harmonic_number
        )
        ic(section)
        self.config[section] = {
            "Amplitude": 0
        }
        ic(self.config[section])
        ic("Pipe Harmonic Settings Initialized.")

    def init_pipe_harmonic_adsr_settings(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> None:
        ic("Initializing Pipe Harmonic ADSR Settings...")
        ic()
        ic(rank_number)
        ic(pipe_number)
        ic(harmonic_number)
        section: str = self.pipe_harmonics_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number,
            harmonic_number=harmonic_number
        )
        ic(section)
        self.config[section] = {
            "Attack Time": 0,
            "Decay Time": 0,
            "Sustain Level": 0,
            "Release Time": 0
        }
        ic(self.config[section])
        ic("Pipe Harmonic ADSR Settings Initialized.")

    def init_pipe_adsr_settings(
            self,
            rank_number: int,
            pipe_number: int,
    ) -> None:
        ic("Initializing Pipe ADSR Settings...")
        ic()
        ic(rank_number)
        ic(pipe_number)
        section: str = self.pipe_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number
        )
        ic(section)
        self.config[section] = {
            "Attack Time": 0,
            "Decay Time": 0,
            "Sustain Level": 0,
            "Release Time": 0
        }
        ic(self.config[section])
        ic("Pipe ADSR Settings Initialized.")


    #**************************************************************************
    # Section Deletion
    #**************************************************************************
    def clear_config(self) -> None:
        ic("Clearing Config...")
        ic()
        for key in self.config.keys():
            ic(key)
            del self.config[key]
        ic(self.config)
        ic("Config Cleared.")

    def del_stop_settings(self) -> None:
        ic("Deleting Stop Settings...")
        ic()
        sections: list[str] = [self.stop_settings,]
        ic(sections)
        self.__del_sections(sections)
        ic("Stop Settings Deleted.")

    def del_rank_settings(
            self,
            rank_number: int
    ) -> None:
        ic("Deleting Rank Settings...")
        ic()
        ic(rank_number)
        sections: list[str] = [
            self.rank_settings(rank_number=rank_number),
            self.rank_adsr_settings(rank_number=rank_number)
        ]
        ic(sections)
        for harmonic in range(1, 20):
            ic(harmonic)
            sections.append(
                self.rank_harmonics_settings(
                    rank_number=rank_number,
                    harmonic_number=harmonic)
            )
            sections.append(
                self.rank_harmonics_adsr_settings(
                    rank_number=rank_number,
                    harmonic_number=harmonic)
            )
            ic(sections)
        for pipe in range(1, 61):
            ic(pipe)
            sections.append(
                self.pipe_settings(
                    rank_number=rank_number,
                    pipe_number=pipe)
            )
            sections.append(
                self.pipe_adsr_settings(
                    rank_number=rank_number,
                    pipe_number=pipe)
            )
            for harmonic in range(1, 20):
                sections.append(
                    self.pipe_harmonics_settings(
                        rank_number=rank_number,
                        pipe_number=pipe,
                        harmonic_number=harmonic
                    )
                )
                sections.append(
                    self.pipe_harmonics_adsr_settings(
                        rank_number=rank_number,
                        pipe_number=pipe,
                        harmonic_number=harmonic
                    )
                )
        ic(sections)
        self.__del_sections(sections)
        ic("Rank Settings Deleted.")

    def del_pipe_settings(
            self,
            rank_number: int,
            pipe_number: int
    ) -> None:
        ic("Deleting Pipe Settings...")
        ic()
        ic(rank_number)
        ic(pipe_number)
        number_harmonics: int = int(
            self.config[self.rank_settings(rank_number)]["number of harmonics"]
        )
        ic(number_harmonics)
        sections: list[str] = [
            self.pipe_settings(rank_number, pipe_number),
            self.pipe_adsr_settings(rank_number, pipe_number)
        ]
        ic(sections)
        for harmonic in range(1, number_harmonics+1):
            ic(harmonic)
            sections.append(
                self.pipe_harmonics_settings(
                    rank_number=rank_number,
                    pipe_number=pipe_number,
                    harmonic_number=harmonic)
            )
            sections.append(
                self.pipe_harmonics_adsr_settings(
                    rank_number=rank_number,
                    pipe_number=pipe_number,
                    harmonic_number=harmonic)
            )
        ic(sections)
        self.__del_sections(sections)
        ic("Pipe Settings Deleted.")

    def del_harmonic_settings(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> None:
        ic("Deleting Harmonic Settings...")
        ic()
        ic(rank_number)
        ic(harmonic_number)
        sections: list[str] = [
            self.rank_harmonics_settings(
                rank_number=rank_number,
                harmonic_number=harmonic_number
            ),
            self.rank_harmonics_adsr_settings(
                rank_number=rank_number,
                harmonic_number=harmonic_number
            )
        ]
        for pipe in range(1, 61):
            sections.append(
                self.pipe_harmonics_settings(
                    rank_number=rank_number,
                    pipe_number=pipe,
                    harmonic_number=harmonic_number
                )
            )
            sections.append(
                self.pipe_harmonics_adsr_settings(
                    rank_number=rank_number,
                    pipe_number=pipe,
                    harmonic_number=harmonic_number
                )
            )
        ic(sections)
        self.__del_sections(sections)
        ic("Harmonic Settings Deleted.")

    def __del_sections(self, sections: list[str]) -> None:
        ic("Deleting Sections...")
        ic(sections)
        for section in sections:
            ic(section)
            self.config.pop(section, None)
        ic(self.config)
        ic("Sections Deleted.")

    #**************************************************************************
    # Field Updating
    #**************************************************************************
    def update_note(
            self,
            rank_number: int,
            pipe_number: int,
            note: str
    ) -> None:
        ic("Updating Note...")
        ic()
        ic(rank_number)
        ic(pipe_number)
        ic(note)
        self.note_set(rank_number, pipe_number, note)
        ic("Note Updated.")

    def update_relative_notes(
            self,
            rank_number: int,
            pipe_number: int,
            notes: tuple[str, ...]
    ) -> None:
        ic("Updating Relative Notes...")
        ic()
        ic(rank_number)
        ic(pipe_number)
        ic(notes)
        number_pipes: int = len(
            range(pipe_number, self.number_pipes_get(rank_number)+1)
        )
        ic(number_pipes)
        number_notes: int = len(notes)
        ic(number_notes)
        if number_notes < number_pipes:
            number_pipes = number_notes
        ic(number_pipes)
        for i in range(number_pipes):
            ic(i)
            pipe = pipe_number + i
            ic(pipe)
            note = notes[i]
            ic(note)
            self.relative_note_set(rank_number, pipe, note)
        ic("Relative Notes Updated.")

    #**************************************************************************
    # Getter and Setter Methods
    #**************************************************************************
    #==========================================================================
    # Stop Settings
    #==========================================================================
    #--------------------------------------------------------------------------
    # Stop Name
    #--------------------------------------------------------------------------
    def stop_name_get(self) -> str:
        ic("Getting Stop Name...")
        ic()
        section: str = self.stop_settings
        ic(section)
        field: str = "Stop Name"
        ic(field)
        stop_name: str = str(self.config[section][field])
        ic(stop_name)
        ic("Stop Name Retrieved.")
        return stop_name

    def stop_name_set(self, value: str) -> None:
        ic("Setting Stop Name...")
        ic()
        ic(value)
        section: str = self.stop_settings
        ic(section)
        field: str = "Stop Name"
        ic(field)
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Stop Name Set.")

    #--------------------------------------------------------------------------
    # Stop Family
    #--------------------------------------------------------------------------
    def stop_family_get(self) -> str:
        ic("Getting Stop Family...")
        ic()
        section: str = self.stop_settings
        ic(section)
        field: str = "Stop Family"
        ic(field)
        stop_family: str = str(self.config[section][field])
        ic(stop_family)
        ic("Stop Family Retrieved.")
        return stop_family

    def stop_family_set(
            self,
            value: str
    ) -> None:
        ic("Setting Stop Family...")
        ic()
        ic(value)
        section: str = self.stop_settings
        ic(section)
        field: str = "Stop Family"
        ic(field)
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Stop Family Set.")

    #--------------------------------------------------------------------------
    # Organ Division
    #--------------------------------------------------------------------------
    def organ_division_get(self) -> str:
        ic("Getting Organ Division...")
        ic()
        section: str = self.stop_settings
        ic(section)
        field: str = "Organ Division"
        ic(field)
        organ_division: str = str(self.config[section][field])
        ic(organ_division)
        ic("Organ Division Retrieved.")
        return organ_division

    def organ_division_set(
            self,
            organ_division: str
    ) -> None:
        ic()
        section: str = self.stop_settings
        field: str = "Organ Division"
        self.config[section][field] = organ_division

    #--------------------------------------------------------------------------
    # Number of Ranks
    #--------------------------------------------------------------------------
    def number_ranks_get(self) -> int:
        ic("Getting Number of Ranks...")
        ic()
        section: str = self.stop_settings
        ic(section)
        field: str = "Number of Ranks"
        ic(field)
        number_ranks: int = int(self.config[section][field])
        ic(number_ranks)
        ic("Number of Ranks Retrieved.")
        return number_ranks

    def number_ranks_set(
            self,
            number_ranks: int
    ) -> None:
        ic()
        section: str = self.stop_settings
        field: str = "Number of Ranks"
        number_rank_sections: int = self.number_ranks_get()
        if number_ranks > number_rank_sections:
            for rank in range(number_rank_sections, number_ranks+1):
                self.init_rank_settings(rank)
        elif number_ranks < number_rank_sections:
            for rank in range(number_ranks, number_rank_sections+1):
                self.del_rank_settings(rank)
        self.config[section][field] = number_ranks

    #--------------------------------------------------------------------------
    # Rank Series
    #--------------------------------------------------------------------------
    def rank_series_get(self) -> str:
        ic()
        section: str = self.stop_settings
        field: str = "Rank Series"
        return str(self.config[section][field])

    def rank_series_set(
            self,
            rank_series: str
    ) -> None:
        ic()
        section: str = self.stop_settings
        field: str = "Rank Series"
        self.config[section][field] = rank_series

    #==========================================================================
    # Rank Settings
    #==========================================================================
    #--------------------------------------------------------------------------
    # Rank Size
    #--------------------------------------------------------------------------
    def rank_size_get(
            self,
            rank_number: int
    ) -> str:
        ic()
        section: str = f"Rank {rank_number} Settings"
        field: str = "Rank Size"
        return str(self.config[section][field])

    def rank_size_set(
            self,
            rank_number: int,
            rank_size: str
    ) -> None:
        ic()
        section: str = f"Rank {rank_number} Settings"
        field: str = "Rank Size"
        self.config[section][field] = rank_size

    #--------------------------------------------------------------------------
    # Number of Pipes
    #--------------------------------------------------------------------------
    def number_pipes_get(
            self,
            rank_number: int
    ) -> int:
        ic()
        section: str = self.rank_settings(rank_number)
        field: str = "Number of Pipes"
        return int(self.config[section][field])

    def number_pipes_set(
            self,
            rank_number: int,
            number_pipes: int
    ) -> None:
        ic()
        section: str = self.rank_settings(rank_number)
        field: str = "Number of Pipes"
        number_pipe_sections: int = self.number_pipes_get(rank_number)
        if number_pipes > number_pipe_sections:
            for pipe in range(number_pipe_sections, number_pipes):
                self.init_pipe_settings(rank_number, pipe)
        elif number_pipes < number_pipe_sections:
            for pipe in range(number_pipes, number_pipe_sections):
                self.del_pipe_settings(rank_number, pipe)
        self.config[section][field] = number_pipes

    #--------------------------------------------------------------------------
    # Pipe Type
    #--------------------------------------------------------------------------
    def pipe_type_get(
            self,
            rank_number: int
    ) -> str:
        ic()
        section: str = self.rank_settings(rank_number)
        field: str = "Pipe Type"
        return str(self.config[section][field])

    def pipe_type_set(
            self,
            rank_number: int,
            pipe_type: str
    ) -> None:
        ic()
        section: str = self.rank_settings(rank_number)
        field: str = "Pipe Type"
        self.config[section][field] = pipe_type

    #--------------------------------------------------------------------------
    # Starting Note
    #--------------------------------------------------------------------------
    def starting_note_get(
            self,
            rank_number: int
    ) -> str:
        ic()
        section: str = self.rank_settings(rank_number)
        field: str = "Starting Note"
        return str(self.config[section][field])

    def starting_note_set(
            self,
            rank_number: int,
            starting_note: str,
            notes: tuple[str, ...]
    ) -> None:
        ic()
        section: str = self.rank_settings(rank_number)
        field: str = "Starting Note"
        self.config[section][field] = starting_note
        number_pipes: int = len(notes)
        for pipe in range(1, number_pipes+1):
            self.note_set(rank_number, pipe, notes[pipe-1])
            self.relative_note_set(rank_number, pipe, notes[pipe-1])

    #--------------------------------------------------------------------------
    # Frequency Offset
    #--------------------------------------------------------------------------
    def frequency_offset_get(
            self,
            rank_number: int
    ) -> int:
        ic()
        section: str = self.rank_settings(rank_number)
        field: str = "Frequency Offset"
        return int(self.config[section][field])

    def frequency_offset_set(
            self,
            rank_number: int,
            frequency_offset: int
    ) -> None:
        ic()
        section: str = self.rank_settings(rank_number)
        field: str = "Frequency Offset"
        self.config[section][field] = frequency_offset

    #--------------------------------------------------------------------------
    # Number of Harmonics
    #--------------------------------------------------------------------------
    def number_harmonics_get(
            self,
            rank_number: int
    ) -> int:
        ic()
        section: str = self.rank_settings(rank_number)
        field: str = "Number of Harmonics"
        return int(self.config[section][field])

    def number_harmonics_set(
            self,
            rank_number: int,
            number_harmonics: int
    ) -> None:
        ic()
        section: str = self.rank_settings(rank_number)
        field: str = "Number of Harmonics"
        number_harmonic_sections: int = self.number_harmonics_get(rank_number)
        number_pipes: int = self.number_pipes_get(rank_number)
        if number_harmonics > number_harmonic_sections:
            for harmonic in range(
                number_harmonic_sections, number_harmonics+1
            ):
                self.init_rank_harmonic_settings(rank_number, harmonic)
                for pipe in range(1, number_pipes):
                    self.init_pipe_harmonic_settings(
                        rank_number, pipe, harmonic
                    )
        elif number_harmonics < number_harmonic_sections:
            for harmonic in range(
                number_harmonics, number_harmonic_sections+1
            ):
                self.del_harmonic_settings(rank_number, harmonic)
        self.config[section][field] = number_harmonics

    #==========================================================================
    # Rank Harmonic Settings
    #==========================================================================
    #--------------------------------------------------------------------------
    # Amplitude
    #--------------------------------------------------------------------------
    def rank_harmonic_amplitude_get(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> int:
        ic()
        section: str = self.rank_harmonics_settings(
            rank_number=rank_number,
            harmonic_number=harmonic_number
        )
        field: str = "Amplitude"
        return int(self.config[section][field])

    def rank_harmonic_amplitude_set(
            self,
            rank_number: int,
            harmonic_number: int,
            amplitude: int
    ) -> None:
        ic()
        section: str = self.rank_harmonics_settings(
            rank_number=rank_number,
            harmonic_number=harmonic_number
        )
        field: str = "Amplitude"
        self.config[section][field] = amplitude

    #--------------------------------------------------------------------------
    # ADSR Settings
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    # Attack Time
    #--------------------------------------------------------------------------
    def rank_harmonic_attack_time_get(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> int:
        ic()
        section: str = self.rank_harmonics_adsr_settings(
            rank_number=rank_number,
            harmonic_number=harmonic_number
        )
        field: str = "Attack Time"
        return int(self.config[section][field])

    def rank_harmonic_attack_time_set(
            self,
            rank_number: int,
            harmonic_number: int,
            attack_time: int
    ) -> None:
        ic()
        section: str = self.rank_harmonics_adsr_settings(
            rank_number=rank_number,
            harmonic_number=harmonic_number
        )
        field: str = "Attack Time"
        self.config[section][field] = attack_time

    #--------------------------------------------------------------------------
    # Decay Time
    #--------------------------------------------------------------------------
    def rank_harmonic_decay_time_get(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> int:
        ic()
        section: str = self.rank_harmonics_adsr_settings(
            rank_number=rank_number,
            harmonic_number=harmonic_number
        )
        field: str = "Decay Time"
        return int(self.config[section][field])

    def rank_harmonic_decay_time_set(
            self,
            rank_number: int,
            harmonic_number: int,
            decay_time: int
    ) -> None:
        ic()
        section: str = self.rank_harmonics_adsr_settings(
            rank_number=rank_number,
            harmonic_number=harmonic_number
        )
        field: str = "Decay Time"
        self.config[section][field] = decay_time

    #--------------------------------------------------------------------------
    # Sustain Level
    #--------------------------------------------------------------------------
    def rank_harmonic_sustain_level_get(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> int:
        ic()
        section: str = self.rank_harmonics_adsr_settings(
            rank_number=rank_number,
            harmonic_number=harmonic_number
        )
        field: str = "Sustain Level"
        return int(self.config[section][field])

    def rank_harmonic_sustain_level_set(
            self,
            rank_number: int,
            harmonic_number: int,
            sustain_level: int
    ) -> None:
        ic()
        section: str = self.rank_harmonics_adsr_settings(
            rank_number=rank_number,
            harmonic_number=harmonic_number
        )
        field: str = "Sustain Level"
        self.config[section][field] = sustain_level

    #--------------------------------------------------------------------------
    # Release Time
    #--------------------------------------------------------------------------
    def rank_harmonic_release_time_get(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> int:
        ic()
        section: str = self.rank_harmonics_adsr_settings(
            rank_number=rank_number,
            harmonic_number=harmonic_number
        )
        field: str = "Release Time"
        return int(self.config[section][field])

    def rank_harmonic_release_time_set(
            self,
            rank_number: int,
            harmonic_number: int,
            release_time: int
    ) -> None:
        section: str = self.rank_harmonics_adsr_settings(
            rank_number=rank_number,
            harmonic_number=harmonic_number
        )
        field: str = "Release Time"
        self.config[section][field] = release_time

    #==========================================================================
    # Rank ADSR Settings
    #==========================================================================
    #--------------------------------------------------------------------------
    # Attack Time
    #--------------------------------------------------------------------------
    def rank_attack_time_get(
            self,
            rank_number: int
    ) -> int:
        ic()
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Attack Time"
        return int(self.config[section][field])

    def rank_attack_time_set(
            self,
            rank_number: int,
            attack_time: int
    ) -> None:
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Attack Time"
        self.config[section][field] = attack_time

    #--------------------------------------------------------------------------
    # Decay Time
    #--------------------------------------------------------------------------
    def rank_decay_time_get(
            self,
            rank_number: int
    ) -> int:
        ic()
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Decay Time"
        return int(self.config[section][field])

    def rank_decay_time_set(
            self,
            rank_number: int,
            decay_time: int
    ) -> None:
        ic()
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Decay Time"
        self.config[section][field] = decay_time

    #--------------------------------------------------------------------------
    # Sustain Level
    #--------------------------------------------------------------------------
    def rank_sustain_level_get(
            self,
            rank_number: int
    ) -> int:
        ic()
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Sustain Level"
        return int(self.config[section][field])

    def rank_sustain_level_set(
            self,
            rank_number: int,
            sustain_level: int
    ) -> None:
        ic()
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Sustain Level"
        self.config[section][field] = sustain_level

    #--------------------------------------------------------------------------
    # Release Time
    #--------------------------------------------------------------------------
    def rank_release_time_get(
            self,
            rank_number: int
    ) -> int:
        ic()
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Release Time"
        return int(self.config[section][field])

    def rank_release_time_set(
            self,
            rank_number: int,
            release_time: int
    ) -> None:
        ic()
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Release Time"
        self.config[section][field] = release_time

    #==========================================================================
    # Pipe Settings
    #==========================================================================
    #--------------------------------------------------------------------------
    # Note
    #--------------------------------------------------------------------------
    def note_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> str:
        ic()
        section: str = self.pipe_settings(
            rank_number=rank_number,
            pipe_number=pipe_number
            )
        field: str = "Note"
        return str(self.config[section][field])

    def note_set(
            self,
            rank_number: int,
            pipe_number: int,
            note: str
    ) -> None:
        ic()
        section: str = self.pipe_settings(
            rank_number=rank_number,
            pipe_number=pipe_number
            )
        field: str = "Note"
        self.config[section][field] = note

    #--------------------------------------------------------------------------
    # Relative Note
    #--------------------------------------------------------------------------
    def relative_note_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> str:
        ic()
        section: str = self.pipe_settings(
            rank_number=rank_number,
            pipe_number=pipe_number
            )
        field: str = "Relative Note"
        return str(self.config[section][field])

    def relative_note_set(
            self,
            rank_number: int,
            pipe_number: int,
            relative_note: str,
    ) -> None:
        ic()
        section: str = self.pipe_settings(
            rank_number=rank_number,
            pipe_number=pipe_number
            )
        field: str = "Relative Note"
        self.config[section][field] = relative_note

    #==========================================================================
    # Pipe Harmonic Settings
    #==========================================================================
    #--------------------------------------------------------------------------
    # Amplitude
    #--------------------------------------------------------------------------
    def pipe_harmonic_amplitude_get(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> int:
        ic()
        section: str = self.pipe_harmonics_settings(
            rank_number=rank_number,
            pipe_number=pipe_number,
            harmonic_number=harmonic_number
        )
        field: str = "Amplitude"
        return int(self.config[section][field])

    def pipe_harmonic_amplitude_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            amplitude: int
    ) -> None:
        ic()
        section: str = self.pipe_harmonics_settings(
            rank_number=rank_number,
            pipe_number=pipe_number,
            harmonic_number=harmonic_number
        )
        field: str = "Amplitude"
        self.config[section][field] = amplitude

    #--------------------------------------------------------------------------
    # ADSR Settings
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    # Attack Time
    #--------------------------------------------------------------------------
    def pipe_harmonic_attack_time_get(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> int:
        ic()
        section: str = self.pipe_harmonics_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number,
            harmonic_number=harmonic_number
        )
        field: str = "Attack Time"
        return int(self.config[section][field])

    def pipe_harmonic_attack_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            attack_time: int
    ) -> None:
        ic()
        section: str = self.pipe_harmonics_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number,
            harmonic_number=harmonic_number
        )
        field: str = "Attack Time"
        self.config[section][field] = attack_time

    #--------------------------------------------------------------------------
    # Decay Time
    #--------------------------------------------------------------------------
    def pipe_harmonic_decay_time_get(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> int:
        ic()
        section: str = self.pipe_harmonics_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number,
            harmonic_number=harmonic_number
        )
        field: str = "Decay Time"
        return int(self.config[section][field])

    def pipe_harmonic_decay_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            decay_time: int
    ) -> None:
        ic()
        section: str = self.pipe_harmonics_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number,
            harmonic_number=harmonic_number
        )
        field: str = "Decay Time"
        self.config[section][field] = decay_time

    #--------------------------------------------------------------------------
    # Sustain Level
    #--------------------------------------------------------------------------
    def pipe_harmonic_sustain_level_get(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> int:
        ic()
        section: str = self.pipe_harmonics_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number,
            harmonic_number=harmonic_number
        )
        field: str = "Sustain Level"
        return int(self.config[section][field])

    def pipe_harmonic_sustain_level_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            sustain_level: int
    ) -> None:
        ic()
        section: str = self.pipe_harmonics_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number,
            harmonic_number=harmonic_number
        )
        field: str = "Sustain Level"
        self.config[section][field] = sustain_level

    #--------------------------------------------------------------------------
    # Release Time
    #--------------------------------------------------------------------------
    def pipe_harmonic_release_time_get(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> int:
        ic()
        section: str = self.pipe_harmonics_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number,
            harmonic_number=harmonic_number
        )
        field: str = "Release Time"
        return int(self.config[section][field])

    def pipe_harmonic_release_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            release_time: int
    ) -> None:
        ic()
        section: str = self.pipe_harmonics_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number,
            harmonic_number=harmonic_number
        )
        field: str = "Release Time"
        self.config[section][field] = release_time

    #==========================================================================
    # Pipe ADSR Settings
    #==========================================================================
    #--------------------------------------------------------------------------
    # Attack Time
    #--------------------------------------------------------------------------
    def pipe_attack_time_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> int:
        ic()
        section: str = self.pipe_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number
        )
        field: str = "Attack Time"
        return int(self.config[section][field])

    def pipe_attack_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            attack_time: int
    ) -> None:
        ic()
        section: str = self.pipe_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number
        )
        field: str = "Attack Time"
        self.config[section][field] = attack_time

    #--------------------------------------------------------------------------
    # Decay Time
    #--------------------------------------------------------------------------
    def pipe_decay_time_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> int:
        ic()
        section: str = self.pipe_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number
        )
        field: str = "Decay Time"
        return int(self.config[section][field])

    def pipe_decay_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            decay_time: int
    ) -> None:
        ic()
        section: str = self.pipe_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number
        )
        field: str = "Decay Time"
        self.config[section][field] = decay_time

    #--------------------------------------------------------------------------
    # Sustain Level
    #--------------------------------------------------------------------------
    def pipe_sustain_level_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> int:
        ic()
        section: str = self.pipe_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number
        )
        field: str = "Sustain Level"
        return int(self.config[section][field])

    def pipe_sustain_level_set(
            self,
            rank_number: int,
            pipe_number: int,
            sustain_level: int
    ) -> None:
        ic()
        section: str = self.pipe_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number
        )
        field: str = "Sustain Level"
        self.config[section][field] = sustain_level

    #--------------------------------------------------------------------------
    # Release Time
    #--------------------------------------------------------------------------
    def pipe_release_time_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> int:
        ic()
        section: str = self.pipe_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number
        )
        field: str = "Release Time"
        return int(self.config[section][field])

    def pipe_release_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            release_time: int
    ) -> None:
        ic()
        section: str = self.pipe_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number
        )
        field: str = "Release Time"
        self.config[section][field] = release_time

    #**************************************************************************
    # Sections
    #**************************************************************************
    @property
    def stop_settings(self) -> str:
        return "Stop Settings"

    def rank_settings(self, rank_number: int) -> str:
        return f"Rank {rank_number} Settings"

    def rank_harmonics_settings(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> str:
        return f"Rank {rank_number} - Harmonic {harmonic_number} Settings"

    def rank_harmonics_adsr_settings(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> str:
        rank: str = f"Rank {rank_number}"
        harmonics: str = f"Harmonic {harmonic_number}"
        return f"{rank} - {harmonics} - ADSR Settings"

    def rank_adsr_settings(self, rank_number: int) -> str:
        return f"Rank {rank_number} - ADSR Settings"

    def pipe_settings(self, rank_number: int, pipe_number: int) -> str:
        return f"Rank {rank_number} - Pipe {pipe_number} Settings"

    def pipe_harmonics_settings(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> str:
        rank: str = f"Rank {rank_number}"
        pipe: str = f"Pipe {pipe_number}"
        harmonics: str = f"Harmonic {harmonic_number}"
        return f"{rank} - {pipe} - {harmonics} - Settings"

    def pipe_harmonics_adsr_settings(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> str:
        rank: str = f"Rank {rank_number}"
        pipe: str = f"Pipe {pipe_number}"
        harmonics: str = f"Harmonic {harmonic_number}"
        return f"{rank} - {pipe} - {harmonics} - ADSR Settings"

    def pipe_adsr_settings(
            self,
            rank_number: int,
            pipe_number: int
    ) -> str:
        rank: str = f"Rank {rank_number}"
        pipe: str = f"Pipe {pipe_number}"
        return f"{rank} - {pipe} - ADSR Settings"


if __name__ == "__main__":
    stop_config: StopConfig = StopConfig()
    stop_config.load_file("src/config/stops/AEOLINE 8'.json")
    ic(stop_config.rank_size_get(1))
