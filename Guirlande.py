from Decoration import *

class Guirlande(Decoration):
    def __init__(self, Longueur, Couleur, Masse):
        Decoration.__init__(self, Couleur, Masse)
        self._Longueur = Longueur

    #def setLongueur(self, Longueur):
        #self.__Longueur = Longueur

    #def getLongueur(self):
        #return self.__Longueur

    def afficher(self):
        pass
