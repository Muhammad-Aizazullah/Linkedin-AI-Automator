import google.generativeai as genai
from config import Config

genai.configure(api_key=Config.GEMINI_API_KEY)

def get_trending_topic():
    # Model name changed to gemini-pro
    model = genai.GenerativeModel('gemini-pro')
    prompt = "Suggest one highly specific, trending technical topic in Computer Vision right now. Return only the topic name, no extra text."
    response = model.generate_content(prompt)
    return response.text.strip()