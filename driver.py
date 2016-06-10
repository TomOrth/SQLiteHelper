import sqlite3
from SQLiteHelper import SQLiteHelper

db = SQLiteHelper("database")
print("connect")
db.table("dbTest").withColumns("ID","PRODUCT","NAME").withDataTypes("INT PRIMARY KEY NOT NULL", "INT", "CHAR(50)").createTable()
