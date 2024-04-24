from __future__ import annotations

import json
import os

import requests
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


def blogpost(url):
    downloads = Downloader(url)
    downloads.audio()
    downloads.video()

    transcription_file = Transcriber("audio.mp4")
    transcription_file.transcribe()

    keywords = Summarizer(api_key, "transcription.txt")
    keyword = keywords.generate_summary()

    blogpost = Blogger(api_key, "transcription.txt", "generated_blogpost.txt")
    blogpost.generate_blogpost()

    frames = Framer("video.mp4")
    frame = frames.get_video_frames()

    scores = Scorer(frame, keyword)
    score = scores.score_frames()

    save = Saver(frame, score)
    save.save_best_frames()


if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    blogpost(url)
