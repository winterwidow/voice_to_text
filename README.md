# voice_to_text

## **transcribe_audio function:**

- The speech_recognition library processes the audio file.
- The function recognize_google(audio) transcribes the speech to text.

## **clean_audio function:**

- The transcribed text is passed through clean_text().
- It removes unwanted characters, special symbols, and normalizes the text.

## **summarize_text function:**

- The cleaned text is summarized using a pre-trained NLP model (pipeline("summarization")).
- This model condenses long speech into concise key points.

##**upload_file function:**

- The Tkinter GUI lets the user select an audio file using filedialog.askopenfilename().
- The selected file is passed to the transcribe_audio() function
- The transcription and summary are updated dynamically in Tkinter labels (label_transcription and label_summary), and result sare displayed.

