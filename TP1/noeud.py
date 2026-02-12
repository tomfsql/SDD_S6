class Noeud:
    def __init__(self):
        self.name = ""
        self.next = None

    def setNext(self, newNext):
        self.next = newNext

    def getNext(self):
        return self.next

    def removeNext(self):
        if(self.next != None):
            self.next = None

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