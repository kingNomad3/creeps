class Creep:
    def __init__(self, parent):
        self.parent = parent
        self.vie = 20
        self.vitesse = 5
        self.couleur = "red"
        self.depart_creep  = [100,0]
        self.dimensions = {
            "cx": 160,
            "cy": 0,
            "x1": 240,
            "y1": 80}


    def mouvement_creep(self):
        pivot_courrant = self.parent.chemin.pivots[1]

        if self.dimensions["cy"] < pivot_courrant[1]:
            self.dimensions["cy"]+= 1

        elif self.dimensions["cx"] < pivot_courrant[0]:
            self.dimensions["cx"]+= 1

        elif self.dimensions["cy"] < pivot_courrant[1]:
            self.dimensions["cy"] -= 1

        elif self.dimensions["cx"] < pivot_courrant[0]:
            self.dimensions["cx"] -= 1


