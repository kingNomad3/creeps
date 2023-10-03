from tkinter import *

class Vue:
    def __init__(self, parent, modele):
        self.parent = parent
        self.modele = modele
        self.root = Tk()
        self.init_fenetre()

    def init_fenetre(self):
        self.frame_jeu = Canvas(self.root, height=960, width=1280, bg="black")
        self.frame_jeu.pack()
        self.terrain = self.frame_jeu.create_rectangle(0,0,1282,720, fill='white') # Pixel de trop
        self.afficher_chemin()
        self.afficher_creep()


    def afficher_chemin(self):
        for i in self.modele.chemin.chemin:
            self.frame_jeu.create_rectangle(i[0][0]+40, i[0][1], i[1][0]+40, i[1][1], width=80, fill='yellow', tags=("bordures",))

    def afficher_creep(self):
        for i in self.modele.creeps:
            self.frame_jeu.create_oval(i.dimensions["cx"], i.dimensions["cy"],i.dimensions["x1"], i.dimensions["y1"], fill="red", tags=("creeps",))

    def afficher_modele(self):
        self.frame_jeu.delete("creeps")
        self.afficher_creep()