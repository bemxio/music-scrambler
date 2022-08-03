# Music Scrambler
A Python project to split a song by the song's beats, and then mess the order of the beats in various ways.

Made for fun, inspired by [these](https://www.youtube.com/watch?v=09tzb8lkMwE) kinds of videos.

## Setup
Obviously, you will need [Python](https://www.python.org/) to run it. Make sure the version is 3.10 though.

You will also need to install `ffmpeg` for a wider support of audio formats.

For Linux systems, install it using your package manager.
For Windows peeps, follow [this](https://www.wikihow.com/Install-FFmpeg-on-Windows) tutorial.

1. Clone this repository somewhere on your computer.
2. Install the project's requirements using `python -m pip install -r requirements.txt`.
3. Done! Everything should be working nicely now.

## Usage
Simply run:
```sh
python -m scrambler --help
```

to find out all of the available options you can use.