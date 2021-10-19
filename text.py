import pygame
from globalnepremenne import g

class text:
    def __init__(self, x, y,co,velkost,farba,font,roh="lavy_horny"):#ako positional arguemnt dorobit podla ktoreho rohu sa zobrazuje
        self.co = co
        self.velkost = velkost
        self.farba = farba
        self.font = font
        self.x = x
        self.y = y
        self.roh = roh
        self.surface = self.generujSurface(co,velkost,farba,font)

    def generujSurface(self,co,velkost,farba,font):
        Fond = pygame.font.Font(font, velkost)    
        textSurface = Fond.render(co, True, farba)
        # TextSurf, TextRect = (textSurface, textSurface.get_rect())
        # TextRect.center = (self.x, self.y)
        return textSurface

    def zobraz(self,kamSurface=g.Displej):
        pygame.zobraz(self.surface,(self.x,self.y),ui=True,surface=kamSurface,roh=self.roh)

    def zmenText(self,novyText):
        self.co = novyText
        self.surface = self.generujSurface(self.co,self.velkost,self.farba,self.font)

    def zmenVelkost(self,velkost):
        self.velkost = velkost
        self.surface = self.generujSurface(self.co,self.velkost,self.farba,self.font)

    def zmenFarbu(self,farba):
        self.farba = farba
        self.surface = self.generujSurface(self.co,self.velkost,self.farba,self.font)

    def zmenPoziciu(self,x,y):
        self.x = x
        self.y = y

    def zmenFont(self):
        pass