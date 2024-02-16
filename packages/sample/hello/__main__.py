import os
from pymongo import MongoClient

def main(args):
      dbName = "myriad"
      mongo_db = MongoClient(
            "mongodb+srv://doapps-5865b38b-6ce0-4a8f-bad8-6c7a1a3328fa:5J8AYo60Z3K792fW@cluster0.j3uxfgx.mongodb.net/myriad"
      )[dbName]
      
      tweet_data = mongo_db.tweets.find_one({})
      name = args.get("name", "stranger")
      greeting = "Hello " + name + "!"
      print(greeting)
      return {
            "body": {
                  "message": greeting,
                  "tweet": tweet_data["tweet"],
                  "database": os.getenv('DATABASE_HOST')
                  }
      }
  