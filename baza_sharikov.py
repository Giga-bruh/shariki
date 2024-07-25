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
    def ypravlenie(self):
       if self.pramoygolnik.centerx+50>=SCREEN_WIDTH or self.pramoygolnik.x<=0:
            self.speed_x = -self.speed_x

       if self.pramoygolnik.topleft[1] <= 0 or self.pramoygolnik.bottomright[1]+50 >= SCREEN_HEIGHT:
            self.speed_y = -self.speed_y







    def otrisovka(self):


        pygame.draw.ellipse(self.igra.screen, self.color, self.pramoygolnik)

    def update(self):
        self.ypravlenie()
        self.otrisovka()

