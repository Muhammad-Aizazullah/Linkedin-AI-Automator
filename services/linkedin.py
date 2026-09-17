import requests
from config import Config

def post_to_linkedin(text, image_url=None):
    token = Config.LINKEDIN_ACCESS_TOKEN
    urn = Config.LINKEDIN_PERSON_URN
    
    if not token or token == 'yahan_access_token_dalna_ha':
        print("LinkedIn Token missing.")
        return False
        
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'X-Restli-Protocol-Version': '2.0.0'
    }
    
    payload = {
        "author": urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": text},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }
    
    response = requests.post('https://api.linkedin.com/v2/ugcPosts', headers=headers, json=payload)
    return response.status_code == 201