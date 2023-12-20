import subprocess
import sys


def convert(video):
    cmd = [
        "ffmpeg",
        "-i",
        video,
        "-vn",
        "-acodec",
        "libmp3lame",
        "-ab",
        "192k",
        "-ar",
        "44100",
        "-y",
        "audio.mp3",
    ]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print("conversion error")


if len(sys.argv) != 2:
    print("USAGE: py converter.py <video>")
else:
    convert(sys.argv[1])
