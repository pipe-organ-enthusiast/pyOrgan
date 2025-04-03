"""adsr.py
ADSR - Attack, Decay, Release, Sustain
Attack - Starts when air enters the pipe, ends when peak sound reached
Decay - Starts when pipe reaches peak sound, ends when sound has "settled"
Sustain - Level at which sound settles in the pipe
Release - Starts when air stops flowing through the pipe
"""
from typing import Self, Literal
#-----------------------------------------------------------------------------------------------------------------------
from icecream import ic  # type: ignore


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
        ic("Initializing ADSR Envelope")
        self.attack = attack_time
        self.decay = decay_time
        self.sustain = sustain_level
        self.release = release_time
        self.samplerate = samplerate
        ic("ADSR Envelope Initialized")

    #===================================================================================================================
    # Generator Methods
    #===================================================================================================================
    def __iter__(self) -> Self:
        ic("Starting ADSR Envelope")
        self.__value: float = self.MIN_LEVEL
        self.__phase: Literal[
            "ATTACK",
            "DECAY",
            "SUSTAIN",
            "RELEASE"
        ] = "ATTACK"
        ic(self.__phase)
        return self

    #-------------------------------------------------------------------------------------------------------------------
    def __next__(self) -> float:
        ic("Generating ADSR Value")
        min_level: float = self.MIN_LEVEL
        max_level: float = self.MAX_LEVEL
        modifier: float = self.__value
        ic(modifier)
        ic(self.__phase)
        match self.__phase:
            case "ATTACK":
                self.__value += self.__attack_modifier
                ic(self.__value)
                if self.__value >= max_level:
                    self.__value = max_level
                    ic(self.__value)
                    self.__phase = "DECAY"
                    ic(self.__phase)
            case "DECAY":
                self.__value -= self.__decay_modifier
                ic(self.__value)
                if self.__value <= self.sustain:
                    self.__value = self.sustain
                    ic(self.__value)
                    self.__phase = "SUSTAIN"
                    ic(self.__phase)
            case "SUSTAIN":
                self.__value = self.sustain
                ic(self.__value)
            case "RELEASE":
                self.__value -= self.__release_modifier
                ic(self.__value)
                if self.__value <= min_level:
                    self.__value = min_level
                    ic(self.__value)
        ic("ADSR Value Generated")
        return modifier

    #===================================================================================================================
    # Control Methods
    #===================================================================================================================
    def start_release(self) -> None:
        ic("Starting Release Phase")
        self.__reached_level: float = self.__value
        ic(self.__reached_level)
        self.__phase = "RELEASE"
        ic(self.__phase)
        ic("Release Phase Started")

    #===================================================================================================================
    # Properties
    #===================================================================================================================
    #*******************************************************************************************************************
    # Levels
    #*******************************************************************************************************************
    @property
    def MIN_LEVEL(self) -> float:
        ic("Getting Minimum Level")
        min_level: float = 0.0
        ic(min_level)
        ic("Minimum Level Retrieved")
        return min_level

    #-------------------------------------------------------------------------------------------------------------------
    @property
    def MAX_LEVEL(self) -> float:
        ic("Getting Maximum Level")
        max_level: float = 1.0
        ic(max_level)
        ic("Maximum Level Retrieved")
        return max_level

    #*******************************************************************************************************************
    # Modifiers
    #*******************************************************************************************************************
    @property
    def __attack_modifier(self) -> float:
        ic("Getting Attack Modifier")
        attack_samples: float = self.attack * self.samplerate
        ic(attack_samples)
        attack_modifier: float = self.MAX_LEVEL / attack_samples
        ic(attack_modifier)
        ic("Attack Modifier Retrieved")
        return attack_modifier

    #-------------------------------------------------------------------------------------------------------------------
    @property
    def __decay_modifier(self) -> float:
        ic("Getting Decay Modifier")
        decay_level: float = self.MAX_LEVEL - self.sustain
        ic(decay_level)
        decay_samples: float = self.decay * self.samplerate
        ic(decay_samples)
        decay_modifier: float = decay_level / decay_samples
        ic(decay_modifier)
        ic("Decay Modifier Retrieved")
        return decay_modifier

    #-------------------------------------------------------------------------------------------------------------------
    @property
    def __release_modifier(self) -> float:
        ic("Getting Release Modifier")
        level_ratio: float = self.__reached_level / self.sustain
        ic(level_ratio)
        release_rate: float = self.release * self.samplerate
        ic(release_rate)
        release_samples: float = level_ratio * release_rate
        ic(release_samples)
        release_modifier: float = self.__reached_level / release_samples
        ic(release_modifier)
        ic("Release Modifier Retrieved")
        return release_modifier

    #*******************************************************************************************************************
    # Return Value, Phase from Generator
    #*******************************************************************************************************************
    @property
    def value(self) -> float:
        ic("Getting ADSR Value")
        ic(self.__value)
        ic("ADSR Value Retrieved")
        return self.__value

    #-------------------------------------------------------------------------------------------------------------------
    @property
    def phase(self) -> Literal["ATTACK", "DECAY", "SUSTAIN", "RELEASE"]:
        ic("Getting ADSR Phase")
        ic(self.__phase)
        ic("ADSR Phase Retrieved")
        return self.__phase

    #*******************************************************************************************************************
    # Attack
    #*******************************************************************************************************************
    @property
    def attack(self) -> float:
        ic("Getting Attack Time")
        ic(self.__attack)
        ic("Attack Time Retrieved")
        return self.__attack

    #-------------------------------------------------------------------------------------------------------------------
    @attack.setter
    def attack(self, value: float) -> None:
        ic("Setting Attack Time")
        ic(value)
        self.__attack: float = abs(value)
        ic(self.__attack)
        ic("Attack Time Set")

    #*******************************************************************************************************************
    # Decay
    #*******************************************************************************************************************
    @property
    def decay(self) -> float:
        ic("Getting Decay Time")
        ic(self.__decay)
        ic("Decay Time Retrieved")
        return self.__decay

    #-------------------------------------------------------------------------------------------------------------------
    @decay.setter
    def decay(self, value: float) -> None:
        ic("Setting Decay Time")
        ic(value)
        self.__decay: float = abs(value)
        ic(self.__decay)
        ic("Decay Time Set")

    #*******************************************************************************************************************
    # Sustain
    #*******************************************************************************************************************
    @property
    def sustain(self) -> float:
        ic("Getting Sustain Level")
        ic(self.__sustain)
        ic("Sustain Level Retrieved")
        return self.__sustain

    #-------------------------------------------------------------------------------------------------------------------
    @sustain.setter
    def sustain(self, value: float) -> None:
        ic("Setting Sustain Level")
        ic(value)
        if value < self.MIN_LEVEL:
            value = self.MIN_LEVEL
        elif value > self.MAX_LEVEL:
            value = self.MAX_LEVEL
        ic(value)
        self.__sustain: float = value
        ic(self.__sustain)
        ic("Sustain Level Set")

    #*******************************************************************************************************************
    # Release
    #*******************************************************************************************************************
    @property
    def release(self) -> float:
        ic("Getting Release Time")
        ic(self.__release)
        ic("Release Time Retrieved")
        return self.__release

    #-------------------------------------------------------------------------------------------------------------------
    @release.setter
    def release(self, value: float) -> None:
        ic("Setting Release Time")
        ic(value)
        self.__release: float = abs(value)
        ic(self.__release)
        ic("Release Time Set")

    #*******************************************************************************************************************
    # Samplerate
    #*******************************************************************************************************************
    @property
    def samplerate(self) -> int:
        ic("Getting Samplerate")
        ic(self.__samplerate)
        ic("Samplerate Retrieved")
        return self.__samplerate

    #-------------------------------------------------------------------------------------------------------------------
    @samplerate.setter
    def samplerate(self, value: int) -> None:
        ic("Setting Samplerate")
        ic(value)
        self.__samplerate: int = abs(value)
        ic(self.__samplerate)
        ic("Samplerate Set")
