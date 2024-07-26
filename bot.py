import pygame

import baza_sharikov
from nastroiki import *
import random

class Bot(baza_sharikov.Baza):
    def __init__(self, igra, x, y,color,radiys:int):
        super().__init__(igra,x,y,color,radiys)
        self.speed_x=random.randint(1,3)

        self.x_dvishenia = random.randint(0, 900)
        self.y_dvishenia = random.randint(0, 600)
        self.speed_y=random.randint(1,3)


    def ypravlenie(self):

        for kto_peresek in self.igra.spisok_botov:
            if self.pramoygolnik.centerx + 30 >= SCREEN_WIDTH or self.pramoygolnik.x-10 <= 0 or self.pramoygolnik.y-10 <= 0 or self.pramoygolnik.y+30  >= SCREEN_HEIGHT:
                self.random_storona = random.randint(0, 3)
                if self.random_storona == 0:
                    self.kakaya_storona_x = random.randint(30, 870)
                    self.kakaya_storona_y = 30
                if self.random_storona == 1:
                    self.kakaya_storona_y = random.randint(30, 570)
                    self.kakaya_storona_x = 30
                if self.random_storona == 2:
                    self.kakaya_storona_y = 570
                    self.kakaya_storona_x = random.randint(30, 870)
                if self.random_storona == 3:
                    self.kakaya_storona_x = 870
                    self.kakaya_storona_y = random.randint(30, 570)
                self.pramoygolnik.x=self.kakaya_storona_x
                self.pramoygolnik.y=self.kakaya_storona_y
                self.x_dvishenia = random.randint(0, 900)
                self.y_dvishenia = random.randint(0, 600)

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

            self.x_dvishenia = random.randint(30, 900)
            self.y_dvishenia = random.randint(30, 600)









    def otrisovka(self):
        super().otrisovka()





