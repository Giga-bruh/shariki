

import pygame as pg

from nastroiki import *
import baza_sharikov





class Player(baza_sharikov.Baza):
    def __init__(self, igra, x, y, color, radiys: int):
        super().__init__(igra, x, y, color, radiys)
        self.speed_x = 1
        self.speed_y = 1

        self.gde_mishka=0
        self.idti_ili_net=0

    def ypravlenie(self):


        self.gde_mishka=pg.mouse.get_pos()

        if self.pramoygolnik.x+30 >= SCREEN_WIDTH :
            self.pramoygolnik.x -=1
        if self.pramoygolnik.x-10 <=0:
            self.pramoygolnik.x+=1
        if self.pramoygolnik.y-10 <= 0 :
            self.pramoygolnik.y +=1
        if  self.pramoygolnik.y+30  >= SCREEN_HEIGHT:
            self.pramoygolnik.y -=1

        else:
            if self.pramoygolnik.center!=self.gde_mishka and self.idti_ili_net==1:


                if self.gde_mishka[0]>self.pramoygolnik.center[0]:


                    self.pramoygolnik.centerx+=1
                elif self.gde_mishka[0]<self.pramoygolnik.center[0]:

                    self.pramoygolnik.centerx-=1
                if self.gde_mishka[1]<self.pramoygolnik.center[1]:

                    self.pramoygolnik.centery-=1
                elif self.gde_mishka[1]>self.pramoygolnik.center[1]:

                    self.pramoygolnik.centery+=1





    def sieden_ili_net(self):
        for sieden_ili_net in self.igra.spisok_botov:


                    if self.pramoygolnik_proverka.colliderect(sieden_ili_net.pramoygolnik_proverka):

                        if self.radiys> sieden_ili_net.radiys:
                            self.igra.spisok_botov.remove(sieden_ili_net)
                            self.pramoygolnik.width +=sieden_ili_net.radiys//2
                            self.pramoygolnik.height+=sieden_ili_net.radiys//2
                            self.pramoygolnik_proverka.width += sieden_ili_net.radiys // 2
                            self.pramoygolnik_proverka.height += sieden_ili_net.radiys // 2
                        elif self.radiys<sieden_ili_net.radiys:



                            self.igra.proigral_ili_pobedil= "вы проиграли"

                    if self.radiys>=100:
                        self.igra.proigral_ili_pobedil="вы победили"
    def otrisovka(self):
        super().otrisovka()

