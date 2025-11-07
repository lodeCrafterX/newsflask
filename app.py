from flask import Flask, render_template
from fetch_nasa import get_nasa_news
from ai_summarizer import summarize_data
from db_save import save_to_db

app = Flask(__name__)

@app.route('/')
def home():
    data = get_nasa_news()
    summary = summarize_data(data)
    save_to_db(summary)
    return render_template('index.html', news=summary)

if __name__ == "main":
    app.run(host='0.0.0.0', port=5000)
