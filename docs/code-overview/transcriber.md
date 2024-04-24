# Transcriber Class

## Description

The `Transcriber` class provides functionality for transcribing audio files using the whisper library.

## Class Definition
```python
from __future__ import annotations
import whisper
from whisper.utils import get_writer

class Transcriber:
    def __init__(self, filename: str):
        """
        Initialize the Transcriber instance.

        Parameters:
            filename : str
                The filename of the audio file to transcribe.
        """
        pass

    def transcribe(self):
        """
        Transcribe the audio file and save the transcription in a text file (UTF-8) and an SRT file.

        Notes:
            The transcription text file will be named "transcription.txt" in the current directory.
            The SRT file will be created in the specified output directory (default: "./").
        """
        pass
```
## Methods

`__init__(filename)`
- Initializes a Transcriber instance with the provided audio file filename.

`transcribe()`
- Transcribes the audio file and saves the transcription in a text file (UTF-8) and an SRT file.

## Example Usage
```python
# Initialize Transcriber instance
transcriber = Transcriber(filename="audio.wav")

# Transcribe the audio file
transcriber.transcribe()
```
## Usage Notes

- Ensure you have the whisper library installed (pip install whisper).
- Provide the correct audio file filename when initializing the Transcriber instance.
- The transcribe() method transcribes the audio file using the whisper library and saves the transcription in a text file named "transcription.txt" and an SRT file.

## Dependencies

- whisper: Used for audio transcription.

## Related Links

- whisper Documentation
