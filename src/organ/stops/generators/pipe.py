"""Pipe Generator"""
#=======================================================================================================================
# Dependencies
#=======================================================================================================================
from harmonic_adsr import HarmonicADSR
from adsr import ADSR
#-----------------------------------------------------------------------------------------------------------------------
from typing import Self


#=======================================================================================================================
class Pipe:
    def __init__(
            self,
            frequency: float,
            amplitudes: list[float],
            harmonic_attack_times: list[float],
            harmonic_decay_times: list[float],
            harmonic_sustain_levels: list[float],
            harmonic_release_times: list[float],
            attack_time: float,
            decay_time: float,
            sustain_level: float,
            release_time: float,
            samplerate: int,
    ) -> None:
        self.__harmonics = [
            HarmonicADSR(
                frequency=frequency * i,
                amplitude=amplitudes[i],
                attack_time=harmonic_attack_times[i],
                decay_time=harmonic_decay_times[i],
                sustain_level=harmonic_sustain_levels[i],
                release_time=harmonic_release_times[i],
                samplerate=samplerate
            )
            for i in range(len(amplitudes))
        ]
        self.__adsr: ADSR = ADSR(
            attack_time=attack_time,
            decay_time=decay_time,
            sustain_level=sustain_level,
            release_time=release_time,
            samplerate=samplerate
        )

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
        )
        sample: float = modifier * harmonics
        return sample

    #===================================================================================================================
    # Properties
    #===================================================================================================================
    #-------------------------------------------------------------------------------------------------------------------
    # Frequency
    #-------------------------------------------------------------------------------------------------------------------
    @property
    def frequency(self) -> float:
        return self.__harmonics[0].frequency
    
    #-------------------------------------------------------------------------------------------------------------------
    @frequency.setter
    def frequency(self, value: float) -> None:
        for harmonic in self.__harmonics:
            harmonic.frequency = value * self.__harmonics.index(harmonic) + 1

    #-------------------------------------------------------------------------------------------------------------------
    # Amplitude
    #-------------------------------------------------------------------------------------------------------------------
    def amplitude_get(self, harmonic: int) -> float:
        return self.__harmonics[harmonic].amplitude

    #-------------------------------------------------------------------------------------------------------------------
    def amplitude_set(self, harmonic: int, value: float) -> None:
        self.__harmonics[harmonic].amplitude = value

    #-------------------------------------------------------------------------------------------------------------------
    def amplitude_get_all(self) -> list[float]:
        return [harmonic.amplitude for harmonic in self.__harmonics]

    #-------------------------------------------------------------------------------------------------------------------
    def amplitude_set_all(self, values: list[float]) -> None:
        for i in range(len(self.__harmonics)):
            self.__harmonics[i].amplitude = values[i]

    #-------------------------------------------------------------------------------------------------------------------
    # Attack Time - Harmonics
    #-------------------------------------------------------------------------------------------------------------------
    def attack_time_harmonic_get(self, harmonic: int) -> float:
        return self.__harmonics[harmonic].attack_time

    #-------------------------------------------------------------------------------------------------------------------
    def attack_time_harmonic_set(self, harmonic: int, value: float) -> None:
        self.__harmonics[harmonic].attack_time = value

    #-------------------------------------------------------------------------------------------------------------------
    def attack_time_harmonic_get_all(self) -> list[float]:
        return [harmonic.attack_time for harmonic in self.__harmonics]

    #-------------------------------------------------------------------------------------------------------------------
    def attack_time_harmonic_set_all(self, values: list[float]) -> None:
        for i in range(len(self.__harmonics)):
            self.__harmonics[i].attack_time = values[i]

    #-------------------------------------------------------------------------------------------------------------------
    # Decay Time - Harmonics
    #-------------------------------------------------------------------------------------------------------------------
    def decay_time_harmonic_get(self, harmonic: int) -> float:
        return self.__harmonics[harmonic].decay_time

    #-------------------------------------------------------------------------------------------------------------------
    def decay_time_harmonic_set(self, harmonic: int, value: float) -> None:
        self.__harmonics[harmonic].decay_time = value

    #-------------------------------------------------------------------------------------------------------------------
    def decay_time_harmonic_get_all(self) -> list[float]:
        return [harmonic.decay_time for harmonic in self.__harmonics]

    #-------------------------------------------------------------------------------------------------------------------
    def decay_time_harmonic_set_all(self, values: list[float]) -> None:
        for i in range(len(self.__harmonics)):
            self.__harmonics[i].decay_time = values[i]

    #-------------------------------------------------------------------------------------------------------------------
    # Sustain Level - Harmonics
    #-------------------------------------------------------------------------------------------------------------------
    def sustain_level_harmonic_get(self, harmonic: int) -> float:
        return self.__harmonics[harmonic].sustain_level

    #-------------------------------------------------------------------------------------------------------------------
    def sustain_level_harmonic_set(self, harmonic: int, value: float) -> None:
        self.__harmonics[harmonic].sustain_level = value

    #-------------------------------------------------------------------------------------------------------------------
    def sustain_level_harmonic_get_all(self) -> list[float]:
        return [harmonic.sustain_level for harmonic in self.__harmonics]

    #-------------------------------------------------------------------------------------------------------------------
    def sustain_level_harmonic_set_all(self, values: list[float]) -> None:
        for i in range(len(self.__harmonics)):
            self.__harmonics[i].sustain_level = values[i]

    #-------------------------------------------------------------------------------------------------------------------
    # Release Time - Harmonics
    #-------------------------------------------------------------------------------------------------------------------
    def release_time_harmonic_get(self, harmonic: int) -> float:
        return self.__harmonics[harmonic].release_time

    #-------------------------------------------------------------------------------------------------------------------
    def release_time_harmonic_set(self, harmonic: int, value: float) -> None:
        self.__harmonics[harmonic].release_time = value

    #-------------------------------------------------------------------------------------------------------------------
    def release_time_harmonic_get_all(self) -> list[float]:
        return [harmonic.release_time for harmonic in self.__harmonics]

    #-------------------------------------------------------------------------------------------------------------------
    def release_time_harmonic_set_all(self, values: list[float]) -> None:
        for i in range(len(self.__harmonics)):
            self.__harmonics[i].release_time = values[i]

    #-------------------------------------------------------------------------------------------------------------------
    # Attack Time - ADSR
    #-------------------------------------------------------------------------------------------------------------------
    @property
    def attack_time(self) -> float:
        return self.__adsr.attack_time

    #-------------------------------------------------------------------------------------------------------------------
    @attack_time.setter
    def attack_time(self, value: float) -> None:
        self.__adsr.attack_time = value

    #-------------------------------------------------------------------------------------------------------------------
    # Decay Time - ADSR
    #-------------------------------------------------------------------------------------------------------------------
    @property
    def decay_time(self) -> float:
        return self.__adsr.decay_time

    #-------------------------------------------------------------------------------------------------------------------
    @decay_time.setter
    def decay_time(self, value: float) -> None:
        self.__adsr.decay_time = value

    #-------------------------------------------------------------------------------------------------------------------
    # Sustain Level - ADSR
    #-------------------------------------------------------------------------------------------------------------------
    @property
    def sustain_level(self) -> float:
        return self.__adsr.sustain_level

    #-------------------------------------------------------------------------------------------------------------------
    @sustain_level.setter
    def sustain_level(self, value: float) -> None:
        self.__adsr.sustain_level = value

    #-------------------------------------------------------------------------------------------------------------------
    # Release Time - ADSR
    #-------------------------------------------------------------------------------------------------------------------
    @property
    def release_time(self) -> float:
        return self.__adsr.release_time

    #-------------------------------------------------------------------------------------------------------------------
    @release_time.setter
    def release_time(self, value: float) -> None:
        self.__adsr.release_time = value

    #-------------------------------------------------------------------------------------------------------------------
    # Samplerate
    #-------------------------------------------------------------------------------------------------------------------
    @property
    def samplerate(self) -> int:
        return self.__adsr.samplerate

    @samplerate.setter
    def samplerate(self, value: int) -> None:
        for harmonic in self.__harmonics:
            harmonic.samplerate = value
        self.__adsr.samplerate = value
