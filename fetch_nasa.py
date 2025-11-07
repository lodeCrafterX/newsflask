import requests

def get_nasa_news():
    api_key = "M4tSQDoE2oxsEqUcOIq0QQyn2TX1MhJfJeo01AcW"
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raise exception for HTTP errors
        return [response.json()]  # wrap in list to keep consistent with summary
    except requests.RequestException as e:
        print("Error fetching NASA news:", e)
        return []
