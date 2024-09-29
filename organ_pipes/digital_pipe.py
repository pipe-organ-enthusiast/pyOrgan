"""digital_pipe.py

Combination of mulitple harmonics and adsr to create a digital representation
of an organ pipe

Pipe Attributes:
    Fundimental Frequency
    Type: Open vs Closed
    Number of Harmonics
"""
from harmonic import Harmonic
from adsr import ADSR
from typing import Self, Literal


class DigitalPipe:
    def __init__(
            self,
            frequency: float,
            pipe_type: Literal["OPEN", "CLOSED"],
            number_harmonics: int,
            amplitudes: list[float],
            attack_time: float,
            decay_time: float,
            sustain_level: float,
            release_time: float,
            samplerate: int,
    ) -> None:
        self.frequency: float = frequency
        self.pipetype: Literal["OPEN", "CLOSED"] = pipe_type
        self.nharmonics = number_harmonics
        self.amplitudes = amplitudes
        self.attack: float = attack_time
        self.decay: float = decay_time
        self.sustain: float = sustain_level
        self.release: float = release_time
        self.samplerate: int = samplerate
        self.__harmonics: list[Harmonic] = self.__init_harmonics()
        self.__adsr: ADSR = self.__init_adsr()

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
        self.__harmonics_value = sum(
        [next(harmonic) for harmonic in self.__harmonics]
        ) / self.nharmonics
        self.__adsr_value = next(self.__adsr)
        return adsr_modifier * harmonics_sample

    def __calc_harmonic_frequencies(self, harmonic: int) -> float:
        match self.pipetype:
            case "OPEN":
                return self.frequency * (harmonic + 1)
            case "CLOSED":
                return self.frequency * (2 * harmonic + 1)

    def __init_harmonics(self) -> list[Harmonic]:
        return [
            Harmonic(
                frequency=self.__calc_harmonic_frequencies(x),
                amplitude=self.amplitudes[x],
                samplerate=self.samplerate
            ) for x in range(self.nharmonics)
        ]

    def __init_adsr(self) -> ADSR:
        return ADSR(
            attack_time=self.attack,
            decay_time=self.decay,
            sustain_level=self.sustain,
            release_time=self.release,
            samplerate=self.samplerate
        )

    def start_adsr_release(self) -> None:
        self.__adsr.start_release()

    def adjust_frequency(self, frequency: float) -> None:
        self.frequency = frequency
        self.__harmonics = self.__init_harmonics()

    def adjust_pipetype(self, pipe_type: Literal["OPEN", "CLOSED"]) -> None:
        self.pipetype = pipe_type
        self.__harmonics = self.__init_harmonics()

    def adjust_harmonics(self, num_harmonics: int) -> None:
        amplitudes: list[float] = self.amplitudes
        self.nharmonics = num_harmonics
        self.amplitudes = amplitudes
        self.__harmonics = self.__init_harmonics()

    def adjust_amplitude(
            self,
            harmonic: int,
            amplitude: float
    ) -> None:
        self.amplitudes[harmonic] = amplitude
        self.__harmonics = self.__init_harmonics()

    def adjust_attack(self, attack_time: float) -> None:
        self.attack = attack_time
        self.__adsr = self.__init_adsr()

    def adjust_decay(self, decay_time: float) -> None:
        self.decay = decay_time
        self.__adsr = self.__init_adsr()

    def adjust_sustain(self, sustain_level: float) -> None:
        self.sustain = sustain_level
        self.__adsr = self.__init_adsr()

    def adjust_release(self, release_time: float) -> None:
        self.release = release_time
        self.__adsr = self.__init_adsr()

    def adjust_samplerate(self, samplerate: int) -> None:
        self.samplerate = samplerate
        self.__harmonics = self.__init_harmonics()
        self.__adsr = self.__init_adsr()

    ###########################################################################
    @property
    def num_adsr_release_samples(self) -> None:
        return self.__adsr.num_release_samples

    #**************************************************************************
    @property
    def nharmonics(self) -> int:
        return self.__nharmonics

    @nharmonics.setter
    def nharmonics(self, n: int) -> None:
        self.__nharmonics: int = abs(n)

    #--------------------------------------------------------------------------
    @property
    def amplitudes(self) -> list[float]:
        return self.__amplitudes

    @amplitudes.setter
    def amplitudes(self, a: list[float]) -> None:
        if len(a) > self.nharmonics:
            while True:
                a.pop(-1)
        elif len(a) < self.nharmonics:
            while True:
                a.append(0.0)
        self.__amplitudes: list[float] = a


if __name__ == "__main__":
    pipe: DigitalPipe = DigitalPipe(
        frequency=440.0,
        pipe_type="OPEN",
        number_harmonics=4,
        amplitudes=[0.4, 0.1, 0.05, 0.009],
        attack_time=0.2,
        decay_time=0.15,
        sustain_level=0.95,
        release_time=0.8,
        samplerate=48000
    )
    iter(pipe)
    waveform: list[float] = [
        next(pipe) for _ in range(2 * pipe.samplerate)
    ]
    pipe.start_adsr_release()
    tail: list[float] = [
        next(pipe) for _ in range(pipe.num_adsr_release_samples + 2)
    ]
    waveform += tail
    print(waveform)
