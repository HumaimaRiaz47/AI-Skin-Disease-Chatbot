
# from skinClassifier import predict_skin_disease

# image_path = "sample.jpg"   # Change to your image path

# disease, confidence = predict_skin_disease(image_path)

# print(f"Predicted Disease : {disease}")
# print(f"Confidence        : {confidence:.2f}%")


from voice_of_the_patients import transcribe_with_groq

text = transcribe_with_groq("finag fine.mp3")

print(text)