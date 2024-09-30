"""organ_pipe.py

Higher Level Organ Pipe Class used to create a Pipe Generator.
"""
from generators import PipeGenerator
import organlib


class OrganPipe:
    def __init__(
            self,
            keyboard_note: str,
            real_note: str,
            rank_size: str,
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
        self.nharmonics = number_harmonics
        self.amplitudes = amplitudes
        self.attack = attack_time
        self.decay = decay_time
        self.sustain = sustain_level
        self.release = release_time
        self.samplerate = samplerate


if __name__ == "__main__":
    pass
