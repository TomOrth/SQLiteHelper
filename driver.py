import sqlite3
from SQLiteHelper import SQLiteHelper

db = SQLiteHelper("database")
print("connect")

db.table("dbTest").withColumns("ID","QUANTITY","NAME").withDataTypes("INT PRIMARY KEY NOT NULL", "TEXT", "TEXT").createTable()
print("table made")

db.table("dbTest").insert(1, "Two", "Foo").into("ID", "QUANTITY", "NAME")
print("insert made")
