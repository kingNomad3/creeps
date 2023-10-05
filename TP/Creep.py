numero_id = 0

def prochain_id():
    global numero_id
    numero_id += 1
    return "creep_" + str(numero_id)

class Creep:
    def __init__(self, parent):
        self.parent = parent
        self.pivot = 1
        self.vie = 20
        self.vitesse = 5
        self.id = prochain_id()
        self.couleur = "red"
        self.dimensions = {
            "x1": 160,
            "y1": 0,
            "x2": 240,
            "y2": 80
        }
        self.is_alive = True
        self.a_tue = False




    def mouvement_creep(self):
        pivot_actuel = self.parent.chemin.pivots[self.pivot]
        monter = 1
        a_droite = 1
        if self.dimensions["x1"] == pivot_actuel[0] and self.dimensions["y2"] == pivot_actuel[1]:
            self.pivot = self.pivot + 1
        pivot_actuel = self.parent.chemin.pivots[self.pivot]

        if self.dimensions["x1"] == pivot_actuel[0]:
            if self.dimensions["y2"] - pivot_actuel[1] > 0:
                monter = monter * -1
            self.dimensions["y1"] = self.dimensions["y1"] + 10 * monter
            self.dimensions["y2"] = self.dimensions["y2"] + 10 * monter

        elif self.dimensions["y2"] == pivot_actuel[1]:
            if self.dimensions["x1"] - pivot_actuel[0] > 0:
                a_droite = a_droite * -1
            self.dimensions["x1"] = self.dimensions["x1"] + 10 * a_droite
            self.dimensions["x2"] = self.dimensions["x2"] + 10 * a_droite

        if self.dimensions["x1"] == 1120 and self.dimensions["y2"] == 640:
            self.is_alive = False
            self.a_tue = True


