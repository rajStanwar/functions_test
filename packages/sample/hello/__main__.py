import os
def main(args):
      name = args.get("name", "stranger")
      greeting = "Hello " + name + "!"
      print(greeting)
      return {
            "body": {
                  "message": greeting,
                  "database": os.getenv('DATABASE_HOST')
                  }
      }
  