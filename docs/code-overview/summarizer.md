# Summarizer Class

## Description

The `Summarizer` class provides functionality for generating summaries of text content using the OpenAI API.

## Class Definition
```python
from __future__ import annotations
import json
import requests

class Summarizer:
    def __init__(self, api_key: str, transcription_filename: str):
        """
        Initialize the Summarizer instance.

        Parameters:
            api_key : str
                Your OpenAI API key for authentication.
            transcription_filename : str
                The filename of the transcription file containing content for summarization.
        """
        pass

    def generate_summary(self) -> str:
        """
        Generate a summary of the text content.

        Returns:
            str
                The generated summary.
        """
        pass
```
## Methods

`__init__(api_key, transcription_filename)`
- Initializes a Summarizer instance with the provided OpenAI API key and transcription filename.

`generate_summary()`
- Generates a summary of the text content using the OpenAI API and returns it.

## Example Usage
```python
# Initialize Summarizer instance
summarizer = Summarizer(api_key="YOUR_API_KEY", transcription_filename="transcription.txt")

# Generate summary
summary = summarizer.generate_summary()
```
## Usage Notes

- Ensure you have a valid OpenAI API key (api_key) before using the Summarizer class.
- Provide the correct filename for the transcription file (transcription_filename).
- The generate_summary() method sends the text content to the OpenAI API and retrieves a summary.

## Dependencies

- json: Used for JSON handling.
- requests: Used for making HTTP requests to the OpenAI API.

## Related Links

- OpenAI API Documentation
- Requests Library Documentation
