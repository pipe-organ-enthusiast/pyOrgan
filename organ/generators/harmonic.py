"""harmonic.py
Harmonic: Sine Wave

Sine Wave Equation:
Waveform = Amplitude * Sin(2 * Pi * Frequency * NSamples / Samplerate)
"""

from math import pi, sin
from typing import Self


class Harmonic:
    def __init__(
            self,
            frequency: float,
            amplitude: float,
            samplerate: int
    ) -> None:
        self.frequency = frequency
        self.amplitude = amplitude
        self.samplerate = samplerate

    def __iter__(self) -> Self:
        self.__value: float = self.MIN_AMPLITUDE
        return self

    def __next__(self) -> float:
        # calculates current sine wave sample
        sample: float = self.amplitude * sin(self.__value)
        
        # applies calculation for the next sin wave sample
        self.__value += 2 * pi * self.frequency / self.samplerate
        
        return sample

    ###########################################################################
    @property
    def MIN_AMPLITUDE(self) -> float:
        return 0.0

    @property
    def MAX_AMPLITUDE(self) -> float:
        return 1.0

    #**************************************************************************
    @property
    def frequency(self) -> float:
        return self.__frequency

    @frequency.setter
    def frequency(self, f: float) -> None:
        self.__frequency: float = abs(f)

    #--------------------------------------------------------------------------
    @property
    def amplitude(self) -> float:
        return self.__amplitude

    @amplitude.setter
    def amplitude(self, a: float) -> None:
        if a < self.MIN_AMPLITUDE:
            a = self.MIN_AMPLITUDE
        elif a > self.MAX_AMPLITUDE:
            a = self.MAX_AMPLITUDE
        self.__amplitude: float = a

    #--------------------------------------------------------------------------
    @property
    def samplerate(self) -> int:
        return self.__samplerate

    @samplerate.setter
    def samplerate(self, s: int) -> None:
        self.__samplerate: int = abs(s)
