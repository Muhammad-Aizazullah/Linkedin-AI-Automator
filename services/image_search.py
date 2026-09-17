import requests
from config import Config

def get_image(topic):
    # Pela option: Unsplash for real, professional photos
    url = f"https://api.unsplash.com/search/photos?query={topic}&client_id={Config.UNSPLASH_ACCESS_KEY}&per_page=1"
    try:
        res = requests.get(url).json()
        if res['results']:
            return res['results'][0]['urls']['regular']
    except Exception as e:
        print("Unsplash error:", e)
        pass
    
    # Dusra option (Fallback): Pollinations AI for generated image
    return f"https://image.pollinations.ai/prompt/{topic} professional tech aesthetic"