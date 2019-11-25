import os

class DaoObject:
    
    def __init__(self,filepath):   
        with open(filepath,"r+") as file:
            list = file.readlines() 
        self.count = len(list)
        self.filepath = filepath
        print("The size of db is: ",self.count)
        return

    def addItem(self, item):
        filepath = self.filepath
        file = open(filepath,"a")
        file.write("{}\n".format(item))
        return

    def delItem(self, target):
        filepath = self.filepath
        with open(filepath,"w") as f:
            lines = f.readlines()
            for line in lines:
                if line.strip("\n") != target:
                    f.write(line)
        return

    def updateItem(self, item, target):
        filepath = self.filepath
        with open(filepath,"w") as f:
            lines = f.readlines()
            for line in lines:
                if line.strip("\n") != target:
                    f.write(line)
                else:
                    f.write(item)
        return

    def queryItem(self, key):
        filepath = self.filepath
        with open(filepath,"r") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if(lines[i]==key):
                    print ("This is No.{} of text.").format(i)
        return


obj = DaoObject("./db.txt")