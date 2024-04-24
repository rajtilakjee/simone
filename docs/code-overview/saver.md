# Saver Class

## Description

The `Saver` class provides functionality for saving the best frames from a list of frames based on their scores using the OpenCV and NumPy libraries.

## Class Definition
```python
from __future__ import annotations
import cv2
import numpy as np

class Saver:
    def __init__(self, frames: list, scores: list):
        """
        Initialize the Saver instance.

        Parameters:
            frames : list
                A list of frames (images) to be saved.
            scores : list
                A list of scores corresponding to the frames.
        """
        pass

    def save_best_frames(self):
        """
        Save the best frames based on their scores.

        Notes:
            Assumes that the frames and scores lists are non-empty and have the same length.
        """
        pass
```
## Methods

`__init__(frames, scores)`
- Initializes a Saver instance with the provided lists of frames and scores.

`save_best_frames()`
- Saves the best frames from the list based on their scores.

## Example Usage
```python
# Assuming 'frames' and 'scores' are defined elsewhere
frames = [...]  # List of frames
scores = [...]  # List of scores

# Initialize Saver instance
saver = Saver(frames=frames, scores=scores)

# Save the best frames
saver.save_best_frames()
```
## Usage Notes

- Ensure you have the OpenCV (cv2) and NumPy (np) libraries installed (pip install opencv-python numpy).
- Provide non-empty lists of frames and scores when initializing the Saver instance.
- The save_best_frames() method saves the top three frames with the highest scores as JPEG images.

## Dependencies

- cv2 (OpenCV): Used for image processing and saving images.
- numpy: Used for numerical computations and array manipulations.

## Related Links

- OpenCV Documentation
- NumPy Documentation
