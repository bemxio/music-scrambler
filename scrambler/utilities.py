from pydub import AudioSegment
from typing import List

def beat_length(bpm: int) -> int:
    return int(60 / bpm * 1000)

def beat_amount(audio: AudioSegment, beat_length: int) -> int:
    return len(audio) // beat_length

def split_into_beats(audio: AudioSegment, bpm: int) -> List[AudioSegment]:
    length = beat_length(bpm)
    duration = beat_amount(audio, length)

    return [audio[length * index : length * (index + 1)] for index in range(duration)]

def join_beats(beats: List[AudioSegment]) -> AudioSegment:
    return sum(beats)