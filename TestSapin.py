from Sapin import *
from Decoration import *
from Boule import *
from Guirlande import *
from GuirlandeLumineuse import *


Sapin = Sapin(5000,0)

Boule1 = Boule(5,'bleu',15)
Sapin.ajouter(Boule1)
Sapin.afficherSapin()

GuirlandeLumineuse1 = GuirlandeLumineuse(50,'bleu',50,80)
Sapin.ajouter(GuirlandeLumineuse1)
Sapin.afficherSapin()
