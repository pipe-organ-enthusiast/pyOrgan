"""adsr.py
ADSR - Attack, Decay, Release, Sustain
Attack - Starts when air enters the pipe, ends when peak sound reached
Decay - Starts when pipe reaches peak sound, ends when sound has "settled"
Sustain - Level at which sound settles in the pipe
Release - Starts when air stops flowing through the pipe
"""
from typing import Self, Literal


class ADSR:
    def __init__(
            self,
            attack_time: float,
            decay_time: float,
            sustain_level: float,
            release_time: float,
            samplerate: int
    ) -> None:
        self.attack = attack_time
        self.decay = decay_time
        self.sustain = sustain_level
        self.release = release_time
        self.samplerate = samplerate

    def __iter__(self) -> Self:
        self.__value: float = self.MIN_LEVEL
        self.__phase: Literal[
            "ATTACK",
            "DECAY",
            "SUSTAIN",
            "RELEASE"
        ] = "ATTACK"
        return self

    def __next__(self) -> float:
        modifier: float = self.__value
        match self.__phase:
            case "ATTACK":
                self.__value += self.__attack_modifier
                if self.__value >= self.MAX_LEVEL:
                    self.__value = self.MAX_LEVEL
                    self.__phase = "DECAY"
            case "DECAY":
                self.__value -= self.__decay_modifier
                if self.__value <= self.sustain:
                    self.__value = self.sustain
                    self.__phase = "SUSTAIN"
            case "SUSTAIN":
                self.__value = self.sustain
            case "RELEASE":
                self.__value -= self.__release_modifier
                if self.__value <= self.MIN_LEVEL:
                    self.__value = self.MIN_LEVEL
        return modifier

    def start_release(self) -> None:
        self.__reached_level: float = self.__value
        self.__phase = "RELEASE"

    ###########################################################################
    @property
    def MIN_LEVEL(self) -> float:
        return 0.0

    @property
    def MAX_LEVEL(self) -> float:
        return 1.0

    @property
    def __attack_modifier(self) -> float:
        attack_samples: float = self.attack * self.samplerate
        return self.MAX_LEVEL / attack_samples

    @property
    def __decay_modifier(self) -> float:
        decay_level: float = self.MAX_LEVEL - self.sustain
        decay_samples: float = self.decay * self.samplerate
        return decay_level / decay_samples

    @property
    def __release_modifier(self) -> float:
        level_ratio: float = self.__reached_level / self.sustain
        release_rate: float = self.release * self.samplerate
        release_samples: float = level_ratio * release_rate
        return self.__reached_level / release_samples

    @property
    def value(self) -> float:
        return self.__value

    @property
    def phase(self) -> Literal["ATTACK", "DECAY", "SUSTAIN", "RELEASE"]:
        return self.__phase

    #**************************************************************************
    @property
    def attack(self) -> float:
        return self.__attack

    @attack.setter
    def attack(self, a: float) -> None:
        self.__attack: float = abs(a)

    #--------------------------------------------------------------------------
    @property
    def decay(self) -> float:
        return self.__decay

    @decay.setter
    def decay(self, d: float) -> None:
        self.__decay: float = abs(d)

    #--------------------------------------------------------------------------
    @property
    def sustain(self) -> float:
        return self.__sustain

    @sustain.setter
    def sustain(self, s: float) -> None:
        if s < self.MIN_LEVEL:
            s = self.MIN_LEVEL
        elif s > self.MAX_LEVEL:
            s = self.MAX_LEVEL
        self.__sustain: float = s

    #--------------------------------------------------------------------------
    @property
    def release(self) -> float:
        return self.__release

    @release.setter
    def release(self, r: float) -> None:
        self.__release: float = abs(r)

    #--------------------------------------------------------------------------
    @property
    def samplerate(self) -> int:
        return self.__samplerate

    @samplerate.setter
    def samplerate(self, sr: int) -> None:
        self.__samplerate: int = abs(sr)
