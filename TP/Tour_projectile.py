import helper as hp


class Tour_projectile():
    def __init__(self, parent, x, y):
        self.x = x
        self.y = y
        self.parent = parent
        self.rayon = 150
        self.dommage = 5
        self.cible_courante = None

    def chercher_cible(self):
        if not self.cible_courante:
            for i in self.parent.creeps:
                distance = hp.calcDistance(self.x, self.y, i.dimensions["x1"], i.dimensions["y1"])
                if distance <= self.rayon:
                    self.cible_courante = i
        else:
            if self.cible_courante > self.rayon:
                self.cible_courante = None

    def attaquer_cible(self):
        self.cible_courante.vie -= self.dommage