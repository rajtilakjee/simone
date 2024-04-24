from __future__ import annotations

import cv2
import pytesseract
from pytesseract import Output


class Scorer:
    def __init__(self, frames, keywords):
        self.frames = frames
        self.keywords = keywords

    def score_frames(self):
        pytesseract.pytesseract.tesseract_cmd = (
            "C:/Program Files/Tesseract-OCR/tesseract.exe"
        )
        scores = []
        for frame in self.frames:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            extracted_text = pytesseract.image_to_string(
                gray_frame,
                config="--psm 6",
                output_type=Output.STRING,
            )

            frame_score = 0
            for keyword in self.keywords:
                if keyword.lower() in extracted_text.lower():
                    frame_score += 1

            scores.append(frame_score)
        return scores
