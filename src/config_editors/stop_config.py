import json


class StopConfig:
    def __init__(self) -> None:
        self.config: dict = {}

    #**************************************************************************
    # File Operations
    #**************************************************************************
    def load_file(
            self,
            file: str
    ) -> None:
        with open(file, "r") as config_file:
            self.config = json.load(config_file)

    def save_file(self, file) -> None:
        with open(file, "w") as config_file:
            json.dump(self.config, config_file, indent=4)

    #**************************************************************************
    # Section Creation
    #**************************************************************************

    #==========================================================================
    # Default Config
    #==========================================================================
    def init_default_config(self) -> None:
        self.init_stop_settings()
        self.init_rank_settings(1)
        self.init_rank_harmonic_settings(1, 1)
        self.init_rank_harmonic_adsr_settings(1, 1)
        self.init_rank_adsr_settings(1)
        for pipe in range(1, self.number_pipes_get(1)):
            self.init_pipe_settings(1, pipe)
            self.init_pipe_harmonic_settings(1, pipe, 1)
            self.init_pipe_harmonic_adsr_settings(1, pipe, 1)
            self.init_pipe_adsr_settings(1, pipe)

    #==========================================================================
    # Stop Settings
    #==========================================================================
    def init_stop_settings(self) -> None: 
        self.config[self.stop_settings] = {
            "Stop Name": "",
            "Stop Family": "",
            "Organ Division": "",
            "Number of Ranks": 1,
            "Rank Series": ""
        }

    #==========================================================================
    # Rank Settings
    #==========================================================================
    def init_rank_settings(self, rank_number: int) -> None:
        self.config[self.rank_settings(rank_number)] = {
            "Rank Size": "",
            "Pipe Type": "",
            "Starting Note": "C2",
            "Frequency Offset": 0,
            "Number of Pipes": 61,
            "Number of Harmonics": 1
        }

    def init_rank_harmonic_settings(
            self, 
            rank_number: int, 
            harmonic_number: int
    ) -> None:
        self.config[
            self.rank_harmonics_settings(
                rank_number = rank_number, 
                harmonic_number = harmonic_number
            )
        ] = {
            "Amplitude": 0
        }

    def init_rank_harmonic_adsr_settings(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> None:
        self.config[
            self.rank_harmonics_adsr_settings(
                rank_number = rank_number,
                harmonic_number = harmonic_number
            )
        ] = {
            "Attack Time": 0,
            "Decay Time": 0,
            "Sustain Level": 0,
            "Release Time": 0
        }

    def init_rank_adsr_settings(self, rank_number: int) -> None:
        self.config[self.rank_adsr_settings(rank_number=rank_number)] = {
            "Attack Time": 0,
            "Decay Time": 0,
            "Sustain Level": 0,
            "Release Time": 0
        }

    #==========================================================================
    # Pipe Settings
    #==========================================================================
    def init_pipe_settings(
            self,
            rank_number: int,
            pipe_number: int
    ) -> None:
        self.config[
            self.pipe_settings(
                rank_number=rank_number,
                pipe_number=pipe_number
            )
        ] = {
            "Note": "",
            "Relative Note": ""
        }

    def init_pipe_harmonic_settings(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> None:
        self.config[
            self.pipe_harmonics_settings(
                rank_number=rank_number,
                pipe_number=pipe_number,
                harmonic_number=harmonic_number
            )
        ] = {
            "Amplitude": 0
        }

    def init_pipe_harmonic_adsr_settings(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> None:
        self.config[
            self.pipe_harmonics_adsr_settings(
                rank_number=rank_number,
                pipe_number=pipe_number,
                harmonic_number=harmonic_number
            )
        ] = {
            "Attack Time": 0,
            "Decay Time": 0,
            "Sustain Level": 0,
            "Release Time": 0
        }

    def init_pipe_adsr_settings(
            self,
            rank_number: int,
            pipe_number: int,
    ) -> None:
        self.config[
            self.pipe_adsr_settings(
                rank_number=rank_number,
                pipe_number=pipe_number
            )
        ] = {
            "Attack Time": 0,
            "Decay Time": 0,
            "Sustain Level": 0,
            "Release Time": 0
        }

    #**************************************************************************
    # Section Deletion
    #**************************************************************************
    def clear_config(self) -> None:
        for key in self.config.keys():
            del self.config[key]

    def del_stop_settings(self) -> None:
        sections: list[str] = [
            self.stop_settings,
        ]
        self.__del_sections(sections)

    def del_rank_settings(
            self,
            rank_number: int
    ) -> None:
        sections: list[str] = [
            self.rank_settings(rank_number=rank_number),
            self.rank_adsr_settings(rank_number=rank_number)
        ]
        for harmonic in range(1, 20):
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
        for pipe in range(1, 61):
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
        self.__del_sections(sections)

    def del_pipe_settings(
            self,
            rank_number: int,
            pipe_number: int
    ) -> None:
        number_harmonics: int = int(
            self.config[self.rank_settings(rank_number)]["number of harmonics"]
        )
        sections: list[str] = [
            self.pipe_settings(rank_number, pipe_number),
            self.pipe_adsr_settings(rank_number, pipe_number)
        ]
        for harmonic in range(1, number_harmonics):
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
        self.__del_sections(sections)

    def del_harmonic_settings(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> None:
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
        self.__del_sections(sections)

    def __del_sections(self, sections: list[str]) -> None:
        for section in sections:
            self.config.pop(section, None)

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
        section: str = self.stop_settings
        field: str = "Stop Name"
        return self.config[section][field]

    def stop_name_set(
            self, 
            stop_name: str
    ) -> None:
        section: str = self.stop_settings
        field: str = "Stop Name"
        self.config[section][field] = stop_name

    #--------------------------------------------------------------------------
    # Stop Family
    #--------------------------------------------------------------------------
    def stop_family_get(self) -> str:
        section: str = self.stop_settings
        field: str = "Stop Family"
        return self.config[section][field]

    def stop_family_set(
            self,
            stop_family: str
    ) -> None:
        section: str = self.stop_settings
        field: str = "Stop Family"
        self.config[section][field] = stop_family

    #--------------------------------------------------------------------------
    # Organ Division
    #--------------------------------------------------------------------------
    def organ_division_get(self) -> str:
        section: str = self.stop_settings
        field: str = "Organ Division"
        return self.config[section][field]

    def organ_division_set(
            self,
            organ_division: str
    ) -> None:
        section: str = self.stop_settings
        field: str = "Organ Division"
        self.config[section][field] = organ_division

    #--------------------------------------------------------------------------
    # Number of Ranks
    #--------------------------------------------------------------------------
    def number_ranks_get(self) -> int:
        section: str = self.stop_settings
        field: str = "Number of Ranks"
        return self.config[section][field]

    def number_ranks_set(
            self,
            number_ranks: int
    ) -> None:
        section: str = self.stop_settings
        field: str = "Number of Ranks"
        self.config[section][field] = number_ranks

    #--------------------------------------------------------------------------
    # Rank Series
    #--------------------------------------------------------------------------
    def rank_series_get(self) -> str:
        section: str = self.stop_settings
        field: str = "Rank Series"
        return self.config[section][field]

    def rank_series_set(
            self,
            rank_series: str
    ) -> None:
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
        section: str = f"Rank {rank_number} Settings"
        field: str = "Rank Size"
        return self.config[section][field]

    def rank_size_set(
            self,
            rank_number: int,
            rank_size: str
    ) -> None:
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
        section: str = self.rank_settings(rank_number)
        field: str = "Number of Pipes"
        return self.config[section][field]

    def number_pipes_set(
            self, 
            rank_number: int, 
            number_pipes: int
    ) -> None:
        section: str = self.rank_settings(rank_number)
        field: str = "Number of Pipes"
        self.config[section][field] = number_pipes

    #--------------------------------------------------------------------------
    # Pipe Type
    #--------------------------------------------------------------------------
    def pipe_type_get(
            self, 
            rank_number: int
    ) -> str:
        section: str = self.rank_settings(rank_number)
        field: str = "Pipe Type"
        return self.config[section][field]

    def pipe_type_set(
            self, 
            rank_number: int, 
            pipe_type: str
    ) -> None:
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
        section: str = self.rank_settings(rank_number)
        field: str = "Starting Note"
        return self.config[section][field]

    def starting_note_set(
            self, 
            rank_number: int, 
            starting_note: str
    ) -> None:
        section: str = self.rank_settings(rank_number)
        field: str = "Starting Note"
        self.config[section][field] = starting_note

    #--------------------------------------------------------------------------
    # Frequency Offset
    #--------------------------------------------------------------------------
    def frequency_offset_get(
            self, 
            rank_number: int
    ) -> int:
        section: str = self.rank_settings(rank_number)
        field: str = "Frequency Offset"
        return self.config[section][field]

    def frequency_offset_set(
            self, 
            rank_number: int, 
            frequency_offset: int
    ) -> None:
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
        section: str = self.rank_settings(rank_number)
        field: str = "Number of Harmonics"
        return self.config[section][field]

    def number_harmonics_set(
            self, 
            rank_number: int, 
            number_harmonics: int
    ) -> None:
        section: str = self.rank_settings(rank_number)
        field: str = "Number of Harmonics"
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
        section: str = self.rank_harmonics_settings(
            rank_number=rank_number,
            harmonic_number=harmonic_number
        )
        field: str = "Amplitude"
        return self.config[section][field]

    def rank_harmonic_amplitude_set(
            self,
            rank_number: int,
            harmonic_number: int,
            amplitude: int
    ) -> None:
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
        section: str = self.rank_harmonics_adsr_settings(
            rank_number=rank_number,
            harmonic_number=harmonic_number
        )
        field: str = "Attack Time"
        return self.config[section][field]

    def rank_harmonic_attack_time_set(
            self,
            rank_number: int,
            harmonic_number: int,
            attack_time: int
    ) -> None:
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
        section: str = self.rank_harmonics_adsr_settings(
            rank_number=rank_number,
            harmonic_number=harmonic_number
        )
        field: str = "Decay Time"
        return self.config[section][field]

    def rank_harmonic_decay_time_set(
            self,
            rank_number: int,
            harmonic_number: int,
            decay_time: int
    ) -> None:
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
        section: str = self.rank_harmonics_adsr_settings(
            rank_number=rank_number,
            harmonic_number=harmonic_number
        )
        field: str = "Sustain Level"
        return self.config[section][field]

    def rank_harmonic_sustain_level_set(
            self,
            rank_number: int,
            harmonic_number: int,
            sustain_level: int
    ) -> None:
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
        section: str = self.rank_harmonics_adsr_settings(
            rank_number=rank_number,
            harmonic_number=harmonic_number
        )
        field: str = "Release Time"
        return self.config[section][field]

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
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Attack Time"
        return self.config[section][field]

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
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Decay Time"
        return self.config[section][field]

    def rank_decay_time_set(
            self,
            rank_number: int,
            decay_time: int
    ) -> None:
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
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Sustain Level"
        return self.config[section][field]

    def rank_sustain_level_set(
            self,
            rank_number: int,
            sustain_level: int
    ) -> None:
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
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Release Time"
        return self.config[section][field]

    def rank_release_time_set(
            self,
            rank_number: int,
            release_time: int
    ) -> None:
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
        section: str = self.pipe_settings(
            rank_number=rank_number,
            pipe_number=pipe_number
            )
        field: str = "Note"
        return self.config[section][field]

    def note_set(
            self,
            rank_number: int,
            pipe_number: int,
            note: str
    ) -> None:
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
        section: str = self.pipe_settings(
            rank_number=rank_number,
            pipe_number=pipe_number
            )
        field: str = "Relative Note"
        return self.config[section][field]

    def relative_note_set(
            self,
            rank_number: int,
            pipe_number: int,
            relative_note: str
    ) -> None:
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
        section: str = self.pipe_harmonics_settings(
            rank_number=rank_number,
            pipe_number=pipe_number,
            harmonic_number=harmonic_number
        )
        field: str = "Amplitude"
        return self.config[section][field]

    def pipe_harmonic_amplitude_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            amplitude: int
    ) -> None:
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
        section: str = self.pipe_harmonics_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number,
            harmonic_number=harmonic_number
        )
        field: str = "Attack Time"
        return self.config[section][field]

    def pipe_harmonic_attack_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            attack_time: int
    ) -> None:
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
        section: str = self.pipe_harmonics_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number,
            harmonic_number=harmonic_number
        )
        field: str = "Decay Time"
        return self.config[section][field]

    def pipe_harmonic_decay_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            decay_time: int
    ) -> None:
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
        section: str = self.pipe_harmonics_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number,
            harmonic_number=harmonic_number
        )
        field: str = "Sustain Level"
        return self.config[section][field]

    def pipe_harmonic_sustain_level_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            sustain_level: int
    ) -> None:
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
        section: str = self.pipe_harmonics_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number,
            harmonic_number=harmonic_number
        )
        field: str = "Release Time"
        return self.config[section][field]

    def pipe_harmonic_release_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            release_time: int
    ) -> None:
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
        section: str = self.pipe_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number
        )
        field: str = "Attack Time"
        return self.config[section][field]

    def pipe_attack_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            attack_time: int
    ) -> None:
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
        section: str = self.pipe_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number
        )
        field: str = "Decay Time"
        return self.config[section][field]

    def pipe_decay_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            decay_time: int
    ) -> None:
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
        section: str = self.pipe_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number
        )
        field: str = "Sustain Level"
        return self.config[section][field]

    def pipe_sustain_level_set(
            self,
            rank_number: int,
            pipe_number: int,
            sustain_level: int
    ) -> None:
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
        section: str = self.pipe_adsr_settings(
            rank_number=rank_number,
            pipe_number=pipe_number
        )
        field: str = "Release Time"
        return self.config[section][field]

    def pipe_release_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            release_time: int
    ) -> None:
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
    def stop_settings(self) -> dict:
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
    print(stop_config.rank_size_get(1))
