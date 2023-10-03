numero_id = 0

def prochain_id():
    global numero_id
    numero_id += 1
    return "creep_" + str(numero_id)

class Creep:
    def __init__(self, parent):
        self.parent = parent
        self.vie = 20
        self.vitesse = 5
        self.id = prochain_id()
        self.couleur = "red"
        self.dimensions = {
            "cx": 160,
            "cy": 0,
            "x1": 240,
            "y1": 80
        }

    def mouvement_creep(self):
        pivot_courrant = self.parent.chemin.pivots[1]

        if self.dimensions["cy"] < pivot_courrant[1]:
            self.dimensions["cy"] += 10
            self.dimensions["y1"] += 10

        elif self.dimensions["cx"] < pivot_courrant[0]:
            self.dimensions["cx"] += 10
            self.dimensions["x1"] += 10

        elif self.dimensions["cy"] > pivot_courrant[1]:
            self.dimensions["cy"] -= 10
            self.dimensions["y1"] -= 10

        elif self.dimensions["cx"] > pivot_courrant[0]:
            self.dimensions["cx"] -= 10
            self.dimensions["x1"] -= 10


