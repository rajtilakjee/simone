from __future__ import annotations

import cv2


class Framer:
    def __init__(self, filename):
        self.filename = filename
        self.num_frames = 10

    def get_video_frames(self):
        frames = []
        cap = cv2.VideoCapture(self.filename)

        if cap.isOpened():
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            interval = int(total_frames / self.num_frames)
            for i in range(total_frames):
                ret, frame = cap.read()
                if ret:
                    if i % interval == 0:
                        frames.append(frame)
                else:
                    break
            cap.release()
        return frames
