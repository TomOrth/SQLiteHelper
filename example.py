from SQLiteHelper import SQLiteHelper as sq

db = sq.Connect("database")
print("connect")
print(db.table("test").tableExists())
db.table("dbTest").withColumns("ID","QUANTITY","NAME").withDataTypes("INT PRIMARY KEY NOT NULL", "TEXT", "TEXT").createTable()
print("table made")

db.table("dbTest").insert(1, "Two", "Foo").into("ID", "QUANTITY", "NAME")
db.table("dbTest").insert(2, "Three", "Bar").into("ID", "QUANTITY", "NAME")
print("insert made")

results = db.table("dbTest").select("ID", "QUANTITY", "NAME").execute()
whereResults = db.table("dbTest").select("ID", "QUANTITY", "NAME").where("ID").equals(1).execute()

print("Simple select statement results\n")
for row in results:
    for w in range(len(row)):
        print(row[w])
print("\nWhere clause select statement results\n")
for row in whereResults:
    for x in range(len(row)):
        print(row[x])

print("\nUpdating first ID to have new quantity\n")
db.table("dbTest").update("QUANTITY").setTo("Four").where("ID").equals(1).execute()

results = db.table("dbTest").select("ID", "QUANTITY", "NAME").execute()
for row in results:
    for y in range(len(row)):
        print(row[y])

print("\nDeleting entry with ID of 2\n")
db.table("dbTest").delete().where("ID").equals(2).execute()

results = db.table("dbTest").select("ID", "QUANTITY", "NAME").execute()
for row in results:
    for z in range(len(row)):
        print(row[z])
