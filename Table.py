class Table(object):
    def __init__(self, tableName="Simple"):
        self.tableName = tableName
    def getTableName(self):
        return self.tableName
    def setConnection(self, conn):
        self.conn = conn
    def getConnection(self):
        return self.conn
    def setTable(self, tab):
        self.tab = tab
    def withColumns(self, *columns):
        self.columns = columns
        return self
    def withDataTypes(self, *dataTypes):
        self.dataTypes = dataTypes
        return self
    def createTable(self):
        CREATE_TABLE = "CREATE TABLE " + self.getTableName() + "("
        for x in range(len(self.columns)):
            CREATE_TABLE += self.columns[x] + " " + self.dataTypes[x]
            if(x != len(self.columns)-1):
                CREATE_TABLE += ", "
        CREATE_TABLE += ");"   
        self.getConnection().execute(CREATE_TABLE)
    def insert(self, *insertData):
        self.insertData = insertData
        return self
    def into(self, *columnInserts):
        INSERT = 'INSERT INTO ' + self.getTableName() + ' ('
        for col in range(len(columnInserts)):
            INSERT += columnInserts[col]
            if(col != len(columnInserts) - 1):
                INSERT += ', '
        INSERT += ') VALUES ('
        for dat in range(len(self.insertData)):
            INSERT += "?"
            if(dat != len(self.insertData) - 1):
                INSERT += ', '
        INSERT += ')'
        print(INSERT)
        self.getConnection().execute(INSERT, self.insertData)  
        self.getConnection().commit()    
