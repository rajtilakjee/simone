from __future__ import annotations

import cv2
import pytesseract
from pytesseract import Output


class Scorer:
    def __init__(self, frames, keywords, path_to_tesseract):
        self.frames = frames
        self.keywords = keywords
        self.path_to_tesseract = path_to_tesseract

    def score_frames(self):
        pytesseract.pytesseract.tesseract_cmd = self.path_to_tesseract
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
