from tinydb import TinyDB, Query, where
# from tinydb.storages import MemoryStorage

# Create a database in memory
# db = TinyDB('storage=MemoryStorage')

db = TinyDB('db.json', indent=4)

# db.insert({'name': 'John Doe', 'score': 0})

# db.insert_multiple([
#     {'name': 'Jane Doe', 'score': 0},
#     {'name': 'Joe Doe', 'score': 0}
# ])

User = Query()

john = db.search(User.name == "John Doe")
john_unique = db.get(User.name == "John Doe")
print(john)
print(john_unique)

high_scores = db.search(where('score') > 0)
print(high_scores)

print(len(db))
print(db.contains(User.name == "John Doe"))
print(db.count(User.name == "John Doe"))
print(db.contains(User.name == "Jean Doe"))