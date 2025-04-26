"""Organ Pipe"""
#=======================================================================================================================
# DEPENDENCIES
#=======================================================================================================================
from .generators import PipeGenerator, HarmonicGenerator, SinewaveGenerator, ADSR
from ..organlib import calc_frequency_equal_temperment, NOTE_TO_MIDI
#-----------------------------------------------------------------------------------------------------------------------
from typing import Literal


#=======================================================================================================================
# PIPE
#=======================================================================================================================
class Pipe:
    def __init__(
            self,
            note: str,
            relative_note: str,
            rank_size: str,
            pipe_type: Literal["OPEN", "CLOSED"],
            frequency_offset: int,
            number_harmonics: int,
            amplitudes: list[float],
            attack_times: list[float],
            decay_times: list[float],
            sustain_levels: list[float],
            release_times: list[float],
            attack_time: float,
            decay_time: float,
            sustain_level: float,
            release_time: float,
            samplerate: int
    ) -> None:
        self.__note: str = note
        self.__relative_note: str = relative_note
        self.__rank_size: str = rank_size
        self.__pipe_type: str = pipe_type
        self.__frequency_offset: int = frequency_offset
        self.__number_harmonics: int = number_harmonics
        self.__amplitudes: list[float] = amplitudes
        self.__attack_times: list[float] = attack_times
        self.__decay_times: list[float] = decay_times
        self.__sustain_levels: list[float] = sustain_levels
        self.__release_times: list[float] = release_times
        self.__attack_time: float = attack_time
        self.__decay_time: float = decay_time
        self.__sustain_level: float = sustain_level
        self.__release_time: float = release_time
        self.__samplerate: int = samplerate
        self.__init_pipe_generator()

    #===================================================================================================================
    # PIPE LOGIC
    #===================================================================================================================
    def start(self) -> None:
        iter(self.__pipe_generator)

    def play(
            self,
            number_samples: int
    ) -> list[float]:
        return [next(self.__pipe_generator) for _ in range(number_samples)]

    def stop(self) -> None:
        self.__pipe_generator.stop()

    #===================================================================================================================
    # CREATE GENERATORS
    #===================================================================================================================
    def __init_pipe_generator(self) -> None:
        adsr: ADSR = self.__init_adsr()
        harmonics: list[HarmonicGenerator] = self.__init_harmonics()
        self.__pipe_generator: PipeGenerator = PipeGenerator(
            adsr=adsr,
            harmonics=harmonics
        )

    #-------------------------------------------------------------------------------------------------------------------
    def __init_harmonics(self) -> list[HarmonicGenerator]:
        return [
            HarmonicGenerator(
                sinewave=SinewaveGenerator(
                    frequency=self.__calculate_harmonic_frequency(harmonic),
                    amplitude=self.__amplitudes[harmonic],
                    samplerate=self.__samplerate
                ),
                adsr=ADSR(
                    attack_time=self.__attack_times[harmonic],
                    decay_time=self.__decay_times[harmonic],
                    sustain_level=self.__sustain_levels[harmonic],
                    release_time=self.__release_times[harmonic],
                    samplerate=self.__samplerate
                )
            ) for harmonic in range(self.__number_harmonics)
        ]

    #-------------------------------------------------------------------------------------------------------------------
    def __init_adsr(self) -> ADSR:
        return ADSR(
            attack_time=self.__attack_time,
            decay_time=self.__decay_time,
            sustain_level=self.__sustain_level,
            release_time=self.__release_time,
            samplerate=self.__samplerate
        )

    #-------------------------------------------------------------------------------------------------------------------
    def __update_pipe_generator(self) -> None:
        del self.__pipe_generator
        self.__init_pipe_generator()


    #===================================================================================================================
    # Frequency Calculators
    #===================================================================================================================
    def __calculate_frequency_open_pipe(
            self, 
            harmonic: int
    ) -> float:
        return self.frequency * (harmonic + 1)

    #-------------------------------------------------------------------------------------------------------------------
    def __calculate_frequency_closed_pipe(
            self,
            harmonic: int
    ) -> float:
        return self.frequency * (2 * harmonic + 1)

    #-------------------------------------------------------------------------------------------------------------------
    def __calculate_harmonic_frequency(
            self,
            harmonic: int
    ) -> float:
        match self.__pipe_type:
            case "OPEN":
                return self.__calculate_frequency_open_pipe(harmonic)
            case "CLOSED":
                return self.__calculate_frequency_closed_pipe(harmonic)
            case _:
                return 0.0

    def __update_harmonic_frequencies(self) -> None:
        for harmonic in range(self.__pipe_generator.number_harmonics):
            self.__pipe_generator.frequency_set(
                harmonic=harmonic, 
                value=self.__calculate_harmonic_frequency(harmonic)
            )

    #===================================================================================================================
    # UPDATE PARAMETERS
    #===================================================================================================================
    def update_note(
            self,
            note: str
    ) -> None:
        self.__note = note

    #-------------------------------------------------------------------------------------------------------------------
    def update_relative_note(
            self,
            note: str
    ) -> None:
        self.__relative_note = note
        self.__update_harmonic_frequencies()

    #-------------------------------------------------------------------------------------------------------------------
    def update_rank_size(
            self,
            rank_size: str
    ) -> None:
        self.__rank_size = rank_size
        self.__update_harmonic_frequencies()

    #-------------------------------------------------------------------------------------------------------------------
    def update_pipe_type(
            self,
            pipe_type: str
    ) -> None:
        self.__pipe_type = pipe_type
        self.__update_harmonic_frequencies()

    #-------------------------------------------------------------------------------------------------------------------
    def update_frequency_offset(
            self,
            frequency: int
    ) -> None:
        self.__frequency_offset = frequency
        self.__update_harmonic_frequencies()

    #-------------------------------------------------------------------------------------------------------------------
    def update_number_harmonics(
            self,
            number_harmonics: int
    ) -> None:
        self.__number_harmonics = abs(number_harmonics)
        self.__update_pipe_generator()

    #-------------------------------------------------------------------------------------------------------------------
    def update_amplitude(
            self,
            harmonic: int,
            amplitude: float
    ) -> None:
        self.__amplitudes[harmonic] = abs(amplitude)
        self.__pipe_generator.amplitude_set(
            harmonic=harmonic,
            value=amplitude
        )

    #-------------------------------------------------------------------------------------------------------------------
    def update_harmonic_attack_time(
            self,
            harmonic: int,
            time: float
    ) -> None:
        self.__attack_times[harmonic] = abs(time)
        self.__pipe_generator.harmonic_attack_time_set(
            harmonic=harmonic,
            value=time
        )

    #-------------------------------------------------------------------------------------------------------------------
    def update_harmonic_decay_time(
            self,
            harmonic: int,
            time: float
    ) -> None:
        self.__decay_times[harmonic] = abs(time)
        self.__pipe_generator.harmonic_decay_time_set(
            harmonic=harmonic,
            value=time
        )

    #-------------------------------------------------------------------------------------------------------------------
    def update_harmonic_sustain_level(
            self,
            harmonic: int,
            level: float
    ) -> None:
        self.__sustain_levels[harmonic] = abs(level)
        self.__pipe_generator.harmonic_sustain_level_set(
            harmonic=harmonic,
            value=level
        )

    #-------------------------------------------------------------------------------------------------------------------
    def update_harmonic_release_time(
            self,
            harmonic: int,
            time: float
    ) -> None:
        self.__release_times[harmonic] = abs(time)
        self.__pipe_generator.harmonic_release_time_set(
            harmonic=harmonic,
            value=time
        )

    #-------------------------------------------------------------------------------------------------------------------
    def update_attack_time(
            self,
            time: float
    ) -> None:
        self.__attack_time = abs(time)
        self.__pipe_generator.attack_time_set(time)

    #-------------------------------------------------------------------------------------------------------------------
    def update_decay_time(
            self,
            time: float
    ) -> None:
        self.__decay_time = abs(time)
        self.__pipe_generator.decay_time_set(time)

    #-------------------------------------------------------------------------------------------------------------------
    def update_sustain_level(
            self,
            level: float
    ) -> None:
        self.__sustain_level = abs(level)
        self.__pipe_generator.sustain_level_set(level)

    #-------------------------------------------------------------------------------------------------------------------
    def update_release_time(
            self,
            time: float
    ) -> None:
        self.__release_time = abs(time)
        self.__pipe_generator.release_time_set(time)

    #-------------------------------------------------------------------------------------------------------------------
    def update_samplerate(
            self,
            samplerate: int
    ) -> None:
        self.__samplerate = abs(samplerate)
        self.__update_pipe_generator()

    #===================================================================================================================
    # PROPERTIES
    #===================================================================================================================

    @property
    def frequency(self) -> float:
        return calc_frequency_equal_temperment(
            note=self.__relative_note,
            rank=self.__rank_size
        ) + self.__frequency_offset

    @property
    def midi_number(self) -> int:
        return NOTE_TO_MIDI[self.__note]
