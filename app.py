import streamlit as st
from summarize import generate_summary, extract_key_points, extract_action_items
from transcribe import transcribe_audio
import tempfile
import os

st.set_page_config(page_title="AI Meeting Summarizer", layout="wide")

st.title("🧠 AI Meeting Summarizer")
st.markdown("Convert meeting recordings or text into actionable summaries")

# Sidebar for settings
with st.sidebar:
    st.header("Settings")
    max_summary_length = st.slider("Summary Length", 50, 300, 150)

option = st.radio("Choose Input Type:", ["Text", "Audio"])

text_data = ""

# TEXT INPUT
if option == "Text":
    text_data = st.text_area("Enter Meeting Text", height=200, placeholder="Paste your meeting transcript here...")

# AUDIO INPUT
elif option == "Audio":
    uploaded_file = st.file_uploader("Upload Audio File", type=["mp3", "wav", "m4a"])

    if uploaded_file:
        with st.spinner("Transcribing audio..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                tmp.write(uploaded_file.read())
                tmp_path = tmp.name
            
            try:
                text_data = transcribe_audio(tmp_path)
                os.unlink(tmp_path)
                
                st.subheader("📄 Transcribed Text")
                st.write(text_data)
            except Exception as e:
                st.error(f"Transcription error: {str(e)}")

# PROCESS BUTTON
if st.button("Generate Summary", type="primary"):
    if text_data and text_data.strip():
        with st.spinner("Processing..."):
            try:
                summary = generate_summary(text_data)
                key_points = extract_key_points(text_data)
                actions = extract_action_items(text_data)

                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📌 Summary")
                    st.write(summary)
                
                with col2:
                    st.subheader("✅ Action Items")
                    if actions:
                        for i, act in enumerate(actions, 1):
                            st.write(f"{i}. {act}")
                    else:
                        st.info("No clear action items detected.")

                st.subheader("🔑 Key Points")
                if key_points:
                    for point in key_points:
                        st.write(f"• {point}")
                else:
                    st.info("No key points extracted.")
            except Exception as e:
                st.error(f"Processing error: {str(e)}")
    else:
        st.warning("⚠️ Please provide input text or upload an audio file")