import speech_recognition as sr
import re
from transformers import pipeline
import tkinter as tk
from tkinter import filedialog

# Initialize speech recognizer
recognizer = sr.Recognizer()


# to get the audio to convert to text
def transcribe_audio(audio_file):

    with sr.AudioFile(audio_file) as source:

        audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio)
            return text

        except sr.UnknownValueError:
            return "Could not understand audio"

        except sr.RequestError:
            return "API unavailable"


# cleaning and normalisation
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
    return text


# to summarize the converted text
def summarize_text(text):
    summarizer = pipeline("summarization")
    return summarizer(text, max_length=50, min_length=20, do_sample=False)[0][
        "summary_text"
    ]


# gui using tkinter
def upload_file():

    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])

    if file_path:
        transcription = transcribe_audio(file_path)
        label_transcription.config(text=f"Transcribed Text:\n{transcription}")

        if transcription not in ["Could not understand audio", "API unavailable"]:
            summary = summarize_text(transcription)
            label_summary.config(text=f"Summary:\n{summary}")


# Example usage

root = tk.Tk()
root.title("Voice-to-Text Generator")

button_upload = tk.Button(root, text="Upload Audio", command=upload_file)
button_upload.pack(pady=10)

label_transcription = tk.Label(
    root, text="Transcription will appear here", wraplength=400, justify="left"
)
label_transcription.pack(pady=5)

label_summary = tk.Label(
    root, text="Summary will appear here", wraplength=400, justify="left"
)
label_summary.pack(pady=5)

root.mainloop()
