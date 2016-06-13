import sqlite3
from SQLiteHelper import SQLiteHelper

db = SQLiteHelper("database")
print("connect")

db.table("dbTest").withColumns("ID","QUANTITY","NAME").withDataTypes("INT PRIMARY KEY NOT NULL", "TEXT", "TEXT").createTable()
print("table made")

db.table("dbTest").insert(1, "Two", "Foo").into("ID", "QUANTITY", "NAME")
db.table("dbTest").insert(2, "Three", "Bar").into("ID", "QUANTITY", "NAME")
print("insert made")

results = db.table("dbTest").select("ID", "QUANTITY", "NAME").query()
whereResults = db.table("dbTest").select("ID", "QUANTITY", "NAME").where("ID").equals(1).query()

print("Simple select statement results\n")
for row in results:
    for x in range(len(row)):
        print(row[x])
print("\nWhere clause select statement results\n")
for row in whereResults:
    for y in range(len(row)):
        print(row[y])

