from globalnepremenne import g
import pygame
from klavesy import je_keydown, je_keyup
from loaderObrazkov import o
import mys
import text as Text

maskamys = pygame.mask.from_surface(o.pixel)
maskamys.fill()

tlacidla = []
def update():
    for i in tlacidla:
        i.update()

def zobraz():
    for i in tlacidla:
        i.zobraz()

class tlacidlo:
    def __init__(self, Nobrazok, Aobrazok, x, y,text="",velkost=15,farba=(0,0,0),font=g.tlacidlovy):#dorobit roh podla ktoreho sa zobrazuje
        
        self.Nobrazok = Nobrazok
        self.Aobrazok = Aobrazok
        self.surface = Nobrazok
        self.kompletSurface = Nobrazok
        self.x = x
        self.y = y
        self.text = Text.text(self.surface.get_width()/2,self.surface.get_height()/2,text,velkost,farba,font,roh="stred")#x, y,co,velkost,farba,font
        self.maska = pygame.mask.from_surface(Nobrazok)
        self.jeStlacene = False
        self.jeKeydown = False
        self.jeKeyup = False
        self.hover = "N"
        self.predoslyHover = self.hover
        self.zmenaHover = False
        tlacidla.append(self)
        self.zobrazText()

    def update(self):
        offset = (mys.pozicia[0] - int(self.x), mys.pozicia[1] - int(self.y))#offset myse od laveho horneho rohu obrazku
        if self.maska.overlap(maskamys, offset) is None:
            self.surface = self.Nobrazok
            self.hover = "N"
            #self.text.zmenPoziciu(self.Nobrazok.get_width()/2,self.Nobrazok.get_height()/2)
            self.jeStlacene = False
        else:
            self.surface = self.Aobrazok
            self.hover = "A"
            #self.text.zmenPoziciu(self.Aobrazok.get_width()/2,self.Aobrazok.get_height()/2)
            self.jeKeydown = False
            if mys.click[0] == 1 and self.jeStlacene == False:
                self.jeKeydown = True
            
            self.jeKeyup = False
            if self.jeStlacene == True and mys.click[0] == 0:
                self.jeKeyup = True

            self.jeStlacene = False
            if mys.click[0] == 1:
                self.jeStlacene = True

        if self.hover != self.predoslyHover:
            self.zmenaHover = True
            self.zobrazText()
        else:
            self.zmenaHover = False

        self.predoslyHover = self.hover


    def zobrazText(self):
        self.kompletSurface = self.surface.copy()
        self.text.zobraz(kamSurface=self.kompletSurface)

    def zobraz(self):
        pygame.zobraz(self.kompletSurface,(self.x,self.y), ui=True)

    def je_stlacene(self):
        return self.jeStlacene

    def je_keydown(self):
        return self.jeKeydown

    def je_keyup(self):
        return self.jeKeyup

    def je_zmena_hover(self):#minuly frame som bol mimo, teraz som v alebo naopak
        return self.zmenaHover

    def zmenText(self,novy):
        self.text.zmenText(novy)
        self.zobrazText()