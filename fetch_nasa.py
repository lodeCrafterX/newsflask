import requests

def get_nasa_news():
    api_key = "M4tSQDoE2oxsEqUcOIq0QQyn2TX1MhJfJeo01AcW"  # Replace with your NASA API Key
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    response = requests.get(url)
    return response.json()
