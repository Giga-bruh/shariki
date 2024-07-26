import random
import igrok
import time
import pygame as p
import bot
p.init()
import pygame.freetype
from nastroiki import *
class Game:
    def __init__(self):

        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Шарики")
        self.izmenisla_ili_net=0
        self.tekst = p.freetype.Font("kartinki/comic-sans-ms.ttf", 80)
        self.igrok = igrok.Player(self,SCREEN_WIDTH/2, SCREEN_HEIGHT/2, [255, 255, 255],
                          20 )

        self.proigral_ili_pobedil=0
        self.spisok_botov=[]
        self.sobitie_sozdania=p.USEREVENT
        self.sobitie_dvishenia=p.USEREVENT+1
        p.time.set_timer(self.sobitie_dvishenia,100)
        p.time.set_timer(self.sobitie_sozdania, 1000)

        self.clock = pg.time.Clock()
        self.run()
    def run(self):
        while True:

                self.event()
                self.update()
                self.draw()
                self.igrok.sieden_ili_net()
                for boti in self.spisok_botov:
                    boti.ypravlenie()
                self.clock.tick(FPS)
                self.screen.fill([1, 1, 1])




    def event(self):
        for event in p.event.get():
            if event.type==pg.QUIT:
                quit()
            if event.type==self.sobitie_sozdania and len(self.spisok_botov)<=20:

                self.random_storona = random.randint(0, 3)
                if self.random_storona==0:
                    self.kakaya_storona_x=random.randint(30,870)
                    self.kakaya_storona_y=30
                if self.random_storona==1:
                    self.kakaya_storona_y = random.randint(30, 570)
                    self.kakaya_storona_x = 30
                if self.random_storona==2:
                    self.kakaya_storona_y =  570
                    self.kakaya_storona_x = random.randint(30,870)
                if self.random_storona == 3:
                    self.kakaya_storona_x = 870
                    self.kakaya_storona_y = random.randint(30, 570)


                self.bot = bot.Bot(self,self.kakaya_storona_x,self.kakaya_storona_y,
                                   [random.randint(1,255),random.randint(1,255),random.randint(1,255)], random.randint(self.igrok.radiys//2, self.igrok.radiys*2) )
                self.spisok_botov.append(self.bot)
            if event.type==self.sobitie_dvishenia and self.igrok.pramoygolnik.centerx!=self.igrok.gde_mishka:
                self.igrok.idti_ili_net=1


    def draw(self):
        if self.igrok.radiys <= 100 and self.proigral_ili_pobedil == 0:


            if self.izmenisla_ili_net==1:
                self.igrok = igrok.Player(self, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, [255, 255, 255],
                                          self.igrok.radiys )
            p.draw.rect(self.screen, [250, 0, 0], [0, 0, 900, 600], 5)
        else:
            self.tekst.render_to(self.screen, [SCREEN_WIDTH/4, SCREEN_HEIGHT/3], self.proigral_ili_pobedil, [255, 255, 255])
        p.display.flip()
    def update(self):
        if self.igrok.radiys != 100 and self.proigral_ili_pobedil == 0:
            for bot in self.spisok_botov:
                bot.update()
            self.igrok.update()




if __name__ == "__main__":
    Game()