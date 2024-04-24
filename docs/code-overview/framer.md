# Framer Class

## Description

The `Framer` class provides functionality for extracting frames from a video file using the OpenCV library.

## Class Definition
```python
from __future__ import annotations
import cv2

class Framer:
    def __init__(self, filename: str):
        """
        Initialize the Framer instance.

        Parameters:
            filename : str
                The filename of the video file to extract frames from.
        """
        pass

    def get_video_frames(self):
        """
        Extract frames from the video file.

        Returns:
            list
                A list of frames extracted from the video.
        """
        pass
```
## Methods

`__init__(filename)`
- Initializes a Framer instance with the provided video file filename.

`get_video_frames()`
- Extracts frames from the video file and returns a list of frames.

## Example Usage
```python
# Initialize Framer instance
framer = Framer(filename="video.mp4")

# Get video frames
frames = framer.get_video_frames()
```
## Usage Notes

- Ensure you have the OpenCV library installed (pip install opencv-python).
- Provide the correct video file filename when initializing the Framer instance.
- The get_video_frames() method extracts frames from the video file and returns them as a list of frames.

## Dependencies

- cv2 (OpenCV): Used for working with images and videos.

## Related Links

- OpenCV Documentation
