from __future__ import annotations

import whisper
from whisper.utils import get_writer


class Transcriber:
    def __init__(self, filename):
        self.filename = filename

    def transcribe(self):
        output_directory = "./"
        model = whisper.load_model("base")
        result = model.transcribe(self.filename)

        with open("transcription.txt", "w", encoding="utf-8") as txt:
            txt.write(result["text"])

        srt_writer = get_writer("srt", output_directory)
        srt_writer(result, self.filename)
