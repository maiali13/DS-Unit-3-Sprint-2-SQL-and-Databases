import sqlite3
import os
import pandas as pd


DF_URL = "https://raw.githubusercontent.com/maiali13/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv"

df = pd.read_csv(DF_URL)

# Blank database
SQL_FNAME = "buddymove_holidayiq.sqlite3"
# Delete any preexisting DB
if os.path.exists(SQL_FNAME):
    os.remove(SQL_FNAME)

DB_FPATH = os.path.join(os.path.dirname(__file__), SQL_FNAME)

# Insert data into new table
conn = sqlite3.connect(DB_FPATH)
df.to_sql("review", conn)
cursor = conn.cursor()

# Assignment queries
# Count how many rows you have - it should be 249!
query = """
SELECT COUNT(*)
FROM review;
"""
q = cursor.execute(query).fetchall()
print(q[0], "Total rows/users")

# How many users who reviewed at least 100 Nature in the category
# also reviewed at least 100 in the Shopping category?
query1 = """
SELECT COUNT(*)
FROM review
WHERE Nature >= 100 AND Shopping >= 100
"""
q1 = cursor.execute(query1).fetchall()
print("Number of users with over 100 reviews in nature and shopping", q1[0])

# (Stretch) What are the average number of reviews for each category?

# Close all connections and cursors
conn.commit()
curs.close()
conn.close()
