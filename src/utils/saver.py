from __future__ import annotations

import cv2
import numpy as np


class Saver:
    def __init__(self, frames, scores):
        self.frames = frames
        self.scores = scores

    def save_best_frames(self):
        if self.frames and self.scores and len(self.frames) == len(self.scores):
            scores = np.array(self.scores)
            top_indices = np.argsort(scores)[-3:]
            for i in top_indices:
                frame = self.frames[i]
                score = scores[i]
                file_name = f"top_frame_{i}_score_{score}.jpg"
                cv2.imwrite(file_name, frame)
