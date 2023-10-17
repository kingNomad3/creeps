import helper as hp
from Obus import *


class Tour_poison():
    def __init__(self, parent, x, y):
        self.x = x
        self.y = y
        self.parent = parent
        self.fire_rate = 500
        self.rayon = 250
        self.dommage = 20
        self.temps_poison = 2000
        self.cible_courante = None
        self.obus = None
        self.creeps_trop_loin = []
        self.distance_avant = {}
        self.active = True

    def chercher_cible(self, temps):
        if not len(self.creeps_trop_loin) >= len(self.parent.creeps):
            if not self.cible_courante:
                for i in self.parent.creeps:
                    if i.rayon:
                        distance = hp.Helper.calcDistance(self.x, self.y, i.dimensions["x1"], i.dimensions["y1"])
                        if distance <= self.rayon:
                            self.cible_courante = i
                            print("la cibles est chercher")
                            return True
                        else:

                            print("`la cibles n;est pas chercher")
                            if i.id in self.distance_avant and distance > self.distance_avant[i.id]:
                                i.rayon = False
                                self.creeps_trop_loin.append(i)
                            else:
                                self.distance_avant[i.id] = distance
            else:
                distance = hp.Helper.calcDistance(self.x, self.y, self.cible_courante.dimensions["x1"],
                                                  self.cible_courante.dimensions["y1"])
                if distance > self.rayon or self.cible_courante.vie <= 0:
                    self.cible_courante = None
                    self.parent.parent.vue.effacer_obus(self.obus)
                    self.obus = None

        else: self.active = False
        return False

    def attaquer_cible(self):
        if self.cible_courante.vie > 0:
            if not self.obus:
                self.obus = Obus(self)
            else:

                collision = self.obus.voyage_cible()
                if collision:
                    self.cible_courante.vie -= self.dommage
                    self.parent.parent.vue.effacer_obus(self.obus)
                    self.obus = None
                    print(self.cible_courante.vie)
                    print(self.obus)

        if not len(self.creeps_trop_loin) >= len(self.parent.creeps) and self.cible_courante:
            self.cible_courante = None
            #print("ça marche pas")

