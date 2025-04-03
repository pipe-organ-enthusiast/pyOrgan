"""harmonic.py
Harmonic: Sine Wave

Sine Wave Equation:
Waveform = Amplitude * Sin(2 * Pi * Frequency * NSamples / Samplerate)
"""
#-----------------------------------------------------------------------------------------------------------------------
from math import pi, sin
from typing import Self
#-----------------------------------------------------------------------------------------------------------------------
from icecream import ic  # type: ignore


class Harmonic:
    def __init__(
            self,
            frequency: float,
            amplitude: float,
            amplitude_modifier: float,
            amplitude_scaler: float,
            samplerate: int
    ) -> None:
        ic("Initializing Harmonic Generator")
        self.frequency = frequency
        self.amplitude = amplitude
        self.amplitude_modifier = amplitude_modifier
        self.amplitude_scaler = amplitude_scaler
        self.samplerate = samplerate
        ic("Harmonic Generator Initialized")

    #===================================================================================================================
    # Generator Methods
    #===================================================================================================================
    def __iter__(self) -> Self:
        ic("Starting Harmonic Generator")
        min_amplitude: float = self.MIN_AMPLITUDE
        ic(min_amplitude)
        self.__value: float = self.MIN_AMPLITUDE
        ic(self.__value)
        ic("Harmonic Generator Started")
        return self

    def __next__(self) -> float:
        ic("Generating Harmonic Sample")
        # calculates current sine wave sample
        sample: float = self.amplitude * sin(self.__value)
        ic(sample)
        # applies calculation for the next sin wave sample
        self.__value += 2 * pi * self.frequency / self.samplerate
        ic(self.__value)
        ic("Harmonic Sample Generated")
        return sample

    #===================================================================================================================
    # Properties
    #===================================================================================================================
    #*******************************************************************************************************************
    # Amplitude Properties
    #*******************************************************************************************************************
    @property
    def MIN_AMPLITUDE(self) -> float:
        ic("Getting Minimum Amplitude")
        min_amplitude: float = 0.0
        ic(min_amplitude)
        ic("Minimum Amplitude Retrieved")
        return min_amplitude

    #-------------------------------------------------------------------------------------------------------------------
    @property
    def MAX_AMPLITUDE(self) -> float:
        ic("Getting Maximum Amplitude")
        max_amplitude: float = 1.0
        ic(max_amplitude)
        ic("Maximum Amplitude Retrieved")
        return max_amplitude

    #*******************************************************************************************************************
    # Frequency
    #*******************************************************************************************************************
    @property
    def frequency(self) -> float:
        ic("Getting Frequency")
        ic(self.__frequency)
        ic("Frequency Retrieved")
        return self.__frequency

    #-------------------------------------------------------------------------------------------------------------------
    @frequency.setter
    def frequency(self, value: float) -> None:
        ic("Setting Frequency")
        ic(value)
        self.__frequency: float = abs(value)
        ic(self.__frequency)
        ic("Frequency Set")

    #*******************************************************************************************************************
    # Amplitude
    #*******************************************************************************************************************
    @property
    def amplitude(self) -> float:
        ic("Getting Amplitude")
        ic(self.__amplitude)
        ic("Amplitude Retrieved")
        return self.__amplitude

    #-------------------------------------------------------------------------------------------------------------------
    @amplitude.setter
    def amplitude(self, value: float) -> None:
        ic("Setting Amplitude")
        ic(value)
        if value < self.MIN_AMPLITUDE:
            value = self.MIN_AMPLITUDE
        elif value > self.MAX_AMPLITUDE:
            value = self.MAX_AMPLITUDE
        ic(value)
        self.__amplitude: float = value
        ic(self.__amplitude)
        ic("Amplitude Set")

    #*******************************************************************************************************************
    # Amplitude Modifier
    #*******************************************************************************************************************
    @property
    def amplitude_modifier(self) -> float:
        """Returns the value of the amplitude modifier.
        
        This value is used in the ATTACK phase of an ADSR Envelope as a
        means of altering the rate at which the harmonic reaches peek value.
        """
        ic("Getting Amplitude Modifier")
        ic(self.__amplitude_modifier)
        ic("Amplitude Modifier Retrieved")
        return self.__amplitude_modifier

    @amplitude_modifier.setter
    def amplitude_modifier(self, value: float) -> None:
        """Sets the value for the Amplitude Modifier.
        This value is used in the ATTACK phase of an ADSR Envelope as a
        means of altering the rate at which the harmonic reaches peek value.
        """
        ic("Setting Amplitude Modifier")
        ic(value)
        if value > self.MAX_AMPLITUDE:
            value = self.MAX_AMPLITUDE
        elif value < self.MIN_AMPLITUDE:
            value = self.MIN_AMPLITUDE
        ic(value)
        self.__amplitude_modifier: float = value
        ic(self.__amplitude_modifier)
        ic("Amplitude Modifier Set")

    #*******************************************************************************************************************
    # Amplitude Scaler
    #*******************************************************************************************************************
    @property
    def amplitude_scaler(self) -> float:
        """Returns the value of the Amplitude Scaler.
        The Amplitude Scaler determines the rate at which the amplitude
        of the harmonic spikes to it's peek.
        """
        ic("Getting Amplitude Scaler")
        ic(self.__amplitude_scaler)
        ic("Amplitude Scaler Retrieved")
        return self.__amplitude_scaler

    #-------------------------------------------------------------------------------------------------------------------
    @amplitude_scaler.setter
    def amplitude_scaler(self, value: float) -> None:
        """Sets the value of the Amplitude Scaler.
        
        The Amplitude Scaler determines the rate at which the amplitude
        of the harmonic spikes to it's peek.
        """
        ic("Setting Amplitude Scaler")
        ic(value)
        self.__amplitude_scaler: float = abs(value)
        ic(self.__amplitude_scaler)
        ic("Amplitude Scaler Set")

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
