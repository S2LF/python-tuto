from tinydb import TinyDB, Query, where

db = TinyDB('db.json', indent=4)

users = db.table('Users')
roles = db.table('Roles')

users.insert_multiple([
    {'name': 'John Doe', 'score': 0},
    {'name': 'Jane Doe', 'score': 0},
    {'name': 'Joe Doe', 'score': 0}
])

roles.insert_multiple([
    {'name': 'Junior'},
    {'name': 'Senior'},
    {'name': 'Pythonista'}
])