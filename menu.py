import pygame, time, math, random, threading

pygame.init()

from globalnepremenne import init as G_init
G_init()
from globalnepremenne import g

from sprity import init as S_init
S_init()
from sprity import s

import niepygame
from loaderObrazkov import o,t,a,z

import klavesy
import ratacfps
ratacfpsF = ratacfps.ratacfps(10,"F")
ratacfpsZ = ratacfps.ratacfps(25,"Z")

from tlacidla import tlacidlo
import tlacidla
from animacie import animacia,obrazky_v_case
import animacie
import mys
import main
from funkcie import resetScreen

class myThread (threading.Thread):
   def __init__(self, funkcia):
      threading.Thread.__init__(self)
      self.funkcia = funkcia
   def run(self):
      self.funkcia()


myska = None
koniec = False
levely1 = None

def fyzika():
    global g,koniec
    while not koniec and not klavesy.je_koniec():
        #print("f")
        mys.update()
        klavesy.update()

        tlacidla.update()
        animacie.update()

        level = levely1.spustiLevel()
        if level != False:
            koniec = True
            main.spustit(level)
            break
        # if hrat.je_keyup():
        #     koniec = True
        #     #time.sleep(1)
        #     main.spustit()
        #     break

        ratacfpsF.update()


def zobrazovac():
    global g
    while not koniec and not klavesy.je_koniec():
        #print("z")
        g.Displej.fill(g.farby.modra)

        levely1.zobraz()

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
    #hrat = tlacidlo(t.testtlacidloN,t.testtlacidloA,500,500,text="hrat")
    myska = s.mys(o.mys)
    levely1 = s.levelSet(o.level1Panak,o.level1Pozadie,(400,100),(100,100),t.levelA,t.levelN)
    globals().update(locals())#globalne premenne rozsiri o lokalne
    gameloop()

if __name__ == "__main__":
    spustit()
#gameloop()