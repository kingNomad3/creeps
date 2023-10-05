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
        if self.modele.tour_a_creer != -1 and self.modele.x and self.modele.y:
            print("wkewoke")
            self.modele.creer_tour()
            self.vue.afficher_tours()
        self.nouvelle_partie()

    def nouvelle_partie(self):
        if len(self.modele.creeps) == 0:
            pass
        if self.temps % 30000 == 0:
            self.modele.compteur = 0