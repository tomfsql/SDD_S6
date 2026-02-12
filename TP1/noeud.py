class Noeud:
    def __init__(self):
        self.name = ""
        self.next = None

    def setnext(self, newNext):
        self.next = newNext
    
    def setName(self, newName):
        self.name = newName

    def getName(self) -> str:
        if(self.name != None):
            return self.name
        else:
            return "None"

    def __repr__(self) -> str:
        if(self != None and self.name != None):
            return self.name
        else:
            return "None"