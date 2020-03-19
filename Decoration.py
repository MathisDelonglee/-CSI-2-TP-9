from abc import ABC, abstractmethod


class Decoration(ABC):
    def __init__(self, Couleur, Masse):
        self._Couleur = Couleur
        self._Masse = Masse

    #def setCouleur(self, Couleur):
        #self.__Couleur = Couleur

    #def setMasse(self, Masse):
        #self.__Masse = Masse

    #def getCouleur(self):
        #return self.__Couleur

    #def getMasse(self):
        #return self.__Masse

    @abstractmethod
    def afficher(self):
        pass
