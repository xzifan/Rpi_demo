import os

class DaoObject:
    
    
    
    def __init__(self,filepath):   
        with open(filepath,"r+") as file:
            list = file.readlines() 
        self.count = len(list)
        print("The size of db is: ",self.count)
        return

    def addItem(self, item):
        file = open(filepath,"r+")
        file.write("{}".format(item))
        self.__init__(filepath)
        return

    def delItem(self, target):
        with open(filepath,"w") as f:
            for line in lines:
                if line.strip("\n") != target:
                    f.write(line)
        return

    def updateItem(self, item, target):

        return

    def queryItem(self, key):
        
        return


obj = DaoObject("./db.txt")