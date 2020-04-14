import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "chinook.db"
#DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "rpg_db.sqlite3")

conn = sqlite3.connect("/home/mai/Desktop/DS-Unit-3-Sprint-2-SQL-and-Databases//module1-introduction-to-sql/rpg_db.sqlite3")
#print("CONNECTION:", connection)
cursor = conn.cursor()

# How many total Characters are there?
query1 = """
SELECT count(*)
FROM charactercreator_character
AS character_count
"""
q1 = cursor.execute(query1).fetchall()[0]
print("Total number of characters: ", q1[0])


# How many of each specific subclass?
query2 = """
SELECT COUNT(DISTINCT(character_ptr_id))
FROM charactercreator_cleric;
"""
q2 = cursor.execute(query2).fetchall()[0]
print("Total number of clerics: ", q2[0])

query3 = """
SELECT COUNT(DISTINCT(character_ptr_id))
FROM charactercreator_mage;
"""
q3 = cursor.execute(query3).fetchall()[0]
print("Total number of mages: ", q3[0])

query4= """
SELECT COUNT(DISTINCT(character_ptr_id))
FROM charactercreator_fighter;
"""
q4 = cursor.execute(query4).fetchall()[0]
print("Total number of fighters: ", q4[0])

query5= """
SELECT COUNT(DISTINCT(character_ptr_id))
FROM charactercreator_thief;
"""
q5 = cursor.execute(query5).fetchall()[0]
print("Total number of thiefs: ", q5[0])

query6= """
SELECT COUNT(DISTINCT(mage_ptr_id))
FROM charactercreator_necromancer;
"""
q6 = cursor.execute(query6).fetchall()[0]
print("Total number of necromancers: ", q6[0])


# How many total Items?
query7 = """
SELECT  count(*)
FROM armory_item
"""
q7 = cursor.execute(query7).fetchall()[0]
print("Total number of items: ", q7[0])


# How many of the Items are weapons? How many are not?
query8 = """
SELECT  count(*)
FROM armory_weapon
"""
q8 = cursor.execute(query8).fetchall()[0]
print("Total number of weapon-type items: ", q8[0])
print("Total number of non-weapon-type items: ", q7[0]-q8[0])


# How many Items does each character have? (Return first 20 rows)
query9 = """
SELECT COUNT(character_id)
FROM charactercreator_character_inventory
GROUP By character_id
LIMIT 20
"""
print('How many items does each character have? (first 20 rows):')
print(cursor.execute(query9).fetchall())


# How many Weapons does each character have? (Return first 20 rows)
query10 = """
SELECT COUNT(item_ptr_id)
FROM charactercreator_character_inventory
LEFT JOIN armory_weapon
ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id
GROUP By character_id
LIMIT 20
"""
print('How many weapons does each character have? (first 20 rows)')
print(cursor.execute(query10).fetchall())


# On average, how many Items does each Character have?
query11 = """
SELECT AVG(item_count) AS avg_items_per_char
FROM (SELECT DISTINCT character_id AS character_id,
COUNT(character_id) AS item_count
FROM charactercreator_character_inventory
GROUP BY character_id)
"""
print("On average, how many items does each Character have?")
print(cursor.execute(query11).fetchall()[0])


# On average, how many Weapons does each character have?
query12 = """
SELECT AVG(weapon_count) AS avg_weapons_per_char
FROM (SELECT DISTINCT character_id AS character_id,
COUNT(character_id) AS weapon_count
FROM charactercreator_character_inventory
WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)
GROUP BY character_id)
"""
print("On average, how many weapons does each Character have?")
print(cursor.execute(query12).fetchall()[0])
