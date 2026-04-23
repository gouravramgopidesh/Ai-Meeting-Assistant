# 🧠 AI Meeting Summarizer

An intelligent AI-powered application that summarizes meeting content from **text input** or **audio (MP3 files)**.
It uses **speech recognition + NLP models** to generate concise summaries, key points, and actionable insights.

---

## 🚀 Features

* 🎤 **Audio to Text Conversion** (MP3 support)
* ✍️ **Text-based Meeting Input**
* 📌 **Automatic Summary Generation**
* 🔑 **Key Points Extraction**
* ✅ **Action Item Detection**
* ⚡ Lightweight and optimized for low-RAM systems

---

## 🛠️ Tech Stack

* **Frontend/UI:** Streamlit
* **Speech Recognition:** OpenAI Whisper
* **NLP Model:** Hugging Face Transformers (FLAN-T5)
* **Language:** Python

---

## 📂 Project Structure

```
ai_meeting_summarizer/
│
├── app.py              # Main Streamlit app
├── summarize.py        # NLP summarization logic
├── transcribe.py       # Audio to text conversion
├── requirements.txt    # Dependencies
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/ai-meeting-summarizer.git
cd ai-meeting-summarizer
```

---

### 2. Create virtual environment (recommended)

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
streamlit run app.py
```

---

## 📸 How It Works

1. Choose input type:

   * Text input
   * Audio (MP3 upload)

2. If audio is uploaded:

   * Converted to text using Whisper

3. The system:

   * Generates summary
   * Extracts key points
   * Identifies action items

---

## 💡 Example Use Cases

* Business meetings
* Online lectures
* Interview recordings
* Team discussions

---

## ⚡ Performance Optimization

* Uses **lightweight FLAN-T5 model** instead of heavy BART
* Whisper base model for efficient transcription
* Designed to run on systems with limited RAM

---

## 🧠 Future Improvements

* Speaker identification
* Timestamp-based summaries
* Export summaries to PDF
* Integration with GPT APIs for advanced summarization

---

## 🤝 Contribution

Contributions are welcome!
Feel free to fork this repository and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Developed by G.V.S GOURAV RAM

---

## ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub!
