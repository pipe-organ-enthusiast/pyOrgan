"""organ_pipe.py

Higher Level Organ Pipe Class used to create a Pipe Generator.
"""
from generators import PipeGenerator
import organlib
from typing import Literal


class OrganPipe:
    def __init__(
            self,
            keyboard_note: str,
            real_note: str,
            rank_size: str,
            pipe_type: Literal["OPEN", "CLOSED"],
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
        self.pipetype = pipe_type
        self.amplitudes: list[float] = amplitudes
        self.attack: float = attack_time
        self.decay: float = decay_time
        self.sustain: float = sustain_level
        self.release: float = release_time
        self.samplerate: int = samplerate

    def start(self) -> None:
        self.__pipegenerator: PipeGenerator = PipeGenerator(
            frequency=self.__frequency,
            pipe_type=self.pipetype,
            amplitudes=self.amplitudes,
            attack_time=self.attack,
            decay_time=self.decay,
            sustain_level=self.sustain,
            release_time=self.release,
            samplerate=self.samplerate
        )

    def stop(self) -> None:
        self.__pipe.start_adsr_release()

    ###########################################################################
    @property
    def __frequency(self) -> float:
        return organlib.calc_frequency_equal_temperment(
            note=self.realnote,
            rank=self.ranksize
        )

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

    #--------------------------------------------------------------------------
    @property
    def pipetype(self) -> Literal["OPEN", "CLOSED"]:
        return self.__pipetype

    @pipetype.setter
    def pipetype(self, pipe_type: Literal["OPEN", "CLOSED"]) -> None:
        if not pipe_type == "OPEN" or not pipe_type == "CLOSED":
            pipe_type = "OPEN"
        self.__pipetype = pipe_type


if __name__ == "__main__":
    pass
