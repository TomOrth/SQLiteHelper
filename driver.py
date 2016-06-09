import sqlite3
from SQLiteHelper import SQLiteHelper

db = SQLiteHelper("database")
print("connect")
db.table("dbTest").withColumns(["1","2","3"]).withDataTypes(["INTEGER", "INTEGER", "VARCHAR"])
