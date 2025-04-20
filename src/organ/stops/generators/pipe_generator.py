"""Pipe Generator"""
#=======================================================================================================================
# Dependencies
#=======================================================================================================================
from harmonic_generator import HarmonicGenerator
from adsr_envelope import ADSR
#-----------------------------------------------------------------------------------------------------------------------
from typing import Self


#=======================================================================================================================
class PipeGenerator:
    def __init__(
            self,
            adsr: ADSR,
            harmonic: list[HarmonicGenerator]
    ) -> None:
        self.__harmonics = harmonic
        self.__adsr: ADSR = adsr

    #===================================================================================================================
    # Generator Methods
    #===================================================================================================================
    def __iter__(self) -> Self:
        for harmonic in self.__harmonics:
            iter(harmonic)
        iter(self.__adsr)
        return self

    #-------------------------------------------------------------------------------------------------------------------
    def __next__(self) -> float:
        modifier: float = next(self.__adsr)
        harmonics: float = sum(
            [next(harmonic) for harmonic in self.__harmonics]
        ) / len(self.__harmonics)
        sample: float = modifier * harmonics
        return sample

    #===================================================================================================================
    # Properties
    #===================================================================================================================
    #-------------------------------------------------------------------------------------------------------------------
    # Frequency
    #-------------------------------------------------------------------------------------------------------------------
    def frequency_get(
            self,
            harmonic: int
    ) -> float:
        return self.__harmonics[harmonic].frequency

    #-------------------------------------------------------------------------------------------------------------------
    def frequency_set(
            self,
            harmonic: int,
            value: float
    ) -> None:
        self.__harmonics[harmonic].frequency = value

    #-------------------------------------------------------------------------------------------------------------------
    # Amplitude
    #-------------------------------------------------------------------------------------------------------------------
    def amplitude_get(
            self,
            harmonic: int
    ) -> float:
        return self.__harmonics[harmonic].amplitude

    #-------------------------------------------------------------------------------------------------------------------
    def amplitude_set(
            self,
            harmonic: int,
            value: float
    ) -> None:
        self.__harmonics[harmonic].amplitude = value

    #-------------------------------------------------------------------------------------------------------------------
    # Harmonic ADSR Attack Time
    #-------------------------------------------------------------------------------------------------------------------
    def harmonic_attack_time_get(
            self,
            harmonic: int
    ) -> float:
        return self.__harmonics[harmonic].attack_time

    #-------------------------------------------------------------------------------------------------------------------
    def harmonic_attack_time_set(
            self,
            harmonic: int,
            value: float
    ) -> None:
        self.__harmonics[harmonic].attack_time = value

    #-------------------------------------------------------------------------------------------------------------------
    # Harmonic ADSR Decay Time
    #-------------------------------------------------------------------------------------------------------------------
    def harmonic_decay_time_get(
            self,
            harmonic: int
    ) -> float:
        return self.__harmonics[harmonic].decay_time

    #-------------------------------------------------------------------------------------------------------------------
    def harmonic_decay_time_set(
            self,
            harmonic: int,
            value: float
    ) -> None:
        self.__harmonics[harmonic].decay_time = value

    #-------------------------------------------------------------------------------------------------------------------
    # Harmonic ADSR Sustain Level
    #-------------------------------------------------------------------------------------------------------------------
    def harmonic_sustain_level_get(
            self,
            harmonic: int
    ) -> float:
        return self.__harmonics[harmonic].sustain_level

    #-------------------------------------------------------------------------------------------------------------------
    def harmonic_sustain_level_set(
            self,
            harmonic: int,
            value: float
    ) -> None:
        self.__harmonics[harmonic].sustain_level = value

    #-------------------------------------------------------------------------------------------------------------------
    # Harmonic ADSR Release Time
    #-------------------------------------------------------------------------------------------------------------------
    def harmonic_release_time_get(
            self,
            harmonic: int
    ) -> float:
        return self.__harmonics[harmonic].release_time

    #-------------------------------------------------------------------------------------------------------------------
    def harmonic_release_time_set(
            self,
            harmonic: int,
            value: float
    ) -> None:
        self.__harmonics[harmonic].release_time = value

    #-------------------------------------------------------------------------------------------------------------------
    # Attack Time
    #-------------------------------------------------------------------------------------------------------------------
    def attack_time_get(self) -> float:
        return self.__adsr.attack_time

    #-------------------------------------------------------------------------------------------------------------------
    def attack_time_set(
            self,
            value: float
    ) -> None:
        self.__adsr.attack_time = value

    #-------------------------------------------------------------------------------------------------------------------
    # Decay Time
    #-------------------------------------------------------------------------------------------------------------------
    def decay_time_get(self) -> float:
        return self.__adsr.decay_time

    #-------------------------------------------------------------------------------------------------------------------
    def decay_time_set(
            self,
            value: float
    ) -> None:
        self.__adsr.decay_time = value

    #-------------------------------------------------------------------------------------------------------------------
    # Sustain Level
    #-------------------------------------------------------------------------------------------------------------------
    def sustain_level_get(self) -> float:
        return self.__adsr.sustain_level

    #-------------------------------------------------------------------------------------------------------------------
    def sustain_level_set(
            self,
            value: float
    ) -> None:
        self.__adsr.sustain_level = value

    #-------------------------------------------------------------------------------------------------------------------
    # Release Time
    #-------------------------------------------------------------------------------------------------------------------
    def release_time_get(self) -> float:
        return self.__adsr.release_time

    #-------------------------------------------------------------------------------------------------------------------
    def release_time_set(
            self,
            value: float
    ) -> None:
        self.__adsr.release_time = value

    #-------------------------------------------------------------------------------------------------------------------
    # Samplerate
    #-------------------------------------------------------------------------------------------------------------------
    def samplerate_get(self) -> int:
        samplerate = self.__adsr.samplerate
        for harmonic in self.__harmonics:
            if harmonic.samplerate != samplerate:
                harmonic.samplerate = samplerate
        return samplerate

    def samplerate_set(
            self,
            value: int
    ) -> None:
        self.__adsr.samplerate = value
        for harmonic in self.__harmonics:
            harmonic.samplerate = value
