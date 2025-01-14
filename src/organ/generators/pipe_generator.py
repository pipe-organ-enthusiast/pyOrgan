"""pipe_generator.py

Combination of mulitple harmonics and adsr to create a digital representation
of an organ pipe

Pipe Attributes:
    Fundimental Frequency
    Type: Open vs Closed
    Harmonic Amplitudes
    Amplitude Modifiers - Modifies the amplitude in ADSR
    Amplitude Scalers - Determines rate of change of amplitude in ADSR
    ADSR Parameters
"""
from .harmonic import Harmonic
from .adsr import ADSR
from typing import Self, Literal


class PipeGenerator:
    def __init__(
            self,
            frequency: float,
            pipe_type: Literal["OPEN", "CLOSED"],
            amplitudes: list[float],
            amplitude_modifiers: list[float],
            amplitude_scalers: list[float],
            attack_time: float,
            decay_time: float,
            sustain_level: float,
            release_time: float,
            samplerate: int,
    ) -> None:
        self.__harmonics: list[Harmonic] = [
            Harmonic(
                frequency=self.__calc_harmonic_frequencies(
                    pipe_type=pipe_type,
                    frequency=frequency,
                    harmonic=x
                ),
                amplitude=amplitudes[x],
                amplitude_modifier=amplitude_modifiers[x],
                amplitude_scaler=amplitude_scalers[x],
                samplerate=samplerate
            ) for x in range(len(amplitudes))
        ]
        self.__adsr: ADSR = ADSR(
            attack_time=attack_time,
            decay_time=decay_time,
            sustain_level=sustain_level,
            release_time=release_time,
            samplerate=samplerate
        )

    def __iter__(self) -> Self:
        self.__harmonics_value: float = 0.0
        self.__adsr_value: float = 0.0
        for harmonic in self.__harmonics:
            iter(harmonic)
        iter(self.__adsr)
        return self

    def __next__(self) -> float:
        harmonics_sample: float = self.__harmonics_value
        adsr_modifier: float = self.__adsr_value
        
        # Determines the harmonics sample based on adsr phase
        if self.__adsr.phase == "ATTACK":
            # 
            self.__harmonics_value = sum(
                [
                    harmonic.ampmod * next(harmonic)
                    for harmonic in self.__harmonics
                ]
            ) / len(self.__harmonics)
            for harmonic in self.__harmonics:
                harmonic.ampmod *= harmonic.ampscale
                if harmonic.ampmod >= 1.0:
                    harmonic.ampmod = 1.0
        else:
            self.__harmonics_value = sum(
                [next(harmonic) for harmonic in self.__harmonics]
            ) / len(self.__harmonics)
        
        self.__adsr_value = next(self.__adsr)
        
        return adsr_modifier * harmonics_sample

    def __calc_harmonic_frequencies(
            self,
            pipe_type: Literal["OPEN", "CLOSED"],
            frequency: float,
            harmonic: int
    ) -> float:
        match pipe_type:
            case "OPEN":
                return frequency * (harmonic + 1)
            case "CLOSED":
                return frequency * (2 * harmonic + 1)

    def start_adsr_release(self) -> None:
        self.__adsr.start_release()
