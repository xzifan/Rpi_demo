import pytest
import io
from demo_DAO import DaoObject 


class TestClass:
    def _get_DAO_object(self):
        filePath = "./test_db.txt"
        try:
            os.remove(path_of_file)
        except:
            try:
                with open(filePath,"w") as f:
                    f.truncate(0)
            except FileNotFoundError:
                with open(filePath, 'w+') as f:
                    print("File created!")
        obj = DaoObject(filePath)
        return obj

    def _get_item_at(self,idx):
        with open("./test_db.txt","r") as f:
            lines  = f.readlines()
            #stripping the newline character:
            lines = [line.rstrip('\n') for line in open('./test_db.txt')]
            return lines[idx]
        pass

    def _get_list_length(self):
        with open("./test_db.txt","r") as f:
            lines  = f.readlines()
            #stripping the newline character:
            lines = [line.rstrip('\n') for line in open('./test_db.txt')]
            return len(lines)
        pass

    def test_add(self):
        obj = self._get_DAO_object()
        obj.addItem("Pythons")

        assert self._get_item_at(0) == "Pythons", "Creating item is failed."

    def test_update(self):
        obj = self._get_DAO_object()
        obj.addItem("Pythons")
        obj.updateItem("Vipers","Pythons")
        assert self._get_item_at(0) == "Vipers","Updating item is failed."

    def test_delete(self):
        obj = self._get_DAO_object()
        obj.addItem("Pythons")
        obj.delItem("Pythons")
        assert self._get_list_length() == 0,"Deleting item is failed."

    def test_query(self):
        obj = self._get_DAO_object()
        obj.addItem("Pythons")
        assert obj.queryItem("Pythons") != 0, "Query item is failed."