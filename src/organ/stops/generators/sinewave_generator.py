"""Sine Wave Generator
Harmonic: Sine Wave

Sine Wave Equation:
Waveform = Amplitude * Sin(2 * Pi * Frequency * NSamples / Samplerate)
"""
#=======================================================================================================================
# Dependencies
#=======================================================================================================================
from math import pi, sin
from typing import Self
#-----------------------------------------------------------------------------------------------------------------------
from icecream import ic  # type: ignore


class SinewaveGenerator:
    def __init__(
            self,
            frequency: float,
            amplitude: float,
            #amplitude_modifier: float,
            #amplitude_scaler: float,
            samplerate: int
    ) -> None:
        self.frequency = frequency
        self.amplitude = amplitude
        #self.amplitude_modifier = amplitude_modifier
        #self.amplitude_scaler = amplitude_scaler
        self.samplerate = samplerate

    #===================================================================================================================
    # Generator Methods
    #===================================================================================================================
    def __iter__(self) -> Self:
        self.__value: float = self.MIN_AMPLITUDE
        return self

    #-------------------------------------------------------------------------------------------------------------------
    def __next__(self) -> float:
        # calculates current sine wave sample
        sample: float = self.amplitude * sin(self.__value)
        # applies calculation for the next sin wave sample
        self.__value += 2 * pi * self.frequency / self.samplerate
        return sample

    #===================================================================================================================
    # Properties
    #===================================================================================================================
    #*******************************************************************************************************************
    # Amplitude Properties
    #*******************************************************************************************************************
    @property
    def MIN_AMPLITUDE(self) -> float:
        min_amplitude: float = 0.0
        return min_amplitude

    #-------------------------------------------------------------------------------------------------------------------
    @property
    def MAX_AMPLITUDE(self) -> float:
        max_amplitude: float = 1.0
        return max_amplitude

    #*******************************************************************************************************************
    # Frequency
    #*******************************************************************************************************************
    @property
    def frequency(self) -> float:
        return self.__frequency

    #-------------------------------------------------------------------------------------------------------------------
    @frequency.setter
    def frequency(self, value: float) -> None:
        self.__frequency: float = abs(value)

    #*******************************************************************************************************************
    # Amplitude
    #*******************************************************************************************************************
    @property
    def amplitude(self) -> float:
        return self.__amplitude

    #-------------------------------------------------------------------------------------------------------------------
    @amplitude.setter
    def amplitude(self, value: float) -> None:
        if value < self.MIN_AMPLITUDE:
            value = self.MIN_AMPLITUDE
        elif value > self.MAX_AMPLITUDE:
            value = self.MAX_AMPLITUDE
        self.__amplitude: float = value

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
