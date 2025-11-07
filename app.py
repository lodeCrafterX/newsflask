from flask import Flask, render_template
from fetch_nasa import get_nasa_news
from ai_summarizer import summarize_data
from db_save import save_to_db

app = Flask(__name__)

@app.route('/')
def home():
    data = get_nasa_news()  # fetch NASA APOD
    if not data:
        return "🚨 Unable to fetch NASA news right now.", 500

    summary = summarize_data(data)
    if summary:
        save_to_db(summary)

    return render_template('index.html', news=summary)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
