from flask import Flask, render_template
from fetch_nasa import get_nasa_news

app = Flask(name)

@app.route('/')
def home():
    news = get_nasa_news()
    return render_template('index.html', news=news)

if name == "main":
    app.run(host='0.0.0.0', port=5000)
