from services.image_search import get_image
from services.image_generator import generate_ai_image

def process_image_request(topic):
    # Pehle search karega, na milne par generate karega
    img_url = get_image(topic)
    if not img_url:
        img_url = generate_ai_image(topic + " professional corporate aesthetic")
    return img_url