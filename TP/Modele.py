from Chemin import *
from Creep import *
from Tour import *


class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.creeps = []
        self.chemin = Chemin()
        self.tours = []
        self.creer_creeps()


    def creer_creeps(self):
         creep = Creep(self)
         self.creeps.append(creep)

    def creer_tour(self):
        tour = Tour()
        self.tours.append(tour)

    def travailler(self):
        if len(self.creeps) < 19 and self.parent.temps % 500 == 0:
            self.creer_creeps()
        for i in self.creeps:
            i.mouvement_creep()
            if not i.is_alive:
                self.creeps.remove(i)
