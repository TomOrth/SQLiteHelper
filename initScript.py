class init(object):
    def __init__(self):
        self.columns = ["ID", "QUANTITY", "NAME"]
        self.datatypes = ["INT PRIMARY KEY NOT NULL", "TEXT", "TEXT"]
        self.seed = [["1", "Two", "Foo"],
                     ["2", "Three", "Bar"]]
        
