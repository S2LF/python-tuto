from tinydb import TinyDB, Query, where

db = TinyDB('db.json', indent=4)


db.update({"score": 10}, where('name') == "John Doe")

db.update({"roles": ["Junior"]})

db.update({"role" : ['Pythonista']}, where("name") == "Jane Doe")

db.upsert({"name": "Pierre", "score": 0, "roles": ["Senior"]}, where("name") == "Pierre")

db.remove(where('name') == "Pierre")

# truncate la db
# db.truncate()