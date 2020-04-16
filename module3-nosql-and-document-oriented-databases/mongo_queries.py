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
A:

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
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


query = """
SELECT (*)
FROM charactercreator_character;
"""
q = curs.execute(query).fetchall()

curs.close()
