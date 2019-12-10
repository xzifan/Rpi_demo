import os

class DaoObject:
    
    def __init__(self,filepath):  
        '''
        Initializing db.txt file.
        ''' 
        self.filepath = filepath
        try:
            with open(filepath,"w") as f:
                f.truncate(0)
        except FileNotFoundError:
            with open(filepath, 'w+') as f:
                print("File created!")
        return

    def addItem(self, item):
        '''
        Append a new item to the list.
        '''
        filepath = self.filepath
        file = open(filepath,"a")
        file.write("{}\n".format(item))
        return

    def delItem(self, target):
        '''
        Delete a existing item.
        '''
        if (not self.itemExist(target)):
            print("Item does not exist!")
            pass
        filepath = self.filepath
        with open(filepath, "r") as f:
            lines = f.readlines()
        with open(filepath, "w") as f:
            for line in lines:
                if line.strip("\n") != target:
                    f.write(line)
        return

    def updateItem(self, item, target):
        '''
        Update a existing item with keyword and replace it with new item
        '''
        # print("updating",self.filepath)
        if (not self.itemExist(target)):
            print("Item does not exist!")
            return
        filepath = self.filepath
        with open(filepath, "r") as f:
            lines = f.readlines()
        with open(filepath, "w") as f:
            for line in lines:
                if line.strip("\n") != target:
                    f.write(line)
                else:
                    f.write(item+"\n")
        return

    def queryItem(self, key):
        '''
        Query the database with the keyword
        Return the idex of item starting from 1.
        it would be 0 if item does not exist. 
        '''
        filepath = self.filepath
        with open(filepath,"r") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if(lines[i].strip("\n")==key):
                    print ("This is No.{} of text.".format(i))
                    return i+1
            return 0

    def sortItem(self):
        filepath = self.filepath
        with open(filepath, "r") as f:
            lines = f.readlines()
        if (len(lines)>0):
            with open(filepath, "w") as f:
                lines.sort();
                for line in lines:
                    f.write(line) 
        return
    
    def itemExist(self,item):
        return self.queryItem(item) != 0
# obj = DaoObject("./db.txt")