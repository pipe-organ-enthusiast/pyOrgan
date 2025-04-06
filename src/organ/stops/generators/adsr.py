"""ADSR Envelope Generator
ADSR - Attack, Decay, Release, Sustain
Attack - Starts when air enters the pipe, ends when peak sound reached
Decay - Starts when pipe reaches peak sound, ends when sound has "settled"
Sustain - Level at which sound settles in the pipe
Release - Starts when air stops flowing through the pipe
"""
#=======================================================================================================================
# Dependencies
#=======================================================================================================================
from typing import Self, Literal


#=======================================================================================================================
class ADSR:
    def __init__(
            self,
            attack_time: float,
            decay_time: float,
            sustain_level: float,
            release_time: float,
            samplerate: int
    ) -> None:
        self.attack_time = attack_time
        self.decay_time = decay_time
        self.sustain_level = sustain_level
        self.release_time = release_time
        self.samplerate = samplerate

    #===================================================================================================================
    # Generator Methods
    #===================================================================================================================
    def __iter__(self) -> Self:
        self.__value: float = self.MIN_LEVEL
        self.__phase: Literal[
            "ATTACK",
            "DECAY",
            "SUSTAIN",
            "RELEASE"
        ] = "ATTACK"
        return self

    #-------------------------------------------------------------------------------------------------------------------
    def __next__(self) -> float:
        min_level: float = self.MIN_LEVEL
        max_level: float = self.MAX_LEVEL
        modifier: float = self.__value
        match self.__phase:
            case "ATTACK":
                self.__value += self.__attack_modifier
                if self.__value >= max_level:
                    self.__value = max_level
                    self.__phase = "DECAY"
            case "DECAY":
                self.__value -= self.__decay_modifier
                if self.__value <= self.sustain_level:
                    self.__value = self.sustain_level
                    self.__phase = "SUSTAIN"
            case "SUSTAIN":
                self.__value = self.sustain_level
            case "RELEASE":
                self.__value -= self.__release_modifier
                if self.__value <= min_level:
                    self.__value = min_level
        return modifier

    #===================================================================================================================
    # Control Methods
    #===================================================================================================================
    def start_release(self) -> None:
        self.__reached_level: float = self.__value
        self.__phase = "RELEASE"

    #===================================================================================================================
    # Properties
    #===================================================================================================================
    #*******************************************************************************************************************
    # Levels
    #*******************************************************************************************************************
    @property
    def MIN_LEVEL(self) -> float:
        min_level: float = 0.0
        return min_level

    #-------------------------------------------------------------------------------------------------------------------
    @property
    def MAX_LEVEL(self) -> float:
        max_level: float = 1.0
        return max_level

    #*******************************************************************************************************************
    # Modifiers
    #*******************************************************************************************************************
    @property
    def __attack_modifier(self) -> float:
        attack_samples: float = self.attack_time * self.samplerate
        attack_modifier: float = self.MAX_LEVEL / attack_samples
        return attack_modifier

    #-------------------------------------------------------------------------------------------------------------------
    @property
    def __decay_modifier(self) -> float:
        decay_level: float = self.MAX_LEVEL - self.sustain_level
        decay_samples: float = self.decay_time * self.samplerate
        decay_modifier: float = decay_level / decay_samples
        return decay_modifier

    #-------------------------------------------------------------------------------------------------------------------
    @property
    def __release_modifier(self) -> float:
        level_ratio: float = self.__reached_level / self.sustain_level
        release_rate: float = self.release_time * self.samplerate
        release_samples: float = level_ratio * release_rate
        release_modifier: float = self.__reached_level / release_samples
        return release_modifier

    #*******************************************************************************************************************
    # Return Value, Phase from Generator
    #*******************************************************************************************************************
    @property
    def value(self) -> float:
        return self.__value

    #-------------------------------------------------------------------------------------------------------------------
    @property
    def phase(self) -> Literal["ATTACK", "DECAY", "SUSTAIN", "RELEASE"]:
        return self.__phase

    #*******************************************************************************************************************
    # Attack
    #*******************************************************************************************************************
    @property
    def attack_time(self) -> float:
        return self.__attack

    #-------------------------------------------------------------------------------------------------------------------
    @attack_time.setter
    def attack_time(self, value: float) -> None:
        self.__attack: float = abs(value)

    #*******************************************************************************************************************
    # Decay
    #*******************************************************************************************************************
    @property
    def decay_time(self) -> float:
        return self.__decay

    #-------------------------------------------------------------------------------------------------------------------
    @decay_time.setter
    def decay_time(self, value: float) -> None:
        self.__decay: float = abs(value)

    #*******************************************************************************************************************
    # Sustain
    #*******************************************************************************************************************
    @property
    def sustain_level(self) -> float:
        return self.__sustain_level

    #-------------------------------------------------------------------------------------------------------------------
    @sustain_level.setter
    def sustain_level(self, value: float) -> None:
        if value < self.MIN_LEVEL:
            value = self.MIN_LEVEL
        elif value > self.MAX_LEVEL:
            value = self.MAX_LEVEL
        self.__sustain_level: float = value

    #*******************************************************************************************************************
    # Release
    #*******************************************************************************************************************
    @property
    def release_time(self) -> float:
        return self.__release_time

    #-------------------------------------------------------------------------------------------------------------------
    @release_time.setter
    def release_time(self, value: float) -> None:
        self.__release_time: float = abs(value)

    #*******************************************************************************************************************
    # Samplerate
    #*******************************************************************************************************************
    @property
    def samplerate(self) -> int:
        return self.__samplerate

    #-------------------------------------------------------------------------------------------------------------------
    @samplerate.setter
    def samplerate(self, value: int) -> None:
        self.__samplerate: int = abs(value)
