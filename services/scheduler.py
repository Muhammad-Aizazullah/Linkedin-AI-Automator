import schedule
import time
import requests

def generate_daily_draft():
    print("Executing 12:05 AM task: Generating new draft...")
    try:
        # App ki apni API ko call kray ga
        requests.post('http://127.0.0.1:5000/api/generate', json={"topic": "Computer Vision"})
    except Exception as e:
        print(f"Error: {e}")

def auto_post_unrejected():
    print("Executing 11:59 AM task: Checking pending posts...")
    # Yahan API endpoint call hoga jo pending posts ko publish kray ga
    # (Ye route hum app.py mein add krr saktay hein)
    pass

# Schedule tasks according to your time
schedule.every().day.at("00:05").do(generate_daily_draft)
schedule.every().day.at("11:59").do(auto_post_unrejected)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == '__main__':
    run_scheduler()