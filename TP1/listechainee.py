from noeud import Noeud
class ListeChainee:
    def __init__(self):
        self.tete = None
        self.last = None

    def setHead(self, newHead):
        self.tete = newHead
        self.last = newHead

    def getLast(self) -> Noeud | None:
        if(self.last != None):
            return self.last
        else:
            return None

    def getHead(self) -> Noeud | None:
        if(self != None and self.tete != None):
            return self.tete
        else:
            return None

    def append(self, inserted):
        last = self.getLast()
        if (last != None):
            last.setNext(inserted)
    def insertAtGivenPos(self, valeur, position):
        currentPosition  = 0
        if(self.getHead() != None):
            currentNode = self.getHead()
        while(currentPosition < position -1 and currentNode != None):
            if(currentNode.getNext() != None):
                currentNode = currentNode.getNext()
                currentPosition+=1
        if(currentNode != None and currentNode.getNext() != None):
            newNext = currentNode.getNext()
            currentNode.setNext(valeur)
            valeur.setNext(newNext)
    
    def removeAtGivenPos(self, position):
        currentPosition  = 0
        if(self.getHead() != None):
            currentNode = self.getHead()
        while(currentPosition < position -1 and currentNode != None):
            if(currentNode.getNext() != None):
                currentNode = currentNode.getNext()
                currentPosition+=1
        if(currentNode != None and currentNode.getNext() != None):
            toDelete = currentNode.getNext()
            if(toDelete != None and toDelete.getNext() != None):
                nextOne = toDelete.getNext()
            currentNode.setNext(nextOne)

    def removeLast(self):
        last = self.getLast()
        if(last != None):
            last.removeNext()

    def seek(self, valeur) -> bool :
        if(self.getHead() != None and self.__repr__ == valeur):
            return True
        else:
            value = None
            noeud = self.getHead()
            while(noeud.__repr__ != valeur and noeud != None and noeud.getNext() != None):
                noeud = noeud.getNext()
            if(noeud.__repr__ == valeur):
                return True
            return False

    def get(self, valeur) -> Noeud | None :
        if(self.getHead() != None and self.__repr__ == valeur):
            return self.getHead()
        else:
            value = None
            noeud = self.getHead()
            while(noeud.__repr__ != valeur and noeud != None and noeud.getNext() != None):
                noeud = noeud.getNext()
            return noeud

    def taille(self) -> int:
        if(self.getHead() == None):
            return 0
        else:
            taille = 1
            noeud = self.getHead()
            while(noeud != None and noeud.getNext() != None):
                noeud = noeud.getNext()
                taille+=1
            return taille
    def estVide(self) -> bool:
        return (self.getHead() == None)

