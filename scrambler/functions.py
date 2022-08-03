from pydub import AudioSegment
from typing import List

def repeat(beats: List[AudioSegment], beat: int) -> List[AudioSegment]:
    length = len(beats)
    length -= length % 4

    return [beats[index // 4 * 4 + (beat - 1)] for index in range(length)]

def reverse(beats: List[AudioSegment]) -> List[AudioSegment]:
    return beats[::-1]