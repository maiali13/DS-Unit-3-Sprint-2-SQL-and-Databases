# Assignment 4 answers

import sqlite3
import os
import psychopg2 #pipenv install python-dotenv psycopg2-binary
import pandas as pd
from dotenv import load_dotenv

"""
    Assignment 4
    How many passengers survived, and how many died?
    How many passengers were in each class?
    How many passengers survived/died within each class?
    What was the average age of survivors vs nonsurvivors?
    What was the average age of each passenger class?
    What was the average fare by passenger class? By survival?
    How many siblings/spouses aboard on average, by passenger class? By survival?
    How many parents/children aboard on average, by passenger class? By survival?
    Do any passengers have the same name?
    (Bonus! Hard, may require pulling and processing with Python) How many married couples were aboard the Titanic? Assume that two people (one Mr. and one Mrs.) with the same last name and with at least 1 sibling/spouse aboard are a married couple.
"""

DF_URL = "titanic.csv"
DB_URL = "titanic.sqlite3"

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

load_dotenv()

#create connection and cursor
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
cursor = conn.cursor()

df = pd.read_csv(DF_URL)

#delete db if preexisting
if os.path.exists(DB_URL):
    os.remove(DB_URL)

#(re)create and convert df
ti_conn = sqlite3.connect(DB_URL)
ti_curs = ti_conn.cursor()
df.to_sql("titanic", ti_conn, if_exists="replace")

# assignment queries
# How many passengers survived, and how many died?
query = """
SELECT survived,
COUNT(*)
FROM titanic
GROUP BY survived;
"""
q = cursor.execute(query).fetchall()[0]
print("How many passengers survived, and how many died?", q)

# How many passengers were in each class?
query1 = """
SELECT COUNT(*)
FROM titanic
GROUP BY pclass;
"""
q1 = cursor.execute(query1).fetchall()[0]
print("How many passengers were in each class?", q1)

# How many passengers survived/died within each class?
query2 = """
SELECT pclass, COUNT(*)
FROM titanic
GROUP BY pclass
ORDER BY pclass, survived;
"""
q2 = cursor.execute(query2).fetchall()[0]
print("How many passengers survived/died within each class?", q2)

# What was the average age of survivors vs nonsurvivors?
query3 = """
SELECT survived AVG(age)
FROM titanic
GROUP BY survived
"""
q3 = cursor.execute(query3).fetchall()[0]
print("What was the average age of survivors vs nonsurvivors?", q3)

# What was the average age of each passenger class?
query4 = """
SELECT pclass, AVG(age)
FROM titanic
GROUP BY pclass
ORDER BY pclass;
"""
q4 = cursor.execute(query4).fetchall()[0]
print("What was the average age of each passenger class?", q4)

# What was the average fare by passenger class? By survival?
query5 = """
SELECT pclass, AVG(fare)
FROM titanic
GROUP BY pclass
ORDER BY pclass;
"""
q5 = cursor.execute(query5).fetchall()[0]
print("What was the average fare by passenger class? By survival?", q5)

# How many siblings/spouses aboard on average, by passenger class? By survival?
query6 = """
SELECT survived, AVG(siblings_spouses_aboard)
FROM titanic
GROUP BY pclass, survival;
"""
q6 = cursor.execute(query6).fetchall()[0]
print("How many siblings/spouses aboard on average, by passenger class? By survival?", q6)

# How many parents/children aboard on average, by passenger class? By survival?
query7 = """
SELECT pclass, survived, AVG(parents_children_aboard)
FROM titanic
GROUP BY pclass, survived;
"""
q7 = cursor.execute(query7).fetchall()[0]
print("How many parents/children aboard on average, by passenger class? By survival?", q7)

# Do any passengers have the same name?
query8 = """
SELECT name, COUNT(*)
FROM titanic
GROUP BY name
HAVING COUNT(*) > 1
"""
q8 = cursor.execute(query8).fetchall()[0]
print("How many passengers have the same name?", q8[0])
