from Decoration import *

class Sapin:
    def __init__(self, MasseMax, MasseTotale):
        self.__MasseMax = MasseMax
        self.__MasseTotale = MasseTotale
        self.__decoliste=[]

    def setMasseMax(self, MasseMax):
        self.__MasseMax = MasseMax

    def setMasseTotale(self, MasseTotale):
        self.__MasseTotale = MasseTotale

    def getMasseMax(self):
        return self.__MasseMax

    def getMasseTotale(self):
        return self.__MasseTotale

    def ajouter(self,deco):
        self.__decoliste.append(deco)
        self.__MasseTotale += deco._Masse

    def supprimer(self,deco):
        self.__decoliste.remove(deco)
        self.__MasseTotale -= deco._Masse




    def afficherSapin(self):
        MasseMax = self.getMasseMax()
        MasseTotale = self.getMasseTotale()
        print("Ce sapin de Noel peut supporter",MasseMax,'g de décoration.')
        if MasseTotale == 0:
            print("Il ne contient actuellement aucune décoration.")
        else:
            print("Il contient actuellement",MasseTotale,"g de décorations, listées ci-après:")
        if len(self.__decoliste)!=0:
            for i in self.__decoliste :
                i.afficher()

        else :
            print("Il ne contient actuellement aucune decoration.\n-----")
        print("-----")
