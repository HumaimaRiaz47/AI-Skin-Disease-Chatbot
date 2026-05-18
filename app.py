# app.py

import os
import tempfile
import gradio as gr
from brain__of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patients import transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_elevenlabs

# SYSTEM PROMPT
system_prompt = """
You have to act as a professional doctor, i know you are not but this is for learning purpose. 
What's in this image?. Do you find anything wrong with it medically? 
If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
Donot say 'In the image I see' but say 'With what I see, I think you have ....'
Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
Keep your answer concise (max 2 sentences). No preamble, start your answer right away please
"""

# PROCESS INPUTS FUNCTION
def process_inputs(audio_filepath, image_filepath):
    # Step 1: Convert speech to text
    speech_to_text_output = transcribe_with_groq(
        GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
        audio_filepath=audio_filepath,
        stt_model="whisper-large-v3"
    )

    # Step 2: Analyze image (if provided)
    if image_filepath:
        doctor_response = analyze_image_with_query(
            query=system_prompt + speech_to_text_output, 
            encoded_image=encode_image(image_filepath), 
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )
    else:
        doctor_response = "No image provided for me to analyze"

    # Step 3: Convert doctor response to speech
    output_audio_path = os.path.join(tempfile.gettempdir(), "final.mp3")
    text_to_speech_with_elevenlabs(
        input_text=doctor_response, 
        output_filepath=output_audio_path
    )

    # Step 4: Return results
    return speech_to_text_output, doctor_response, output_audio_path

# GRADIO INTERFACE
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath", label="Your Question (Voice)"),
        gr.Image(type="filepath", label="Medical Image (Optional)")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(type="filepath", label="Doctor's Voice Response")
    ],
    title="AI Doctor with Vision and Voice",
    description="Upload your question via voice and optionally a medical image. Get AI doctor diagnosis and voice response."
)

# LAUNCH APP
if __name__ == "__main__":
    iface.launch(debug=True)
