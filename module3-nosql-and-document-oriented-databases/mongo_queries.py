# mongodb+srv://user1:<password>@cluster0-9dgqe.mongodb.net/test?retryWrites=true&w=majority
# app/mongo_queries.py
​
import pymongo
import json
import os
from dotenv import load_dotenv
​
load_dotenv()

"""
Q: How was working with MongoDB different from working with PostgreSQL? What was easier, and what was harder?
A: Mongo stores data in dictionaries/documents vs PostreSQL stores data in
relational databases. So MongoDB is more flexible and the data isnt in a
rigid strucutre like PostgreSQL. I like PostgreSQL because the standerdized data
structure is better for long-term development and I prefer traditional SQL
querying over dealing with json.
"""
​
DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")
#MONGO_URL = os.getenv("MONGO_URL", default="OOPS")
​
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)
​
client = pymongo.MongoClient(connection_uri)
#client = pymongo.MongoClient(MONGO_URL)
print("----------------")
print("CLIENT:", type(client), client)
​
db = client.inclass_db_ds13 # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)
​
collection = db.pokemon_test # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)
​
print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names()) # won't see until after inserting data
​
# note:look more into os.path 
RPG_FPATH = os.path.join(os.getcwd(),'..','module1-introduction-to-sql','rpg_db.sqlite3')
conn = sqlite3.connect(RPG_FPATH)
curs = conn.cursor()


query = """
SELECT (*)
FROM charactercreator_character;
"""
q1 = curs.execute(query).fetchall()

for character in q1:
    insert_character = {
        'character_id': character[0],
        'name': character[1],
        'level': character[2],
        'exp': character[3],
        'hp': character[4],
        'strength': character[5],
        'intelligence': character[6],
        'dexterity': character[7],
        'wisdom': character[8]
    }
    db.charactercreator_character.insert_one(insert_character)

q2 = db.charactercreator_character.find_one()

print(q2)
curs.close()
