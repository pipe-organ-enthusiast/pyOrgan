"""Organ Pipe"""
#=======================================================================================================================
# DEPENDENCIES
#=======================================================================================================================
from generators import PipeGenerator, HarmonicGenerator, SinewaveGenerator, ADSR  # type: ignore
from organlib import calc_frequency_equal_temperment


#=======================================================================================================================
# PIPE
#=======================================================================================================================
class Pipe:
    def __init__(
            self,
            note: str,
            relative_note: str,
            rank_size: str,
            pipe_type: str,
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
        self.note = note
        self.relative_note = relative_note
        self.rank_size = rank_size
        self.pipe_type = pipe_type
        self.frequency_offset = frequency_offset
        self.number_harmonics = number_harmonics
        self.amplitudes = amplitudes
        self.attack_times = attack_times
        self.decay_times = decay_times
        self.sustain_levels = sustain_levels
        self.release_times = release_times
        self.attack_time = attack_time
        self.decay_time = decay_time
        self.sustain_level = sustain_level
        self.release_time = release_time
        self.samplerate = samplerate

    def init_pipe_generator(self) -> None:
        ...

    def init_harmonics_open(self) -> list[HarmonicGenerator]:
        return [
            HarmonicGenerator(
                sinewave=SinewaveGenerator(
                    frequency=self.frequency * (harmonic + 1),
                    amplitude=self.amplitudes[harmonic],
                    samplerate=self.samplerate
                ),
                adsr=ADSR(
                    attack_time=self.attack_times[harmonic],
                    decay_time=self.decay_times[harmonic],
                    sustain_level=self.sustain_levels[harmonic],
                    release_time=self.release_times[harmonic],
                    samplerate=self.samplerate
                )
            ) for harmonic in range(self.number_harmonics)
        ]

    def init_harmonics_closed(self) -> list[HarmonicGenerator]:
        return [
            HarmonicGenerator(
                sinewave=SinewaveGenerator(
                    frequency=self.frequency * (2 * harmonic + 1),
                    amplitude=self.amplitudes[harmonic],
                    samplerate=self.samplerate
                ),
                adsr=ADSR(
                    attack_time=self.attack_times[harmonic],
                    decay_time=self.decay_times[harmonic],
                    sustain_level=self.sustain_levels[harmonic],
                    release_time=self.release_times[harmonic],
                    samplerate=self.samplerate
                )
            ) for harmonic in range(self.number_harmonics)
        ]

    @property
    def frequency(self) -> float:
        return calc_frequency_equal_temperment(
            note=self.note,
            rank=self.rank_size
        )

