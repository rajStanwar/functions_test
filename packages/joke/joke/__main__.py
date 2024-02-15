import pyjokes
import pymongo
import os



def main():
  try:
    mongo_uri = "mongodb+srv://doapps-5865b38b-6ce0-4a8f-bad8-6c7a1a3328fa:9e2506TgD3YE4lW1@mongodb-do-function-test-6c227d6b.mongo.ondigitalocean.com/myriad"
    print(mongo_uri)
    client = pymongo.MongoClient(mongo_uri)
    db = client["myriad"]
    joke = pyjokes.get_joke()
    
    # insert joke in the database
    print("Joke: ", joke)
    
    db.jokes.insert_one({"joke": joke})
    return {
      "body": {
        "response_type": "in_channel",
        "text": joke,
        "uri": mongo_uri
      }
    }
  except Exception as e:
    return {
      "body": {
        "response_type": "error",
        "error": e,
      }
    }