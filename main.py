import pygame, math, random, threading,time

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
import vyhralsi,prehralsi,menu
import text
import cas

from funkcie import resetScreen


class myThread (threading.Thread):
   def __init__(self, funkcia):
      threading.Thread.__init__(self)
      self.funkcia = funkcia
   def run(self):
      self.funkcia()


vyhrat = None
prehrat = None
spetDoMenu = None
testHrac = None
trubiroh = None
myska = None
paused = False
pauza = None
odpauza = None
Xtlacidlo = None
testText = None
koniec = False
stena = None
level = None

z.testMuzika.play()
z.testMuzika.set_volume(0.3)
def fyzika():
    global g,paused,pauza,odpauza,koniec,stena,level
    while not koniec and not klavesy.je_koniec():
        if not paused:
            mys.update()
            klavesy.update()

            if klavesy.je_keyup('v'):
                z.test.play()
                animacia(a.animacia,0.7,500,20,loop=False)

            tlacidla.update()
            animacie.update()

            # stena.update()
            if level.update() == False:
                koniec = True
                vyhralsi.spustit()
                break


            if vyhrat.je_keyup():
                koniec = True
                vyhralsi.spustit()
                break

            if prehrat.je_keyup():
                koniec = True
                prehralsi.spustit()
                break

            if spetDoMenu.je_keyup():
                koniec = True
                menu.spustit()
                break

            if pauza.je_keyup():
                cas.pause()
                odpauza = tlacidlo(t.odpauzaN,t.odpauzaA,700,50,text="odpauznut")
                paused = True

            if Xtlacidlo.je_keyup():
                koniec = True
                
            #time.sleep(0.1)
            ratacfpsF.update()
        else:
            mys.update()
            tlacidla.update()
            klavesy.update()

            if odpauza.je_keyup():
                cas.unpause()
                paused = False
                odpauza.zmazSa()
            


def zobrazovac():
    global g
    while not koniec and not klavesy.je_koniec():
        g.Displej.fill(g.farby.modra)

        # stena.zobraz()
        pygame.zobraz(o.panak,(300,475),roh="stred")
        level.zobraz()

        tlacidla.zobraz()
        animacie.zobraz()
        ratacfpsF.zobraz()
        ratacfpsZ.zobraz()

        if paused:
            g.Displej.fill((g.farby.modra)) #nejaky iny overlay asi polotransparentny
            odpauza.zobraz()

        myska.zobraz()
        pygame.display.update()
        ratacfpsZ.update()

def gameloop():
    global zobrazovacThread
    thread = myThread(fyzika)
    thread.start()
    zobrazovac()

def spustit(levelI):
    #global vyhrat,prehrat,testHrac,trubiroh,myska,pauza
    koniec = False
    resetScreen()
    vyhrat = tlacidlo(t.vyhralsiN,t.vyhralsiA,1300,500,text="vyhrat")
    prehrat = tlacidlo(t.prehralsiN,t.prehralsiA,1410,500,text="prehrat")
    spetDoMenu = tlacidlo(t.spetDoMenuN,t.spetDoMenuA,1520,500,text="menu")
    pauza = tlacidlo(t.pauzaN,t.pauzaA,1500,50,text="pauznut")
    Xtlacidlo = tlacidlo(t.XN,t.XA,g.moj_width-5,5,roh="pravy_horny")
    myska = s.mys(o.mys)
#    stena = s.stena(o.stena,pygame.Surface((580,580)),5)
    level = s.level(*levelI)
    
    globals().update(locals())
    gameloop()


# if __name__ == "__main__":
#     spustit(0,0,0)

'''
co treba spravit:
otacanie obrazkov - ked zobrazujem, pridat otocenie a suradnice body oatacania     asi netreba
otestovat konvert na .exe - poslat darebakom na otestovanie     #vytazny command: python3 -m PyInstaller --onefile main.py    potom z folderu dist presunut .exe do normalneho, aby videl obrazky.

tlacidlo pauza - funguje, len cas stale bezi
detekcia kolizie(lubovolneho prekryvu) nepriehladnych casti lubovolnych dvoch spritov
aby to fungovalo aj na obrazovkach s inym rozlisenim - asi to bude mat proste konstantne rozlisenie
tlacidlo X aby som to vedel vypnut ked to je na fulscreen

bugy:
maska tlacidla sa neupdatuje ked sa scalne displej asi nemenit pocas scalovanie ale az na konci, tlacidla sa pocas toho asi aj tak nepouziju, mozno chceme disable tlacidla
mys mozem tahat mimo obrazovky doprava a dole

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