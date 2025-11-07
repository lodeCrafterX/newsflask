from flask import Flask, render_template
from fetch_nasa import get_nasa_news

app = Flask(_name_)

@app.route('/')
def home():
    news = get_nasa_news()
    return render_template('index.html', news=news)

if _name_ == "main":
    app.run(host='0.0.0.0', port=5000)
