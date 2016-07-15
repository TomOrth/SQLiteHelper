import sqlite3
class Connect(object):
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
class Table(object):
    #tableName
    def getTableName(self):
        return self.tab
    #sets reference to sqlite3 connection
    def setConnection(self, conn):
        self.conn = conn
    #returns sqlite3 connection
    def getConnection(self):
        return self.conn
    #sets tableName
    def setTable(self, tab):
        self.tab = tab
    #detects if table exists
    def tableExists(self):
        isExist = False
        try:
           self.getConnection().execute("SELECT * FROM " + self.getTableName())
           isExist = True
        except sqlite3.OperationalError:
           isExist = False
        return isExist
    #Initializes table
    def init(self, preset):
        if(not self.tableExists()):
            columns = preset.columns
            datatypes = preset.datatypes
            self.withColumns(*columns).withDataTypes(*datatypes).createTable()
            if(len(preset.seed) > 0):
                for index in range(len(preset.seed)):
                    tmp = preset.seed
                    self.insert(*tmp[index]).into(*columns)

    #creates columns for table
    def withColumns(self, *columns):
        self.columns = columns
        return self
    #create data types for columns
    def withDataTypes(self, *dataTypes):
        self.dataTypes = dataTypes
        return self
    #execute creating table
    def createTable(self):
        CREATE_TABLE = "CREATE TABLE " + self.getTableName() + "("
        for x in range(len(self.columns)):
            CREATE_TABLE += self.columns[x] + " " + self.dataTypes[x]
            if(x != len(self.columns)-1):
                CREATE_TABLE += ", "
        CREATE_TABLE += ");"
        self.getConnection().execute(CREATE_TABLE)
    #data to insert
    def insert(self, *insertData):
        self.insertData = insertData
        return self
    #performs the insertion
    def into(self, *columnInserts):
        INSERT = "INSERT INTO " + self.getTableName() + " ("
        for col in range(len(columnInserts)):
            INSERT += columnInserts[col]
            if(col != len(columnInserts) - 1):
                INSERT += ", "
        INSERT += ") VALUES ("
        for dat in range(len(self.insertData)):
            INSERT += "?"
            if(dat != len(self.insertData) - 1):
                INSERT += ", "
        INSERT += ")"
        self.getConnection().execute(INSERT, self.insertData)
        self.getConnection().commit()
    #columns to select from
    def select(self, *selection):
        self.selection = selection
        self.status = "norm"
        return self
    #selection parameter columns
    def where(self, *params):
        self.params = params
        return self
    #data for condition
    def equals(self, *vals):
        self.vals = vals
        if(self.status != "delete" and self.status != "update"):
            self.status = "where"
        return self
    #data fields to update
    def update(self, *updateColumns):
        self.updateColumns = updateColumns
        return self
    #data items to use in update
    def setTo(self, *updateVals):
        self.updateVals = updateVals
        self.status = "update"
        return self
    def delete(self):
        self.status = "delete"
        return self
    #main execute statement
    def execute(self):
        if(self.status == "norm"):
            QUERY = "SELECT "
            for cols in range(len(self.selection)):
                QUERY += self.selection[cols]
                if(cols != len(self.selection) - 1):
                    QUERY += ", "
            QUERY += " FROM " + self.getTableName()
            cursor = self.getConnection().execute(QUERY)
            return cursor
        elif(self.status == "where"):
            QUERY = "SELECT "
            for cols in range(len(self.selection)):
                QUERY += self.selection[cols]
                if(cols != len(self.selection) - 1):
                    QUERY += ", "
            QUERY += " FROM " + self.getTableName() + " WHERE "
            for p in range(len(self.params)):
               QUERY += self.params[p] + "=?"
               if(p != len(self.params) - 1):
                   QUERY += ", "
            cursor = self.getConnection().execute(QUERY, self.vals)
            return cursor
        elif(self.status == "update"):
            QUERY = "UPDATE " + self.getTableName() + " SET "
            for upCols in range(len(self.updateColumns)):
                QUERY += self.updateColumns[upCols] + "=?"
                if(upCols != len(self.updateColumns) - 1):
                    QUERY += ", "
            QUERY += " WHERE "
            for whereCol in range(len(self.params)):
                QUERY += self.params[whereCol] + "=?"
                if(whereCol != len(self.params) - 1):
                    QUERY += ", "
            finalParams = self.updateVals + self.vals
            self.getConnection().execute(QUERY, finalParams)
            self.getConnection().commit()
        elif(self.status == "delete"):
            QUERY = "DELETE FROM " + self.getTableName() + " WHERE "
            for delClause in range(len(self.params)):
                QUERY += self.params[delClause] + "=?"
                if(delClause != len(self.params) - 1):
                    QUERY += ", "
            self.getConnection().execute(QUERY, self.vals)
            self.getConnection().commit()
