import google.generativeai as genai
from config import Config

genai.configure(api_key=Config.GEMINI_API_KEY)

def generate_post(topic="Computer Vision"):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"""
    Write a highly professional 150-word LinkedIn post about {topic}. 
    Keep it factual, clean, and concrete. 
    Strict formatting rules: Do not use emoji icons, do not use em dashes, and do not use vague AI-style copy.
    Include 2 relevant hashtags at the very end.
    """
    response = model.generate_content(prompt)
    return response.text