import requests
import time

def get_nasa_news(max_retries=3, backoff=5):
    api_key = "M4tSQDoE2oxsEqUcOIq0QQyn2TX1MhJfJeo01AcW"
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, timeout=15)  # shorter timeout per attempt
            response.raise_for_status()
            return response.json()  # return dict
        except requests.RequestException as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt < max_retries:
                sleep_time = backoff * attempt
                print(f"Retrying in {sleep_time} seconds...")
                time.sleep(sleep_time)
            else:
                print("Failed to fetch NASA news after multiple attempts.")
                return {}  # return empty dict on final failure
