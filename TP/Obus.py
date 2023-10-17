numero_id = 0


def prochain_id():
    global numero_id
    numero_id += 1
    return "tour_" + str(numero_id)


class Obus():
    def __init__(self, parent):
        self.parent = parent
        self.x = parent.x
        self.y = parent.y
        self.alive = True
        self.collision = False
        self.id = "obus_" + prochain_id()
        self.id_tkinter = None



    def voyage_cible(self):
        cible_x = self.parent.cible_courante.dimensions["x1"] + 38
        cible_y = self.parent.cible_courante.dimensions["y1"] + 40

        if cible_x > self.x:
            self.x += 30
        if cible_x < self.x:
            self.x -= 30
        if cible_y > self.y:
            self.y += 30
        if cible_y < self.y:
            self.y -= 30

        if (abs(cible_y - self.y) <= 20
                and abs(cible_x - self.x) <= 20):
            print("shoot")
            self.alive = False
            self.collision = True

        return self.collision