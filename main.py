import os
from moviepy.editor import VideoFileClip, AudioFileClip
from googletrans import Translator
from gtts import gTTS
import whisper_timestamped as whisper
import pysrt


language_choices = {
    0: ('bn', 'Bengali'),
    1: ('gu', 'Gujarati'),
    2: ('hi', 'Hindi'),
    3: ('kn', 'Kannada'),
    4: ('ml', 'Malayalam'),
    5: ('mr', 'Marathi'),
    6: ('ne', 'Nepali'),
    7: ('ta', 'Tamil'),
    8: ('te', 'Telugu'),
    9: ('ur', 'Urdu')
}

video_path = input("Enter the video path: ")


for key, value in language_choices.items():
    print(f"{key}: {value[1]}")
language_choice = int(input("Enter the number corresponding to the language: "))
language_code = language_choices[language_choice][0]

video = VideoFileClip(video_path)
video.audio.write_audiofile("my_audio.wav")

audio = whisper.load_audio("my_audio.wav")
model = whisper.load_model("tiny", device="cpu")
result = whisper.transcribe(model, audio, language="en")
text = result["text"]

subs = pysrt.SubRipFile()
translator = Translator()
for i, segment in enumerate(result["segments"]):
    if "words" in segment:
        sentence = " ".join([word["text"] for word in segment["words"]])  
        translated_sentence = translator.translate(sentence, dest=language_code).text  

        start_word = segment["words"][0]
        end_word = segment["words"][-1]

        start_seconds = int(start_word["start"])
        start_microseconds = int((start_word["start"] - start_seconds) * 1e6)
        end_seconds = int(end_word["end"])
        end_microseconds = int((end_word["end"] - end_seconds) * 1e6)

        start = pysrt.srttime.SubRipTime(0, 0, start_seconds, start_microseconds // 1000)
        end = pysrt.srttime.SubRipTime(0, 0, end_seconds, end_microseconds // 1000)

        item = pysrt.SubRipItem(index=i + 1, start=start, end=end, text=translated_sentence)
        subs.append(item)
subs.save("subtitles.srt", encoding="utf-8")


translated = translator.translate(text, dest=language_code).text

tts = gTTS(text=translated, lang=language_code)
tts.save("my_translated_audio.mp3")

audio = AudioFileClip("my_translated_audio.mp3")
video.set_audio(audio).write_videofile("my_new_video.mp4")

os.remove("my_audio.wav")
os.remove("my_translated_audio.mp3")