from Guirlande import *

class GuirlandeLumineuse(Guirlande):
    def __init__(self, Longueur, Couleur, Masse, NbreLumiere):
        Guirlande.__init__(self, Longueur, Couleur, Masse)
        self._NbreLumiere = NbreLumiere

    #def setNbreLumiere(self, NbreLumiere):
        #self.__NbreLumiere = NbreLumiere

    #def getNbreLumiere(self):
        #return self.__NbreLumiere

    def afficher(self):
        NbreLumiere = self._NbreLumiere
        Couleur = self._Couleur
        Masse = self._Masse
        Longueur = self._Longueur
        print("* Guirlande lumineuse",Couleur,"de",Longueur,"cm de long, possédant",NbreLumiere,"lumières et pesant",Masse,"g.")
