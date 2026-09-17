from services.linkedin import post_to_linkedin

def publish_content(text, image_url):
    # Is agent ko future analytics track karne k liye expand kiya ja sakta hai
    return post_to_linkedin(text, image_url)