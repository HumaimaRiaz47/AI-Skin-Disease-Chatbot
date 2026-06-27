"""
app.py

AI Skin Disease Chatbot

Pipeline

Patient Voice
        │
        ▼
Whisper
        │
        ▼
Speech To Text
        │
        ▼
EfficientNet Skin Classifier
        │
        ▼
Disease + Confidence
        │
        ▼
Llama
        │
        ▼
Medical Explanation
        │
        ▼
ElevenLabs
        │
        ▼
Voice Response
"""

import os
import tempfile
import gradio as gr

from dotenv import load_dotenv

from skinClassifier import predict_skin_disease
from brain__of_the_doctor import generate_medical_response
from voice_of_the_patients import transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_elevenlabs
import uuid

load_dotenv()

# --------------------------------------------------------
# Main Function
# --------------------------------------------------------

def process_inputs(audio_filepath, image_filepath):

    # -------------------------------
    # Validate Image
    # -------------------------------

    if image_filepath is None:

        return (
            "",
            "No Image",
            "0 %",
            "Please upload a skin image.",
            None
        )

    # -------------------------------
    # Speech To Text
    # -------------------------------

    speech_text = ""

    if audio_filepath is not None:

        try:

            speech_text = transcribe_with_groq(
                audio_filepath
            )

        except Exception as e:

            speech_text = f"Speech Recognition Error: {e}"

    else:

        speech_text = "No voice question provided."

    # -------------------------------
    # Predict Disease
    # -------------------------------

    disease, confidence = predict_skin_disease(
        image_filepath
    )

    # -------------------------------
    # Generate Explanation
    # -------------------------------

    doctor_response = generate_medical_response(
        disease=disease,
        confidence=confidence,
        patient_question=speech_text
    )

    # -------------------------------
    # Convert To Voice
    # -------------------------------

    output_audio = os.path.join(
        tempfile.gettempdir(),
        f"{uuid.uuid4()}.mp3"
    )

    text_to_speech_with_elevenlabs(
        input_text=doctor_response,
        output_filepath=output_audio
    )

    return (
        speech_text,
        disease,
        f"{confidence:.2f} %",
        doctor_response,
        output_audio
    )

# --------------------------------------------------------
# Gradio UI
# --------------------------------------------------------

with gr.Blocks(
    title="AI Skin Disease Chatbot"
) as demo:

    gr.Markdown(
        """
        # 🩺 AI Skin Disease Chatbot

        Upload a skin image, ask your question using your voice,
        and receive an AI-powered explanation.

        ---
        """
    )

    with gr.Row():

        with gr.Column():

            image_input = gr.Image(
                type="filepath",
                label="📷 Upload Skin Image"
            )

            audio_input = gr.Audio(
                sources=["microphone"],
                type="filepath",
                label="🎤 Ask Your Question"
            )

            submit_btn = gr.Button(
                "🔍 Analyze",
                variant="primary"
            )

        with gr.Column():

            disease_output = gr.Textbox(
                label="🦠 Predicted Disease"
            )

            confidence_output = gr.Textbox(
                label="📊 Confidence"
            )

            speech_output = gr.Textbox(
                label="📝 Speech to Text"
            )

            doctor_output = gr.Textbox(
                label="👨‍⚕️ Doctor Explanation",
                lines=10
            )

            audio_output = gr.Audio(
                label="🔊 Doctor Voice Response",
                type="filepath"
            )

    gr.Markdown("---")

    gr.Markdown(
        """
        ## ⚠️ Medical Disclaimer

        This AI assistant is intended for educational and research purposes only.

        It is **NOT** a substitute for professional medical advice,
        diagnosis, or treatment.

        Always consult a qualified dermatologist for any medical concerns.
        """
    )

    submit_btn.click(
        fn=process_inputs,
        inputs=[
            audio_input,
            image_input
        ],
        outputs=[
            speech_output,
            disease_output,
            confidence_output,
            doctor_output,
            audio_output
        ]
    )

# --------------------------------------------------------
# Launch
# --------------------------------------------------------

if __name__ == "__main__":

    demo.launch(
        debug=True
    )