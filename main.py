import pygame, time, math, random, threading

#from pygame.mask import _Offset

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
import vyhralsi,prehralsi
import text

class myThread (threading.Thread):
   def __init__(self, funkcia):
      threading.Thread.__init__(self)
      self.funkcia = funkcia
   def run(self):
      self.funkcia()


vyhrat = None
prehrat = None
testHrac = None
trubiroh = None
myska = None

z.testMuzika.play()
z.testMuzika.set_volume(0.3)
def fyzika():
    global g,koniec
    while not koniec and not klavesy.je_koniec():
        #print("f")
        mys.update()
        klavesy.update()

        #g.offsetKamery[0] -= 0.05# funguje
        g.scaleKamery = 0.5

        if klavesy.je_keyup('v'):
            z.test.play()
            animacia(a.animacia,0.7,500,20,loop=False)
            print("grg")

        testHrac.update()
        trubiroh.update()
        # sprity.update()

        tlacidla.update()
        animacie.update()

        if vyhrat.je_keyup():
            koniec = True
            #time.sleep(1)
            vyhralsi.spustit()
            break

        if prehrat.je_keyup():
            koniec = True
            prehralsi.spustit()
            break

        #time.sleep(0.02)
        ratacfpsF.update()


def zobrazovac():
    global g
    while not koniec and not klavesy.je_koniec():
        #print("z")
        g.Displej.fill(g.farby.modra)
        #print("sem som sa dostal")
        pygame.zobraz(o.pozadie,(40,40))
        testHrac.zobraz()
        trubiroh.zobraz()# sprity.draw(g.Displej)
        pygame.zobraz(o.auto,(g.displej_width/2,g.displej_height),roh="lavy_dolny")

        tlacidla.zobraz()
        animacie.zobraz()
        ratacfpsF.zobraz()
        ratacfpsZ.zobraz()

        #print(bubu.surface.get_width())

        myska.zobraz()
        pygame.display.update()
        ratacfpsZ.update()

def gameloop():
    global zobrazovacThread
    thread = myThread(fyzika)#zobrazovac
    thread.start()
    print("gameloop")
    zobrazovac()#fyzika()

def spustit():
    global vyhrat,prehrat,testHrac,trubiroh,myska
    reset()
    #volajakeTlacidlo = tlacidlo(t.testtlacidloN,t.testtlacidloA,500,500)
    vyhrat = tlacidlo(t.vyhralsiN,t.vyhralsiA,700,500,text="vyhrat")
    prehrat = tlacidlo(t.prehralsiN,t.prehralsiA,810,500,text="prehrat")
    testHrac = s.hrac(o.test1)#
    trubiroh = s.trubiroh(o.auto)
    myska = s.mys(o.mys)
    #bubu = text.text(0,0,"bubacik",10,g.farby.cierna,g.basic_font,roh="pravy_dolny")
    # sprity = pygame.sprite.Group()
    # sprity.add(trubiroh)#cim neskor pridam tym viac vpredu je
    # sprity.add(testHrac)
    
    #globals().update(locals())
    print("spustam")
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

'''
co treba spravit:
otestovat konvert na .exe
tlacidlo pauza
detekcia kolizie(lubovolneho prekryvu) nepriehladnych casti lubovolnych dvoch spritov
otacanie obrazkov - ked zobrazujem, pridat otocenie a suradnice body oatacania
aby to fungovalo aj na obrazovkach s inym rozlisenim

bugy:
maska tlacidla sa neupdatuje ked sa scalne displej asi nemenit pocas scalovanie ale az na konci, tlacidla sa pocas toho asi aj tak nepouziju, mozno chceme disable tlacidla

adam:
text input
textove pole - automaticky enter..., input cisel(slider alebo sipky zvecsit zmensit)

???:
particle system
zarovnavanie textu - da sa velmi lahko spravit ak treba
mat co najmenej veci v classe g
hp bar linearne sa zmensujuci on hit
grid tlacidiel, kazde identifikovatelne riadkom a stlpcom
Updatovat iba časť obrazovky, ktoré sa zmenili oproti predošlému framu

tlacidlo sa trosku zvecsi on hover - Aobrazok stacia aby bol vecsi
zrychlovanie, spomalovanie automaticky pri hybani - ked nastavim rychlost, bude na nu najprv zrychlovat/spomalovat
'''