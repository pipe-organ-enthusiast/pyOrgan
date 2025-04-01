import json
from icecream import ic # type: ignore
#------------------------------------------------------------------------------


class StopConfig:
    def __init__(self) -> None:
        ic("Initializing StopConfig...")
        self.config: dict[str, dict[str, str | int]] = {}
        ic(self.config)
        ic("StopConfig Initialized")

    #===============================================================================================
    # File Operations
    #===============================================================================================
    def load_file(
            self,
            file: str
    ) -> None:
        ic("Loading File...")
        ic(file)
        with open(file, "r") as config_file:
            self.config = json.load(config_file)
        ic(self.config)
        ic("File Loaded.")

    #-----------------------------------------------------------------------------------------------
    def save_file(
            self,
            file: str
    ) -> None:
        ic("Saving File...")
        ic(file)
        with open(file, "w") as config_file:
            json.dump(self.config, config_file, indent=4)
            ic(f"{self.config} saved to {file}")
        ic("File Saved.")

    #===============================================================================================
    # Config Creation
    #===============================================================================================
    def init_default_config(self) -> None:
        ic("Initializing Default Config...")
        self.clear_config()
        self.init_stop_config()
        ic(self.config)
        ic("Default Config Initialized.")

    #-----------------------------------------------------------------------------------------------
    def init_stop_config(self) -> None:
        ic("Initializing Stop Config...")
        self.init_stop_settings()
        number_ranks: int = self.number_ranks_get()
        ic(number_ranks)
        for rank in range(1, number_ranks+1):
            ic(rank)
            self.init_rank_config(rank)
        ic("Stop Config Initialized.")

    #-----------------------------------------------------------------------------------------------
    def init_rank_config(
            self,
            rank_number: int
    ) -> None:
        ic("Initializing Rank Config...")
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

    #-----------------------------------------------------------------------------------------------
    def init_rank_harmonics_config(
            self,
            rank_number: int
    ) -> None:
        ic("Initializing Rank Harmonics Config...")
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

    #-----------------------------------------------------------------------------------------------
    def init_pipe_config(
            self,
            rank_number: int,
            pipe_number: int
    ) -> None:
        ic("Initializing Pipe Config...")
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
            self.init_pipe_harmonic_settings(rank_number, pipe_number, harmonic)
            self.init_pipe_harmonic_adsr_settings(rank_number, pipe_number, harmonic)
        ic("Pipe Config Initialized.")

    #-----------------------------------------------------------------------------------------------
    def init_harmonic_config(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> None:
        ic("Initializing Harmonic Config...")
        ic(rank_number)
        ic(pipe_number)
        ic(harmonic_number)
        self.init_rank_harmonic_settings(rank_number, harmonic_number)
        self.init_rank_harmonic_adsr_settings(rank_number, harmonic_number)
        self.init_pipe_harmonic_settings(rank_number, pipe_number, harmonic_number)
        self.init_pipe_harmonic_adsr_settings(rank_number, pipe_number, harmonic_number)
        ic("Harmonic Config Initialized.")

    #===============================================================================================
    # Section Initialization
    #===============================================================================================
    def init_stop_settings(self) -> None:
        ic("Initializing Stop Settings...")
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

    #-----------------------------------------------------------------------------------------------
    def init_rank_settings(
            self,
            rank_number: int
    ) -> None:
        ic("Initializing Rank Settings...")
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

    #-----------------------------------------------------------------------------------------------
    def init_rank_harmonic_settings(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> None:
        ic("Initializing Rank Harmonic Settings...")
        ic(rank_number)
        ic(harmonic_number)
        section: str = self.rank_harmonics_settings(rank_number, harmonic_number)
        ic(section)
        self.config[section] = {"Amplitude": 0}
        ic(self.config[section])
        ic("Rank Harmonic Settings Initialized.")

    #-----------------------------------------------------------------------------------------------
    def init_rank_harmonic_adsr_settings(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> None:
        ic("Initializing Rank Harmonic ADSR Settings...")
        ic(rank_number)
        ic(harmonic_number)
        section: str = self.rank_harmonics_adsr_settings(rank_number, harmonic_number)
        ic(section)
        self.config[section] = {
            "Attack Time": 0,
            "Decay Time": 0,
            "Sustain Level": 0,
            "Release Time": 0
        }
        ic(self.config[section])
        ic("Rank Harmonic ADSR Settings Initialized.")

    #-----------------------------------------------------------------------------------------------
    def init_rank_adsr_settings(
            self,
            rank_number: int
    ) -> None:
        ic("Initializing Rank ADSR Settings...")
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

    #-----------------------------------------------------------------------------------------------
    def init_pipe_settings(
            self,
            rank_number: int,
            pipe_number: int
    ) -> None:
        ic("Initializing Pipe Settings...")
        ic(rank_number)
        ic(pipe_number)
        section: str = self.pipe_settings(rank_number, pipe_number)
        ic(section)
        self.config[section] = {
            "Note": "",
            "Relative Note": ""
        }
        ic(self.config[section])
        ic("Pipe Settings Initialized.")

    #-----------------------------------------------------------------------------------------------
    def init_pipe_harmonic_settings(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> None:
        ic("Initializing Pipe Harmonic Settings...")
        ic(rank_number)
        ic(pipe_number)
        ic(harmonic_number)
        section: str = self.pipe_harmonics_settings(rank_number, pipe_number, harmonic_number)
        ic(section)
        self.config[section] = {"Amplitude": 0}
        ic(self.config[section])
        ic("Pipe Harmonic Settings Initialized.")

    #-----------------------------------------------------------------------------------------------
    def init_pipe_harmonic_adsr_settings(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> None:
        ic("Initializing Pipe Harmonic ADSR Settings...")
        ic(rank_number)
        ic(pipe_number)
        ic(harmonic_number)
        section: str = self.pipe_harmonics_adsr_settings(rank_number, pipe_number, harmonic_number)
        ic(section)
        self.config[section] = {
            "Attack Time": 0,
            "Decay Time": 0,
            "Sustain Level": 0,
            "Release Time": 0
        }
        ic(self.config[section])
        ic("Pipe Harmonic ADSR Settings Initialized.")

    #-----------------------------------------------------------------------------------------------
    def init_pipe_adsr_settings(
            self,
            rank_number: int,
            pipe_number: int,
    ) -> None:
        ic("Initializing Pipe ADSR Settings...")
        ic(rank_number)
        ic(pipe_number)
        section: str = self.pipe_adsr_settings(rank_number, pipe_number)
        ic(section)
        self.config[section] = {
            "Attack Time": 0,
            "Decay Time": 0,
            "Sustain Level": 0,
            "Release Time": 0
        }
        ic(self.config[section])
        ic("Pipe ADSR Settings Initialized.")

    #===============================================================================================
    # Section Deletion
    #===============================================================================================
    def clear_config(self) -> None:
        ic("Clearing Config...")
        for key in self.config.keys():
            ic(key)
            del self.config[key]
        ic(self.config)
        ic("Config Cleared.")

    #-----------------------------------------------------------------------------------------------
    def del_stop_settings(self) -> None:
        ic("Deleting Stop Settings...")
        sections: list[str] = [self.stop_settings,]
        ic(sections)
        self.__del_sections(sections)
        ic("Stop Settings Deleted.")

    #-----------------------------------------------------------------------------------------------
    def del_rank_settings(
            self,
            rank_number: int
    ) -> None:
        ic("Deleting Rank Settings...")
        ic(rank_number)
        sections: list[str] = [
            self.rank_settings(rank_number),
            self.rank_adsr_settings(rank_number)
        ]
        ic(sections)
        for harmonic in range(1, 20):
            ic(harmonic)
            sections.append(self.rank_harmonics_settings(rank_number, harmonic))
            sections.append(self.rank_harmonics_adsr_settings(rank_number, harmonic))
        for pipe in range(1, 61):
            ic(pipe)
            sections.append(self.pipe_settings(rank_number, pipe))
            sections.append(self.pipe_adsr_settings(rank_number, pipe))
            for harmonic in range(1, 20):
                sections.append(self.pipe_harmonics_settings(rank_number, pipe, harmonic))
                sections.append(self.pipe_harmonics_adsr_settings(rank_number, pipe, harmonic))
        ic(sections)
        self.__del_sections(sections)
        ic("Rank Settings Deleted.")
    
    #-----------------------------------------------------------------------------------------------
    def del_pipe_settings(
            self,
            rank_number: int,
            pipe_number: int
    ) -> None:
        ic("Deleting Pipe Settings...")
        ic(rank_number)
        ic(pipe_number)
        number_harmonics: int = self.number_harmonics_get(rank_number)
        ic(number_harmonics)
        sections: list[str] = [
            self.pipe_settings(rank_number, pipe_number),
            self.pipe_adsr_settings(rank_number, pipe_number)
        ]
        ic(sections)
        for harmonic in range(1, number_harmonics+1):
            ic(harmonic)
            sections.append(self.pipe_harmonics_settings(rank_number, pipe_number, harmonic))
            sections.append(self.pipe_harmonics_adsr_settings(rank_number, pipe_number, harmonic))
        ic(sections)
        self.__del_sections(sections)
        ic("Pipe Settings Deleted.")
    
    #-----------------------------------------------------------------------------------------------
    def del_harmonic_settings(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> None:
        ic("Deleting Harmonic Settings...")
        ic(rank_number)
        ic(harmonic_number)
        sections: list[str] = [
            self.rank_harmonics_settings(rank_number, harmonic_number),
            self.rank_harmonics_adsr_settings(rank_number, harmonic_number)
        ]
        for pipe in range(1, 61):
            sections.append(self.pipe_harmonics_settings(rank_number, pipe, harmonic_number))
            sections.append(self.pipe_harmonics_adsr_settings(rank_number, pipe, harmonic_number))
        ic(sections)
        self.__del_sections(sections)
        ic("Harmonic Settings Deleted.")
    
    #-----------------------------------------------------------------------------------------------
    def __del_sections(
            self,
            sections: list[str]
    ) -> None:
        ic("Deleting Sections...")
        ic(sections)
        for section in sections:
            ic(section)
            self.config.pop(section, None)
        ic(self.config)
        ic("Sections Deleted.")

    #===============================================================================================
    # Field Updating
    #===============================================================================================
    def update_note(
            self,
            rank_number: int,
            pipe_number: int,
            note: str
    ) -> None:
        ic("Updating Note...")
        ic(rank_number)
        ic(pipe_number)
        ic(note)
        self.note_set(rank_number, pipe_number, note)
        ic("Note Updated.")

    #-----------------------------------------------------------------------------------------------
    def update_relative_notes(
            self,
            rank_number: int,
            pipe_number: int,
            notes: tuple[str, ...]
    ) -> None:
        ic("Updating Relative Notes...")
        ic(rank_number)
        ic(pipe_number)
        ic(notes)
        number_pipes: int = len(range(pipe_number, self.number_pipes_get(rank_number)+1))
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

    #===============================================================================================
    # Getter and Setter Methods
    #===============================================================================================
    #***********************************************************************************************
    # Stop Name
    #***********************************************************************************************
    def stop_name_get(self) -> str:
        ic("Getting Stop Name...")
        section: str = self.stop_settings
        field: str = "Stop Name"
        stop_name: str = str(self.config[section][field])
        ic(stop_name)
        ic("Stop Name Retrieved.")
        return stop_name

    #-----------------------------------------------------------------------------------------------
    def stop_name_set(
            self,
            value: str
    ) -> None:
        ic("Setting Stop Name...")
        ic(value)
        section: str = self.stop_settings
        field: str = "Stop Name"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Stop Name Set.")

    #***********************************************************************************************
    # Stop Family
    #***********************************************************************************************
    def stop_family_get(self) -> str:
        ic("Getting Stop Family...")
        section: str = self.stop_settings
        field: str = "Stop Family"
        stop_family: str = str(self.config[section][field])
        ic(stop_family)
        ic("Stop Family Retrieved.")
        return stop_family

    #-----------------------------------------------------------------------------------------------
    def stop_family_set(
            self,
            value: str
    ) -> None:
        ic("Setting Stop Family...")
        ic(value)
        section: str = self.stop_settings
        field: str = "Stop Family"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Stop Family Set.")

    #***********************************************************************************************
    # Organ Division
    #***********************************************************************************************
    def organ_division_get(self) -> str:
        ic("Getting Organ Division...")
        section: str = self.stop_settings
        field: str = "Organ Division"
        organ_division: str = str(self.config[section][field])
        ic(organ_division)
        ic("Organ Division Retrieved.")
        return organ_division

    #-----------------------------------------------------------------------------------------------
    def organ_division_set(
            self,
            value: str
    ) -> None:
        ic("Setting Organ Division...")
        section: str = self.stop_settings
        field: str = "Organ Division"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Organ Division Set.")

    #***********************************************************************************************
    # Number of Ranks
    #***********************************************************************************************
    def number_ranks_get(self) -> int:
        ic("Getting Number of Ranks...")
        section: str = self.stop_settings
        field: str = "Number of Ranks"
        number_ranks: int = int(self.config[section][field])
        ic(number_ranks)
        ic("Number of Ranks Retrieved.")
        return number_ranks

    #-----------------------------------------------------------------------------------------------
    def number_ranks_set(
            self,
            value: int
    ) -> None:
        ic("Setting Number of Ranks...")
        section: str = self.stop_settings
        field: str = "Number of Ranks"
        number_rank_sections: int = self.number_ranks_get()
        if value > number_rank_sections:
            for rank in range(number_rank_sections, value+1):
                self.init_rank_config(rank)
        elif value < number_rank_sections:
            for rank in range(value, number_rank_sections+1):
                self.del_rank_settings(rank)
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Number of Ranks Set.")

    #***********************************************************************************************
    # Rank Series
    #***********************************************************************************************
    def rank_series_get(self) -> str:
        ic("Getting Rank Series...")
        section: str = self.stop_settings
        field: str = "Rank Series"
        rank_series: str = str(self.config[section][field])
        ic(rank_series)
        ic("Rank Series Retrieved.")
        return rank_series

    #-----------------------------------------------------------------------------------------------
    def rank_series_set(
            self,
            value: str
    ) -> None:
        ic("Setting Rank Series...")
        ic(value)
        section: str = self.stop_settings
        field: str = "Rank Series"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Rank Series Set.")

    #***********************************************************************************************
    # Rank Size
    #***********************************************************************************************
    def rank_size_get(
            self,
            rank_number: int
    ) -> str:
        ic("Getting Rank Size...")
        ic(rank_number)
        section: str = f"Rank {rank_number} Settings"
        field: str = "Rank Size"
        rank_size: str = str(self.config[section][field])
        ic(rank_size)
        ic("Rank Size Retrieved.")
        return rank_size

    #-----------------------------------------------------------------------------------------------
    def rank_size_set(
            self,
            rank_number: int,
            value: str
    ) -> None:
        ic("Setting Rank Size...")
        ic(rank_number)
        ic(value)
        section: str = f"Rank {rank_number} Settings"
        field: str = "Rank Size"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Rank Size Set.")

    #***********************************************************************************************
    # Number of Pipes
    #***********************************************************************************************
    def number_pipes_get(
            self,
            rank_number: int
    ) -> int:
        ic("Getting Number of Pipes...")
        ic(rank_number)
        section: str = self.rank_settings(rank_number)
        field: str = "Number of Pipes"
        number_pipes: int = int(self.config[section][field])
        ic(number_pipes)
        ic("Number of Pipes Retrieved.")
        return number_pipes

    #-----------------------------------------------------------------------------------------------
    def number_pipes_set(
            self,
            rank_number: int,
            value: int
    ) -> None:
        ic("Setting Number of Pipes...")
        ic(rank_number)
        ic(value)
        section: str = self.rank_settings(rank_number)
        field: str = "Number of Pipes"
        number_pipe_sections: int = self.number_pipes_get(rank_number)
        if value > number_pipe_sections:
            for pipe in range(number_pipe_sections, value):
                self.init_pipe_config(rank_number, pipe)
        elif value < number_pipe_sections:
            for pipe in range(value, number_pipe_sections):
                self.del_pipe_settings(rank_number, pipe)
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Number of Pipes Set.")

    #***********************************************************************************************
    # Pipe Type
    #***********************************************************************************************
    def pipe_type_get(
            self,
            rank_number: int
    ) -> str:
        ic("Getting Pipe Type...")
        ic(rank_number)
        section: str = self.rank_settings(rank_number)
        field: str = "Pipe Type"
        pipe_type: str = str(self.config[section][field])
        ic(pipe_type)
        ic("Pipe Type Retrieved.")
        return pipe_type

    #-----------------------------------------------------------------------------------------------
    def pipe_type_set(
            self,
            rank_number: int,
            value: str
    ) -> None:
        ic("Setting Pipe Type...")
        ic(rank_number)
        ic(value)
        section: str = self.rank_settings(rank_number)
        field: str = "Pipe Type"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Pipe Type Set.")

    #***********************************************************************************************
    # Starting Note
    #***********************************************************************************************
    def starting_note_get(
            self,
            rank_number: int
    ) -> str:
        ic("Getting Starting Note...")
        ic(rank_number)
        section: str = self.rank_settings(rank_number)
        field: str = "Starting Note"
        starting_note: str = str(self.config[section][field])
        ic(starting_note)
        ic("Starting Note Retrieved.")
        return starting_note

    #-----------------------------------------------------------------------------------------------
    def starting_note_set(
            self,
            rank_number: int,
            starting_note: str,
            values: tuple[str, ...]
    ) -> None:
        ic("Setting Starting Note...")
        ic(rank_number)
        ic(starting_note)
        ic(values)
        section: str = self.rank_settings(rank_number)
        field: str = "Starting Note"
        self.config[section][field] = starting_note
        ic(self.config[section][field])
        number_pipes: int = len(values)
        for pipe in range(1, number_pipes+1):
            self.note_set(rank_number, pipe, values[pipe-1])
            self.relative_note_set(rank_number, pipe, values[pipe-1])
        ic("Starting Note Set.")

    #***********************************************************************************************
    # Frequency Offset
    #***********************************************************************************************
    def frequency_offset_get(
            self,
            rank_number: int
    ) -> int:
        ic("Getting Frequency Offset...")
        ic(rank_number)
        section: str = self.rank_settings(rank_number)
        field: str = "Frequency Offset"
        frequency_offset: int = int(self.config[section][field])
        ic(frequency_offset)
        ic("Frequency Offset Retrieved.")
        return frequency_offset

    #-----------------------------------------------------------------------------------------------
    def frequency_offset_set(
            self,
            rank_number: int,
            value: int
    ) -> None:
        ic("Setting Frequency Offset...")
        ic(rank_number)
        ic(value)
        section: str = self.rank_settings(rank_number)
        field: str = "Frequency Offset"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Frequency Offset Set.")

    #***********************************************************************************************
    # Number of Harmonics
    #***********************************************************************************************
    def number_harmonics_get(
            self,
            rank_number: int
    ) -> int:
        ic("Getting Number of Harmonics...")
        ic(rank_number)
        section: str = self.rank_settings(rank_number)
        field: str = "Number of Harmonics"
        number_harmonics: int = int(self.config[section][field])
        ic(number_harmonics)
        ic("Number of Harmonics Retrieved.")
        return number_harmonics

    #-----------------------------------------------------------------------------------------------
    def number_harmonics_set(
            self,
            rank_number: int,
            value: int
    ) -> None:
        ic("Setting Number of Harmonics...")
        ic(rank_number)
        ic(value)
        section: str = self.rank_settings(rank_number)
        field: str = "Number of Harmonics"
        number_harmonic_sections: int = self.number_harmonics_get(rank_number)
        number_pipes: int = self.number_pipes_get(rank_number)
        if value > number_harmonic_sections:
            for harmonic in range(number_harmonic_sections, value+1):
                for pipe in range(1, number_pipes):
                    self.init_harmonic_config(rank_number, pipe, harmonic)
        elif value < number_harmonic_sections:
            for harmonic in range(
                value, number_harmonic_sections+1
            ):
                self.del_harmonic_settings(rank_number, harmonic)
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Number of Harmonics Set.")

    #***********************************************************************************************
    # Rank Harmonic Amplitude
    #***********************************************************************************************
    def rank_harmonic_amplitude_get(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> int:
        ic("Getting Rank Harmonic Amplitude...")
        ic(rank_number)
        ic(harmonic_number)
        section: str = self.rank_harmonics_settings(rank_number, harmonic_number)
        field: str = "Amplitude"
        rank_harmonic_amplitude: int = int(self.config[section][field])
        ic(rank_harmonic_amplitude)
        ic("Rank Harmonic Amplitude Retrieved.")
        return rank_harmonic_amplitude

    #-----------------------------------------------------------------------------------------------
    def rank_harmonic_amplitude_set(
            self,
            rank_number: int,
            harmonic_number: int,
            value: int
    ) -> None:
        ic("Setting Rank Harmonic Amplitude...")
        ic(rank_number)
        ic(harmonic_number)
        ic(value)
        section: str = self.rank_harmonics_settings(rank_number, harmonic_number)
        field: str = "Amplitude"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Rank Harmonic Amplitude Set.")

    #***********************************************************************************************
    # Rank Harmonic Attack Time
    #***********************************************************************************************
    def rank_harmonic_attack_time_get(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> int:
        ic("Getting Rank Harmonic Attack Time...")
        ic(rank_number)
        ic(harmonic_number)
        section: str = self.rank_harmonics_adsr_settings(rank_number, harmonic_number)
        field: str = "Attack Time"
        rank_harmonic_attack_time: int = int(self.config[section][field])
        ic(rank_harmonic_attack_time)
        ic("Rank Harmonic Attack Time Retrieved.")
        return rank_harmonic_attack_time

    #-----------------------------------------------------------------------------------------------
    def rank_harmonic_attack_time_set(
            self,
            rank_number: int,
            harmonic_number: int,
            value: int
    ) -> None:
        ic("Setting Rank Harmonic Attack Time...")
        ic(rank_number)
        ic(harmonic_number)
        section: str = self.rank_harmonics_adsr_settings(rank_number, harmonic_number)
        field: str = "Attack Time"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Rank Harmonic Attack Time Set.")

    #***********************************************************************************************
    # Rank Harmonic Decay Time
    #***********************************************************************************************
    def rank_harmonic_decay_time_get(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> int:
        ic("Getting Rank Harmonic Decay Time...")
        ic(rank_number)
        ic(harmonic_number)
        section: str = self.rank_harmonics_adsr_settings(rank_number, harmonic_number)
        field: str = "Decay Time"
        rank_harmonic_decay_time: int = int(self.config[section][field])
        ic(rank_harmonic_decay_time)
        ic("Rank Harmonic Decay Time Retrieved.")
        return rank_harmonic_decay_time

    #-----------------------------------------------------------------------------------------------
    def rank_harmonic_decay_time_set(
            self,
            rank_number: int,
            harmonic_number: int,
             value: int
    ) -> None:
        ic("Setting Rank Harmonic Decay Time...")
        ic(rank_number)
        ic(harmonic_number)
        ic(value)
        section: str = self.rank_harmonics_adsr_settings(rank_number, harmonic_number)
        field: str = "Decay Time"
        self.config[section][field] =  value
        ic(self.config[section][field])
        ic("Rank Harmonic Decay Time Set.")

    #***********************************************************************************************
    # Rank Harmonic Sustain Level
    #***********************************************************************************************
    def rank_harmonic_sustain_level_get(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> int:
        ic("Getting Rank Harmonic Sustain Level...")
        ic(rank_number)
        ic(harmonic_number)
        section: str = self.rank_harmonics_adsr_settings(rank_number, harmonic_number)
        field: str = "Sustain Level"
        rank_harmonic_sustain_level: int = int(self.config[section][field])
        ic(rank_harmonic_sustain_level)
        ic("Rank Harmonic Sustain Level Retrieved.")
        return rank_harmonic_sustain_level

    #-----------------------------------------------------------------------------------------------
    def rank_harmonic_sustain_level_set(
            self,
            rank_number: int,
            harmonic_number: int,
            value: int
    ) -> None:
        ic("Setting Rank Harmonic Sustain Level...")
        ic(rank_number)
        ic(harmonic_number)
        ic(value)
        section: str = self.rank_harmonics_adsr_settings(rank_number, harmonic_number)
        field: str = "Sustain Level"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Rank Harmonic Sustain Level Set.")

    #***********************************************************************************************
    # Rank Harmonic Release Time
    #***********************************************************************************************
    def rank_harmonic_release_time_get(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> int:
        ic("Getting Rank Harmonic Release Time...")
        ic(rank_number)
        ic(harmonic_number)
        section: str = self.rank_harmonics_adsr_settings(rank_number, harmonic_number)
        field: str = "Release Time"
        rank_harmonic_release_time: int = int(self.config[section][field])
        ic(rank_harmonic_release_time)
        ic("Rank Harmonic Release Time Retrieved.")
        return rank_harmonic_release_time

    #-----------------------------------------------------------------------------------------------
    def rank_harmonic_release_time_set(
            self,
            rank_number: int,
            harmonic_number: int,
            value: int
    ) -> None:
        ic("Setting Rank Harmonic Release Time...")
        ic(rank_number)
        ic(harmonic_number)
        ic(value)
        section: str = self.rank_harmonics_adsr_settings(rank_number, harmonic_number)
        field: str = "Release Time"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Rank Harmonic Release Time Set.")

    #***********************************************************************************************
    # Rank Attack Time
    #***********************************************************************************************
    def rank_attack_time_get(
            self,
            rank_number: int
    ) -> int:
        ic("Getting Rank Attack Time...")
        ic(rank_number)
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Attack Time"
        rank_attack_time: int = int(self.config[section][field])
        ic(rank_attack_time)
        ic("Rank Attack Time Retrieved.")
        return rank_attack_time

    #-----------------------------------------------------------------------------------------------
    def rank_attack_time_set(
            self,
            rank_number: int,
            value: int
    ) -> None:
        ic("Setting Rank Attack Time...")
        ic(rank_number)
        ic(value)
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Attack Time"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Rank Attack Time Set.")

    #***********************************************************************************************
    # Rank Decay Time
    #***********************************************************************************************
    def rank_decay_time_get(
            self,
            rank_number: int
    ) -> int:
        ic("Getting Rank Decay Time...")
        ic(rank_number)
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Decay Time"
        rank_decay_time: int = int(self.config[section][field])
        ic(rank_decay_time)
        ic("Rank Decay Time Retrieved.")
        return rank_decay_time

    #-----------------------------------------------------------------------------------------------
    def rank_decay_time_set(
            self,
            rank_number: int,
            value: int
    ) -> None:
        ic("Setting Rank Decay Time...")
        ic(rank_number)
        ic(value)
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Decay Time"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Rank Decay Time Set.")

    #***********************************************************************************************
    # Rank Sustain Level
    #***********************************************************************************************
    def rank_sustain_level_get(
            self,
            rank_number: int
    ) -> int:
        ic("Getting Rank Sustain Level...")
        ic(rank_number)
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Sustain Level"
        rank_sustain_level: int = int(self.config[section][field])
        ic(rank_sustain_level)
        ic("Rank Sustain Level Retrieved.")
        return rank_sustain_level

    #-----------------------------------------------------------------------------------------------
    def rank_sustain_level_set(
            self,
            rank_number: int,
            value: int
    ) -> None:
        ic("Setting Rank Sustain Level...")
        ic(rank_number)
        ic(value)
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Sustain Level"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Rank Sustain Level Set.")

    #***********************************************************************************************
    # Rank Release Time
    #***********************************************************************************************
    def rank_release_time_get(
            self,
            rank_number: int
    ) -> int:
        ic("Getting Rank Release Time...")
        ic(rank_number)
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Release Time"
        rank_release_time: int = int(self.config[section][field])
        ic(rank_release_time)
        ic("Rank Release Time Retrieved.")
        return rank_release_time

    #-----------------------------------------------------------------------------------------------
    def rank_release_time_set(
            self,
            rank_number: int,
            value: int
    ) -> None:
        ic("Setting Rank Release Time...")
        ic(rank_number)
        ic(value)
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Release Time"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Rank Release Time Set.")

    #***********************************************************************************************
    # Note
    #***********************************************************************************************
    def note_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> str:
        ic("Getting Note...")
        ic(rank_number)
        ic(pipe_number)
        section: str = self.pipe_settings(rank_number, pipe_number)
        field: str = "Note"
        note: str = str(self.config[section][field])
        ic(note)
        ic("Note Retrieved.")
        return note

    #-----------------------------------------------------------------------------------------------
    def note_set(
            self,
            rank_number: int,
            pipe_number: int,
            value: str
    ) -> None:
        ic("Setting Note...")
        ic(rank_number)
        ic(pipe_number)
        ic(value)
        section: str = self.pipe_settings(rank_number, pipe_number)
        field: str = "Note"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Note Set.")

    #***********************************************************************************************
    # Relative Note
    #***********************************************************************************************
    def relative_note_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> str:
        ic("Getting Relative Note...")
        ic(rank_number)
        ic(pipe_number)
        section: str = self.pipe_settings(rank_number, pipe_number)
        field: str = "Relative Note"
        relative_note: str = str(self.config[section][field])
        ic(relative_note)
        ic("Relative Note Retrieved.")
        return relative_note

    #-----------------------------------------------------------------------------------------------
    def relative_note_set(
            self,
            rank_number: int,
            pipe_number: int,
            value: str,
    ) -> None:
        ic("Setting Relative Note...")
        ic(rank_number)
        ic(pipe_number)
        ic(value)
        section: str = self.pipe_settings(rank_number, pipe_number)
        field: str = "Relative Note"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Relative Note Set.")

    #***********************************************************************************************
    # Pipe Harmonic Amplitude
    #***********************************************************************************************
    def pipe_harmonic_amplitude_get(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> int:
        ic("Getting Pipe Harmonic Amplitude...")
        ic(rank_number)
        ic(pipe_number)
        ic(harmonic_number)
        section: str = self.pipe_harmonics_settings(rank_number, pipe_number, harmonic_number)
        field: str = "Amplitude"
        pipe_harmonic_amplitude: int = int(self.config[section][field])
        ic(pipe_harmonic_amplitude)
        ic("Pipe Harmonic Amplitude Retrieved.")
        return pipe_harmonic_amplitude

    #-----------------------------------------------------------------------------------------------
    def pipe_harmonic_amplitude_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            value: int
    ) -> None:
        ic("Setting Pipe Harmonic Amplitude...")
        ic(rank_number)
        ic(pipe_number)
        ic(harmonic_number)
        ic(value)
        section: str = self.pipe_harmonics_settings(rank_number, pipe_number, harmonic_number)
        field: str = "Amplitude"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Pipe Harmonic Amplitude Set.")

    #***********************************************************************************************
    # Pipe Harmonic Attack Time
    #***********************************************************************************************
    def pipe_harmonic_attack_time_get(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> int:
        ic("Getting Pipe Harmonic Attack Time...")
        ic(rank_number)
        ic(pipe_number)
        ic(harmonic_number)
        section: str = self.pipe_harmonics_adsr_settings(rank_number, pipe_number, harmonic_number)
        field: str = "Attack Time"
        pipe_harmonic_attack_time: int = int(self.config[section][field])
        ic(pipe_harmonic_attack_time)
        ic("Pipe Harmonic Attack Time Retrieved.")
        return pipe_harmonic_attack_time

    #-----------------------------------------------------------------------------------------------
    def pipe_harmonic_attack_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            value: int
    ) -> None:
        ic("Setting Pipe Harmonic Attack Time...")
        ic(rank_number)
        ic(pipe_number)
        ic(harmonic_number)
        ic(value)
        section: str = self.pipe_harmonics_adsr_settings(rank_number, pipe_number, harmonic_number)
        field: str = "Attack Time"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Pipe Harmonic Attack Time Set.")

    #***********************************************************************************************
    # Pipe Harmonic Decay Time
    #***********************************************************************************************
    def pipe_harmonic_decay_time_get(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> int:
        ic("Getting Pipe Harmonic Decay Time...")
        ic(rank_number)
        ic(pipe_number)
        ic(harmonic_number)
        section: str = self.pipe_harmonics_adsr_settings(rank_number, pipe_number, harmonic_number)
        field: str = "Decay Time"
        pipe_harmonic_decay_time: int = int(self.config[section][field])
        ic(pipe_harmonic_decay_time)
        ic("Pipe Harmonic Decay Time Retrieved.")
        return pipe_harmonic_decay_time

    #-----------------------------------------------------------------------------------------------
    def pipe_harmonic_decay_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            value: int
    ) -> None:
        ic("Setting Pipe Harmonic Decay Time...")
        ic(rank_number)
        ic(pipe_number)
        ic(harmonic_number)
        ic(value)
        section: str = self.pipe_harmonics_adsr_settings(rank_number, pipe_number, harmonic_number)
        field: str = "Decay Time"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Pipe Harmonic Decay Time Set.")

    #***********************************************************************************************
    # Pipe Harmonic Sustain Level
    #***********************************************************************************************
    def pipe_harmonic_sustain_level_get(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> int:
        ic("Getting Pipe Harmonic Sustain Level...")
        ic(rank_number)
        ic(pipe_number)
        ic(harmonic_number)
        section: str = self.pipe_harmonics_adsr_settings(rank_number, pipe_number, harmonic_number)
        field: str = "Sustain Level"
        pipe_harmonic_sustain_level: int = int(self.config[section][field])
        ic(pipe_harmonic_sustain_level)
        ic("Pipe Harmonic Sustain Level Retrieved.")
        return pipe_harmonic_sustain_level

    #-----------------------------------------------------------------------------------------------
    def pipe_harmonic_sustain_level_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            value: int
    ) -> None:
        ic("Setting Pipe Harmonic Sustain Level...")
        ic(rank_number)
        ic(pipe_number)
        ic(harmonic_number)
        ic(value)
        section: str = self.pipe_harmonics_adsr_settings(rank_number, pipe_number, harmonic_number)
        field: str = "Sustain Level"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Pipe Harmonic Sustain Level Set.")

    #***********************************************************************************************
    # Pipe Harmonic Release Time
    #***********************************************************************************************
    def pipe_harmonic_release_time_get(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> int:
        ic("Getting Pipe Harmonic Release Time...")
        ic(rank_number)
        ic(pipe_number)
        ic(harmonic_number)
        section: str = self.pipe_harmonics_adsr_settings(rank_number, pipe_number, harmonic_number)
        field: str = "Release Time"
        pipe_harmonic_release_time: int = int(self.config[section][field])
        ic(pipe_harmonic_release_time)
        ic("Pipe Harmonic Release Time Retrieved.")
        return pipe_harmonic_release_time

    #-----------------------------------------------------------------------------------------------
    def pipe_harmonic_release_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            value: int
    ) -> None:
        ic("Getting Pipe Harmonic Release Time...")
        ic(rank_number)
        ic(pipe_number)
        ic(harmonic_number)
        ic(value)
        section: str = self.pipe_harmonics_adsr_settings(rank_number, pipe_number, harmonic_number)
        field: str = "Release Time"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Pipe Harmonic Release Time Set.")

    #***********************************************************************************************
    # Pipe Attack Time
    #***********************************************************************************************
    def pipe_attack_time_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> int:
        ic("Getting Pipe Attack Time...")
        ic(rank_number)
        ic(pipe_number)
        section: str = self.pipe_adsr_settings(rank_number, pipe_number)
        field: str = "Attack Time"
        pipe_attack_time: int = int(self.config[section][field])
        ic(pipe_attack_time)
        ic("Pipe Attack Time Retrieved.")
        return pipe_attack_time

    #-----------------------------------------------------------------------------------------------
    def pipe_attack_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            value: int
    ) -> None:
        ic("Setting Pipe Attack Time...")
        ic(rank_number)
        ic(pipe_number)
        ic(value)
        section: str = self.pipe_adsr_settings(rank_number, pipe_number)
        field: str = "Attack Time"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Pipe Attack Time Set.")

    #***********************************************************************************************
    # Pipe Decay Time
    #***********************************************************************************************
    def pipe_decay_time_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> int:
        ic("Getting Pipe Decay Time...")
        ic(rank_number)
        ic(pipe_number)
        section: str = self.pipe_adsr_settings(rank_number, pipe_number)
        field: str = "Decay Time"
        pipe_decay_time: int = int(self.config[section][field])
        ic(pipe_decay_time)
        ic("Pipe Decay Time Retrieved.")
        return pipe_decay_time

    #-----------------------------------------------------------------------------------------------
    def pipe_decay_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            value: int
    ) -> None:
        ic("Setting Pipe Decay Time...")
        ic(rank_number)
        ic(pipe_number)
        ic(value)
        section: str = self.pipe_adsr_settings(rank_number, pipe_number)
        field: str = "Decay Time"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Pipe Decay Time Set.")

    #***********************************************************************************************
    # Pipe Sustain Level
    #***********************************************************************************************
    def pipe_sustain_level_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> int:
        ic("Getting Pipe Sustain Level...")
        ic(rank_number)
        ic(pipe_number)
        section: str = self.pipe_adsr_settings(rank_number, pipe_number)
        field: str = "Sustain Level"
        pipe_sustain_level: int = int(self.config[section][field])
        ic(pipe_sustain_level)
        ic("Pipe Sustain Level Retrieved.")
        return pipe_sustain_level

    #-----------------------------------------------------------------------------------------------
    def pipe_sustain_level_set(
            self,
            rank_number: int,
            pipe_number: int,
            value: int
    ) -> None:
        ic("Setting Pipe Sustain Level...")
        ic(rank_number)
        ic(pipe_number)
        ic(value)
        section: str = self.pipe_adsr_settings(rank_number, pipe_number)
        field: str = "Sustain Level"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Pipe Sustain Level Set.")

    #***********************************************************************************************
    # Pipe Release Time
    #***********************************************************************************************
    def pipe_release_time_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> int:
        ic("Getting Pipe Release Time...")
        ic(rank_number)
        ic(pipe_number)
        section: str = self.pipe_adsr_settings(rank_number, pipe_number)
        field: str = "Release Time"
        pipe_release_time: int = int(self.config[section][field])
        ic(pipe_release_time)
        ic("Pipe Release Time Retrieved.")
        return pipe_release_time

    #-----------------------------------------------------------------------------------------------
    def pipe_release_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            value: int
    ) -> None:
        ic("Setting Pipe Release Time...")
        ic(rank_number)
        ic(pipe_number)
        ic(value)
        section: str = self.pipe_adsr_settings(rank_number, pipe_number)
        field: str = "Release Time"
        self.config[section][field] = value
        ic(self.config[section][field])
        ic("Pipe Release Time Set.")

    #***********************************************************************************************
    # Sections
    #***********************************************************************************************
    @property
    def stop_settings(self) -> str:
        section: str = "Stop Settings"
        ic(section)
        return section

    #-----------------------------------------------------------------------------------------------
    def rank_settings(
            self,
            rank_number: int
    ) -> str:
        section: str = f"Rank {rank_number} Settings"
        ic(section)
        return section

    #-----------------------------------------------------------------------------------------------
    def rank_harmonics_settings(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - Harmonic {harmonic_number} Settings"
        ic(section)
        return section

    #-----------------------------------------------------------------------------------------------
    def rank_harmonics_adsr_settings(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> str:
        rank: str = f"Rank {rank_number}"
        harmonics: str = f"Harmonic {harmonic_number}"
        section: str = f"{rank} - {harmonics} - ADSR Settings"
        ic(section)
        return section

    #-----------------------------------------------------------------------------------------------
    def rank_adsr_settings(
            self,
            rank_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - ADSR Settings"
        ic(section)
        return section

    #-----------------------------------------------------------------------------------------------
    def pipe_settings(
            self,
            rank_number: int,
            pipe_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} Settings"
        ic(section)
        return section

    #-----------------------------------------------------------------------------------------------
    def pipe_harmonics_settings(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> str:
        rank: str = f"Rank {rank_number}"
        pipe: str = f"Pipe {pipe_number}"
        harmonics: str = f"Harmonic {harmonic_number}"
        section: str = f"{rank} - {pipe} - {harmonics} - Settings"
        ic(section)
        return section

    #-----------------------------------------------------------------------------------------------
    def pipe_harmonics_adsr_settings(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> str:
        rank: str = f"Rank {rank_number}"
        pipe: str = f"Pipe {pipe_number}"
        harmonics: str = f"Harmonic {harmonic_number}"
        section: str = f"{rank} - {pipe} - {harmonics} - ADSR Settings"
        ic(section)
        return section

    #-----------------------------------------------------------------------------------------------
    def pipe_adsr_settings(
            self,
            rank_number: int,
            pipe_number: int
    ) -> str:
        rank: str = f"Rank {rank_number}"
        pipe: str = f"Pipe {pipe_number}"
        section: str = f"{rank} - {pipe} - ADSR Settings"
        ic(section)
        return section


#===================================================================================================
# Executable
#===================================================================================================
if __name__ == "__main__":
    stop_config: StopConfig = StopConfig()
    stop_config.load_file("src/config/stops/AEOLINE 8'.json")
    ic(stop_config.rank_size_get(1))
