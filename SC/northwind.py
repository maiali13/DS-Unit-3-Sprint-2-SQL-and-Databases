# Unit 3 Sprint 2 Challenge
import sqlite3

# Load DB
connect = sqlite3.connect('northwind_small.sqlite3')
cursor = connect.cursor()

# Part 2
# What are the ten most expensive items (per unit price) in the database?
query = """
SELECT ProductName
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""
q = cursor.execute(query).fetchall()
print("10 most expensive products: ", q)

# What is the average age of an employee at the time of their hiring?
# (Hint: a   lot of arithmetic works with dates.)
query1 = """
SELECT ROUND(AVG(HireDate - BirthDate), 1)
FROM Employee;
"""
q1 = cursor.execute(query1).fetchall()
print("Average age of employees at hire: ", q1)

# (*Stretch*) How does the average age of employee at hire vary by city?
query2 = """
SELECT City, ROUND(AVG(HireDate - BirthDate), 1)
FROM Employee
GROUP BY City;
"""
q2 = cursor.execute(query2).fetchall()
print("Average age of employees at hire by city: ", q2)


# Part 3
# What are the ten most expensive items (per unit price) in the databse
# *and* their suppliers?
query3 = """
SELECT UnitPrice, ProductName, CompanyName
FROM (SELECT Product.UnitPrice, Product.ProductName, Supplier.CompanyName
FROM Product
JOIN Supplier
WHERE Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10);
"""
q3 = cursor.execute(query3).fetchall()
print("10 most expensive products and suppliers: ", q3)

# What is the largest category (by number of unique products in it)?
query4 = """
SELECT Category.CategoryName, COUNT(DISTINCT ProductName) AS TotalProducts
FROM Product
JOIN Category ON Product.CategoryID = Category.Id
ORDER BY TotalProducts DESC
LIMIT 1;
"""
q4 = cursor.execute(query4).fetchall()
print("Largest category by number of unique products: ", q4)

# (*Stretch*)
# Who's the employee with the most territories?
# Use `TerritoryId` (not name, region, or other fields) as the unique
# identifier for territories.
# oh well, tried
query5 = """
SELECT Employee.LastName, COUNT(DISTINCT Territory.Id)
FROM Employee, Territory, EmployeeTerritory
WHERE EmployeeTerritory.EmployeeId = Employee.Id AND EmployeeTerritory.TerritoryId = Territory.Id
GROUP BY employee.id
ORDER BY EmployeeTerritory.TerritoryId DESC
LIMIT 1;
"""
q5 = cursor.execute(query5).fetchall()
print("Employee with the most territory: ", q5)
