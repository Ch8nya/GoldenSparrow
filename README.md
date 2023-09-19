# VideoAndSubtitlesDubber

This is a Python program that translates the video in one language to another using Google Translate. It uses the whisper-timestamped package for segmenting the audio and translating it.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7+
- A virtual environment (venv)
- [whisper-timestamped](https://github.com/linto-ai/whisper-timestamped) library
- Other Python libraries: moviepy, googletrans, gtts, pysrt

### Installing

1. Clone the repository:
bash git clone https://github.com/Ch8nya/VideoAndSubtitlesDubber.git 
cd VideoAndSubtitlesDubber


2. Create a virtual environment and activate it:
bash python3 -m venv venv source venv/bin/activate


3. Install the necessary libraries:
bash pip install -r requirements.txt

## Whisper-Timestamped Installation

VideoAndSubtitlesDubber uses the Whisper-Timestamped tool for multilingual automatic speech recognition with word-level timestamps and confidence. This tool is necessary for accurate voice dubbing as well as subtile file (.srt) creation.

To install Whisper-Timestamped, first ensure that you have Python3 (version 3.7 or higher, 3.9 is recommended) and ffmpeg installed on your system. If not, follow the instructions on the Whisper repository here.

For a light installation suitable for CPU, install a light version of torch before installing whisper-timestamped. Run the following commands:
pip3 install torch torchaudio

Then, clone the whisper-timestamped repository and install it:
git clone https://github.com/linto-ai/whisper-timestamped
cd whisper-timestamped/
python3 setup.py install

 To make sure that whisper is installed run this on your command line
 whisper_timestamped --help

## Running the Program

1. Activate the virtual environment:
bash source venv/bin/activate


2. Run the main Python script:
bash python main.py

Follow the prompts to enter the video path and choose the language for translation.
