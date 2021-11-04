from os import terminal_size
from pygame import surface
from globalnepremenne import g
import pygame
import klavesy
from animacie import animacia, obrazky_v_case
from rychlost import rychlost,linearnyPohyb
import mys
import cas
from text import text
from tlacidla import tlacidlo
from loaderObrazkov import o,t,z,a
import konstanty as k
import math
from funkcie import *
import time

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
            self.rychlostScalovania = 580/(casDokopy**5)# pixelov za sekundu

            zacScale = 20
            self.zacCas = (zacScale/self.rychlostScalovania)**(1/5)
            print("zacCas",self.zacCas)
            self.rychlostScalovania = 580/((casDokopy+self.zacCas)**5)
            
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
                self.scale = self.rychlostScalovania * (self.zacCas+cas.cas()-self.casZ)**5#self.scale += self.rychlostScalovania*self.dt.update()# * (cas.cas()-self.casZ)**4
            else:#koniec
                return False
            
                # self.scale = 0
                # self.casZ = cas.cas()
            
            self.obrazok = pygame.transform.scale(self.povodnyObrazok, (int(self.scale),int(self.scale)) )
            if self.scale > 580:
                self.rychlostScalovania *= 1.04
                # print("stena prechadza, trvalo",cas.cas()-self.casZ)
                return 'presla'
        def zobraz(self):
            pygame.zobraz(self.obrazok,(290,290),roh="stred",surface=self.surface)
            #pygame.zobraz(self.surface,(k.xStenoDispleja,k.yStenoDispleja))

    class levelSet:#menu
        def __init__(self,obrazokPostavy,obrazokPozadia,posT,posP,klavesyPoz,cislo):#klavesyPoz = {'a':[0,1,0,2]...}
            self.cislo = cislo#0/1/2
            self.klavesyPoz = klavesyPoz
            self.obrazokPostavy = obrazokPostavy
            self.obrazokPozadia = obrazokPozadia
            medzeraTlacidiel = 50
            velkostTextuTlacidiel = 60
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
                self.tlacidla.append(tlacidlo(t.levelyN[i+cislo*5],t.levelyA[i+cislo*5],self.xT+(k.sirkaLevelTlacidla+medzeraTlacidiel)*i,self.yT,text=f"{i+cislo*5+1}",velkost=velkostTextuTlacidiel,textOffset=[0,7]))
            
            for i in self.zamknute:
                self.tlacidla.append(tlacidlo(t.levelyN[i+cislo*5],t.levelyN[i+cislo*5],self.xT+(k.sirkaLevelTlacidla+medzeraTlacidiel)*i,self.yT,text=f"{i+cislo*5+1}",velkost=velkostTextuTlacidiel,disabled=True,textOffset=[0,7]))
                self.tlacidla.append(tlacidlo(o.zamok,o.zamok,self.xT+(k.sirkaLevelTlacidla+medzeraTlacidiel)*i,self.yT,text=f"",velkost=velkostTextuTlacidiel,disabled=True))

            for i in g.unlocknuteLevely:
                s,l = i#set,level
                animacia(a.zamok,2,self.xT+(k.sirkaLevelTlacidla+medzeraTlacidiel)*l,self.yT)

            # self.levelN = levelN
            # self.levelA = levelA
            self.medzeraTlacidiel = medzeraTlacidiel
            # print(self.odomknute,"odoodod")
        
        def spustiLevel(self):#cisla levelov su [0,4]
            if self.cislo == 0:
                if self.tlacidla[0].je_keyup():
                    casy = [1.5, 3.5, 5.5, 8.0, 10.5, 13.0, 15.0, 18.0, 22.0, 25.0, 27.0, 29.5, 32.0, 34.5, 36.5, 38.5, 41.5, 43.5, 47.0, 49.5, 52.0, 54.0, 56.0, 58.0, 60.5, 62.5, 64.5, 67.0, 69.5, 71.5, 73.0, 75.0, 78.0, 80.0, 82.5, 85.0, 87.5, 90.0, 94.0, 96.0, 98.0, 100.0, 103.0, 105.0, 107.5, 110.0, 112.0, 114.0, 116.5, 118.5, 121.0, 125.0, 127.0, 129.0, 134.5, 137.0, 139.0, 141.5, 144.0, 146.0, 147.5, 149.0, 150.5, 152.0, 153.5, 155.0, 157.0, 159.0, 161.0, 163.0, 165.0, 166.5]
                    pismena = ['x', 'x', 'l', 'l', 'x', 'x', 'x', 'l', 'l', 'x', 'x', 'x', 'l', 'l', 'x', 'l', 'x', 'l', 'x', 'x', 'x', 'l', 'l', 'l', 'x', 'x', 'l', 'l', 'x', 'x', 'x', 'x', 'l', 'l', 'l', 'x', 'x', 'l', 'x', 'x', 'x', 'x', 'l', 'l', 'l', 'l', 'l', 'x', 'l', 'x', 'l', 'x', 'x', 'x', 'l', 'l', 'l', 'l', 'x', 'x', 'l', 'l', 'x', 'l', 'x', 'l', 'x', 'x', 'l', 'l', 'l', 'x']
                    return [casy,pismena,self.klavesyPoz,1.5,self.cislo,0]#[0,[8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],0]#input pre level
                if self.tlacidla[1].je_keyup():
                    casy = [1.0, 2.5, 4.5, 6.0, 7.5, 9.5, 12.0, 13.5, 16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 27.5, 29.5, 31.0, 33.0, 35.0, 37.0, 39.0, 41.0, 43.0, 45.0, 47.0, 48.5, 50.0, 51.5, 53.0, 55.0, 57.0, 59.0, 61.0, 63.0, 65.0, 67.0, 69.0, 71.0, 73.0, 75.0, 77.0, 79.0, 80.5, 82.0, 83.5, 85.0, 88.0, 89.3, 90.6, 91.9, 96.0, 97.3, 98.6, 99.9, 102.0, 104.0, 106.0, 108.0, 110.0, 112.0, 114.0, 116.0, 118.0, 120.0, 122.0, 124.0, 126.0, 128.0, 130.0, 132.0, 134.0, 136.0, 137.3, 138.6, 139.9, 141.2, 142.5, 143.8, 145.1, 146.4, 147.7, 150.0, 152.0, 154.0, 156.0, 158.0, 160.0, 162.0, 164.0, 165.3]
                    pismena = ['x', 'l', 'g', 'x', 'g', 'l', 'l', 'g', 'x', 'g', 'l', 'x', 'x', 'x', 'l', 'l', 'g', 'g', 'l', 'l', 'g', 'g', 'x', 'x', 'l', 'l', 'l', 'x', 'x', 'x', 'g', 'g', 'g', 'x', 'l', 'g', 'x', 'l', 'g', 'x', 'l', 'g', 'x', 'x', 'x', 'x', 'g', 'g', 'g', 'g', 'l', 'l', 'l', 'l', 'g', 'l', 'x', 'l', 'g', 'x', 'x', 'l', 'g', 'x', 'g', 'l', 'g', 'l', 'x', 'g', 'x', 'l', 'g', 'g', 'x', 'l', 'l', 'g', 'x', 'x', 'l', 'x', 'x', 'l', 'l', 'g', 'g', 'g', 'x', 'l']
                    return[casy,pismena,self.klavesyPoz,1.3,self.cislo,1]
                if self.tlacidla[2].je_keyup():
                    casy = []
                    pismena = []
                    return[casy,pismena,self.klavesyPoz,2.5,self.cislo,2]
                if self.tlacidla[3].je_keyup():
                    casy = []
                    pismena = []
                    return[casy,pismena,self.klavesyPoz,2.5,self.cislo,3]
                if self.tlacidla[4].je_keyup():
                    casy = []
                    pismena = []
                    return[casy,pismena,self.klavesyPoz,2.5,self.cislo,4]

            return False#[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],['x','l','g','y','x']

        def zobraz(self):
            pygame.zobraz(self.obrazokPozadia, (self.xP-50,self.yP-50))
            pygame.zobraz(self.obrazokPostavy, (self.xP,self.yP))

    class klavesnica:
        def __init__(self,klavesyPoz):
            sirka = 110#aj vyska
            self.sirka = 110
            medzera = 10#medzi klavesmi
            offset = [20,10]
            posun1 = 40
            posun2 = 80
            self.pozicie = {
                'q':(0+offset[0],0+offset[1]),'w':(sirka+medzera+offset[0],0+offset[1]),'e':(sirka*2+medzera*2+offset[0],0+offset[1]),'r':(sirka*3+medzera*3+offset[0],0+offset[1]),'t':(sirka*4+medzera*4+offset[0],0+offset[1]),'y':(sirka*5+medzera*5+offset[0],0+offset[1]),'u':(sirka*6+medzera*6+offset[0],0+offset[1]),'i':(sirka*7+medzera*7+offset[0],0+offset[1]),'o':(sirka*8+medzera*8+offset[0],0+offset[1]),'p':(sirka*9+medzera*9+offset[0],0+offset[1]),
                'a':(0+posun1+offset[0],sirka+medzera+offset[1]),'s':(sirka+posun1+medzera+offset[0],sirka+medzera+offset[1]),'d':(sirka*2+posun1+medzera*2+offset[0],sirka+medzera+offset[1]),'f':(sirka*3+posun1+medzera*3+offset[0],sirka+medzera+offset[1]),'g':(sirka*4+posun1+medzera*4+offset[0],sirka+medzera+offset[1]),'h':(sirka*5+posun1+medzera*5+offset[0],sirka+medzera+offset[1]),'j':(sirka*6+posun1+medzera*6+offset[0],sirka+medzera+offset[1]),'k':(sirka*7+posun1+medzera*7+offset[0],sirka+medzera+offset[1]),'l':(sirka*8+posun1+medzera*8+offset[0],sirka+medzera+offset[1]),
                'z':(posun2+offset[0],sirka*2+medzera*2+offset[1]),'x':(sirka+posun2+medzera+offset[0],sirka*2+medzera*2+offset[1]),'c':(sirka*2+posun2+medzera*2+offset[0],sirka*2+medzera*2+offset[1]),'v':(sirka*3+posun2+medzera*3+offset[0],sirka*2+medzera*2+offset[1]),'b':(sirka*4+posun2+medzera*4+offset[0],sirka*2+medzera*2+offset[1]),'n':(sirka*5+posun2+medzera*5+offset[0],sirka*2+medzera*2+offset[1]),'m':(sirka*6+posun2+medzera*6+offset[0],sirka*2+medzera*2+offset[1])
            }
            self.texty = []
            for pismeno in self.pozicie:
                pozicia = [self.pozicie[pismeno][0]+sirka/2 , self.pozicie[pismeno][1]+sirka/2-10]
                self.texty.append(text(pozicia[0],pozicia[1],pismeno,32,(0,0,0),g.basic_hruby_font,roh='stred'))

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
                pygame.zobraz( self.klavesObrazokPozy[pismeno] , (self.pozicie[pismeno][0]+self.sirka/2,self.pozicie[pismeno][1]+self.sirka/2) ,roh='stred')

            for i in self.texty:
                i.zobraz()

    class panak:
        def __init__(self,klavesyPoz):
            self.pozicia = [2,2,2,2]#lr,pr,ln,pn
            self.surface = poziciaZKoncatin(self.pozicia)
            self.klavesyPoz = klavesyPoz
            self.beziAnimacia = False
            self.animacia = None
            self.casAnimacie = 0.1

        def animacia_obrazky(self,koncatina,koncatina2,p1,p2):#koncatina lr,pr...
            obrazky = []
            kn = koncatina
            kn2 = koncatina2
            if p1 == 0:
                if p2 == 0:
                    obrazky = [eval(f"o.{kn2}[0]")]
                if p2 == 1:
                    obrazky = eval(f"a.{kn}01.copy()")
                if p2 == 2:
                    obrazky = eval(f"a.{kn}02.copy()")
            if p1 == 1:
                if p2 == 0:
                    obrazky = eval(f"a.{kn}01.copy()")
                    obrazky.reverse()
                if p2 == 1:
                    obrazky = [eval(f"o.{kn2}[1]")]
                if p2 == 2:
                    obrazky = eval(f"a.{kn}12.copy()")
            if p1 == 2:
                if p2 == 0:
                    obrazky = eval(f"a.{kn}02.copy()")
                    print(obrazky)
                    obrazky.reverse()
                if p2 == 1:
                    obrazky = eval(f"a.{kn}12.copy()")
                    obrazky.reverse()
                if p2 == 2:
                    obrazky = [eval(f"o.{kn2}[2]")]

            if len(obrazky) != 1:
                del obrazky[0]

            return obrazky

        def update(self):
            #print(klavesy.naposledy_pismeno())
            if len(klavesy.keydown_klavesi) > 0:
                pismeno = klavesy.keydown_klavesi[0]
                if pismeno in self.klavesyPoz:
                    p1 = self.pozicia
                    p2 = self.klavesyPoz[pismeno]
                    
                    self.alr = obrazky_v_case(self.animacia_obrazky('lr','lavaRuka',p1[0],p2[0]),self.casAnimacie)
                    self.apr = obrazky_v_case(self.animacia_obrazky('pr','pravaRuka',p1[1],p2[1]),self.casAnimacie)
                    self.aln = obrazky_v_case(self.animacia_obrazky('ln','lavaNoha',p1[2],p2[2]),self.casAnimacie)
                    self.apn = obrazky_v_case(self.animacia_obrazky('pn','pravaNoha',p1[3],p2[3]),self.casAnimacie)
                    self.beziAnimacia = True

                    self.pozicia = self.klavesyPoz[pismeno]
                    # self.surface = poziciaZKoncatin(self.pozicia)
            if self.beziAnimacia == True:
                if self.alr.skoncil_som():
                    self.beziAnimacia = False
                    self.surface = poziciaZKoncatin(self.pozicia)

        def zobraz(self):
            if self.beziAnimacia:
                self.surface = o.vajce.copy()
                pygame.zobraz(self.alr.aktualnyObrazok(),(0,0),surface=self.surface)
                pygame.zobraz(self.apr.aktualnyObrazok(),(0,0),surface=self.surface)
                pygame.zobraz(self.aln.aktualnyObrazok(),(0,0),surface=self.surface)
                pygame.zobraz(self.apn.aktualnyObrazok(),(0,0),surface=self.surface)
            pygame.zobraz(self.surface,(k.xStenoDispleja,k.yStenoDispleja),roh='stred')

    class level:
        def __init__(self,casyStien,pismenaStien,klavesyPoz,casSteny,cisloSetu,cisloLevelu):#na spusteni levelu
            self.casyStien = casyStien #casStenyPredNaburanimDoVajca je konstantny
            self.casyStien.append(1000000)
            self.pismenaStien = pismenaStien#pismena, ktore treba stlacit
            self.klavesyPoz = klavesyPoz#klavesyPoz = {'a':[0,1,0,2]...}
            self.indexCasu = 0
            self.indexKlavesov = 0
            self.klavesnica = s.klavesnica(self.klavesyPoz)
            self.casZ = cas.cas()
            self.steny = []
            self.casSteny = casSteny#kym stena nabura do vajca
            self.cisloSetu = cisloSetu#[0,2]
            self.cisloLevelu = cisloLevelu#[0,4]
            self.surface = pygame.Surface((580,580))
            self.panak = s.panak(klavesyPoz)
            self.muzika = z.muzikyLevelov[self.cisloSetu][self.cisloLevelu]#muzika
            self.muzika.play()
            self.minulePresla = None
            self.casNaburania = None
            self.freeznutyScreen = None
            g.unlocknuteLevely = []
            klavesy.naposledyPismeno = ''

        def update(self):#scalovanie steny, detekovanie inputu
            self.panak.update()

            if (cas.cas()-self.casZ)+self.casSteny > self.casyStien[self.indexCasu]:
                print(f"nadisiel cas na stenu {self.indexCasu}")
                
                print("grg",tuple(self.klavesyPoz[self.pismenaStien[self.indexCasu]]))
                self.steny.append(s.stena(o.steny[self.cisloSetu][tuple(self.klavesyPoz[self.pismenaStien[self.indexCasu]])], self.surface ,self.casSteny))#self.obrazkyStien[self.indexSteny]
                self.indexCasu += 1
            
            for i,stena in enumerate(self.steny):
                supdate = stena.update()
                if supdate == False:
                    del self.steny[i]
                
                if supdate == 'presla' and stena != self.minulePresla:
                    Npismeno = klavesy.naposledy_pismeno()
                    print("Npismeno",Npismeno,"malo byt",self.pismenaStien[self.indexKlavesov])
                    if Npismeno != self.pismenaStien[self.indexKlavesov]:
                        self.muzika.stop()
                        self.casNaburania = time.time()
                        self.freeznutyScreen = g.Displej.copy()
                        #cas.pause()
                        #return 'f'
                        #return False#nabural som

                    self.indexKlavesov += 1
                    self.minulePresla = stena

            if self.casNaburania != None:
                if time.time()-self.casNaburania > 0.6:
                    return False
            
            if len(self.steny) == 0 and self.indexCasu == len(self.casyStien)-1:
                self.updateOdomknute()
                self.muzika.stop()
                return True#updatnut odomknute

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
                if odomknutost[self.cisloSetu][self.cisloLevelu+1] == 0:
                    odomknutost[self.cisloSetu][self.cisloLevelu+1] = 1
                    g.unlocknuteLevely.append([self.cisloSetu,self.cisloLevelu+1])
            if self.cisloLevelu == 2 and self.cisloSetu < 2:
                if odomknutost[self.cisloSetu+1][0] == 0:
                    odomknutost[self.cisloSetu+1][0] = 1
                    g.unlocknuteLevely.append([self.cisloSetu+1,0])
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

            if self.freeznutyScreen != None:
                pygame.zobraz(self.freeznutyScreen,(0,0))

def init():
    global s
    s = S()