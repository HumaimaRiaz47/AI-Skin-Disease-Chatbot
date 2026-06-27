"""
voice_of_the_patient.py

Converts patient's speech into text using
Groq Whisper.
"""

import os
from dotenv import load_dotenv
from groq import Groq

# -----------------------------------
# Load Environment Variables
# -----------------------------------

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if GROQ_API_KEY is None:
    raise ValueError("GROQ_API_KEY not found in .env file")

client = Groq(api_key=GROQ_API_KEY)

# -----------------------------------
# Whisper Model
# -----------------------------------

STT_MODEL = "whisper-large-v3"

# -----------------------------------
# Speech To Text
# -----------------------------------

def transcribe_with_groq(audio_filepath):
    """
    Converts speech to text.

    Parameters
    ----------
    audio_filepath : str

    Returns
    -------
    str
        Transcribed text
    """

    with open(audio_filepath, "rb") as audio_file:

        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model=STT_MODEL,
            language="en",
            response_format="text"
        )

    return transcription