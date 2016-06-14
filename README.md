# SQLiteHelper
Wrapper of the sqlite3 module for ease of use.  Inspired by the SQLite design of Android using factory methods for some operations

Install the module via pip:
```python
pip install SQLiteHelper
```
To make a Database connection:
```python
from SQLiteHelper import SQLiteHelper as sq

db = sq.Connect("database")
```
This creates a db file named database.db

Next is an example of building a table named content with 3 columns, ID(INT PRIMARY KEY NOT NULL), QUANTITY(TEXT), and NAME(TEXT)
```python
db.table("content").withColumns("ID", "QUANTITY", "NAME").withDataTypes("INT PRIMARY KEY NOT NULL", "TEXT", "TEXT").createTable()
```
Now lets insert a row with an ID of 1, Quantity of "Two", and a NAME of "FOO":
```python
db.table("content").insert(1, "Two", "Foo").into("ID", "QUANTITY", "NAME")
```
Now for selecting all entries from a database with no where clause, you do: 
```python
cursor = db.table("content").select("ID", "QUANTITY", "NAME").execute()
```
If you decide to use a where clause:
```python
cursor = db.table("content").select("ID", "QUANTITY", "NAME").where("ID").equals(1).execute()
```
Both methods return a cursor of all the rows, which can be accessed as such:
```python
for row in cursor:
    for x in range(len(row)):
        print(row[x])
```
Updating entries:
```python
db.table("content").update("QUANTITY").setTo("Four").where("ID").equals(1).execute()
```
Deleting entries:
```python
db.table("content").delete().where("ID").equals(1).execute()
```

More features to come. Please post issues and pull requests as needed
