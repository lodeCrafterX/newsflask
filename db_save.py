from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")  # local MongoDB
db = client["nasa_news"]
collection = db["articles"]

def save_to_db(summary):
    if not summary:
        return

    # Use date as unique key to avoid duplicates
    collection.update_one(
        {"date": summary["date"]},
        {"$set": summary},
        upsert=True
    )
    print("✅ Saved to MongoDB!")
