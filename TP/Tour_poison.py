import helper as hp
from Obus import *


class Tour_poison():
    def __init__(self, parent, x, y):
        self.x = x
        self.y = y
        self.parent = parent
        self.fire_rate = 500
        self.rayon = 200
        self.dommage = 5
        self.temps_poison = 2000
        self.cible_courante = None
        self.obus = None
        self.creeps_trop_loin = []
        self.distance_avant = {}
        self.active = True

    def chercher_cible(self, temps):
         for i in self.parent.creeps:
            distance = hp.Helper.calcDistance(self.x, self.y, i.dimensions["x1"], i.dimensions["y1"])
            if distance <= self.rayon:
                self.cible_courante = i
                return True
         return False

    def attaquer_cible(self):
        if hp.Helper.calcDistance(self.x, self.y, self.cible_courante.dimensions["x1"], self.cible_courante.dimensions["y1"]) <= self.rayon:
            if self.obus:
                collision = self.obus.voyage_cible()
                if collision:
                    self.cible_courante.vie -= self.dommage
                    self.parent.parent.vue.effacer_obus(self.obus)
                    self.obus = None
                    if self.cible_courante.vie <= 0:
                        self.cible_courante = None
            else:
                self.obus = Obus(self)
        else:
            self.cible_courante = None
            self.parent.parent.vue.effacer_obus(self.obus)
            self.obus = None

