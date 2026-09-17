import google.generativeai as genai
from config import Config

genai.configure(api_key=Config.GEMINI_API_KEY)

def process_chat_instruction(current_draft, user_instruction):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"""
    You are an AI assistant refining a LinkedIn post.
    Current Draft: {current_draft}
    User Instruction: {user_instruction}
    
    Update the draft based on the user instruction.
    Keep the tone strictly professional, factual, and concrete. Do not use emoji icons, em dashes, or vague AI-style copy. 
    Return ONLY the updated text.
    """
    response = model.generate_content(prompt)
    return response.text