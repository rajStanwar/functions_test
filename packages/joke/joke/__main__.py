print("Inside main.py script")

import pyjokes
import pymongo
import os



def main():
  mongo_uri = "mongodb+srv://doapps-e44dd091-4713-4513-9ea5-222647a16f3a:2Y7x5o01z4b3OpN6@mongodb-do-function-test-6c227d6b.mongo.ondigitalocean.com/admin?tls=true&authSource=admin&replicaSet=mongodb-do-function-test"
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
