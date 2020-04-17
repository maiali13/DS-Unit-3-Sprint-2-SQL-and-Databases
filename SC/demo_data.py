# Unit 3 SPrint 2 Challenge
# Part 1

import sqlite3

connection = sqlite3.connect('demo_data.sqlite3')
cursor = connection.cursor()

# create table, cursor, commit it
create_table = """
CREATE TABLE demo(
s TEXT,
X INT,
y INT
);
"""

cursor.execute(create_table).fetchall()
connection.commit()

# complete table by inserting all given values
cursor.execute("""
INSERT INTO demo(s, x, y)
VALUES ('g', 3 , 9),
('v', 5 , 7),
('f', 8 , 7);
""")
connection.commit()

# queries
# How many rows?
query = """
SELECT COUNT(*)
FROM demo
"""
q = cursor.execute(query).fetchall()
print (q[0], "total rows")

# How many rows are there where both `x` and `y` are at least 5?
query1 = """
SELECT COUNT(*)
FROM demo
WHERE x > 5
AND y > 5;
"""
q1 = cursor.execute(query1).fetchall()
print("Number of rows are there where both `x` & `y` are at least 5: ", q1[0])

# How many unique values of `y` are there
# (hint - `COUNT()` can accept a keyword `DISTINCT`)?
query2 = """
SELECT COUNT(DISTINCT y)
FROM demo
"""
q2 = cursor.execute(query2).fetchall()
print(q2[0], " unique values of y")
