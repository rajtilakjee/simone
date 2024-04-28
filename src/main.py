from __future__ import annotations

import os

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


if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    path_to_tesseract = input(
        "Please enter the path where Tesseract is installed in your system: ",
    )

    print("Downloading audio and video...")
    downloads = Downloader(url)
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

    scores = Scorer(frame, keyword, path_to_tesseract)
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
