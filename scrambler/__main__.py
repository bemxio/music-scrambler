from typing import Optional
from pathlib import Path
import argparse

from pydub import AudioSegment

import scrambler

def main(input_path: Path, bpm: int, output_path: Optional[Path] = None, function: Optional[str] = None, repeat: int = 1):
    output_path = output_path or input_path.with_stem(f"{input_path.stem}_{function}")
    
    audio = AudioSegment.from_file(input_path, format=input_path.suffix[1:])
    beats = scrambler.split_into_beats(audio, bpm)

    match function.lower():
        case "repeat":
            beats = scrambler.repeat(beats, repeat)
        case "reverse":
            beats = scrambler.reverse(beats)
        case _:
            raise ValueError("function name is not implemented")

    audio = scrambler.join_beats(beats)

    audio.export(output_path, format=output_path.suffix[1:])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scramble a song by the beats in various ways.")

    parser.add_argument("input_path", type=Path, help="The input path to an audio file with the song.")
    parser.add_argument(
        "--output_path", "-o",
        type=Path, 
        help="The output path, where the modified song will be saved."
    )
    parser.add_argument(
        "--bpm",
        type=int,
        help="The number of beats per minute of the song."
    )
    parser.add_argument(
        "--function", "-f",
        type=str,
        help="The scrambling function, that will modify the song. The ones that are currently implemented are `repeat` and `reverse`."
    )
    parser.add_argument(
        "--repeat", "-r",
        type=int,
        help="The beat to repeat, when using the `repeat` function.",
        default=1
    )

    main(**vars(parser.parse_args()))