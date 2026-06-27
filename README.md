# 🩺 AI Skin Disease Chatbot

An AI-powered Skin Disease Chatbot that combines **Computer Vision**, **Large Language Models**, **Speech Recognition**, and **Text-to-Speech** to provide an interactive dermatology assistant.

Instead of relying entirely on a Large Language Model to diagnose skin conditions, this project first uses a **fine-tuned EfficientNet-B0 deep learning model** to classify skin diseases from uploaded images. The predicted disease and confidence score are then provided to **Llama 4 (Groq)**, which generates a clear, natural-language explanation for the user.

The chatbot also supports **voice-based interaction** using Whisper Speech-to-Text and ElevenLabs Text-to-Speech, allowing users to ask questions and receive spoken responses.

---

# 🚀 Features

* 🩺 AI Skin Disease Classification
* 🧠 EfficientNet-B0 Deep Learning Model
* 📷 Upload Skin Images
* 🎤 Voice-to-Text using Groq Whisper
* 🤖 AI Medical Explanation using Llama 4
* 🔊 AI Voice Response using ElevenLabs
* 🌐 Interactive Gradio Web Interface
* 📊 Disease Confidence Score
* 🧩 Modular Python Architecture
* ⚡ Fast Groq Inference
* 💻 Cross Platform (Windows, Linux, macOS)

---

# 🏗️ System Architecture

```
                     User

            Upload Image + Voice

                     │

         ┌───────────┴───────────┐

         │                       │

         ▼                       ▼

   Skin Image              Voice Question

         │                       │

         ▼                       ▼

 EfficientNet-B0            Whisper STT

         │                       │

         ▼                       ▼

 Disease Prediction        Speech-to-Text

         └───────────┬───────────┘

                     ▼

            Llama 4 (Groq API)

                     ▼

      AI Medical Explanation

                     ▼

      ElevenLabs Text-to-Speech

                     ▼

            Gradio Web Interface
```

---

# 📁 Project Structure

```
AI_Skin_Disease_Chatbot/

│

├── app.py
├── skin_classifier.py
├── brain_of_the_doctor.py
├── voice_of_the_patient.py
├── voice_of_the_doctor.py

│
├── models/
│     └── final_model.pth

│
├── notebooks/
│     ├── 01_EDA.ipynb
│     ├── 02_Preprocessing.ipynb
│     ├── 03_Train_EfficientNet.ipynb
│     ├── 04_Evaluation.ipynb
│     └── 05_Prediction.ipynb

│
├── dataset/

├── requirements.txt

├── .env

└── README.md
```

---

# 🧠 Deep Learning Model

Model:

* EfficientNet-B0

Framework:

* PyTorch

Input Size:

* 224 × 224 RGB Images

Number of Classes:

* 22 Skin Diseases

Transfer Learning:

* ImageNet Pretrained Weights

Training Strategy:

* Fine-Tuning

Loss Function:

* Cross Entropy Loss

Optimizer:

* Adam

Learning Rate:

* 0.0001

Epochs:

* 15

---

# 📊 Model Performance

| Metric        | Score  |
| ------------- | ------ |
| Test Accuracy | 77.88% |
| Precision     | 78.40% |
| Recall        | 77.88% |
| F1 Score      | 77.85% |

---

# 🩺 Supported Skin Diseases

* Acne
* Actinic Keratosis
* Benign Tumors
* Bullous Disease
* Candidiasis
* Drug Eruption
* Eczema
* Infestations / Bites
* Lichen
* Lupus
* Moles
* Psoriasis
* Rosacea
* Seborrheic Keratoses
* Skin Cancer
* Sun Damage
* Tinea
* Unknown / Normal
* Vascular Tumors
* Vasculitis
* Vitiligo
* Warts

---

# ⚙️ Tech Stack

### Deep Learning

* PyTorch
* TorchVision
* EfficientNet-B0

### Generative AI

* Groq API
* Llama 4 Scout

### Speech AI

* Whisper Large V3
* ElevenLabs

### Computer Vision

* OpenCV
* Pillow

### Frontend

* Gradio

### Utilities

* NumPy
* Pandas
* Matplotlib
* Scikit-Learn

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```
GROQ_API_KEY=YOUR_GROQ_API_KEY

ELEVENLABS_API_KEY=YOUR_ELEVENLABS_API_KEY
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Skin-Disease-Chatbot.git

cd AI-Skin-Disease-Chatbot
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:7860
```

---

# 🧪 Workflow

1. Upload a skin image.
2. Ask your question using your microphone.
3. Whisper converts speech into text.
4. EfficientNet predicts the skin disease.
5. The prediction and confidence score are sent to Llama.
6. Llama generates a medical explanation.
7. ElevenLabs converts the explanation into speech.
8. Gradio displays the complete response.

---

# 📸 Example Output

```
Predicted Disease

Vitiligo

Confidence

97.45%

Question

How can I treat this condition?

AI Response

Vitiligo is a skin condition that causes patches of skin to lose their natural pigment. Although it is generally not harmful, treatment options include topical medications and light therapy. It is recommended to consult a dermatologist for confirmation and appropriate treatment.
```

---

# 🔮 Future Improvements

* Retrieval-Augmented Generation (RAG)
* Medical Knowledge Base
* Top-3 Disease Predictions
* Confidence Visualization
* Patient Report Generation (PDF)
* Conversation Memory
* MongoDB Integration
* User Authentication
* Cloud Deployment
* Mobile Application

---

# ⚠️ Disclaimer

This project is intended **only for educational and research purposes**.

The predictions generated by the deep learning model and the explanations produced by the Large Language Model **must not be considered professional medical advice, diagnosis, or treatment**.

Always consult a qualified healthcare professional or dermatologist for any medical concerns.

---

# 📜 License

This project is released under the MIT License.

---

# 👩‍💻 Author

**Humaima Riaz**

Artificial Intelligence • Computer Vision • Generative AI • Deep Learning

---

⭐ If you found this project useful, please consider giving it a star on GitHub.
