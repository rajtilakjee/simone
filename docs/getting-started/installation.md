# Installation and Usage

These are the details you need to follow in order to make Simone work on your local system. Before installing Simone, you need to install the [dependencies](https://rajtilakjee.github.io/simone/getting-started/dependencies/).

### Install FFMPEG:

1. Download it from the following link: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Follow the instructions on the screen to install it.

### Install Tesseract OCR:

1. Visit the following page for detailed instructions on how to install Tesseract OCR in your system: [https://tesseract-ocr.github.io/tessdoc/Installation.html](https://tesseract-ocr.github.io/tessdoc/Installation.html)

> [!IMPORTANT]
> Remember to find out the path where Tesseract OCR was installed in your system. You'll need this during execution of the program.

### Gemma 7B API Key:

1. Register at [OpenRouter](https://openrouter.ai/)
2. Get an API Key

## Installation

Now that you have installed the dependencies, you can follow these steps to install Simone locally:

- Clone the repository:
```
git clone https://github.com/rajtilakjee/simone.git
```
- Navigate to the project directory:
```
cd simone
```
- Install requirements:
```
pip install -r requirements.txt
```

## Usage

Post installation, this is how to run Simone:

- Run the script:

```
python main.py
```
