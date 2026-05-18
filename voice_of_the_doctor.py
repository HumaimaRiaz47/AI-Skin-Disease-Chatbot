#Step1a: Setup Text to Speech–TTS–model with gTTS

import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="Hi this is Ai with me!"
text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

#Step1b: Setup Text to Speech–TTS–model with ElevenLabs

from elevenlabs.client import ElevenLabs
from elevenlabs.play import save  # for saving audio

# Set your Eleven Labs API key
ELEVENLABS_API_KEY = "sk_881507b1eb823871da893cdc12f16703d3cbbc403047aef3"

# Initialize client
client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

# Step 1: Get available voices
voices_response = client.voices.get_all()  # returns GetVoicesResponse
voices = voices_response.voices          # actual list of Voice objects

if not voices:
    raise ValueError("No voices available in your Eleven Labs account!")

# Pick the first available voice
voice = voices[0]
print(f"Using voice: {voice.name} (ID: {voice.voice_id})")

# Step 2: Function to convert text to speech
def text_to_speech_with_elevenlabs(input_text, output_filepath):
    audio = client.text_to_speech.convert(
        text=input_text,
        voice_id=voice.voice_id,   # Use actual voice_id
        model_id="eleven_turbo_v2",
        output_format="mp3_22050_32"
    )
    save(audio, output_filepath)
    print(f"Saved audio to {output_filepath}")

# Example usage
input_text = "Hello, this is a test from Eleven Labs"
text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing.mp3")




#Step2: Use Model for Text output to Voice
from gtts import gTTS
from playsound import playsound

def text_to_speech_with_gtts(input_text, output_filepath):
    """
    Converts the given text to speech using gTTS, saves it to a file, and plays it.

    Args:
        input_text (str): The text to convert to speech.
        output_filepath (str): The path where the audio file will be saved (e.g., "output.mp3").
    """
    try:
        # Convert text to speech
        tts = gTTS(text=input_text, lang="en", slow=False)
        tts.save(output_filepath)
        print(f"Saved audio to {output_filepath}")

        # Play the audio file
        playsound(output_filepath)

    except Exception as e:
        print(f"An error occurred in text_to_speech_with_gtts: {e}")


# Example usage

input_text = "Welcome! I am your AI Doctor assistant " 
#text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")

from elevenlabs import ElevenLabs, save
from playsound import playsound  

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    # Initialize ElevenLabs client
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    
    # Generate audio using the updated method
    audio = client.text_to_speech.convert(
        text=input_text,
        voice_id=voice.voice_id,   # Use actual voice_id
        model_id="eleven_turbo_v2",
        output_format="mp3_22050_32"
    )
    
    # Save audio
    save(audio, output_filepath)
    print(f"Saved audio to {output_filepath}")
    
    # Play audio
    try:
        playsound(output_filepath)
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")