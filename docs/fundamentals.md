# Installation and Usage

These are the details you need to follow in order to make Simone work on your local system.

## Dependencies

Karpathaize requires the following dependencies to be installed on your system:

- **FFmpeg:** Used for video processing and screenshot extraction. Install FFmpeg from [here](https://ffmpeg.org/download.html).
- **Tesseract OCR Engine:** Used for text recognition in screenshots. Install Tesseract OCR Engine from [here](https://github.com/tesseract-ocr/tesseract).

## Tech Stack

This project leverages the following technologies and libraries:

- **Python:** The core language used for scripting and automation.
- **FFmpeg:** Used for video processing and screenshot extraction.
- **Tesseract OCR Engine:** Used for text recognition in screenshots.
- **Gemma 7B:** Used for generating blog posts and related keywords.
- **OpenRouter:** For using the Gemma 7B free API.

The project also uses other Python libraries for various functionalities. Refer to the `requirements.txt` file for a full list of dependencies.

## Installation

This is how you can install Simone locally:

- Clone the repository:
```
git clone https://github.com/rajtilakjee/simone.git
```
- Navigate to the project directory:
```
cd simone
```
- Install dependencies:
```
pip install -r requirements.txt
```

## Usage

Post installation, this is how to run Simone:

- Run the script:

```
python main.py
```
