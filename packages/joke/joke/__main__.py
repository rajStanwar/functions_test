print("Inside main.py script")

import pyjokes
# import pymongo
# import os

# mongo_url = os.environ.get("DATABASE_URL")
# password = os.environ.get("DATABASE_PASSWORD")
# db_user = os.environ.get("DATABASE_USER")
# db_name = os.environ.get("DATABASE_USER")

def main():
  # print(mongo_url)
  # print(password)
  # print(db_user)
  # print(db_name)
  # client = pymongo.MongoClient(f"mongodb+srv://{db_user}:{password}@{mongo_url}/{db_name}")
  # db = client[db_name]
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
