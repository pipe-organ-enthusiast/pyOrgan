from configparser import ConfigParser


class StopConfig:
    def __init__(self, file) -> None:
        self.configfile: str = file
        self.parser: ConfigParser = ConfigParser()

    #**************************************************************************
    # File Operations
    #**************************************************************************
    def load_file(self) -> None:
        self.parser.read(self.configfile)

    def save_file(self) -> None:
        with open(self.configfile, "w") as file:
            self.parser.write(file)

    #**************************************************************************
    # Section Creation
    #**************************************************************************
    #==========================================================================
    # Stop Settings
    #==========================================================================
    def init_stopsettings(self) -> None: 
        self.parser["Stop Settings"] = {
            "stop name": "",
            "stop family": "",
            "organ division": "",
            "number of ranks": "",
            "rank series": ""
        }

    #==========================================================================
    # Rank Settings
    #==========================================================================
    def init_rank_settings(self, rank_number: int) -> None:
        section: str = f"Rank {rank_number} Settings"
        self.parser[section] = {
            "rank size": "",
            "number of pipes": "",
            "pipe type": "",
            "starting note": "",
            "frequency offset": "",
            "number of harmonics": ""
        }

    def init_rank_harmonic_settings(
            self, 
            rn: int,  # Rank Number 
            hn: int   # Harmonic Number
    ) -> None:
        section: str = f"Rank {rn} - Harmonic {hn} Settings"
        self.parser[section] = {
            "amplitude": ""
        }

    def init_rank_harmonic_adsr_settings(
            self,
            rn: int,  # Rank Number
            hn: int   # Harmonic Number
    ) -> None:
        section: str = f"Rank {rn} - Harmonic {hn} - ADSR Settings"
        self.parser[section] = {
            "attack time": "",
            "decay time": "",
            "sustain level": "",
            "release time": ""
        }

    def init_rank_adsr_settings(self, rank_number: int) -> None:
        section: str = f"Rank {rank_number} - ADSR Settings"
        self.parser[section] = {
            "attack time": "",
            "decay time": "",
            "sustain level": "",
            "release time": ""
        }

    #==========================================================================
    # Pipe Settings
    #==========================================================================
    def init_pipe_settings(
            self,
            rank_number: int,
            pipe_number: int
    ) -> None:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} Settings"
        self.parser[section] = {
            "note": "",
            "relative note": ""
        }

    def init_pipe_harmonic_settings(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> None:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} - Harmonic \
            {harmonic_number} Settings"
        self.parser[section] = {
            "amplitude": ""
        }

    def init_pipe_harmonic_adsr_settings(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> None:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} - Harmonic \
            {harmonic_number} - ADSR Settings"
        self.parser[section] = {
            "Attack Time": "",
            "Decay Time": "",
            "Sustain Level": "",
            "Release Time": ""
        }

    def init_pipe_adsr_settings(
            self,
            rank_number: int,
            pipe_number: int,
    ) -> None:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} \
            - ADSR Settings"
        self.parser[section] = {
            "Attack Time": "",
            "Decay Time": "",
            "Sustain Level": "",
            "Release Time": ""
        }

    #**************************************************************************
    # Field Operations
    #**************************************************************************
    #==========================================================================
    # Stop Settings
    #==========================================================================
    #--------------------------------------------------------------------------
    # Stop Name
    #--------------------------------------------------------------------------
    def stop_name_get(self) -> str:
        section: str = "Stop Settings"
        field: str = "stop name"
        return self.parser[section][field]

    def stop_name_set(
            self, 
            stop_name: str
    ) -> None:
        section: str = "Stop Settings"
        field: str = "stop name"
        self.parser[section][field] = stop_name

    #--------------------------------------------------------------------------
    # Stop Family
    #--------------------------------------------------------------------------
    def stop_family_get(self) -> str:
        section: str = "Stop Settings"
        field: str = "stop family"
        return self.parser[section][field]

    def stop_family_set(
            self,
            stop_family: str
    ) -> None:
        section: str = "Stop Settings"
        field: str = "stop family"
        self.parser[section][field] = stop_family

    #--------------------------------------------------------------------------
    # Organ Division
    #--------------------------------------------------------------------------
    def organ_division_get(self) -> str:
        section: str = "Stop Settings"
        field: str = "organ division"
        return self.parser[section][field]

    def organ_division_set(
            self,
            organ_division: str
    ) -> None:
        section: str = "Stop Settings"
        field: str = "organ division"
        self.parser[section][field] = organ_division

    #--------------------------------------------------------------------------
    # Number of Ranks
    #--------------------------------------------------------------------------
    def number_ranks_get(self) -> str:
        section: str = "Stop Settings"
        field: str = "number of ranks"
        return self.parser[section][field]

    def number_ranks_set(
            self,
            number_ranks: str
    ) -> None:
        section: str = "Stop Settings"
        field: str = "number of ranks"
        self.parser[section][field] = number_ranks

    #--------------------------------------------------------------------------
    # Rank Series
    #--------------------------------------------------------------------------
    def rank_series_get(self) -> str:
        section: str = "Stop Settings"
        field: str = "rank series"
        return self.parser[section][field]

    def rank_series_set(
            self,
            rank_series: str
    ) -> None:
        section: str = "Stop Settings"
        field: str = "rank series"
        self.parser[section][field] = rank_series

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
        field: str = "rank size"
        return self.parser[section][field]

    def rank_size_set(
            self,
            rank_number: int,
            rank_size: str
    ) -> None:
        section: str = f"Rank {rank_number} Settings"
        field: str = "rank size"
        self.parser[section][field] = rank_size

    #--------------------------------------------------------------------------
    # Number of Pipes
    #--------------------------------------------------------------------------
    def number_pipes_get(
            self,
            rank_number: int
    ) -> str:
        section: str = f"Rank {rank_number} Settings"
        field: str = "number of pipes"
        return self.parser[section][field]

    def number_pipes_set(
            self, 
            rank_number: int, 
            number_pipes: str
    ) -> None:
        section: str = f"Rank {rank_number} Settings"
        field: str = "number of pipes"
        self.parser[section][field] = number_pipes

    #--------------------------------------------------------------------------
    # Pipe Type
    #--------------------------------------------------------------------------
    def pipe_type_get(
            self, 
            rank_number: int
    ) -> str:
        section: str = f"Rank {rank_number} Settings"
        field: str = "pipe type"
        return self.parser[section][field]

    def pipe_type_set(
            self, 
            rank_number: int, 
            pipe_type: str
    ) -> None:
        section: str = f"Rank {rank_number} Settings"
        field: str = "pipe type"
        self.parser[section][field] = pipe_type

    #--------------------------------------------------------------------------
    # Starting Note
    #--------------------------------------------------------------------------
    def starting_note_get(
            self, 
            rank_number: int
    ) -> str:
        section: str = f"Rank {rank_number} Settings"
        field: str = "starting note"
        return self.parser[section][field]

    def starting_note_set(
            self, 
            rank_number: int, 
            starting_note: str
    ) -> None:
        section: str = f"Rank {rank_number} Settings"
        field: str = "starting note"
        self.parser[section][field] = starting_note

    #--------------------------------------------------------------------------
    # Frequency Offset
    #--------------------------------------------------------------------------
    def frequency_offset_get(
            self, 
            rank_number: int
    ) -> str:
        section: str = f"Rank {rank_number} Settings"
        field: str = "frequency offset"
        return self.parser[section][field]

    def frequency_offset_set(
            self, 
            rank_number: int, 
            frequency_offset: str
    ) -> None:
        section: str = f"Rank {rank_number} Settings"
        field: str = "frequency offset"
        self.parser[section][field] = frequency_offset

    #--------------------------------------------------------------------------
    # Number of Harmonics
    #--------------------------------------------------------------------------
    def number_harmonics_get(
            self, 
            rank_number: int
    ) -> str:
        section: str = f"Rank {rank_number} Settings"
        field: str = "number of harmonics"
        return self.parser[section][field]

    def number_harmonics_set(
            self, 
            rank_number: int, 
            number_harmonics: str
    ) -> None:
        section: str = f"Rank {rank_number} Settings"
        field: str = "number of harmonics"
        self.parser[section][field] = number_harmonics

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
    ) -> str:
        section: str = f"Rank {rank_number} - Harmonic {harmonic_number} \
            Settings"
        field: str = "amplitude"
        return self.parser[section][field]

    def rank_harmonic_amplitude_set(
            self,
            rank_number: int,
            harmonic_number: int,
            amplitude: str
    ) -> None:
        section: str = f"Rank {rank_number} - Harmonic {harmonic_number} \
            Settings"
        field: str = "amplitude"
        self.parser[section][field] = amplitude

    #--------------------------------------------------------------------------
    # ADSR Settings
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    # Attack Time
    #--------------------------------------------------------------------------
    def rank_harmonic_adsr_attack_time_get(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - Harmonic {harmonic_number} \
            - ADSR Settings"
        field: str = "attack time"
        return self.parser[section][field]

    def rank_harmonic_adsr_attack_time_set(
            self,
            rank_number: int,
            harmonic_number: int,
            attack_time: str
    ) -> None:
        section: str = f"Rank {rank_number} - Harmonic {harmonic_number} \
            - ADSR Settings"
        field: str = "attack time"
        self.parser[section][field] = attack_time

    #--------------------------------------------------------------------------
    # Decay Time
    #--------------------------------------------------------------------------
    def rank_harmonic_adsr_decay_time_get(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - Harmonic {harmonic_number} \
            - ADSR Settings"
        field: str = "decay time"
        return self.parser[section][field]

    def rank_harmonic_adsr_decay_time_set(
            self,
            rank_number: int,
            harmonic_number: int,
            decay_time: str
    ) -> None:
        section: str = f"Rank {rank_number} - Harmonic {harmonic_number} \
            - ADSR Settings"
        field: str = "decay time"
        self.parser[section][field] = decay_time

    #--------------------------------------------------------------------------
    # Sustain Level
    #--------------------------------------------------------------------------
    def rank_harmonic_adsr_sustain_level_get(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - Harmonic {harmonic_number} \
            - ADSR Settings"
        field: str = "sustain level"
        return self.parser[section][field]

    def rank_harmonic_adsr_sustain_level_set(
            self,
            rank_number: int,
            harmonic_number: int,
            sustain_level: str
    ) -> None:
        section: str = f"Rank {rank_number} - Harmonic {harmonic_number} \
            - ADSR Settings"
        field: str = "sustain level"
        self.parser[section][field] = sustain_level

    #--------------------------------------------------------------------------
    # Release Time
    #--------------------------------------------------------------------------
    def rank_harmonic_adsr_release_time_get(
            self,
            rank_number: int,
            harmonic_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - Harmonic {harmonic_number} \
            - ADSR Settings"
        field: str = "release time"
        return self.parser[section][field]

    def rank_harmonic_adsr_release_time_set(
            self,
            rank_number: int,
            harmonic_number: int,
            release_time: str
    ) -> None:
        section: str = f"Rank {rank_number} - Harmonic {harmonic_number} \
            - ADSR Settings"
        field: str = "release time"
        self.parser[section][field] = release_time

    #==========================================================================
    # Rank ADSR Settings
    #==========================================================================
    #--------------------------------------------------------------------------
    # Attack Time
    #--------------------------------------------------------------------------
    def rank_adsr_attack_time_get(
            self,
            rank_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - ADSR Settings"
        field: str = "attack time"
        return self.parser[section][field]

    def rank_adsr_attack_time_set(
            self,
            rank_number: int,
            attack_time: str
    ) -> None:
        section: str = f"Rank {rank_number} - ADSR Settings"
        field: str = "attack time"
        self.parser[section][field] = attack_time

    #--------------------------------------------------------------------------
    # Decay Time
    #--------------------------------------------------------------------------
    def rank_adsr_decay_time_get(
            self,
            rank_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - ADSR Settings"
        field: str = "decay time"
        return self.parser[section][field]

    def rank_adsr_decay_time_set(
            self,
            rank_number: int,
            decay_time: str
    ) -> None:
        section: str = f"Rank {rank_number} - ADSR Settings"
        field: str = "decay time"
        self.parser[section][field] = decay_time

    #--------------------------------------------------------------------------
    # Sustain Level
    #--------------------------------------------------------------------------
    def rank_adsr_sustain_level_get(
            self,
            rank_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - ADSR Settings"
        field: str = "sustain level"
        return self.parser[section][field]

    def rank_adsr_sustain_level_set(
            self,
            rank_number: int,
            sustain_level: str
    ) -> None:
        section: str = f"Rank {rank_number} - ADSR Settings"
        field: str = "sustain level"
        self.parser[section][field] = sustain_level

    #--------------------------------------------------------------------------
    # Release Time
    #--------------------------------------------------------------------------
    def rank_adsr_release_time_get(
            self,
            rank_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - ADSR Settings"
        field: str = "release time"
        return self.parser[section][field]

    def rank_adsr_release_time_set(
            self,
            rank_number: int,
            release_time: str
    ) -> None:
        section: str = f"Rank {rank_number} - ADSR Settings"
        field: str = "release time"
        self.parser[section][field] = release_time

    #==========================================================================
    # Pipe Settings
    #==========================================================================
    #--------------------------------------------------------------------------
    # Note
    #--------------------------------------------------------------------------
    def pipe_note_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} Settings"
        field: str = "note"
        return self.parser[section][field]

    def pipe_note_set(
            self,
            rank_number: int,
            pipe_number: int,
            note: str
    ) -> None:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} Settings"
        field: str = "note"
        self.parser[section][field] = note

    #--------------------------------------------------------------------------
    # Relative Note
    #--------------------------------------------------------------------------
    def pipe_relative_note_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} Settings"
        field: str = "relative note"
        return self.parser[section][field]

    def pipe_relative_note_set(
            self,
            rank_number: int,
            pipe_number: int,
            relative_note: str
    ) -> None:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} Settings"
        field: str = "relative note"
        self.parser[section][field] = relative_note

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
    ) -> str:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} - Harmonic \
            {harmonic_number} Settings"
        field: str = "amplitude"
        return self.parser[section][field]

    def pipe_harmonic_amplitude_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            amplitude: str
    ) -> None:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} - Harmonic \
            {harmonic_number} Settings"
        field: str = "amplitude"
        self.parser[section][field] = amplitude

    #--------------------------------------------------------------------------
    # ADSR Settings
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    # Attack Time
    #--------------------------------------------------------------------------
    def pipe_harmonic_adsr_attack_time_get(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} - Harmonic \
            {harmonic_number} - ADSR Settings"
        field: str = "Attack Time"
        return self.parser[section][field]

    def pipe_harmonic_adsr_attack_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            attack_time: str
    ) -> None:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} - Harmonic \
            {harmonic_number} - ADSR Settings"
        field: str = "Attack Time"
        self.parser[section][field] = attack_time

    #--------------------------------------------------------------------------
    # Decay Time
    #--------------------------------------------------------------------------
    def pipe_harmonic_adsr_decay_time_get(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} - Harmonic \
            {harmonic_number} - ADSR Settings"
        field: str = "Decay Time"
        return self.parser[section][field]

    def pipe_harmonic_adsr_decay_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            decay_time: str
    ) -> None:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} - Harmonic \
            {harmonic_number} - ADSR Settings"
        field: str = "Decay Time"
        self.parser[section][field] = decay_time

    #--------------------------------------------------------------------------
    # Sustain Level
    #--------------------------------------------------------------------------
    def pipe_harmonic_adsr_sustain_level_get(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} - Harmonic \
            {harmonic_number} - ADSR Settings"
        field: str = "Sustain Level"
        return self.parser[section][field]

    def pipe_harmonic_adsr_sustain_level_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            sustain_level: str
    ) -> None:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} - Harmonic \
            {harmonic_number} - ADSR Settings"
        field: str = "Sustain Level"
        self.parser[section][field] = sustain_level

    #--------------------------------------------------------------------------
    # Release Time
    #--------------------------------------------------------------------------
    def pipe_harmonic_adsr_release_time_get(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} - Harmonic \
            {harmonic_number} - ADSR Settings"
        field: str = "Release Time"
        return self.parser[section][field]

    def pipe_harmonic_adsr_release_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            harmonic_number: int,
            release_time: str
    ) -> None:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} - Harmonic \
            {harmonic_number} - ADSR Settings"
        field: str = "Release Time"
        self.parser[section][field] = release_time

    #==========================================================================
    # Pipe ADSR Settings
    #==========================================================================
    #--------------------------------------------------------------------------
    # Attack Time
    #--------------------------------------------------------------------------
    def pipe_adsr_attack_time_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} \
            - ADSR Settings"
        field: str = "Attack Time"
        return self.parser[section][field]

    def pipe_adsr_attack_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            attack_time: str
    ) -> None:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} \
            - ADSR Settings"
        field: str = "Attack Time"
        self.parser[section][field] = attack_time

    #--------------------------------------------------------------------------
    # Decay Time
    #--------------------------------------------------------------------------
    def pipe_adsr_decay_time_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} \
            - ADSR Settings"
        field: str = "Decay Time"
        return self.parser[section][field]

    def pipe_adsr_decay_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            decay_time: str
    ) -> None:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} \
            - ADSR Settings"
        field: str = "Decay Time"
        self.parser[section][field] = decay_time

    #--------------------------------------------------------------------------
    # Sustain Level
    #--------------------------------------------------------------------------
    def pipe_adsr_sustain_level_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} \
            - ADSR Settings"
        field: str = "Sustain Level"
        return self.parser[section][field]

    def pipe_adsr_sustain_level_set(
            self,
            rank_number: int,
            pipe_number: int,
            sustain_level: str
    ) -> None:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} \
            - ADSR Settings"
        field: str = "Sustain Level"
        self.parser[section][field] = sustain_level

    #--------------------------------------------------------------------------
    # Release Time
    #--------------------------------------------------------------------------
    def pipe_adsr_release_time_get(
            self,
            rank_number: int,
            pipe_number: int
    ) -> str:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} \
            - ADSR Settings"
        field: str = "Release Time"
        return self.parser[section][field]

    def pipe_adsr_release_time_set(
            self,
            rank_number: int,
            pipe_number: int,
            release_time: str
    ) -> None:
        section: str = f"Rank {rank_number} - Pipe {pipe_number} \
            - ADSR Settings"
        field: str = "Release Time"
        self.parser[section][field] = release_time
