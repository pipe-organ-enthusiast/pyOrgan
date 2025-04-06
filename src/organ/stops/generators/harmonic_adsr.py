"""HarmonicADSR Generator"""
#=======================================================================================================================
# Dependencies
#=======================================================================================================================
from harmonic import Harmonic
from adsr import ADSR
#-----------------------------------------------------------------------------------------------------------------------
from typing import Self


#=======================================================================================================================
class HarmonicADSR:
    def __init__(
            self,
            frequency: float,
            amplitude: float,
            attack_time: float,
            decay_time: float,
            sustain_level: float,
            release_time: float,
            samplerate: int,
    ) -> None:
        self.__harmonic: Harmonic = Harmonic(
            frequency=frequency,
            amplitude=amplitude,
            samplerate=samplerate,
        )
        self.__adsr: ADSR = ADSR(
            attack_time=attack_time,
            decay_time=decay_time,
            sustain_level=sustain_level,
            release_time=release_time,
            samplerate=samplerate,
        )

    #===================================================================================================================
    # Generator Methods
    #===================================================================================================================
    def __iter__(self) -> Self:
        iter(self.__harmonic)
        iter(self.__adsr)
        return self

    #-------------------------------------------------------------------------------------------------------------------
    def __next__(self) -> float:
        sample: float = next(self.__adsr) * next(self.__harmonic)
        return sample

    #===================================================================================================================
    # Properties
    #===================================================================================================================
    #-------------------------------------------------------------------------------------------------------------------
    # Frequency
    #-------------------------------------------------------------------------------------------------------------------
    @property
    def frequency(self) -> float:
        return self.__harmonic.frequency

    #-------------------------------------------------------------------------------------------------------------------
    @frequency.setter
    def frequency(self, value: float) -> None:
        self.__harmonic.frequency = value

    #-------------------------------------------------------------------------------------------------------------------
    # Amplitude
    #-------------------------------------------------------------------------------------------------------------------
    @property
    def amplitude(self) -> float:
        return self.__harmonic.amplitude

    #-------------------------------------------------------------------------------------------------------------------
    @amplitude.setter
    def amplitude(self, value: float) -> None:
        self.__harmonic.amplitude = value

    #-------------------------------------------------------------------------------------------------------------------
    # Attack Time
    #-------------------------------------------------------------------------------------------------------------------
    @property
    def attack_time(self) -> float:
        return self.__adsr.attack_time

    #-------------------------------------------------------------------------------------------------------------------
    @attack_time.setter
    def attack_time(self, value: float) -> None:
        self.__adsr.attack_time = value

    #-------------------------------------------------------------------------------------------------------------------
    # Decay Time
    #-------------------------------------------------------------------------------------------------------------------
    @property
    def decay_time(self) -> float:
        return self.__adsr.decay_time

    #-------------------------------------------------------------------------------------------------------------------
    @decay_time.setter
    def decay_time(self, value: float) -> None:
        self.__adsr.decay_time = value

    #-------------------------------------------------------------------------------------------------------------------
    # Sustain Level
    #-------------------------------------------------------------------------------------------------------------------
    @property
    def sustain_level(self) -> float:
        return self.__adsr.sustain_level

    #-------------------------------------------------------------------------------------------------------------------
    @sustain_level.setter
    def sustain_level(self, value: float) -> None:
        self.__adsr.sustain_level = value

    #-------------------------------------------------------------------------------------------------------------------
    # Release Time
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
        if self.__harmonic.samplerate != self.__adsr.samplerate:
            self.__adsr.samplerate = self.__harmonic.samplerate
        return self.__harmonic.samplerate

    #-------------------------------------------------------------------------------------------------------------------
    @samplerate.setter
    def samplerate(self, value: int) -> None:
        self.__harmonic.samplerate = value
        self.__adsr.samplerate = value
