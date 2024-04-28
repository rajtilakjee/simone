from __future__ import annotations

import os
from typing import Annotated
from typing import Optional

import typer
from dotenv import load_dotenv
from utils.blogger import Blogger
from utils.downloader import Downloader
from utils.framer import Framer
from utils.saver import Saver
from utils.scorer import Scorer
from utils.summarizer import Summarizer
from utils.transcriber import Transcriber


load_dotenv()
api_key = os.getenv("GEMMA_API_KEY")

__version__ = "2.1.0"


def version_callback(value: bool):
    if value:
        print(f"Simone CLI Version: {__version__}")
        raise typer.Exit()


def main(
    url: Annotated[
        str,
        typer.Option(
            help="URL of the YouTube video. Should be within quotes.",
            rich_help_panel="Customization and Utils",
        ),
    ],
    path: Annotated[
        str,
        typer.Option(
            help="Path where Tesseract is installed in your system. Should be within quotes.",
            rich_help_panel="Customization and Utils",
        ),
    ],
    version: Annotated[
        Optional[bool],
        typer.Option("--version", callback=version_callback),
    ] = None,
):

    print("Downloading audio and video...")
    downloads = Downloader(f"{url}")
    downloads.audio()
    downloads.video()

    print("Transcribing audio...")
    transcription_file = Transcriber("audio.mp4")
    transcription_file.transcribe()

    print("Generating keywords...")
    keywords = Summarizer(api_key, "transcription.txt")
    keyword = keywords.generate_summary()

    print("Generating blog post...")
    blogpost = Blogger(api_key, "transcription.txt", "generated_blogpost.txt")
    blogpost.generate_blogpost()

    print("Scoring frames...")
    frames = Framer("video.mp4")
    frame = frames.get_video_frames()

    scores = Scorer(frame, keyword, f"{path}")
    score = scores.score_frames()

    print("Saving screenshots...")
    save = Saver(frame, score)
    save.save_best_frames()

    print("Tidying things up...")
    os.remove("audio.mp4")
    os.remove("audio.srt")
    os.remove("transcription.txt")
    os.remove("video.mp4")

    print("Blog post and 3 screenshots have been generated!")


if __name__ == "__main__":
    typer.run(main)
