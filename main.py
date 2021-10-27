import pygame, math, random, threading,time

#from pygame.mask import _Offset

pygame.init()
pygame.mixer.init()
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
#import vyhralsi,prehralsi,menu
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
pauza = None
odpauza = None
Xtlacidlo = None
testText = None
koniec = False
stena = None
level = None
loop = 'intro'
levely1 = None
restart = None
hrat = None

z.testMuzika.play()
z.testMuzika.set_volume(0.3)
def fyzika():
    global g,pauza,odpauza,koniec,stena,level,levely1,loop,vyhrat,prehrat,spetDoMenu
    while not koniec and not klavesy.je_koniec():
        mys.update()
        klavesy.update()
        tlacidla.update()
        animacie.update()
        ratacfpsF.update()

        if loop=='main':
            if klavesy.je_keyup('v'):
                z.test.play()
                animacia(a.animacia,0.7,500,20,loop=False)

            if level.update() == False:
                spustitVyhralsi()
                continue

            if vyhrat.je_keyup():
                spustitVyhralsi()
                continue

            if prehrat.je_keyup():
                spustitPrehralsi()
                continue

            if spetDoMenu.je_keyup():
                spustitMenu()
                continue

            if pauza.je_keyup():
                print("spustam pauzu")
                spustitPauza()
                continue

            if Xtlacidlo.je_keyup():
                koniec = True
                
            #time.sleep(0.1)
            
        if loop=='pauza':
            if odpauza.je_keyup():
                cas.unpause()
                odpauza.zmazSa()
                pauza = tlacidlo(t.pauzaN,t.pauzaA,1500,50,text="pauznut")
                vyhrat = tlacidlo(t.vyhralsiN,t.vyhralsiA,1300,500,text="vyhrat")
                prehrat = tlacidlo(t.prehralsiN,t.prehralsiA,1410,500,text="prehrat")
                spetDoMenu = tlacidlo(t.spetDoMenuN,t.spetDoMenuA,1520,500,text="menu")
                loop = 'main'
                continue
                #spustitMain()
        
        if loop=='menu':
            lvl = levely1.spustiLevel()
            if lvl != False:
                # koniec = True
                spustitMain(lvl)
                continue
                
        if loop=='vyhralsi':
            if restart.je_keyup():
                # koniec = True
                spustitMenu()
                continue

        if loop=='prehralsi':
            if restart.je_keyup():
                # koniec = True
                spustitMenu()
                continue
            
        if loop=='intro':
            if hrat.je_keyup():
                spustitMenu()
                continue

def zobrazovac():
    global g
    while not koniec and not klavesy.je_koniec():
        if loop=='main':
            g.Displej.fill(g.farby.modra)
            level.zobraz()
        if loop=='pauza':
            g.Displej.fill((g.farby.modra)) #nejaky iny overlay mozno
            odpauza.zobraz()
        if loop=='menu':
            g.Displej.fill(g.farby.modra)
            levely1.zobraz()
        if loop=='vyhralsi':
            g.Displej.fill(g.farby.zelena)
        if loop=='prehralsi':
            g.Displej.fill(g.farby.cervena)
        if loop=='intro':
            g.Displej.fill(g.farby.cervena)

        tlacidla.zobraz()
        animacie.zobraz()
        ratacfpsF.zobraz()
        ratacfpsZ.zobraz()    

        myska.zobraz()
        pygame.display.update()
        ratacfpsZ.update()

def gameloop():
    thread = myThread(fyzika)
    thread.start()
    zobrazovac()

def spustitMain(levelI):
    #global vyhrat,prehrat,testHrac,trubiroh,myska,pauza
    resetScreen()
    vyhrat = tlacidlo(t.vyhralsiN,t.vyhralsiA,1300,500,text="vyhrat")
    prehrat = tlacidlo(t.prehralsiN,t.prehralsiA,1410,500,text="prehrat")
    spetDoMenu = tlacidlo(t.spetDoMenuN,t.spetDoMenuA,1520,500,text="menu")
    pauza = tlacidlo(t.pauzaN,t.pauzaA,1500,50,text="pauznut")
    Xtlacidlo = tlacidlo(t.XN,t.XA,g.moj_width-5,5,roh="pravy_horny")
    myska = s.mys(o.mys)
    level = s.level(*levelI)
    loop = 'main'
    globals().update(locals())

def spustitMenu():
    resetScreen()
    myska = s.mys(o.mys)
    levely1 = s.levelSet(o.level1Panak,o.level1Pozadie,(400,100),(100,100),t.levelA,t.levelN,{'a':[0,0,0,2],'b':[1,2,2,0]})
    loop = 'menu'
    globals().update(locals())

def spustitVyhralsi():
    resetScreen()
    restart = tlacidlo(t.testtlacidloN,t.testtlacidloA,500,500,text="restart")
    loop = 'vyhralsi'
    globals().update(locals())

def spustitPrehralsi():
    resetScreen()
    restart = tlacidlo(t.testtlacidloN,t.testtlacidloA,500,500,text="restart")
    loop = 'prehralsi'
    globals().update(locals())

def spustitPauza():
    resetScreen()
    cas.pause()
    odpauza = tlacidlo(t.odpauzaN,t.odpauzaA,700,50,text="odpauznut")
    loop = 'pauza'
    globals().update(locals())

def spustitIntro():#spusti sa naozaj len na zaciatku
    # resetScreen()
    myska = s.mys(o.mys)
    hrat = tlacidlo(t.testtlacidloN,t.testtlacidloA,500,500,text="hrat")
    loop = 'intro'
    globals().update(locals())

if __name__ == "__main__":
    spustitIntro()
    gameloop()
    print("quitujem")
    pygame.display.quit()
    pygame.quit()


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