import streamlit as st
from tensorflow.keras.models import load_model
from detect import detect_tumor
from PIL import Image
import os

st.set_page_config(page_title="MRI Brain Tumor Detection", layout="centered")

st.title("🧠 MRI Brain Tumor Detection System")

# Load trained model
model = load_model("model.h5")

uploaded_file = st.file_uploader(
    "Upload MRI Image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded MRI Image", width=300)

    if st.button("Detect Tumor"):
        # Save uploaded image temporarily
        with open("temp.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())

        label, confidence = detect_tumor(model, "temp.jpg")

        st.success(f"🩺 Result: **{label}**")
        st.info(f"📊 Confidence: **{confidence * 100:.2f}%**")

        os.remove("temp.jpg")
