from configparser import ConfigParser
import os


class GeneralOrganConfig:
    def __init__(self) -> None:
        self.parser = ConfigParser()

    def configfile_check(self) -> None:
        if os.path.exists(self.configfile):
            self.read_config()
        else:
            self.init_config()
            self.write_config()

    def init_config(self) -> None:
        general_organ_settings: str = "General Organ Settings"
        self.parser.add_section(general_organ_settings)
        section = self.parser[general_organ_settings]
        section["number divisions"] = "0"
        section["number generals"] = "0"

    def init_config_division_settings(
            self,
            division_num: int
    ) -> None:
        division_settings: str = f"Division {division_num} Settings"
        self.parser.add_section(division_settings)
        section = self.parser[division_settings]
        section["name"] = ""
        section["number of stops"] = "0"
        section["number of divisionals"] = "0"
        section["tremulant"] = "False"
        section["enclosed"] = "False"

    def read_config(self) -> None:
        self.parser.read(self.configfile)

    def write_config(self) -> None:
        with open(self.configfile, "w") as configfile:
            self.parser.write(configfile)

    @property
    def configfile(self) -> str:
        return "config/general_organ_config.ini"
