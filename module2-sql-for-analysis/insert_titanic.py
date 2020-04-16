# insert_titanic.py 
import psycopg2
import os
import sqlite3
import pandas as pd
from dotenv import load_dotenv
​
# adds the contents of the .env file to our environment
# use environment variable

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
load_dotenv()

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print(type(connection)) #> <class 'psycopg2.extensions.connection'>
​
cursor = connection.cursor()
print(type(cursor)) #> <class 'psycopg2.extensions.cursor'>

# create new table with best schema for titanic data (from SQLite to PostgreSQL using Python)
# then write script that connects and uploads data from csv
DF_URL = "titanic.csv"
DB_URL = "titanic.sqlite3"

df = pd.read_csv(DF_URL)
ti_conn = sqlite3.connect(DB_URL)

df.to_sql("titanic", ti_conn, if_exists="replace")
ti_curs = ti_conn.cursor()
titanic = ti_curs.execute('SELECT * FROM titanic').fetchall()
ti_conn.commit()

# edit to drop if preexisting table
create_titanic_table = """
CREATE TABLE IF NOT EXISTS titanic (
    titanic_id SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name TEXT,
    gender varchar NOT NULL,
    age INT,
    siblings_or_spouses_aboard INT,
    parents_or_children_aboard INT,
    fare REAL
);
"""

cursor.execute(create_titanic_table)
connection.commit()

query = '''
SELECT AVG(age)
FROM titanic
'''
q = cursor.execute(query)
print()
​
# ACTUALLY SAVE THE TRANSACTIONS
# if creating tables or inserting data (changing db)
connection.commit()
