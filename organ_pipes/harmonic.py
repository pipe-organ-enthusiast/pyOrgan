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
        self.__value: float = 0.0
        return self

    def __next__(self) -> float:
        sample: float = self.__calc_sample()
        self.__value += self.__value_increment
        return sample

    def __calc_sample(self) -> float:
        return self.amplitude * sin(self.__value)

    ###########################################################################
    @property
    def MIN_AMPLITUDE(self) -> float:
        return 0.0

    @property
    def MAX_AMPLITUDE(self) -> float:
        return 1.0

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


if __name__ == "__main__":
    harmonic: Harmonic = Harmonic(
        frequency=440.0,
        amplitude=0.5,
        samplerate=44100
    )
    iter(harmonic)
    wave: list[float] = [
        next(harmonic) for _ in range(10)
    ]
    print(wave)
