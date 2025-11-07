import requests

def get_nasa_news():
    api_key = "M4tSQDoE2oxsEqUcOIq0QQyn2TX1MhJfJeo01AcW"
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

    try:
        response = requests.get(url, timeout=20)  # increased timeout
        response.raise_for_status()
        return response.json()  # return dict, not list
    except requests.RequestException as e:
        print("Error fetching NASA news:", e)
        return {}  # return empty dict on error
