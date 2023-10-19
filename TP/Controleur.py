from Vue import *
from Modele import *

class Controleur:
    def __init__(self):
        self.temps = 0
        self.vague = 1
        self.vies = 20
        self.argent = 100
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
            self.modele.creer_tour()
        self.vue.afficher_tours()
        self.nouvelle_partie()
        self.vue.afficher_obus()
        for i in self.modele.tours:
            if i.cible_courante:
                i.attaquer_cible()
            else:
                i.chercher_cible(self.temps)
        print(len(self.vue.frame_jeu.find_all()))

    def nouvelle_partie(self):
        if len(self.modele.creeps) == 0:
            pass
        if self.temps % 30000 == 0:
            self.modele.compteur = 0
            self.temps = 0
            self.vague += 1