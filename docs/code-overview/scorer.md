# Scorer Class

## Description

The `Scorer` class provides functionality for scoring frames based on the presence of keywords using the pytesseract library for OCR (Optical Character Recognition) and OpenCV library for image processing.

## Class Definition
```python
from __future__ import annotations
import cv2
import pytesseract
from pytesseract import Output

class Scorer:
    def __init__(self, frames: list, keywords: list):
        """
        Initialize the Scorer instance.

        Parameters:
            frames : list
                A list of frames (images) to be scored.
            keywords : list
                A list of keywords to search for in the frames.
        """
        pass

    def score_frames(self) -> list[int]:
        """
        Score the frames based on the presence of keywords.

        Returns:
            list[int]
                A list of scores corresponding to each frame.
        """
        pass
```
## Methods

`__init__(frames, keywords)`
- Initializes a Scorer instance with the provided lists of frames and keywords.

`score_frames()`
- Scores the frames based on the presence of keywords and returns a list of scores.

## Example Usage
```python
# Assuming 'frames' and 'keywords' are defined elsewhere
frames = [...]  # List of frames
keywords = [...]  # List of keywords

# Initialize Scorer instance
scorer = Scorer(frames=frames, keywords=keywords)

# Score the frames
scores = scorer.score_frames()
```
## Usage Notes

- Ensure you have the pytesseract and OpenCV (cv2) libraries installed (pip install pytesseract opencv-python).
- Provide non-empty lists of frames and keywords when initializing the Scorer instance.
- The score_frames() method uses OCR to extract text from frames and scores each frame based on the presence of keywords.

## Dependencies

- cv2 (OpenCV): Used for image processing.
- pytesseract: Used for Optical Character Recognition (OCR).

## Related Links
- pytesseract Documentation
- OpenCV Documentation
