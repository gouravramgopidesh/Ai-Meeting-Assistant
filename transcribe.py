import whisper
import os

# Load model once (important for speed)
try:
    model = whisper.load_model("base")
except Exception as e:
    print(f"Warning: Could not load whisper model: {e}")
    model = None

def transcribe_audio(file_path):
    """Transcribe audio file to text."""
    if not os.path.exists(file_path):
        return "Error: File not found"
    
    try:
        if model:
            result = model.transcribe(file_path)
            return result["text"]
        else:
            return "Error: Whisper model not loaded"
    except Exception as e:
        return f"Error transcribing audio: {str(e)}"