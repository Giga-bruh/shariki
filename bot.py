import pygame

import baza_sharikov
from nastroiki import *
import random

class Bot(baza_sharikov.Baza):
    def __init__(self, igra, x, y,color,radiys:int):
        super().__init__(igra,x,y,color,radiys)
        self.speed_x=random.randint(1,3)
        self.x_dvishenia = random.randint(30, 850)
        self.y_dvishenia = random.randint(30, 550)
        self.speed_y=random.randint(1,3)


    def ypravlenie(self):
        super().ypravlenie()
        for kto_peresek in self.igra.spisok_botov:
            if self.pramoygolnik.centerx + 50 >= SCREEN_WIDTH or self.pramoygolnik.x <= 0:
                pass


            if self.pramoygolnik.topleft[1] <= 0 or self.pramoygolnik.bottomright[1] + 50 >= SCREEN_HEIGHT:
                pass

        self.random_koordinati=(self.x_dvishenia,self.y_dvishenia)

        if self.pramoygolnik.center!=self.random_koordinati:
            if self.random_koordinati[0] > self.pramoygolnik.center[0]:

                self.pramoygolnik.centerx += 1
            elif self.random_koordinati[0] < self.pramoygolnik.center[0]:

                self.pramoygolnik.centerx -= 1
            if self.random_koordinati[1] < self.pramoygolnik.center[1]:

                self.pramoygolnik.centery -= 1
            elif self.random_koordinati[1] > self.pramoygolnik.center[1]:

                self.pramoygolnik.centery += 1
        else:

            self.x_dvishenia = random.randint(30, 850)
            self.y_dvishenia = random.randint(30, 550)









    def otrisovka(self):
        super().otrisovka()





