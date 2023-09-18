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


## Running the Program

1. Activate the virtual environment:
bash source venv/bin/activate


2. Run the main Python script:
bash python main.py

Follow the prompts to enter the video path and choose the language for translation.
