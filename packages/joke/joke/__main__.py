print("Inside main.py script")

import pyjokes
import pymongo
import os



def main():
  # mongo_uri = os.environ.get("MONGO_URI")
  # print(mongo_uri)
  # client = pymongo.MongoClient(mongo_uri)
  # db = client["myriad"]
  joke = pyjokes.get_joke()
  
  # insert joke in the database
  print("Joke: ", joke)
  
  # db.jokes.insert_one({"joke": joke})
  return {
    "body": {
      "response_type": "in_channel",
      "text": joke
    }
  }
