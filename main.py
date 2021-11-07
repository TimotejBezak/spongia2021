import pygame, math, random, threading,time

from pygame.constants import FULLSCREEN, RESIZABLE
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
from loaderObrazkov import o,t,a,z,loadniZnovu

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
import konstanty as k


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
levely2 = None
levely3 = None
restart = None
hrat = None
animaciaZacLevel = None
inputPreLevel = None
fullscreen = False
# toggleFullscreen = None
nazovHry = None

# z.testMuzika.play()
# z.testMuzika.set_volume(0.3)
def fyzika():
    global g,pauza,odpauza,koniec,stena,level,levely1,loop,vyhrat,prehrat,spetDoMenu,fullscreen
    # while not koniec and not klavesy.je_koniec():
    mys.update()
    klavesy.update()
    tlacidla.update()
    animacie.update()
    ratacfpsF.update()
    if Xtlacidlo.je_keyup():
        koniec = True

    # if toggleFullscreen.je_keyup():
    #     fullscreen = not fullscreen
    #     if fullscreen:
    #         # print(g.sirkaPocitaca,g.moj_width,"sem pozeraaaaaaaaaj")
    #         scaleSirka = g.sirkaPocitaca/g.moj_width
    #         scaleVyska = g.vyskaPocitaca/g.moj_height
    #         g.scaleObrazovky = min(scaleSirka,scaleVyska)#ratam s tym, ze moja obrazovka je najmensia
    #         g.displej_width = int(g.moj_width*g.scaleObrazovky)
    #         g.displej_height = int(g.moj_height*g.scaleObrazovky)
    #         g.Displej = pygame.display.set_mode((g.displej_width, g.displej_height),FULLSCREEN)
    #     else:
    #         g.Displej = pygame.display.set_mode((g.moj_width, g.moj_height))
    #         g.scaleObrazovky = 1
    #     loadniZnovu()#znovu loadne obrazky

    if loop=='main':
        # if klavesy.je_keyup('v'):
        #     z.test.play()
        #     animacia(a.animacia,0.7,500,20,loop=False)

        odpoved = level.update()
        if odpoved == True:
            spustitVyhralsi()
            return#continue
        if odpoved == False:
            spustitPrehralsi()
            return

        #time.sleep(0.1)
        
    if loop=='zaclevel':
        if animaciaZacLevel.skoncil_som() == True:
            spustitMain(inputPreLevel)
            return

    if loop=='pauza':
        if odpauza.je_keyup():
            cas.unpause()
            odpauza.zmazSa()
            pauza = tlacidlo(t.pauzaN,t.pauzaA,1500,50,text="pauznut")
            vyhrat = tlacidlo(t.vyhralsiN,t.vyhralsiA,1300,500,text="vyhrat")
            prehrat = tlacidlo(t.prehralsiN,t.prehralsiA,1410,500,text="prehrat")
            spetDoMenu = tlacidlo(t.spetDoMenuN,t.spetDoMenuA,1520,500,text="menu")
            loop = 'main'
            return
            #spustitMain()
    
    if loop=='menu':
        lvl = levely1.spustiLevel()
        if lvl != False:
            # koniec = True
            spustitZacLevel(lvl)
            return
        lvl = levely2.spustiLevel()
        if lvl != False:
            # koniec = True
            spustitZacLevel(lvl)
            return
        lvl = levely3.spustiLevel()
        if lvl != False:
            # koniec = True
            spustitZacLevel(lvl)
            return
            
    if loop=='vyhralsi':
        if restart.je_keyup():
            # koniec = True
            z.vyhralsi.stop()
            spustitMenu()
            return

    if loop=='prehralsi':
        if restart.je_keyup():
            # koniec = True
            z.prehralsi.stop()
            spustitMenu()
            return
        
    if loop=='intro':
            if hrat.je_keyup():
                spustitMenu()
                return

def zobrazovac():
    global g
    # while not koniec and not klavesy.je_koniec():
    if loop=='main':
        g.Displej.fill((0,0,0))
        level.zobraz()
    if loop=='pauza':
        # g.Displej.fill((g.farby.modra)) #nejaky iny overlay mozno
        odpauza.zobraz()
    if loop=='menu':
        g.Displej.fill((0,0,0))
        pygame.zobraz(o.oblakypozadie,(0,0))
        levely1.zobraz()
        levely2.zobraz()
        levely3.zobraz()
    if loop=='vyhralsi':
        g.Displej.fill((0,0,0))
        pygame.zobraz(o.vyhra,(0,0))
    if loop=='prehralsi':
        g.Displej.fill((0,0,0))
        pygame.zobraz(o.prehra,(0,0))
    if loop=='intro':
        g.Displej.fill((0,0,0))
        pygame.zobraz(o.oblakypozadie,(0,0))
        nazovHry.zobraz()
    if loop=='zaclevel':
        g.Displej.fill((0,0,0))

    tlacidla.zobraz()
    animacie.zobraz()
    ratacfpsF.zobraz()
    ratacfpsZ.zobraz()

    myska.zobraz()
    pygame.display.update()
    ratacfpsZ.update()

def gameloop():
    # thread = myThread(fyzika)
    # thread.start()
    # zobrazovac()
    while not koniec and not klavesy.je_koniec():
        fyzika()
        zobrazovac()


def spustitMain(levelI):
    #global vyhrat,prehrat,testHrac,trubiroh,myska,pauza
    resetScreen()
    Xtlacidlo = tlacidlo(t.XN,t.XA,g.moj_width-5,5,roh="pravy_horny")
    myska = s.mys(o.mys)
    level = s.level(*levelI)
    loop = 'main'
    globals().update(locals())

def spustitZacLevel(lvl):
    resetScreen()
    Xtlacidlo = tlacidlo(t.XN,t.XA,g.moj_width-5,5,roh="pravy_horny")
    myska = s.mys(o.mys)
    animaciaZacLevel = animacia(a.zaciatokLevelu,1.5,0,0)
    inputPreLevel = lvl
    z.dopozadia.stop()
    z.pustivajco.play()
    loop = 'zaclevel'
    globals().update(locals())

def spustitMenu():
    global loop
    resetScreen()
    myska = s.mys(o.mys)
    Xtlacidlo = tlacidlo(t.XN,t.XA,g.moj_width-5,5,roh="pravy_horny")
    levely1 = s.levelSet(o.level1Panak,o.level1Pozadie,(400,100),(100,100),k.ls1k,0)
    levely2 = s.levelSet(o.level2Panak,o.level2Pozadie,(400,400),(100,400),k.ls2k,1)
    levely3 = s.levelSet(o.level3Panak,o.level3Pozadie,(400,700),(100,700),k.ls3k,2)
    if loop != 'intro':
        z.dopozadia.set_volume(0.1)
        z.dopozadia.play(-1)
    loop = 'menu'
    globals().update(locals())

def spustitVyhralsi():
    resetScreen()
    z.vyhralsi.play()
    Xtlacidlo = tlacidlo(t.XN,t.XA,g.moj_width-5,5,roh="pravy_horny")
    restart = tlacidlo(t.restartVyhralsiN,t.restartVyhralsiA,250,500,text="continue",velkost=70)
    loop = 'vyhralsi'
    globals().update(locals())

def spustitPrehralsi():
    resetScreen()
    z.prehralsi.play()
    Xtlacidlo = tlacidlo(t.XN,t.XA,g.moj_width-5,5,roh="pravy_horny")
    restart = tlacidlo(t.restartPrehralsiN,t.restartPrehralsiA,1100,500,text="continue",velkost=70)
    loop = 'prehralsi'
    globals().update(locals())

def spustitPauza():
    resetScreen()
    cas.pause()
    
    odpauza = tlacidlo(t.odpauzaN,t.odpauzaA,700,50,text="odpauznut")
    loop = 'pauza'
    globals().update(locals())

def spustitIntro():#spusti sa naozaj len na zaciatku
    #resetScreen()
    myska = s.mys(o.mys)
    nazovHry = text.text(g.moj_width/2,250,"lačný Rytmus",150,(0,0,0),g.hruby_pixel_font,roh="stred")
    hrat = tlacidlo(t.hratN,t.hratA,g.moj_width/2,700,text="play",velkost=70,roh="stred")
    Xtlacidlo = tlacidlo(t.XN,t.XA,g.moj_width-5,5,roh="pravy_horny")
    # toggleFullscreen = tlacidlo(t.fullscreenN,t.fullscreenA,g.moj_width-40,5,roh="pravy_horny")
    z.dopozadia.set_volume(0.1)
    z.dopozadia.play(-1)
    loop = 'intro'
    globals().update(locals())

def resetScreen():# toto by chcelo byt rovnake vo vsetkych screenoch
    global g
    pygame.event.clear()
    g.koniec = False
    # g.Displej = pygame.display.set_mode((g.displej_width, g.displej_height),FULLSCREEN)
    tlacidla.tlacidla = []
    animacie.animacie = []
    #g.Displej = pygame.display.set_mode((g.displej_width, g.displej_height))
    # toggleFullscreen = tlacidlo(t.fullscreenN,t.fullscreenA,g.moj_width-40,5,roh="pravy_horny")
    g.frameF = 0
    g.frameZ = 0
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