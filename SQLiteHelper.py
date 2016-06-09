import sqlite3
from Table import Table

class SQLiteHelper(object):
    def __init__(self, dbName):
       self.dbName = dbName
       self.tableObj = Table()
       self.conn = sqlite3.connect(dbName + ".db")
    def getDBName(self):
        return self.dbName
    def getConn(self):
        return self.conn
    def table(self, tabl):
        self.tableObj.setConnection(self.getConn())
        self.tableObj.setTable(tabl)
        return self.tableObj
