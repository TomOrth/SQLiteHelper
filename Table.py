class Table(object):
    def __init__(self, tableName="Simple"):
        self.tableName = tableName
    def setConnection(self, conn):
        self.conn = conn
    def setTable(self, tab):
        self.tab = tab
    def withColumns(self, *columns):
        self.columns = columns
        return self
    def withDataTypes(self, *dataTypes):
        self.dataTypes = dataTypes
        return self

