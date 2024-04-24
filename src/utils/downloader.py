from __future__ import annotations

from pytube import YouTube


class Downloader:
    def __init__(self, url):
        self.url = url

    def audio(self):
        yt = YouTube(self.url)
        audio = yt.streams.filter(only_audio=True).first()
        try:
            audio.download(filename="audio.mp4")
        except Exception as e:
            print(e)

    def video(self):
        yt = YouTube(self.url)
        video = yt.streams.get_highest_resolution()
        try:
            video.download(filename="video.mp4")
        except Exception as e:
            print(e)
