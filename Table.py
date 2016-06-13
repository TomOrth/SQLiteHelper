class Table(object):
    def getTableName(self):
        return self.tab
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
    def select(self, *selection):
        self.selection = selection
        self.status = "norm"
        return self
    def where(self, *params):
        self.params = params
        return self
    def equals(self, *vals):
        self.vals = vals
        self.status = "where"
        return self
    def query(self):
        if(self.status == "norm"):
           QUERY = "SELECT "
           for cols in range(len(self.selection)):
               QUERY += self.selection[cols]
               if(cols != len(self.selection) - 1):
                   QUERY += ", "
           QUERY += "  from " + self.getTableName() 
           cursor = self.getConnection().execute(QUERY)
           return cursor
        elif(self.status == "where"):
           QUERY = "SELECT "
           for cols in range(len(self.selection)):
               QUERY += self.selection[cols]
               if(cols != len(self.selection) - 1):
                   QUERY += ", "
           QUERY += " FROM " + self.getTableName() + " where "
           for p in range(len(self.params)):
              QUERY += self.params[p] + "=?"
              if(p != len(self.params) - 1):
                  QUERY += ", "
           print(QUERY)
           cursor = self.getConnection().execute(QUERY, self.vals)
           return cursor
