"""organ_pipe.py

Higher Level Organ Pipe Class used to create a Pipe Generator.
"""
from generators import PipeGenerator
import organlib
from typing import Literal, Generator


class OrganPipe:
    def __init__(
            self,
            keyboard_note: str,
            real_note: str,
            rank_size: str,
            pipe_type: Literal["OPEN", "CLOSED"],
            number_harmonics: int,
            amplitudes: list[float],
            attack_time: float,
            decay_time: float,
            sustain_level: float,
            release_time: float,
            samplerate: int
    ) -> None:
        self.keyboardnote = keyboard_note
        self.realnote = real_note
        self.ranksize = rank_size
        self.__pipegenerator = PipeGenerator(
            frequency=self.__frequency,
            pipe_type=pipe_type,
            number_harmonics=number_harmonics,
            amplitudes=amplitudes,
            attack_time=attack_time,
            decay_time=decay_time,
            sustain_level=sustain_level,
            release_time=release_time,
            samplerate=samplerate
        )

    def start(self) -> None:
        iter(self.__pipegenerator)

    def get_sample(self) -> float:
        return next(self.__pipegenerator)

    def stop(self) -> None:
        self.__pipegenerator.start_adsr_release()

    ###########################################################################
    @property
    def __frequency(self) -> float:
        return organlib.calc_frequency_equal_temperment(
            note=self.realnote,
            rank=self.ranksize
        )

    @property
    def num_release_samples(self) -> int:
        return self.__pipegenerator.num_adsr_release_samples

    #**************************************************************************
    @property
    def keyboardnote(self) -> str:
        return self.__keyboardnote

    @keyboardnote.setter
    def keyboardnote(self, note: str) -> None:
        key_note: str = "C2"
        if not note in organlib.NOTES:
            note = key_note
        self.__keyboardnote: str = note

    #--------------------------------------------------------------------------
    @property
    def realnote(self) -> str:
        return self.__realnote

    @realnote.setter
    def realnote(self, note: str) -> None:
        real_note: str = "C2"
        if not note in organlib.NOTES:
            note = real_note
        self.__realnote = note
        if hasattr(self, "__pipegenerator"):
            self.__pipegenerator.adjust_frequency(self.__frequency)

    #--------------------------------------------------------------------------
    @property
    def ranksize(self) -> str:
        return self.__ranksize

    @ranksize.setter
    def ranksize(self, rank_size: str) -> None:
        rank_size_: str = "8'"
        if not rank_size in organlib.RANK_SIZES:
            rank_size = rank_size_
        self.__ranksize: str = rank_size
        if hasattr(self, "__pipegenerator"):
            self.__pipegenerator.adjust_frequency(self.__frequency)

    #--------------------------------------------------------------------------
    @property
    def pipetype(self) -> Literal["OPEN", "CLOSED"]:
        return self.__pipegenerator.pipetype

    @pipetype.setter
    def pipetype(self, pipe_type: Literal["OPEN", "CLOSED"]) -> None:
        self.__pipegenerator.adjust_pipetype(pipe_type)

    #--------------------------------------------------------------------------
    @property
    def nharmonics(self) -> int:
        return self.__pipegenerator.nharmonics

    @nharmonics.setter
    def nharmonics(self, number_harmonics: int) -> None:
        self.__pipegenerator.adjust_harmonics(number_harmonics)

    #--------------------------------------------------------------------------
    @property
    def amplitudes(self) -> list[float]:
        return self.__pipegenerator.amplitudes

    @amplitudes.setter
    def amplitudes(self, amplitudes: list[float]) -> None:
        self.__pipegenerator.adjust_amplitudes(amplitudes)

    #--------------------------------------------------------------------------
    @property
    def attack(self) -> float:
        return self.__pipegenerator.attack

    @attack.setter
    def attack(self, attack_time: float) -> None:
        self.__pipegenerator.adjust_attack(attack_time)

    #--------------------------------------------------------------------------
    @property
    def decay(self) -> float:
        return self.__pipegenerator.decay

    @decay.setter
    def decay(self, decay_time: float) -> None:
        self.__pipegenerator.adjust_decay(decay_time)

    #--------------------------------------------------------------------------
    @property
    def sustain(self) -> float:
        return self.__pipegenerator.sustain

    @sustain.setter
    def sustain(self, sustain_level: float) -> None:
        self.__pipegenerator.adjust_sustain(sustain_level)

    #--------------------------------------------------------------------------
    @property
    def samplerate(self) -> int:
        return self.__pipegenerator.samplerate

    @samplerate.setter
    def samplerate(self, samplerate: int) -> None:
        self.__pipegenerator.adjust_samplerate(samplerate)


if __name__ == "__main__":
    pipe = OrganPipe(
        keyboard_note="C1",
        real_note="C1",
        rank_size="8'",
        pipe_type="OPEN",
        number_harmonics=2,
        amplitudes=[0.3, 0.1],
        attack_time=0.5,
        decay_time=0.1,
        sustain_level=0.95,
        release_time=0.8,
        samplerate=48000
    )
    pipe.start()
    waveform = [pipe.get_sample() for _ in range(14)]
    pipe.stop()
    tail = [pipe.get_sample() for _ in range(pipe.num_release_samples)]
    print(tail)
