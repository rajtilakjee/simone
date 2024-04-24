# Downloader Class

## Description

The `Downloader` class provides methods for downloading audio and video files from YouTube using the pytube library.

## Class Definition
```python
from __future__ import annotations
from pytube import YouTube

class Downloader:
    def __init__(self, url: str):
        """
        Initialize the Downloader instance.

        Parameters:
            url : str
                The YouTube video URL to download.
        """
        pass

    def audio(self):
        """
        Download the audio-only version of the YouTube video.
        """
        pass

    def video(self):
        """
        Download the highest resolution video of the YouTube video.
        """
        pass
```
## Methods

`__init__(url)`
- Initializes a Downloader instance with the provided YouTube video URL (url).

`audio()`
- Downloads the audio-only version of the YouTube video.

`video()`
- Downloads the highest resolution video of the YouTube video.

## Example Usage
```python
# Initialize Downloader instance
downloader = Downloader(url="https://www.youtube.com/watch?v=VIDEO_ID")

# Download audio-only version
downloader.audio()

# Download highest resolution video
downloader.video()
```
## Usage Notes

- Ensure you have the pytube library installed (pip install pytube).
- Provide a valid YouTube video URL when initializing the Downloader instance.
- The audio() method downloads the audio-only version of the video and saves it as "audio.mp4" in the current directory.
- The video() method downloads the highest resolution video and saves it as "video.mp4" in the current directory.

## Dependencies

- pytube: Used for downloading YouTube videos.

## Related Links

- pytube Documentation
- YouTube API
