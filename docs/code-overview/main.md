# Point of Entry

## Description

This script automates the process of generating a blog post from a YouTube video by performing the following steps:

1. Downloads the audio and video from the YouTube video.
2. Transcribes the audio into text.
3. Generates a summary of keywords from the transcription.
4. Creates a blog post using the generated summary.
5. Extracts frames from the video and scores them based on the keywords.
6. Saves the best frames as images.

## Usage

1. Make sure you have set up the necessary environment variables and installed the required libraries.
2. Run the script and provide the YouTube URL when prompted.

## Steps

1. Enter YouTube URL: [Provide the YouTube video URL]
2. The script will download the audio and video, transcribe the audio, generate a summary of keywords, create a blog post, extract frames, score them, and save the best frames.

## Dependencies

- Python libraries:
  - `requests`: Used for making HTTP requests.
  - `dotenv`: Used for loading environment variables from a `.env` file.

- Custom utility modules:
  - `Downloader`: Downloads audio and video from YouTube.
  - `Transcriber`: Transcribes audio files into text.
  - `Summarizer`: Generates keyword summaries from text content using an API.
  - `Blogger`: Generates blog posts using keyword summaries.
  - `Framer`: Extracts frames from videos.
  - `Scorer`: Scores frames based on keywords.
  - `Saver`: Saves the best frames as images.

## Related Links

- [requests Documentation](https://docs.python-requests.org/en/master/)
- [dotenv Documentation](https://pypi.org/project/python-dotenv/)
