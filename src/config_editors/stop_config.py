from organ import organlib
#-----------------------------------------------------------------------------------------------------------------------
import json
#-----------------------------------------------------------------------------------------------------------------------
from icecream import ic # type: ignore


class StopConfig:
    def __init__(self) -> None:
        ic("Initializing StopConfig...")
        self.config: dict[str, dict[str, str | int]] = {}
        ic("StopConfig Initialized")

    #===================================================================================================================
    # File Operations
    #===================================================================================================================
    def load_file(
            self,
            file: str
    ) -> None:
        ic("Loading File...")
        with open(file, "r") as config_file:
            self.config = json.load(config_file)
        ic("File Loaded.")

    #-------------------------------------------------------------------------------------------------------------------
    def save_file(
            self,
            file: str
    ) -> None:
        ic("Saving File...")
        with open(file, "w") as config_file:
            json.dump(self.config, config_file, indent=4)
        ic("File Saved.")

    #===================================================================================================================
    # Config Creation
    #===================================================================================================================
    def init_default_config(self) -> None:
        ic("Initializing Default Config...")
        self.clear_config()
        self.init_stop_config()
        self.update_starting_note(1)
        ic("Default Config Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def init_stop_config(self) -> None:
        ic("Initializing Stop Config...")
        self.init_stop_settings()
        number_ranks: int = self.number_ranks_get()
        for rank in range(1, number_ranks+1):
            self.init_rank_config(rank)
        ic("Stop Config Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def init_rank_config(
            self,
            rank_number: int
    ) -> None:
        ic("Initializing Rank Config...")
        self.init_rank_settings(rank_number)
        self.init_rank_adsr_settings(rank_number)
        self.init_rank_harmonics_config(rank_number)
        number_pipes: int = self.number_pipes_get(rank_number)
        pipes: range = range(1, number_pipes+1)
        for pipe in pipes:
            self.init_pipe_config(rank_number, pipe)
        ic("Rank Config Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def init_rank_harmonics_config(
            self,
            rank_number: int
    ) -> None:
        ic("Initializing Rank Harmonics Config...")
        number_harmonics: int = self.number_harmonics_get(rank_number)
        harmonics: range = range(1, number_harmonics+1)
        for harmonic in harmonics:
            self.init_rank_harmonic_settings(rank_number, harmonic)
            self.init_rank_harmonic_adsr_settings(rank_number, harmonic)
        ic("Rank Harmonics Config Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def init_pipe_config(
            self,
            rank_number: int,
            pipe_number: int
    ) -> None:
        ic("Initializing Pipe Config...")
        self.init_pipe_settings(rank_number, pipe_number)
        self.init_pipe_adsr_settings(rank_number, pipe_number)
        number_harmonics: int = self.number_harmonics_get(rank_number)
        harmonics: range = range(1, number_harmonics+1)
        for harmonic in harmonics:
            self.init_pipe_harmonic_settings(rank_number, pipe_number, harmonic)
            self.init_pipe_harmonic_adsr_settings(rank_number, pipe_number, harmonic)
        ic("Pipe Config Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def init_harmonic_config(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> None:
        ic("Initializing Harmonic Config...")
        self.init_rank_harmonic_settings(rank_number, harmonic_number)
        self.init_rank_harmonic_adsr_settings(rank_number, harmonic_number)
        self.init_pipe_harmonic_settings(rank_number, pipe_number, harmonic_number)
        self.init_pipe_harmonic_adsr_settings(rank_number, pipe_number, harmonic_number)
        ic("Harmonic Config Initialized.")

    #===================================================================================================================
    # Section Initialization
    #===================================================================================================================
    def init_stop_settings(self) -> None:
        ic("Initializing Stop Settings...")
        section: str = self.stop_settings
        self.config[section] = {
            "Stop Name": "",
            "Stop Family": "",
            "Organ Division": "",
            "Number of Ranks": 1,
            "Rank Series": ""
        }
        ic("Stop Settings Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def init_rank_settings(
            self,
            rank_number: int
    ) -> None:
        ic("Initializing Rank Settings...")
        section: str = self.rank_settings(rank_number)
        self.config[section] = {
            "Rank Size": "",
            "Pipe Type": "",
            "Starting Note": "C2",
            "Frequency Offset": 0,
            "Number of Pipes": 61,
            "Number of Harmonics": 1
        }
        ic("Rank Settings Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def init_rank_harmonic_settings(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> None:
        ic("Initializing Rank Harmonic Settings...")
        section: str = self.rank_harmonics_settings(rank_number, harmonic_number)
        self.config[section] = {"Amplitude": 0}
        ic("Rank Harmonic Settings Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def init_rank_harmonic_adsr_settings(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> None:
        ic("Initializing Rank Harmonic ADSR Settings...")
        section: str = self.rank_harmonics_adsr_settings(rank_number, harmonic_number)
        self.config[section] = {
            "Attack Time": 0,
            "Decay Time": 0,
            "Sustain Level": 0,
            "Release Time": 0
        }
        ic("Rank Harmonic ADSR Settings Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def init_rank_adsr_settings(
            self,
            rank_number: int
    ) -> None:
        ic("Initializing Rank ADSR Settings...")
        section: str = self.rank_adsr_settings(rank_number)
        self.config[section] = {
            "Attack Time": 0,
            "Decay Time": 0,
            "Sustain Level": 0,
            "Release Time": 0
        }
        ic("Rank ADSR Settings Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def init_pipe_settings(
            self,
            rank_number: int,
            pipe_number: int
    ) -> None:
        ic("Initializing Pipe Settings...")
        section: str = self.pipe_settings(rank_number, pipe_number)
        ic(section)
        self.config[section] = {
            "Note": "",
            "Relative Note": ""
        }
        ic("Pipe Settings Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def init_pipe_harmonic_settings(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> None:
        ic("Initializing Pipe Harmonic Settings...")
        section: str = self.pipe_harmonics_settings(rank_number, pipe_number, harmonic_number)
        self.config[section] = {"Amplitude": 0}
        ic("Pipe Harmonic Settings Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def init_pipe_harmonic_adsr_settings(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> None:
        ic("Initializing Pipe Harmonic ADSR Settings...")
        section: str = self.pipe_harmonics_adsr_settings(rank_number, pipe_number, harmonic_number)
        self.config[section] = {
            "Attack Time": 0,
            "Decay Time": 0,
            "Sustain Level": 0,
            "Release Time": 0
        }
        ic("Pipe Harmonic ADSR Settings Initialized.")

    #-------------------------------------------------------------------------------------------------------------------
    def init_pipe_adsr_settings(
            self,
            rank_number: int,
            pipe_number: int,
    ) -> None:
        ic("Initializing Pipe ADSR Settings...")
        section: str = self.pipe_adsr_settings(rank_number, pipe_number)
        self.config[section] = {
            "Attack Time": 0,
            "Decay Time": 0,
            "Sustain Level": 0,
            "Release Time": 0
        }
        ic("Pipe ADSR Settings Initialized.")

    #===================================================================================================================
    # Section Deletion
    #===================================================================================================================
    def clear_config(self) -> None:
        ic("Clearing Config...")
        self.config = {}
        ic("Config Cleared.")

    #-------------------------------------------------------------------------------------------------------------------
    def del_stop_settings(self) -> None:
        ic("Deleting Stop Settings...")
        sections: list[str] = [self.stop_settings,]
        self.__del_sections(sections)
        ic("Stop Settings Deleted.")

    #-------------------------------------------------------------------------------------------------------------------
    def del_rank_settings(
            self,
            rank_number: int
    ) -> None:
        ic("Deleting Rank Settings...")
        sections: list[str] = [section for section in self.config if f"Rank {rank_number}" in section]
        self.__del_sections(sections)

#        sections: list[str] = [
#            self.rank_settings(rank_number),
#            self.rank_adsr_settings(rank_number)
#        ]
#        for harmonic in range(1, 20):
#            sections.append(self.rank_harmonics_settings(rank_number, harmonic))
#            sections.append(self.rank_harmonics_adsr_settings(rank_number, harmonic))
#        for pipe in range(1, 61):
#            sections.append(self.pipe_settings(rank_number, pipe))
#            sections.append(self.pipe_adsr_settings(rank_number, pipe))
#            for harmonic in range(1, 20):
#                sections.append(self.pipe_harmonics_settings(rank_number, pipe, harmonic))
#                sections.append(self.pipe_harmonics_adsr_settings(rank_number, pipe, harmonic))
#        self.__del_sections(sections)
        ic("Rank Settings Deleted.")
    
    #-------------------------------------------------------------------------------------------------------------------
    def del_pipe_settings(
            self,
            rank_number: int,
            pipe_number: int
    ) -> None:
        ic("Deleting Pipe Settings...")
        sections: list[str] = [
            section for section in self.config if f"Rank {rank_number} - Pipe {pipe_number}" in section
        ]
        self.__del_sections(sections)
        #number_harmonics: int = self.number_harmonics_get(rank_number)
        #sections: list[str] = [
        #    self.pipe_settings(rank_number, pipe_number),
        #    self.pipe_adsr_settings(rank_number, pipe_number)
        #]
        #for harmonic in range(1, number_harmonics+1):
        #    sections.append(self.pipe_harmonics_settings(rank_number, pipe_number, harmonic))
        #    sections.append(self.pipe_harmonics_adsr_settings(rank_number, pipe_number, harmonic))
        #self.__del_sections(sections)
        ic("Pipe Settings Deleted.")
    
    #-------------------------------------------------------------------------------------------------------------------
    def del_harmonic_settings(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> None:
        ic("Deleting Harmonic Settings...")
        sections: list[str] = [
            section for section in self.config if f"Rank {rank_number} - Harmonic {harmonic_number}" in section
        ]
        #sections: list[str] = [
        #    self.rank_harmonics_settings(rank_number, harmonic_number),
        #    self.rank_harmonics_adsr_settings(rank_number, harmonic_number)
        #]
        #for pipe in range(1, 61):
        #    sections.append(self.pipe_harmonics_settings(rank_number, pipe, harmonic_number))
        #    sections.append(self.pipe_harmonics_adsr_settings(rank_number, pipe, harmonic_number))
        self.__del_sections(sections)
        ic("Harmonic Settings Deleted.")
    
    #-------------------------------------------------------------------------------------------------------------------
    def __del_sections(
            self,
            sections: list[str]
    ) -> None:
        ic("Deleting Sections...")
        for section in sections:
            ic(section)
            self.config.pop(section, None)
        ic("Sections Deleted.")

    #===================================================================================================================
    # Field Updating
    #===================================================================================================================
    def update_starting_note(
            self,
            rank_number: int
    ) -> None:
        ic("Updating Starting Note...")
        note: str = self.starting_note_get(rank_number)
        self.starting_note_set(rank_number, note)
        i: int = organlib.NOTES.index(note)
        notes: tuple[str, ...] = organlib.NOTES[i:]
        for pipe in range(len(notes)):
            self.note_set(rank_number, pipe+1, notes[pipe])
            self.relative_note_set(rank_number, pipe+1, notes[pipe])

    #-------------------------------------------------------------------------------------------------------------------
    def update_note(
            self,
            rank_number: int,
            pipe_number: int,
            note: str
    ) -> None:
        ic("Updating Note...")
        self.note_set(rank_number, pipe_number, note)
        i: int = organlib.NOTES.index(note)
        notes: tuple[str, ...] = organlib.NOTES[i:]
        self.update_relative_notes(rank_number, pipe_number, notes)
        ic("Note Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def update_relative_notes(
            self,
            rank_number: int,
            pipe_number: int,
            notes: tuple[str, ...]
    ) -> None:
        ic("Updating Relative Notes...")
        number_pipes: int = len(range(pipe_number, self.number_pipes_get(rank_number)+1))
        number_notes: int = len(notes)
        if number_notes < number_pipes:
            number_pipes = number_notes
        for i in range(number_pipes):
            pipe = pipe_number + i
            note = notes[i]
            self.relative_note_set(rank_number, pipe, note)
        ic("Relative Notes Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def update_amplitudes(
            self,
            rank_number: int,
            harmonic_number: int,
            amplitude: int
    ) -> None:
        ic("Updating Amplitudes...")
        self.rank_harmonic_amplitude_set(rank_number, harmonic_number, amplitude)
        for pipe in range(1, self.number_pipes_get(rank_number)+1):
            self.pipe_harmonic_amplitude_set(rank_number, pipe, harmonic_number, amplitude)

    #-------------------------------------------------------------------------------------------------------------------
    def update_attack_times(
            self,
            rank_number: int,
            harmonic_number: int,
            attack_time: int
    ) -> None:
        ic("Updating Attack Times...")
        self.rank_harmonic_attack_time_set(rank_number, harmonic_number, attack_time)
        for pipe in range(1, self.number_pipes_get(rank_number)+1):
            self.pipe_harmonic_attack_time_set(rank_number, pipe, harmonic_number, attack_time)
        ic("Attack Times Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def update_decay_times(
            self,
            rank_number: int,
            harmonic_number: int,
            decay_time: int
    ) -> None:
        ic("Updating Decay Times...")
        self.rank_harmonic_decay_time_set(rank_number, harmonic_number, decay_time)
        for pipe in range(1, self.number_pipes_get(rank_number)+1):
            self.pipe_harmonic_decay_time_set(rank_number, pipe, harmonic_number, decay_time)
        ic("Decay Times Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def update_sustain_levels(
            self,
            rank_number: int,
            harmonic_number: int,
            sustain_level: int
    ) -> None:
        ic("Updating Sustain Levels...")
        self.rank_harmonic_sustain_level_set(rank_number, harmonic_number, sustain_level)
        for pipe in range(1, self.number_pipes_get(rank_number)+1):
            self.pipe_harmonic_sustain_level_set(rank_number, pipe, harmonic_number, sustain_level)
        ic("Sustain Levels Updated.")

    #-------------------------------------------------------------------------------------------------------------------
    def update_release_times(
            self,
            rank_number: int,
            harmonic_number: int,
            release_time: int
    ) -> None:
        ic("Updating Release Times...")
        self.rank_harmonic_release_time_set(rank_number, harmonic_number, release_time)
        for pipe in range(1, self.number_pipes_get(rank_number)+1):
            self.pipe_harmonic_release_time_set(rank_number, pipe, harmonic_number, release_time)
        ic("Release Times Updated.")

    #===================================================================================================================
    # Getter and Setter Methods
    #===================================================================================================================
    #*******************************************************************************************************************
    # Stop Name
    #*******************************************************************************************************************
    def stop_name_get(self) -> str:
        ic("Getting Stop Name...")
        section: str = self.stop_settings
        field: str = "Stop Name"
        stop_name: str = str(self.config[section][field])
        ic("Stop Name Retrieved.")
        return stop_name

    #-------------------------------------------------------------------------------------------------------------------
    def stop_name_set(
            self,
            value: str
    ) -> None:
        ic("Setting Stop Name...")
        section: str = self.stop_settings
        field: str = "Stop Name"
        self.config[section][field] = value
        ic("Stop Name Set.")

    #*******************************************************************************************************************
    # Stop Family
    #*******************************************************************************************************************
    def stop_family_get(self) -> str:
        ic("Getting Stop Family...")
        section: str = self.stop_settings
        field: str = "Stop Family"
        stop_family: str = str(self.config[section][field])
        ic("Stop Family Retrieved.")
        return stop_family

    #-------------------------------------------------------------------------------------------------------------------
    def stop_family_set(
            self,
            value: str
    ) -> None:
        ic("Setting Stop Family...")
        section: str = self.stop_settings
        field: str = "Stop Family"
        self.config[section][field] = value
        ic("Stop Family Set.")

    #*******************************************************************************************************************
    # Organ Division
    #*******************************************************************************************************************
    def organ_division_get(self) -> str:
        ic("Getting Organ Division...")
        section: str = self.stop_settings
        field: str = "Organ Division"
        organ_division: str = str(self.config[section][field])
        ic("Organ Division Retrieved.")
        return organ_division

    #-------------------------------------------------------------------------------------------------------------------
    def organ_division_set(
            self,
            value: str
    ) -> None:
        ic("Setting Organ Division...")
        section: str = self.stop_settings
        field: str = "Organ Division"
        self.config[section][field] = value
        ic("Organ Division Set.")

    #*******************************************************************************************************************
    # Number of Ranks
    #*******************************************************************************************************************
    def number_ranks_get(self) -> int:
        ic("Getting Number of Ranks...")
        section: str = self.stop_settings
        field: str = "Number of Ranks"
        number_ranks: int = int(self.config[section][field])
        ic("Number of Ranks Retrieved.")
        return number_ranks

    #-------------------------------------------------------------------------------------------------------------------
    def number_ranks_set(
            self,
            value: int
    ) -> None:
        ic("Setting Number of Ranks...")
        section: str = self.stop_settings
        field: str = "Number of Ranks"
        number_rank_sections: int = self.number_ranks_get()
        if value > number_rank_sections:
            for rank in range(number_rank_sections+1, value+1):
                self.init_rank_config(rank)
        elif value < number_rank_sections:
            for rank in range(value+1, number_rank_sections+1):
                self.del_rank_settings(rank)
        self.config[section][field] = value
        ic("Number of Ranks Set.")

    #*******************************************************************************************************************
    # Rank Series
    #*******************************************************************************************************************
    def rank_series_get(self) -> str:
        ic("Getting Rank Series...")
        section: str = self.stop_settings
        field: str = "Rank Series"
        rank_series: str = str(self.config[section][field])
        ic("Rank Series Retrieved.")
        return rank_series

    #-------------------------------------------------------------------------------------------------------------------
    def rank_series_set(
            self,
            value: str
    ) -> None:
        ic("Setting Rank Series...")
        section: str = self.stop_settings
        field: str = "Rank Series"
        self.config[section][field] = value
        ic("Rank Series Set.")

    #*******************************************************************************************************************
    # Rank Size
    #*******************************************************************************************************************
    def rank_size_get(
            self,
            rank_number: int
    ) -> str:
        ic("Getting Rank Size...")
        section: str = f"Rank {rank_number} Settings"
        field: str = "Rank Size"
        rank_size: str = str(self.config[section][field])
        ic("Rank Size Retrieved.")
        return rank_size

    #-------------------------------------------------------------------------------------------------------------------
    def rank_size_set(
            self,
            rank_number: int,
            value: str
    ) -> None:
        ic("Setting Rank Size...")
        section: str = f"Rank {rank_number} Settings"
        field: str = "Rank Size"
        self.config[section][field] = value
        ic("Rank Size Set.")

    #*******************************************************************************************************************
    # Number of Pipes
    #*******************************************************************************************************************
    def number_pipes_get(
            self,
            rank_number: int
    ) -> int:
        ic("Getting Number of Pipes...")
        section: str = self.rank_settings(rank_number)
        field: str = "Number of Pipes"
        number_pipes: int = int(self.config[section][field])
        ic("Number of Pipes Retrieved.")
        return number_pipes

    #-------------------------------------------------------------------------------------------------------------------
    def number_pipes_set(
            self,
            rank_number: int,
            value: int
    ) -> None:
        ic("Setting Number of Pipes...")
        section: str = self.rank_settings(rank_number)
        field: str = "Number of Pipes"
        number_pipe_sections: int = self.number_pipes_get(rank_number)
        if value > number_pipe_sections:
            for pipe in range(number_pipe_sections+1, value+1):
                self.init_pipe_config(rank_number, pipe)
        elif value < number_pipe_sections:
            for pipe in range(value+1, number_pipe_sections+1):
                self.del_pipe_settings(rank_number, pipe)
        self.config[section][field] = value
        ic("Number of Pipes Set.")

    #*******************************************************************************************************************
    # Pipe Type
    #*******************************************************************************************************************
    def pipe_type_get(
            self,
            rank_number: int
    ) -> str:
        ic("Getting Pipe Type...")
        section: str = self.rank_settings(rank_number)
        field: str = "Pipe Type"
        pipe_type: str = str(self.config[section][field])
        ic("Pipe Type Retrieved.")
        return pipe_type

    #-------------------------------------------------------------------------------------------------------------------
    def pipe_type_set(
            self,
            rank_number: int,
            value: str
    ) -> None:
        ic("Setting Pipe Type...")
        section: str = self.rank_settings(rank_number)
        field: str = "Pipe Type"
        self.config[section][field] = value
        ic("Pipe Type Set.")

    #*******************************************************************************************************************
    # Starting Note
    #*******************************************************************************************************************
    def starting_note_get(
            self,
            rank_number: int
    ) -> str:
        ic("Getting Starting Note...")
        section: str = self.rank_settings(rank_number)
        field: str = "Starting Note"
        starting_note: str = str(self.config[section][field])
        ic("Starting Note Retrieved.")
        return starting_note

    #-------------------------------------------------------------------------------------------------------------------
    def starting_note_set(
            self,
            rank_number: int,
            starting_note: str,
            #values: tuple[str, ...]
    ) -> None:
        ic("Setting Starting Note...")
        section: str = self.rank_settings(rank_number)
        field: str = "Starting Note"
        self.config[section][field] = starting_note
        note_index: int = organlib.NOTES.index(starting_note)
        notes: tuple[str, ...] = organlib.NOTES[note_index:]
        number_pipes: int = len(notes)
        for pipe in range(1, number_pipes+1):
            self.note_set(rank_number, pipe, notes[pipe-1])
            self.relative_note_set(rank_number, pipe, notes[pipe-1])
        ic("Starting Note Set.")

    #*******************************************************************************************************************
    # Frequency Offset
    #*******************************************************************************************************************
    def frequency_offset_get(
            self,
            rank_number: int
    ) -> int:
        ic("Getting Frequency Offset...")
        section: str = self.rank_settings(rank_number)
        field: str = "Frequency Offset"
        frequency_offset: int = int(self.config[section][field])
        ic("Frequency Offset Retrieved.")
        return frequency_offset

    #-------------------------------------------------------------------------------------------------------------------
    def frequency_offset_set(
            self,
            rank_number: int,
            value: int
    ) -> None:
        ic("Setting Frequency Offset...")
        section: str = self.rank_settings(rank_number)
        field: str = "Frequency Offset"
        self.config[section][field] = value
        ic("Frequency Offset Set.")

    #*******************************************************************************************************************
    # Number of Harmonics
    #*******************************************************************************************************************
    def number_harmonics_get(
            self,
            rank_number: int
    ) -> int:
        ic("Getting Number of Harmonics...")
        section: str = self.rank_settings(rank_number)
        field: str = "Number of Harmonics"
        number_harmonics: int = int(self.config[section][field])
        ic("Number of Harmonics Retrieved.")
        return number_harmonics

    #-------------------------------------------------------------------------------------------------------------------
    def number_harmonics_set(
            self,
            rank_number: int,
            value: int
    ) -> None:
        ic("Setting Number of Harmonics...")
        section: str = self.rank_settings(rank_number)
        field: str = "Number of Harmonics"
        number_harmonic_sections: int = self.number_harmonics_get(rank_number)
        number_pipes: int = self.number_pipes_get(rank_number)
        if value > number_harmonic_sections:
            for harmonic in range(number_harmonic_sections+1, value+1):
                for pipe in range(1, number_pipes+1):
                    self.init_harmonic_config(rank_number, pipe, harmonic)
        elif value < number_harmonic_sections:
            for harmonic in range(
                value+1, number_harmonic_sections+1
            ):
                self.del_harmonic_settings(rank_number, harmonic)
        self.config[section][field] = value
        ic("Number of Harmonics Set.")

    #*******************************************************************************************************************
    # Rank Harmonic Amplitude
    #*******************************************************************************************************************
    def rank_harmonic_amplitude_get(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> int:
        ic("Getting Rank Harmonic Amplitude...")
        section: str = self.rank_harmonics_settings(rank_number, harmonic_number)
        field: str = "Amplitude"
        rank_harmonic_amplitude: int = int(self.config[section][field])
        ic("Rank Harmonic Amplitude Retrieved.")
        return rank_harmonic_amplitude

    #-------------------------------------------------------------------------------------------------------------------
    def rank_harmonic_amplitude_set(
            self,
            rank_number: int,
            harmonic_number: int,
            value: int
    ) -> None:
        ic("Setting Rank Harmonic Amplitude...")
        section: str = self.rank_harmonics_settings(rank_number, harmonic_number)
        field: str = "Amplitude"
        self.config[section][field] = value
        ic("Rank Harmonic Amplitude Set.")

    #*******************************************************************************************************************
    # Rank Harmonic Attack Time
    #*******************************************************************************************************************
    def rank_harmonic_attack_time_get(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> int:
        ic("Getting Rank Harmonic Attack Time...")
        section: str = self.rank_harmonics_adsr_settings(rank_number, harmonic_number)
        field: str = "Attack Time"
        rank_harmonic_attack_time: int = int(self.config[section][field])
        ic("Rank Harmonic Attack Time Retrieved.")
        return rank_harmonic_attack_time

    #-------------------------------------------------------------------------------------------------------------------
    def rank_harmonic_attack_time_set(
            self,
            rank_number: int,
            harmonic_number: int,
            value: int
    ) -> None:
        ic("Setting Rank Harmonic Attack Time...")
        section: str = self.rank_harmonics_adsr_settings(rank_number, harmonic_number)
        field: str = "Attack Time"
        self.config[section][field] = value
        ic("Rank Harmonic Attack Time Set.")

    #*******************************************************************************************************************
    # Rank Harmonic Decay Time
    #*******************************************************************************************************************
    def rank_harmonic_decay_time_get(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> int:
        ic("Getting Rank Harmonic Decay Time...")
        section: str = self.rank_harmonics_adsr_settings(rank_number, harmonic_number)
        field: str = "Decay Time"
        rank_harmonic_decay_time: int = int(self.config[section][field])
        ic("Rank Harmonic Decay Time Retrieved.")
        return rank_harmonic_decay_time

    #-------------------------------------------------------------------------------------------------------------------
    def rank_harmonic_decay_time_set(
            self,
            rank_number: int,
            harmonic_number: int,
            value: int
    ) -> None:
        ic("Setting Rank Harmonic Decay Time...")
        section: str = self.rank_harmonics_adsr_settings(rank_number, harmonic_number)
        field: str = "Decay Time"
        self.config[section][field] =  value
        ic("Rank Harmonic Decay Time Set.")

    #*******************************************************************************************************************
    # Rank Harmonic Sustain Level
    #*******************************************************************************************************************
    def rank_harmonic_sustain_level_get(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> int:
        ic("Getting Rank Harmonic Sustain Level...")
        section: str = self.rank_harmonics_adsr_settings(rank_number, harmonic_number)
        field: str = "Sustain Level"
        rank_harmonic_sustain_level: int = int(self.config[section][field])
        ic("Rank Harmonic Sustain Level Retrieved.")
        return rank_harmonic_sustain_level

    #-------------------------------------------------------------------------------------------------------------------
    def rank_harmonic_sustain_level_set(
            self,
            rank_number: int,
            harmonic_number: int,
            value: int
    ) -> None:
        ic("Setting Rank Harmonic Sustain Level...")
        section: str = self.rank_harmonics_adsr_settings(rank_number, harmonic_number)
        field: str = "Sustain Level"
        self.config[section][field] = value
        ic("Rank Harmonic Sustain Level Set.")

    #*******************************************************************************************************************
    # Rank Harmonic Release Time
    #*******************************************************************************************************************
    def rank_harmonic_release_time_get(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> int:
        ic("Getting Rank Harmonic Release Time...")
        section: str = self.rank_harmonics_adsr_settings(rank_number, harmonic_number)
        field: str = "Release Time"
        rank_harmonic_release_time: int = int(self.config[section][field])
        ic("Rank Harmonic Release Time Retrieved.")
        return rank_harmonic_release_time

    #-------------------------------------------------------------------------------------------------------------------
    def rank_harmonic_release_time_set(
            self,
            rank_number: int,
            harmonic_number: int,
            value: int
    ) -> None:
        ic("Setting Rank Harmonic Release Time...")
        section: str = self.rank_harmonics_adsr_settings(rank_number, harmonic_number)
        field: str = "Release Time"
        self.config[section][field] = value
        ic("Rank Harmonic Release Time Set.")

    #*******************************************************************************************************************
    # Rank Attack Time
    #*******************************************************************************************************************
    def rank_attack_time_get(
            self,
            rank_number: int
    ) -> int:
        ic("Getting Rank Attack Time...")
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Attack Time"
        rank_attack_time: int = int(self.config[section][field])
        ic("Rank Attack Time Retrieved.")
        return rank_attack_time

    #-------------------------------------------------------------------------------------------------------------------
    def rank_attack_time_set(
            self,
            rank_number: int,
            value: int
    ) -> None:
        ic("Setting Rank Attack Time...")
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Attack Time"
        self.config[section][field] = value
        ic("Rank Attack Time Set.")

    #*******************************************************************************************************************
    # Rank Decay Time
    #*******************************************************************************************************************
    def rank_decay_time_get(
            self,
            rank_number: int
    ) -> int:
        ic("Getting Rank Decay Time...")
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Decay Time"
        rank_decay_time: int = int(self.config[section][field])
        ic("Rank Decay Time Retrieved.")
        return rank_decay_time

    #-------------------------------------------------------------------------------------------------------------------
    def rank_decay_time_set(
            self,
            rank_number: int,
            value: int
    ) -> None:
        ic("Setting Rank Decay Time...")
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Decay Time"
        self.config[section][field] = value
        ic("Rank Decay Time Set.")

    #*******************************************************************************************************************
    # Rank Sustain Level
    #*******************************************************************************************************************
    def rank_sustain_level_get(
            self,
            rank_number: int
    ) -> int:
        ic("Getting Rank Sustain Level...")
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Sustain Level"
        rank_sustain_level: int = int(self.config[section][field])
        ic("Rank Sustain Level Retrieved.")
        return rank_sustain_level

    #-------------------------------------------------------------------------------------------------------------------
    def rank_sustain_level_set(
            self,
            rank_number: int,
            value: int
    ) -> None:
        ic("Setting Rank Sustain Level...")
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Sustain Level"
        self.config[section][field] = value
        ic("Rank Sustain Level Set.")

    #*******************************************************************************************************************
    # Rank Release Time
    #*******************************************************************************************************************
    def rank_release_time_get(
            self,
            rank_number: int
    ) -> int:
        ic("Getting Rank Release Time...")
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Release Time"
        rank_release_time: int = int(self.config[section][field])
        ic("Rank Release Time Retrieved.")
        return rank_release_time

    #-------------------------------------------------------------------------------------------------------------------
    def rank_release_time_set(
            self,
            rank_number: int,
            value: int
    ) -> None:
        ic("Setting Rank Release Time...")
        section: str = self.rank_adsr_settings(rank_number)
        field: str = "Release Time"
        self.config[section][field] = value
        ic("Rank Release Time Set.")

    #*******************************************************************************************************************
    # Note
    #*******************************************************************************************************************
    def note_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> str:
        ic("Getting Note...")
        section: str = self.pipe_settings(rank_number, pipe_number)
        field: str = "Note"
        note: str = str(self.config[section][field])
        ic("Note Retrieved.")
        return note

    #-------------------------------------------------------------------------------------------------------------------
    def note_set(
            self,
            rank_number: int,
            pipe_number: int,
            value: str
    ) -> None:
        ic("Setting Note...")
        section: str = self.pipe_settings(rank_number, pipe_number)
        field: str = "Note"
        self.config[section][field] = value
        ic("Note Set.")

    #*******************************************************************************************************************
    # Relative Note
    #*******************************************************************************************************************
    def relative_note_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> str:
        ic("Getting Relative Note...")
        section: str = self.pipe_settings(rank_number, pipe_number)
        field: str = "Relative Note"
        relative_note: str = str(self.config[section][field])
        ic("Relative Note Retrieved.")
        return relative_note

    #-------------------------------------------------------------------------------------------------------------------
    def relative_note_set(
            self,
            rank_number: int,
            pipe_number: int,
            value: str,
    ) -> None:
        ic("Setting Relative Note...")
        section: str = self.pipe_settings(rank_number, pipe_number)
        field: str = "Relative Note"
        self.config[section][field] = value
        ic("Relative Note Set.")

    #*******************************************************************************************************************
    # Pipe Harmonic Amplitude
    #*******************************************************************************************************************
    def pipe_harmonic_amplitude_get(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> int:
        ic("Getting Pipe Harmonic Amplitude...")
        section: str = self.pipe_harmonics_settings(rank_number, pipe_number, harmonic_number)
        field: str = "Amplitude"
        pipe_harmonic_amplitude: int = int(self.config[section][field])
        ic("Pipe Harmonic Amplitude Retrieved.")
        return pipe_harmonic_amplitude

    #-------------------------------------------------------------------------------------------------------------------
    def pipe_harmonic_amplitude_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            value: int
    ) -> None:
        ic("Setting Pipe Harmonic Amplitude...")
        section: str = self.pipe_harmonics_settings(rank_number, pipe_number, harmonic_number)
        field: str = "Amplitude"
        self.config[section][field] = value
        ic("Pipe Harmonic Amplitude Set.")

    #*******************************************************************************************************************
    # Pipe Harmonic Attack Time
    #*******************************************************************************************************************
    def pipe_harmonic_attack_time_get(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> int:
        ic("Getting Pipe Harmonic Attack Time...")
        section: str = self.pipe_harmonics_adsr_settings(rank_number, pipe_number, harmonic_number)
        field: str = "Attack Time"
        pipe_harmonic_attack_time: int = int(self.config[section][field])
        ic("Pipe Harmonic Attack Time Retrieved.")
        return pipe_harmonic_attack_time

    #-------------------------------------------------------------------------------------------------------------------
    def pipe_harmonic_attack_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            value: int
    ) -> None:
        ic("Setting Pipe Harmonic Attack Time...")
        section: str = self.pipe_harmonics_adsr_settings(rank_number, pipe_number, harmonic_number)
        field: str = "Attack Time"
        self.config[section][field] = value
        ic("Pipe Harmonic Attack Time Set.")

    #*******************************************************************************************************************
    # Pipe Harmonic Decay Time
    #*******************************************************************************************************************
    def pipe_harmonic_decay_time_get(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> int:
        ic("Getting Pipe Harmonic Decay Time...")
        section: str = self.pipe_harmonics_adsr_settings(rank_number, pipe_number, harmonic_number)
        field: str = "Decay Time"
        pipe_harmonic_decay_time: int = int(self.config[section][field])
        ic("Pipe Harmonic Decay Time Retrieved.")
        return pipe_harmonic_decay_time

    #-------------------------------------------------------------------------------------------------------------------
    def pipe_harmonic_decay_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            value: int
    ) -> None:
        ic("Setting Pipe Harmonic Decay Time...")
        section: str = self.pipe_harmonics_adsr_settings(rank_number, pipe_number, harmonic_number)
        field: str = "Decay Time"
        self.config[section][field] = value
        ic("Pipe Harmonic Decay Time Set.")

    #*******************************************************************************************************************
    # Pipe Harmonic Sustain Level
    #*******************************************************************************************************************
    def pipe_harmonic_sustain_level_get(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> int:
        ic("Getting Pipe Harmonic Sustain Level...")
        section: str = self.pipe_harmonics_adsr_settings(rank_number, pipe_number, harmonic_number)
        field: str = "Sustain Level"
        pipe_harmonic_sustain_level: int = int(self.config[section][field])
        ic("Pipe Harmonic Sustain Level Retrieved.")
        return pipe_harmonic_sustain_level

    #-------------------------------------------------------------------------------------------------------------------
    def pipe_harmonic_sustain_level_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            value: int
    ) -> None:
        ic("Setting Pipe Harmonic Sustain Level...")
        section: str = self.pipe_harmonics_adsr_settings(rank_number, pipe_number, harmonic_number)
        field: str = "Sustain Level"
        self.config[section][field] = value
        ic("Pipe Harmonic Sustain Level Set.")

    #*******************************************************************************************************************
    # Pipe Harmonic Release Time
    #*******************************************************************************************************************
    def pipe_harmonic_release_time_get(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> int:
        ic("Getting Pipe Harmonic Release Time...")
        section: str = self.pipe_harmonics_adsr_settings(rank_number, pipe_number, harmonic_number)
        field: str = "Release Time"
        pipe_harmonic_release_time: int = int(self.config[section][field])
        ic("Pipe Harmonic Release Time Retrieved.")
        return pipe_harmonic_release_time

    #-------------------------------------------------------------------------------------------------------------------
    def pipe_harmonic_release_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            value: int
    ) -> None:
        ic("Getting Pipe Harmonic Release Time...")
        section: str = self.pipe_harmonics_adsr_settings(rank_number, pipe_number, harmonic_number)
        field: str = "Release Time"
        self.config[section][field] = value
        ic("Pipe Harmonic Release Time Set.")

    #*******************************************************************************************************************
    # Pipe Attack Time
    #*******************************************************************************************************************
    def pipe_attack_time_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> int:
        ic("Getting Pipe Attack Time...")
        section: str = self.pipe_adsr_settings(rank_number, pipe_number)
        field: str = "Attack Time"
        pipe_attack_time: int = int(self.config[section][field])
        ic("Pipe Attack Time Retrieved.")
        return pipe_attack_time

    #-------------------------------------------------------------------------------------------------------------------
    def pipe_attack_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            value: int
    ) -> None:
        ic("Setting Pipe Attack Time...")
        section: str = self.pipe_adsr_settings(rank_number, pipe_number)
        field: str = "Attack Time"
        self.config[section][field] = value
        ic("Pipe Attack Time Set.")

    #*******************************************************************************************************************
    # Pipe Decay Time
    #*******************************************************************************************************************
    def pipe_decay_time_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> int:
        ic("Getting Pipe Decay Time...")
        section: str = self.pipe_adsr_settings(rank_number, pipe_number)
        field: str = "Decay Time"
        pipe_decay_time: int = int(self.config[section][field])
        ic("Pipe Decay Time Retrieved.")
        return pipe_decay_time

    #-------------------------------------------------------------------------------------------------------------------
    def pipe_decay_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            value: int
    ) -> None:
        ic("Setting Pipe Decay Time...")
        section: str = self.pipe_adsr_settings(rank_number, pipe_number)
        field: str = "Decay Time"
        self.config[section][field] = value
        ic("Pipe Decay Time Set.")

    #*******************************************************************************************************************
    # Pipe Sustain Level
    #*******************************************************************************************************************
    def pipe_sustain_level_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> int:
        ic("Getting Pipe Sustain Level...")
        section: str = self.pipe_adsr_settings(rank_number, pipe_number)
        field: str = "Sustain Level"
        pipe_sustain_level: int = int(self.config[section][field])
        ic("Pipe Sustain Level Retrieved.")
        return pipe_sustain_level

    #-------------------------------------------------------------------------------------------------------------------
    def pipe_sustain_level_set(
            self,
            rank_number: int,
            pipe_number: int,
            value: int
    ) -> None:
        ic("Setting Pipe Sustain Level...")
        section: str = self.pipe_adsr_settings(rank_number, pipe_number)
        field: str = "Sustain Level"
        self.config[section][field] = value
        ic("Pipe Sustain Level Set.")

    #*******************************************************************************************************************
    # Pipe Release Time
    #*******************************************************************************************************************
    def pipe_release_time_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> int:
        ic("Getting Pipe Release Time...")
        section: str = self.pipe_adsr_settings(rank_number, pipe_number)
        field: str = "Release Time"
        pipe_release_time: int = int(self.config[section][field])
        ic("Pipe Release Time Retrieved.")
        return pipe_release_time

    #-------------------------------------------------------------------------------------------------------------------
    def pipe_release_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            value: int
    ) -> None:
        ic("Setting Pipe Release Time...")
        section: str = self.pipe_adsr_settings(rank_number, pipe_number)
        field: str = "Release Time"
        self.config[section][field] = value
        ic("Pipe Release Time Set.")

    #*******************************************************************************************************************
    # Sections
    #*******************************************************************************************************************
    @property
    def stop_settings(self) -> str:
        section: str = "Stop Settings"
        return section

    #-------------------------------------------------------------------------------------------------------------------
    def rank_settings(
            self,
            rank_number: int
    ) -> str:
        section: str = f"Rank {rank_number} Settings"
        return section

    #-------------------------------------------------------------------------------------------------------------------
    def rank_harmonics_settings(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - Harmonic {harmonic_number} Settings"
        return section

    #-------------------------------------------------------------------------------------------------------------------
    def rank_harmonics_adsr_settings(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> str:
        rank: str = f"Rank {rank_number}"
        harmonics: str = f"Harmonic {harmonic_number}"
        section: str = f"{rank} - {harmonics} - ADSR Settings"
        return section

    #-------------------------------------------------------------------------------------------------------------------
    def rank_adsr_settings(
            self,
            rank_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - ADSR Settings"
        return section

    #-------------------------------------------------------------------------------------------------------------------
    def pipe_settings(
            self,
            rank_number: int,
            pipe_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} Settings"
        return section

    #-------------------------------------------------------------------------------------------------------------------
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
        return section

    #-------------------------------------------------------------------------------------------------------------------
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
        return section

    #-------------------------------------------------------------------------------------------------------------------
    def pipe_adsr_settings(
            self,
            rank_number: int,
            pipe_number: int
    ) -> str:
        rank: str = f"Rank {rank_number}"
        pipe: str = f"Pipe {pipe_number}"
        section: str = f"{rank} - {pipe} - ADSR Settings"
        return section


#=======================================================================================================================
# Executable
#=======================================================================================================================
if __name__ == "__main__":
    stop_config: StopConfig = StopConfig()
    stop_config.load_file("src/config/stops/AEOLINE 8'.json")
