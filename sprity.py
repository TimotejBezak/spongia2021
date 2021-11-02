from os import terminal_size
from pygame import surface
from globalnepremenne import g
import pygame
import klavesy
from animacie import obrazky_v_case
from rychlost import rychlost,linearnyPohyb
import mys
import cas
from tlacidla import tlacidlo
from loaderObrazkov import o,t,z,a
import konstanty as k
import math
from funkcie import *

class S:

    class mys:
        def __init__(self,image):
            self.image = image
        def zobraz(self):
            if pygame.mouse.get_focused():
                pygame.zobraz(self.image,mys.pozicia,ui=True)

    class hrac(pygame.sprite.Sprite):#pygame.sprite.Sprite()
        def __init__(self,image):
            # super().__init__()
            self.rychlost = rychlost(100)
            self.image = image
            # self.rect = image.get_rect()
            self.x = 100
            self.y = 100

        def update(self):
            vzdialenost = self.rychlost.vzdialenost()
            if klavesy.je_stlaceny("w"):
                self.y -= vzdialenost
            if klavesy.je_stlaceny("s"):
                self.y += vzdialenost
            if klavesy.je_stlaceny("a"):
                self.x -= vzdialenost
            if klavesy.je_stlaceny("d"):
                self.x += vzdialenost
            # self.rect.center = (self.x,self.y)#akokeby zobraz

        def zobraz(self):
            pygame.zobraz(self.image,(self.x,self.y))

    class trubiroh(pygame.sprite.Sprite):
        def __init__(self,image):
            # super().__init__()
            self.image = image
            # self.rect = image.get_rect()
            self.hybac = linearnyPohyb((100,100),(900,400),100)
            self.x,self.y=0,0
        def update(self):
            self.x,self.y = self.hybac.update()
            if self.hybac.koniec():
                self.hybac = linearnyPohyb((100,100),(900,400),100)
            # self.rect.center = (self.x,self.y)
        def zobraz(self):
            pygame.zobraz(self.image,(self.x,self.y))

    class stena:
        def __init__(self,obrazok,surface,casDokopy):#chcem vyratat rychlost(zrychlenie) podla casDakopy
            self.povodnyObrazok = obrazok
            self.obrazok = obrazok
            self.scale = 0#-obrazok.get_width()
            self.koniecScale = 2500
            self.rychlostScalovania = 580/(casDokopy**3)# pixelov za sekundu
            self.dt = cas.dt()
            self.casZ = cas.cas()
            self.surface = surface

        def pozaStena(self,pozaA,stenaA):#strasne pomale
            """do steny vytransparentuje pozu"""
            poza = pozaA.copy()
            stena = stenaA.copy()
            pw,ph = poza.get_size()
            sw,sh = stena.get_size()
            offset = [int((sw-pw)/2),int((sh-ph)/2)]
            for x in range(pw):
                for y in range(ph):
                    r,g,b,a = poza.get_at((x,y))
                    if a != 0:#ak tam nieje poza transparentna
                        stena.set_at((x+offset[0],y+offset[1]), pygame.Color(0,0,0,0))
                        # a1,a2,a3,a4 = 1,1,1,1
                        # if x < pw:
                        #     a1 = poza.get_at((x+1,y))[3]
                        # if y < ph:
                        #     a2 = poza.get_at((x,y+1))[3]
                        # if x > 0:
                        #     a3 = poza.get_at((x-1,y))[3]
                        # if y > 0:
                        #     a4 = poza.get_at((x,y-1))[3]
                        # if a1==0 or a2==0 or a3==0 or a4==0:#ci je na obvode panaka
                        #     for xk in range(100):
                        #         for yk in range(100):
                        #             ak = o.kruh50.get_at((xk,yk))[3]
                        #             if ak != 0:#ak to je v kruhu
                        #                 stena.set_at((x+offset[0]+xk-50,y+offset[1]+yk-50), pygame.Color(0,0,0,0))

            return stena

        def update(self):
            if self.scale < self.koniecScale:
                self.scale = self.rychlostScalovania * (cas.cas()-self.casZ)**3#self.scale += self.rychlostScalovania*self.dt.update()# * (cas.cas()-self.casZ)**4
            else:#koniec
                return False
                # self.scale = 0
                # self.casZ = cas.cas()
            
            self.obrazok = pygame.transform.scale(self.povodnyObrazok, (int(self.scale),int(self.scale)) )
            
        def zobraz(self):
            pygame.zobraz(self.obrazok,(290,290),roh="stred",surface=self.surface)
            #pygame.zobraz(self.surface,(k.xStenoDispleja,k.yStenoDispleja))


    class levelSet:#menu
        def __init__(self,obrazokPostavy,obrazokPozadia,posT,posP,levelA,levelN,klavesyPoz,cislo):#klavesyPoz = {'a':[0,1,0,2]...}
            self.cislo = cislo#0/1/2
            self.klavesyPoz = klavesyPoz
            self.obrazokPostavy = obrazokPostavy
            self.obrazokPozadia = obrazokPozadia
            medzeraTlacidiel = 50
            velkostTextuTlacidiel = 25
            self.xT, self.yT = posT#pozicia tlacidiel
            self.xP, self.yP = posP#pozicia postavy
            
            odomknute = open("odomknute.txt","r")
            self.odomknutost = list(map(int,odomknute.readlines()[cislo].split()))
            odomknute.close()

            self.odomknute = []#od 0 po 4
            self.zamknute = []
            for i,v in enumerate(self.odomknutost):
                if v == 1:
                    self.odomknute.append(i)
                else:
                    self.zamknute.append(i)

            self.tlacidla = []
            for i in self.odomknute:
                self.tlacidla.append(tlacidlo(levelN,levelA,self.xT+(k.sirkaLevelTlacidla+medzeraTlacidiel)*i,self.yT,text=f"{i+1}",velkost=velkostTextuTlacidiel))
            
            for i in self.zamknute:
                self.tlacidla.append(tlacidlo(o.zamknutyLevel,o.zamknutyLevel,self.xT+(k.sirkaLevelTlacidla+medzeraTlacidiel)*i,self.yT,text=f"{i+1}",velkost=velkostTextuTlacidiel,disabled=True))

            self.levelN = levelN
            self.levelA = levelA
            self.medzeraTlacidiel = medzeraTlacidiel
            # print(self.odomknute,"odoodod")
        
        def spustiLevel(self):#spustame levely ak su tlacidla stlacene
            if self.tlacidla[0].je_keyup():
                return [z.testMuzika,[7],['a','b','b','b','a'],self.klavesyPoz,self.cislo,0]#[0,[8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],0]#input pre level
            return False#[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

        def zobraz(self):
            pygame.zobraz(self.obrazokPozadia, (self.xP-50,self.yP-50))
            pygame.zobraz(self.obrazokPostavy, (self.xP,self.yP))
            
    class klavesnica:
        def __init__(self,klavesyPoz):
            sirka = 120
            posun1 = 40
            posun2 = 80
            self.pozicie = {
                'q':(0,0),'w':(sirka,0),'e':(sirka*2,0),'r':(sirka*3,0),'t':(sirka*4,0),'y':(sirka*5,0),'u':(sirka*6,0),'i':(sirka*7,0),'o':(sirka*8,0),'p':(sirka*9,0),
                'a':(0+posun1,sirka),'s':(sirka+posun1,sirka),'d':(sirka*2+posun1,sirka),'f':(sirka*3+posun1,sirka),'g':(sirka*4+posun1,sirka),'h':(sirka*5+posun1,sirka),'j':(sirka*6+posun1,sirka),'k':(sirka*7+posun1,sirka),'l':(sirka*8+posun1,sirka),
                'z':(posun2,sirka*2),'x':(sirka+posun2,sirka*2),'c':(sirka*2+posun2,sirka*2),'v':(sirka*3+posun2,sirka*2),'b':(sirka*4+posun2,sirka*2),'n':(sirka*5+posun2,sirka*2),'m':(sirka*6+posun2,sirka*2)
            }
            self.klavesyPoz = klavesyPoz
            self.klavesObrazokPozy = {}
            self.vytvorPozy()

        def vytvorPozy(self):
            sirka = 110
            for pismeno in self.klavesyPoz:
                print(f"pismeno: {pismeno}, pozicia koncatin: {self.klavesyPoz[pismeno]}")
                obrazok = poziciaZKoncatin(self.klavesyPoz[pismeno])
                scale = min(sirka/obrazok.get_width(),sirka/obrazok.get_height())
                self.klavesObrazokPozy[pismeno] = pygame.transform.scale(obrazok,(int(obrazok.get_width()*scale),int(obrazok.get_height()*scale)))

        def zobraz(self):
            for pismeno in self.pozicie:
                pygame.zobraz(o.pozadieKlavesu,self.pozicie[pismeno])

            for pismeno in self.klavesObrazokPozy:
                pygame.zobraz( self.klavesObrazokPozy[pismeno] , self.pozicie[pismeno] )

    class panak:
        def __init__(self):
            self.pozicia = [0,0,1,2]#lr,pr,ln,pn
            self.test = poziciaZKoncatin(self.pozicia)

        def zobraz(self):
            pygame.zobraz(self.test,(k.xStenoDispleja,k.yStenoDispleja),roh='stred')

    class level:
        def __init__(self,muzika,casyStien,pismenaStien,klavesyPoz,cisloSetu,cisloLevelu):#na spusteni levelu
            self.muzika = muzika
            self.casyStien = casyStien #casStenyPredNaburanimDoVajca je konstantny
            self.casyStien.append(1000000)
            self.pismenaStien = pismenaStien#pismena, ktore treba stlacit
            self.klavesyPoz = klavesyPoz#klavesyPoz = {'a':[0,1,0,2]...}
            self.indexCasu = 0
            self.klavesnica = s.klavesnica(self.klavesyPoz)
            self.casZ = cas.cas()
            self.steny = []
            self.casSteny = 5#kym stena nabura do vajca
            self.cisloSetu = cisloSetu
            self.cisloLevelu = cisloLevelu
            self.surface = pygame.Surface((580,580))
            self.panak = s.panak()
            self.stihol = False
            self.muzika.play()

        def update(self):#scalovanie steny, detekovanie inputu
            if (cas.cas()-self.casZ)+self.casSteny > self.casyStien[self.indexCasu]:
                print(f"nadisiel cas na stenu {self.indexCasu}")
                self.steny.append(s.stena(o.stena, poziciaZKoncatin(self.klavesyPoz[self.pismenaStien[self.indexCasu]]) ,self.casSteny))#self.obrazkyStien[self.indexSteny]
                self.indexCasu += 1

                if not self.stihol:
                    pass#self.muzika.stop()
                    #prehral som
                self.stihol = False
            
            for i,stena in enumerate(self.steny):
                if stena.update() == False:
                    del self.steny[i]
            
            if len(self.steny) == 0 and self.indexCasu == len(self.casyStien)-1:
                self.updateOdomknute()
                self.muzika.stop()
                return False#updatnut odomknute


            # if klavesy.je_keydown(self.pismenaStien[self.indexCasu]):#list index out of range
            #     self.stihol = True

        def updateOdomknute(self):#ked som vyhral       treba este povedat menu, ze ktore levely sa odomkli, aby sa mohla zobrazit animacia
            odomknute = open("odomknute.txt","r")
            odomknutost = [
                list(map(int,odomknute.readline().split())),
                list(map(int,odomknute.readline().split())),
                list(map(int,odomknute.readline().split()))
            ]
            odomknute.close()
            print(odomknutost)
            subor = open('odomknute.txt','w')
            subor.truncate()#snad zmaze veci v nom
            if self.cisloLevelu < 5:
                odomknutost[self.cisloSetu][self.cisloLevelu+1] = 1
            if self.cisloLevelu == 2 and self.cisloSetu < 2:
                odomknutost[self.cisloSetu+1][0] = 1
            for i in range(3):
                subor.write(' '.join(list(map(str,odomknutost[i])))+'\n')
            subor.close()

        def zobraz(self):#reference klavesnica poz nad vajcom
            self.klavesnica.zobraz()
            pygame.zobraz(o.jama , (0,0),surface=self.surface)
            for i in range(len(self.steny)):#iterovat od konca
                self.steny[len(self.steny)-1-i].zobraz()
            pygame.zobraz(self.surface,(k.xStenoDispleja,k.yStenoDispleja),roh='stred')
            self.panak.zobraz()

def init():
    global s
    s = S()