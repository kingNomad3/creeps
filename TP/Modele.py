from Chemin import *
from Creep import *
from Tour_laser import *


class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.creeps = []
        self.chemin = Chemin()
        self.tours = []
        self.creer_creeps()
        self.temps = self.parent.temps
        self.compteur = 0

    def creer_creeps(self):
        creep = Creep(self)
        self.creeps.append(creep)

    def creer_tour(self):
        tour = None
        if self.parent.vue.tour_a_creer == 0:
            tour = Tour_laser(self, self.x, self.y)
        elif self.parent.vue.tour_a_creer == 1:
            tour = Tour_projectile(self, self.x, self.y)
        elif self.parent.vue.tour_a_creer == 2:
            tour = Tour_poison(self, self.x, self.y)
        if tour:
            self.tours.append(tour)
            self.parent.vue.tour_a_creer == -1

    def travailler(self):
        if len(self.creeps) < 19 and self.parent.temps % 700 == 0 and self.compteur < 20:
            self.creer_creeps()
            self.compteur += 1
        for i in self.creeps:
            i.mouvement_creep()
            if not i.is_alive:
                self.creeps.remove(i)
