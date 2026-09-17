def generate_ai_image(prompt):
    # Pollinations AI fallback (No API key required)
    clean_prompt = prompt.replace(" ", "%20")
    # nologo=true ensures no watermarks are added
    return f"https://image.pollinations.ai/prompt/{clean_prompt}?width=800&height=600&nologo=true"