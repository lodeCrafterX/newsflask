from pymongo import MongoClient

# MongoDB connection (local or Atlas)
client = MongoClient("mongodb://localhost:27017/")
db = client["nasa_news"]
collection = db["articles"]

def save_to_db(summary):
    collection.insert_one(summary)
    print("✅ Saved to MongoDB!")
