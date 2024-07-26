import pygame
from nastroiki import *
import random

class Baza:
    def __init__(self, igra, x, y, color, radiys: int):
        super().__init__()
        self.speed_x=1
        self.color=color
        self.x=x

        self.y=y

        self.radiys=radiys
        self.speed_y=1
        self.igra = igra



        self.pramoygolnik=pg.rect.Rect(self.x,self.y,self.radiys,self.radiys)
        self.pramoygolnik_proverka = pg.rect.Rect(self.x, self.y, self.radiys/1.7, self.radiys/1.7)









    def otrisovka(self):

        self.pramoygolnik_proverka.center=self.pramoygolnik.center
        pygame.draw.ellipse(self.igra.screen, self.color, self.pramoygolnik)



    def update(self):
        self.ypravlenie()
        self.otrisovka()

