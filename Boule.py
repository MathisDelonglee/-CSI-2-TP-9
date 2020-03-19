from Decoration import *

class Boule(Decoration):
    def __init__(self, Diametre, Couleur, Masse):
        Decoration.__init__(self, Couleur, Masse)
        self.__Diametre = Diametre

    #def setDiametre(self, Diametre):
        #self.__Diametre = Diametre

    #def getDiametre(self):
        #return self.__Diametre

    def afficher(self):
        Diametre = self.__Diametre
        Couleur = self._Couleur
        Masse = self._Masse
        print("* Boule",Couleur,"de",Diametre,"cm de diamètre, pesant",Masse,"g.")
