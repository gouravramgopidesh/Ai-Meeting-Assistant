from transformers import pipeline
import re

# Initialize summarizer with error handling
try:
    summarizer = pipeline("text2text-generation", model="google/flan-t5-base")
except Exception as e:
    print(f"Warning: Could not load model: {e}")
    summarizer = None

def generate_summary(text):
    """Generate a summary of the meeting text."""
    if not text or len(text.strip()) < 10:
        return "Text too short to summarize."
    
    try:
        if summarizer:
            prompt = f"Summarize the following meeting:\n{text}"
            result = summarizer(prompt, max_length=150, do_sample=False)
            return result[0]['generated_text']
        else:
            # Fallback: return first few sentences
            sentences = re.split(r'[.!?]+', text)
            return ". ".join([s.strip() for s in sentences[:2] if s.strip()]) + "."
    except Exception as e:
        return f"Error generating summary: {str(e)}"


def extract_key_points(text):
    """Extract key points from the text."""
    sentences = re.split(r'[.!?]+', text)
    points = [s.strip() for s in sentences if len(s.strip()) > 10]
    return points[:5]


def extract_action_items(text):
    """Extract action items from the text."""
    keywords = ["should", "must", "need to", "action", "todo", "deadline", "responsible", "will"]
    actions = []

    sentences = re.split(r'[.!?]+', text)
    for sentence in sentences:
        if any(word in sentence.lower() for word in keywords) and len(sentence.strip()) > 5:
            actions.append(sentence.strip())

    return actions[:5]