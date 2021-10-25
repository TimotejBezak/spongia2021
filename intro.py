import pygame, time, math, random, threading

pygame.init()

from globalnepremenne import init as G_init
G_init()
from globalnepremenne import g

from sprity import init as S_init
S_init()
from sprity import s

import niepygame
from loaderObrazkov import o,t,a

import klavesy
import ratacfps
ratacfpsF = ratacfps.ratacfps(10,"F")
ratacfpsZ = ratacfps.ratacfps(25,"Z")

from tlacidla import tlacidlo
import tlacidla
from animacie import animacia,obrazky_v_case
import animacie
import mys
import menu
from funkcie import resetScreen

class myThread (threading.Thread):
   def __init__(self, funkcia):
      threading.Thread.__init__(self)
      self.funkcia = funkcia
   def run(self):
      self.funkcia()


myska = None
hrat = None
koniec = False

def fyzika():
    global g,koniec
    while not koniec and not klavesy.je_koniec():
        #print("f")
        mys.update()
        klavesy.update()

        tlacidla.update()
        animacie.update()

        if hrat.je_keyup():
            koniec = True
            #time.sleep(1)
            menu.spustit()
            break

        ratacfpsF.update()


def zobrazovac():
    global g
    while not koniec and not klavesy.je_koniec():
        #print("z")
        g.Displej.fill(g.farby.cervena)

        tlacidla.zobraz()
        animacie.zobraz()
        ratacfpsF.zobraz()
        ratacfpsZ.zobraz()
        myska.zobraz()
        pygame.display.update()
        ratacfpsZ.update()

def gameloop():
    t = myThread(fyzika)
    t.start()
    zobrazovac()

def spustit():
    #global myska,hrat
    koniec = False
    resetScreen()
    #print(tlacidla.tlacidla)
    hrat = tlacidlo(t.testtlacidloN,t.testtlacidloA,500,500,text="hrat")
    myska = s.mys(o.mys)
    globals().update(locals())#globalne premenne rozsiri o lokalne
    gameloop()

def reset():
    global koniec,g
    koniec = False
    tlacidla.tlacidla = []
    animacie.animacie = []
    g.Displej = pygame.display.set_mode((g.displej_width, g.displej_height))
    g.frameF = 0
    g.frameZ = 0

if __name__ == "__main__":
    spustit()
#gameloop()