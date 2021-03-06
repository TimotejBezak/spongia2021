from globalnepremenne import g
import pygame
from klavesy import je_keydown, je_keyup
from loaderObrazkov import o,z
import mys
import text as Text
import prekryvace

# maskamys = pygame.mask.from_surface(o.pixel)
# maskamys.fill()
mysPrekryvac = prekryvace.prekryvac(o.pixel)

tlacidla = []
def update():
    for i in tlacidla:
        i.update()

def zobraz():
    for i in tlacidla:
        i.zobraz()

class tlacidlo:
    def __init__(self, Nobrazok, Aobrazok, x, y,text="",velkost=15,farba=(0,0,0),font=g.tlacidlovy,roh="lavy_horny",disabled=False,textOffset=[0,0]):#dorobit roh podla ktoreho sa zobrazuje
        # self.textOffset = textOffset
        self.disabled = disabled
        self.Nobrazok = Nobrazok
        self.Aobrazok = Aobrazok
        self.surface = Nobrazok
        self.kompletSurface = Nobrazok
        self.x,self.y = pygame.rohUpdate([x,y],Nobrazok,roh)
        self.text = Text.text(self.surface.get_width()/2+textOffset[0],self.surface.get_height()/2+textOffset[1],text,velkost,farba,font,roh="stred")#x, y,co,velkost,farba,font
        self.jeStlacene = False
        self.jeKeydown = False
        self.jeKeyup = False
        self.hover = "N"
        self.predoslyHover = self.hover
        self.zmenaHover = False
        self.prekryvac = prekryvace.prekryvac(Nobrazok)
        self.prekryvac.updatePos(self.x,self.y)
        tlacidla.append(self)
        self.zobrazText()

    def update(self):
        mysPrekryvac.updatePos(mys.pozicia[0],mys.pozicia[1])
        if self.prekryvac.prekryvaSa(mysPrekryvac):
            self.surface = self.Nobrazok
            self.hover = "N"
            self.jeStlacene = False
        else:
            self.surface = self.Aobrazok
            self.hover = "A"
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
        if self.disabled:
            return False
        return self.jeStlacene

    def je_keydown(self):
        if self.disabled:
            return False
        return self.jeKeydown

    def je_keyup(self):
        if self.disabled:
            return False
        if self.jeKeyup:
            z.klik.play()
        return self.jeKeyup

    def je_zmena_hover(self):#minuly frame bol kurzor mimo, teraz je v alebo naopak
        if self.disabled:
            return False
        return self.zmenaHover

    def zmazSa(self):
        tlacidla.remove(self)

    def zmenText(self,novy):
        self.text.zmenText(novy)
        self.zobrazText()