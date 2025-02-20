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
        self.parser[f"Rank {rank_number} Settings"] = {
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
        self.parser[f"Rank {rn} - Harmonic {hn} Settings"] = {
            "amplitude": ""
        }

    def init_rank_harmonic_adsr_settings(
            self,
            rn: int,  # Rank Number
            hn: int   # Harmonic Number
    ) -> None:
        self.parser[f"Rank {rn} - Harmonic {hn} - ADSR Settings"] = {
            "attack time": "",
            "decay time": "",
            "sustain level": "",
            "release time": ""
        }

    def init_rank_adsr_settings(self, rank_number: int) -> None:
        self.parser[f"Rank {rank_number} - ADSR Settings"] = {
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
            rn: int,  # Rank Number
            pn: int   # Pipe Number
    ) -> None:
        self.parser[f"Rank {rn} - Pipe{pn} Settings"] = {
            "note": "",
            "relative note": ""
        }

    def init_pipe_harmonic_settings(
            self,
            rn: int,  # Rank Number
            pn: int,  # Pipe Number
            hn: int   # Harmonic Number
    ) -> None:
        self.parser[f"Rank {rn} - Pipe {pn} - Harmonic {hn} Settings"] = {
            "amplitude": ""
        }

    def init_pipe_harmonic_adsr_settings(
            self,
            rn: int,  # Rank Number
            pn: int,  # Pipe Number
            hn: int   # Harmonic Number
    ) -> None:
        self.parser[
            f"Rank {rn} - Pipe {pn} - Harmonic {hn} - ADSR Settings"
        ] = {
            "Attack Time": "",
            "Decay Time": "",
            "Sustain Level": "",
            "Release Time": ""
        }

    def init_pipe_adsr_settings(
            self,
            rn: int,  # Rank Number
            pn: int,  # Pipe Number
    ) -> None:
        self.parser[
            f"Rank {rn} - Pipe {pn} - ADSR Settings"
        ] = {
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
        return self.parser["Stop Settings"]["stop name"]

    def stop_name_set(self, stop_name: str) -> None:
        self.parser["Stop Settings"]["stop name"] = stop_name

    #--------------------------------------------------------------------------
    # Stop Family
    #--------------------------------------------------------------------------
    def stop_family_get(self) -> str:
        return self.parser["Stop Settings"]["stop family"]

    def stop_family_set(self, stop_family: str) -> None:
        self.parser["Stop Settings"]["stop family"] = stop_family

    #--------------------------------------------------------------------------
    # Organ Division
    #--------------------------------------------------------------------------
    def organ_division_get(self) -> str:
        return self.parser["Stop Settings"]["organ division"]

    def organ_division_set(self, organ_division: str) -> None:
        self.parser["Stop Settings"]["organ division"] = organ_division

    #--------------------------------------------------------------------------
    # Number of Ranks
    #--------------------------------------------------------------------------
