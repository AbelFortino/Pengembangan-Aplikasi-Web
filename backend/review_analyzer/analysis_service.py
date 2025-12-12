from google import genai
import os

_sentiment_pipeline = None

def get_sentiment_pipeline():
    """Lazy load sentiment pipeline"""
    global _sentiment_pipeline
    if _sentiment_pipeline is None:
        from transformers import pipeline
        _sentiment_pipeline = pipeline(
            "sentiment-analysis", 
            model="finiteautomata/bertweet-base-sentiment-analysis"
        )
    return _sentiment_pipeline

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def analyze_sentiment(text):
    """
    Melakukan analisis sentimen menggunakan Hugging Face pipeline.
    Output: 'POSITIVE', 'NEGATIVE', atau 'NEUTRAL'
    """
    try:
        sentiment_pipeline = get_sentiment_pipeline()
        result = sentiment_pipeline(text)[0]
        label = result['label']
        if label == 'NEG':
            return 'NEGATIVE'
        elif label == 'POS':
            return 'POSITIVE'
        elif label == 'NEU':
            return 'NEUTRAL'
        
        return label.upper()

    except Exception as e:
        print(f"Error during sentiment analysis: {e}")
        return 'NEUTRAL'

def extract_key_points(text):
    """
    Mengekstrak key points dari review menggunakan Gemini.
    """
    try:
        prompt = (
            "Dari ulasan produk berikut, ekstrak 3-5 poin penting (key points) "
            "dalam bentuk daftar poin yang ringkas dan padat. Pisahkan setiap poin "
            "dengan tanda titik koma (;)."
            f"\n\nULASAN: {text}"
            "\n\nKEY POINTS: "
        )
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        print(f"Error during Gemini key points extraction: {e}")
        return "Gagal mengekstrak poin kunci. (Error: API)"