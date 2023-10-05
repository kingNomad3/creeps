from Vue import *
from Modele import *

class Controleur:
    def __init__(self):
        self.temps = 0
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        self.vue.root.after(500, self.boucler_travail)
        self.vue.root.mainloop()

    def boucler_travail(self):
        self.modele.travailler()
        self.vue.afficher_modele()
        self.vue.root.after(50, self.boucler_travail)
        self.temps += 50


