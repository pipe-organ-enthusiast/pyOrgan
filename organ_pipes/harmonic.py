"""harmonic.py
Harmonic: Sine Wave

Sine Wave Equation:
Waveform = Amplitude * Sin(2 * Pi * Frequency * NSamples / Samplerate)
"""

from numpy import pi, sin
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
        self.__value: float = 0.0
        return self

    def __next__(self) -> float:
        sample: float = self.__calc_sample()
        self.__value += self.__value_increment
        return sample

    def __calc_sample(self) -> float:
        return self.amplitude * sin(self.__value)

    @property
    def __value_increment(self) -> float:
        return 2 * pi * self.frequency / self.samplerate

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
        min: float = 0.0
        max: float = 1.0
        if a < min:
            a = min
        elif a > max:
            a = max
        self.__amplitude: float = a

    #--------------------------------------------------------------------------
    @property
    def samplerate(self) -> int:
        return self.__samplerate

    @samplerate.setter
    def samplerate(self, s: int) -> None:
        self.__samplerate: int = abs(s)
