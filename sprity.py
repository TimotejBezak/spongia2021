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
import random

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
        def __init__(self,obrazok,surface,casDokopy,panvica=False):#chcem vyratat rychlost(zrychlenie) podla casDakopy
            self.panvica = panvica
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
            
            self.obrazok = pygame.transform.scale(self.povodnyObrazok, (int(self.scale*(self.povodnyObrazok.get_width()/self.povodnyObrazok.get_height())),int(self.scale)) )
            if self.scale > 580:
                self.rychlostScalovania *= 1.04
                # print("stena prechadza, trvalo",cas.cas()-self.casZ)
                return 'presla'
        def zobraz(self):
            if not self.panvica:
                pygame.zobraz(self.obrazok,(290,290),roh="stred",surface=self.surface)
            else:
                pygame.zobraz(self.obrazok,(290+(self.obrazok.get_width()-self.obrazok.get_height())/2,290),roh="stred",surface=self.surface)
            # pygame.zobraz(self.surface,(k.xStenoDispleja,k.yStenoDispleja))

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
                self.tlacidla.append(tlacidlo(t.levelyN[i+cislo*5],t.levelyA[i+cislo*5],self.xT+(k.sirkaLevelTlacidla+medzeraTlacidiel)*i,self.yT+25,text=f"{i+cislo*5+1}",velkost=velkostTextuTlacidiel,textOffset=[0,7]))
            
            for i in self.zamknute:
                self.tlacidla.append(tlacidlo(t.levelyN[i+cislo*5],t.levelyN[i+cislo*5],self.xT+(k.sirkaLevelTlacidla+medzeraTlacidiel)*i,self.yT+25,text=f"{i+cislo*5+1}",velkost=velkostTextuTlacidiel,disabled=True,textOffset=[0,7]))
                self.tlacidla.append(tlacidlo(o.zamok,o.zamok,self.xT+(k.sirkaLevelTlacidla+medzeraTlacidiel)*i,self.yT+25,text=f"",velkost=velkostTextuTlacidiel,disabled=True))

            pz = False
            for i in g.unlocknuteLevely:
                s,l = i#set,level
                if s == self.cislo:
                    animacia(a.zamok,2,self.xT+(k.sirkaLevelTlacidla+medzeraTlacidiel)*l,self.yT)
                    pz = True
            if pz:
                z.odmlevel.play()
                
            # self.levelN = levelN
            # self.levelA = levelA
            self.medzeraTlacidiel = medzeraTlacidiel
            # print(self.odomknute,"odoodod")
        
        def spustiLevel(self):#cisla levelov su [0,4]
            if self.cislo == 0:
                if self.tlacidla[0].je_keyup():
                    casy = [1.5, 3.5, 5.5, 8.0, 10.5, 13.0, 15.0, 18.0, 22.0, 25.0, 27.0, 29.5, 32.0, 34.5, 36.5, 38.5, 41.5, 43.5, 47.0, 49.5, 52.0, 54.0, 56.0, 58.0, 60.5, 62.5, 64.5, 67.0, 69.5, 71.5, 73.0, 75.0, 78.0, 80.0, 82.5, 85.0, 87.5, 90.0, 94.0, 96.0, 98.0, 100.0, 103.0, 105.0, 107.5, 110.0, 112.0, 114.0, 116.5, 118.5, 121.0, 125.0, 127.0, 129.0, 134.5, 137.0, 139.0, 141.5, 144.0, 146.0, 147.5, 149.0, 150.5, 152.0, 153.5, 155.0, 157.0, 159.0, 161.0, 163.0, 165.0, 166.5]
                    pismena = ['x', 'x', 'l', 'l', 'x', 'x', 'x', 'l', 'l', 'x', 'x', 'x', 'l', 'l', 'x', 'l', 'x', 'l', 'x', 'x', 'x', 'l', 'l', 'l', 'x', 'x', 'l', 'l', 'x', 'x', 'x', 'x', 'l', 'l', 'l', 'x', 'x', 'l', 'x', 'x', 'x', 'x', 'l', 'l', 'l', 'l', 'l', 'x', 'l', 'x', 'l', 'x', 'x', 'x', 'l', 'l', 'l', 'l', 'x', 'x', 'l', 'l', 'x', 'l', 'x', 'l', 'x', 'x', 'l', 'l', 'l', 'x']
                    klavesyPoz = {'x':k.ls1k['x'],'l':k.ls1k['l']}
                    return [casy,pismena,klavesyPoz,1.5,self.cislo,0]#[0,[8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],0]#input pre level
                if self.tlacidla[1].je_keyup():
                    casy = [1.0, 2.5, 4.5, 6.0, 7.5, 9.5, 12.0, 13.5, 16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 27.5, 29.5, 31.0, 33.0, 35.0, 37.0, 39.0, 41.0, 43.0, 45.0, 47.0, 48.5, 50.0, 51.5, 53.0, 55.0, 57.0, 59.0, 61.0, 63.0, 65.0, 67.0, 69.0, 71.0, 73.0, 75.0, 77.0, 79.0, 80.5, 82.0, 83.5, 85.0, 88.0, 89.3, 90.6, 91.9, 96.0, 97.3, 98.6, 99.9, 102.0, 104.0, 106.0, 108.0, 110.0, 112.0, 114.0, 116.0, 118.0, 120.0, 122.0, 124.0, 126.0, 128.0, 130.0, 132.0, 134.0, 136.0, 137.3, 138.6, 139.9, 141.2, 142.5, 143.8, 145.1, 146.4, 147.7, 150.0, 152.0, 154.0, 156.0, 158.0, 160.0, 162.0, 164.0, 165.3]
                    pismena = ['x', 'l', 'g', 'x', 'g', 'l', 'l', 'g', 'x', 'g', 'l', 'x', 'x', 'x', 'l', 'l', 'g', 'g', 'l', 'l', 'g', 'g', 'x', 'x', 'l', 'l', 'l', 'x', 'x', 'x', 'g', 'g', 'g', 'x', 'l', 'g', 'x', 'l', 'g', 'x', 'l', 'g', 'x', 'x', 'x', 'x', 'g', 'g', 'g', 'g', 'l', 'l', 'l', 'l', 'g', 'l', 'x', 'l', 'g', 'x', 'x', 'l', 'g', 'x', 'g', 'l', 'g', 'l', 'x', 'g', 'x', 'l', 'g', 'g', 'x', 'l', 'l', 'g', 'x', 'x', 'l', 'x', 'x', 'l', 'l', 'g', 'g', 'g', 'x', 'l']
                    klavesyPoz = {'x':k.ls1k['x'],'l':k.ls1k['l'],'g':k.ls1k['g']}
                    return[casy,pismena,klavesyPoz,1.3,self.cislo,1]
                if self.tlacidla[2].je_keyup():
                    casy = [1.0, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0, 13.5, 15.0, 16.5, 18.0, 19.5, 21.0, 22.5, 24.0, 25.5, 27.0, 28.5, 30.0, 32.0, 34.0, 36.0, 38.0, 40.0, 42.0, 44.0, 46.0, 48.0, 49.1, 50.2, 51.3, 52.4, 53.5, 54.6, 55.7, 56.8, 57.9, 59.0, 60.1, 61.2, 62.5, 64.0, 65.5, 67.0, 68.5, 70.0, 71.5, 73.0, 74.5, 76.0, 77.1, 78.2, 79.3, 80.4, 81.5, 82.6, 86.0, 87.3]
                    pismena = ['x', 'l', 'g', 'y', 'g', 'l', 'y', 'x', 'l', 'x', 'l', 'x', 'y', 'g', 'y', 'g', 'x', 'y', 'l', 'g', 'l', 'l', 'x', 'x', 'g', 'g', 'y', 'y', 'g', 'x', 'l', 'y', 'g', 'x', 'y', 'l', 'x', 'g', 'y', 'y', 'l', 'y', 'y', 'x', 'x', 'l', 'l', 'g', 'g', 'x', 'y', 'l', 'g', 'g', 'y', 'y', 'l', 'x', 'g']
                    klavesyPoz = {'x':k.ls1k['x'],'l':k.ls1k['l'],'g':k.ls1k['g'],'y':k.ls1k['y']}
                    return[casy,pismena,klavesyPoz,1.1,self.cislo,2]
                if self.tlacidla[3].je_keyup():
                    casy = [1.0, 2.5, 4.0, 5.5, 7.0, 8.5, 10.0, 11.5, 13.0, 14.5, 16.0, 17.5, 19.0, 20.5, 22.0, 23.5, 25.0, 26.5, 28.0, 29.5, 31.0, 32.5, 34.0, 35.5, 37.0, 38.5, 40.0, 41.5, 43.0, 44.5, 46.0, 47.5, 49.0, 50.5, 52.0, 54.0, 56.0, 58.0, 60.0, 62.0, 64.0, 66.0, 68.0, 70.0, 72.0, 73.0, 74.0, 75.0, 76.0, 77.0, 78.0, 79.0, 80.0, 81.0, 82.0, 83.0, 84.5, 86.0, 87.5, 89.0, 90.5, 92.0, 93.5, 95.0, 96.5, 98.0, 99.5, 100.5]
                    pismena = ['x', 'l', 'g', 'y', 'i', 'i', 'y', 'g', 'l', 'x', 'l', 'g', 'x', 'y', 'i', 'y', 'i', 'g', 'x', 'l', 'l', 'l', 'x', 'x', 'y', 'y', 'i', 'i', 'g', 'g', 'l', 'g', 'i', 'y', 'x', 'g', 'g', 'l', 'l', 'y', 'y', 'x', 'x', 'i', 'i', 'l', 'x', 'y', 'g', 'i', 'y', 'l', 'x', 'i', 'g', 'y', 'x', 'g', 'x', 'g', 'y', 'y', 'i', 'i', 'l', 'l', 'y', 'i']
                    klavesyPoz = {'x':k.ls1k['x'],'l':k.ls1k['l'],'g':k.ls1k['g'],'y':k.ls1k['y'],'i':k.ls1k['i']}
                    return[casy,pismena,klavesyPoz,1.0,self.cislo,3]
                if self.tlacidla[4].je_keyup():
                    casy = [1.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0, 32.0, 34.0, 36.0, 38.0, 40.0, 42.0, 44.0, 46.0, 47.5, 49.0, 50.5, 52.0, 53.5, 55.0, 56.0, 57.0, 58.0, 59.0, 60.0, 61.0, 62.0, 63.0, 64.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 71.0, 72.0, 73.0, 74.5, 76.0, 77.5, 79.0, 80.5, 82.0, 83.5, 85.0, 86.5, 88.0, 89.5]
                    pismena = ['x', 'l', 'g', 'y', 'i', 'e', 'e', 'i', 'y', 'g', 'l', 'x', 'x', 'x', 'l', 'l', 'g', 'g', 'e', 'e', 'i', 'i', 'y', 'y', 'i', 'e', 'x', 'l', 'g', 'y', 'x', 'e', 'i', 'l', 'g', 'y', 'x', 'l', 'i', 'e', 'y', 'g', 'x', 'l', 'g', 'y', 'i', 'e', 'e', 'e', 'y', 'y', 'i', 'i', 'x', 'x', 'g', 'g', 'l']
                    klavesyPoz = {'x':k.ls1k['x'],'l':k.ls1k['l'],'g':k.ls1k['g'],'y':k.ls1k['y'],'i':k.ls1k['i'],'e':k.ls1k['e']}
                    return[casy,pismena,klavesyPoz,0.9,self.cislo,4]
            if self.cislo == 1:
                if self.tlacidla[0].je_keyup():
                    casy = [2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0, 25.5, 27.0, 28.5, 30.0, 31.5, 33.0, 34.5, 36.0, 37.5, 39.0, 40.5, 42.0, 44.0, 46.0, 48.0, 50.0, 52.0, 54.0, 55.5]
                    pismena = ['k', 'v', 'a', 'k', 'v', 'a', 'k', 'k', 'v', 'v', 'a', 'a', 'v', 'k', 'a', 'v', 'k', 'a', 'k', 'a', 'v', 'k', 'a', 'v', 'k', 'v', 'a', 'k', 'v', 'a', 'v']
                    klavesyPoz = {'k':k.ls2k['k'],'v':k.ls2k['v'],'a':k.ls2k['a']}
                    return[casy,pismena,klavesyPoz,1.5,self.cislo,0]
                if self.tlacidla[1].je_keyup():
                    casy = [1.0, 3.0, 5.0, 7.0, 9.0, 11.0, 13.0, 15.0, 17.0, 19.0, 21.0, 23.0, 25.0, 27.0, 29.0, 31.0, 33.0, 35.0, 37.0, 39.0, 41.0, 43.0, 45.0, 47.0, 49.0, 51.0, 53.0, 55.0, 57.0, 59.0, 61.0, 63.0, 64.5, 66.0, 67.5, 69.0, 70.5, 72.0, 73.5, 75.0, 76.3, 77.6, 78.9, 80.2, 81.5, 82.8, 84.1, 85.4, 90.0, 92.0, 94.0, 96.0, 98.0, 100.0, 102.0, 104.0, 106.0, 108.0, 110.0, 112.0, 120.0, 121.5]
                    pismena = ['k', 'v', 'a', 'p', 'k', 'v', 'a', 'p', 'k', 'k', 'v', 'v', 'a', 'a', 'p', 'p', 'p', 'a', 'v', 'k', 'p', 'a', 'v', 'k', 'v', 'a', 'k', 'p', 'a', 'p', 'v', 'k', 'k', 'v', 'k', 'v', 'a', 'p', 'a', 'p', 'k', 'v', 'a', 'p', 'p', 'a', 'v', 'k', 'k', 'k', 'p', 'p', 'v', 'v', 'a', 'a', 'k', 'v', 'a', 'p', 'a', 'p']
                    klavesyPoz = klavesyPoz = {'k':k.ls2k['k'],'v':k.ls2k['v'],'a':k.ls2k['a'],'p':k.ls2k['p']}
                    return[casy,pismena,klavesyPoz,1.3,self.cislo,1]
                if self.tlacidla[2].je_keyup():
                    casy = [4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0, 32.0, 34.0, 36.0, 38.0, 40.0, 42.0, 43.1, 44.2, 45.3, 46.4, 47.5, 48.6, 49.7, 50.8, 51.9, 53.0, 56.0, 58.0, 60.0, 62.0, 64.0, 68.0, 69.5, 71.0]
                    pismena = ['k', 'v', 'a', 'p', 'j', 'k', 'v', 'a', 'p', 'j', 'p', 'p', 'v', 'v', 'a', 'a', 'j', 'j', 'k', 'k', 'j', 'a', 'k', 'p', 'v', 'k', 'v', 'a', 'j', 'p', 'k', 'v', 'a', 'p', 'j', 'p', 'v', 'j']
                    klavesyPoz = {'k':k.ls2k['k'],'v':k.ls2k['v'],'a':k.ls2k['a'],'p':k.ls2k['p'],'j':k.ls2k['j']}
                    return[casy,pismena,klavesyPoz,1.1,self.cislo,2]
                if self.tlacidla[3].je_keyup():
                    casy = [1.0, 3.0, 5.0, 7.0, 9.0, 11.0, 13.0, 15.0, 17.0, 19.0, 21.0, 23.0, 25.0, 27.0, 29.0, 31.0, 33.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 46.0, 48.0, 50.0, 51.0, 53.0, 54.5]
                    pismena = ['k', 'v', 'a', 'p', 'j', 'x', 'p', 'j', 'k', 'a', 'v', 'x', 'p', 'j', 'p', 'x', 'j', 'x', 'k', 'a', 'j', 'x', 'v', 'p', 'k', 'x', 'p', 'k', 'x', 'v', 'p', 'j', 'a']
                    klavesyPoz = {'k':k.ls2k['k'],'v':k.ls2k['v'],'a':k.ls2k['a'],'p':k.ls2k['p'],'j':k.ls2k['j'],'x':k.ls2k['x']}
                    return[casy,pismena,klavesyPoz,1.0,self.cislo,3]
                if self.tlacidla[4].je_keyup():
                    casy = [5.0, 7.0, 9.0, 11.0, 13.0, 15.0, 17.0, 19.0, 21.0, 23.0, 25.0, 27.0, 29.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 48.0, 50.0, 52.0, 54.0, 56.0, 58.0, 60.0, 66.0, 67.0, 68.0]
                    pismena = ['k', 'v', 'a', 'p', 'j', 'x', 'r', 'p', 'k', 'j', 'v', 'a', 'x', 'r', 'k', 'j', 'r', 'v', 'p', 'x', 'a', 'k', 'v', 'a', 'p', 'j', 'x', 'r', 'p', 'k', 'a', 'v', 'j', 'x', 'r', 'x', 'v', 'r']
                    klavesyPoz = {'k':k.ls2k['k'],'v':k.ls2k['v'],'a':k.ls2k['a'],'p':k.ls2k['p'],'j':k.ls2k['j'],'x':k.ls2k['x'],'r':k.ls2k['r']}
                    return[casy,pismena,klavesyPoz,0.9,self.cislo,4]
            if self.cislo == 2:
                if self.tlacidla[0].je_keyup():
                    casy = [2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0, 32.0, 34.0, 36.0, 38.0, 40.0, 41.5, 43.0, 44.5, 46.0, 47.5, 49.0, 50.5, 52.0, 54.0, 56.0, 58.0, 60.0, 62.0, 64.0, 65.5]
                    pismena = ['l', 'b', 'q', 'o', 'b', 'b', 'q', 'q', 'l', 'l', 'o', 'o', 'o', 'l', 'q', 'b', 'q', 'l', 'b', 'o', 'l', 'b', 'q', 'o', 'l', 'b', 'q', 'o', 'q', 'o', 'l', 'b', 'o', 'q', 'l']
                    klavesyPoz = {'l':k.ls3k['l'],'b':k.ls3k['b'],'q':k.ls3k['q'],'o':k.ls3k['o']}
                    return[casy,pismena,klavesyPoz,1.5,self.cislo,0]
                if self.tlacidla[1].je_keyup():
                    casy = [5.0, 7.0, 9.0, 11.0, 13.0, 16.0, 18.0, 20.0, 22.0, 24.0, 25.3, 26.6, 27.9, 29.2, 30.5, 31.8, 33.1, 34.4, 35.7, 37.0, 40.0, 42.0, 44.0, 46.0, 48.0, 50.0, 52.0, 54.0, 56.0, 58.0, 60.0, 61.5, 63.0, 64.5, 66.0, 68.0, 70.0, 72.0, 74.0, 76.0, 79.0, 80.3, 81.6]
                    pismena = ['l', 'b', 'q', 'o', 'z', 'z', 'o', 'q', 'b', 'l', 'l', 'b', 'q', 'l', 'b', 'q', 'o', 'z', 'o', 'z', 'l', 'o', 'b', 'z', 'q', 'b', 'b', 'q', 'q', 'o', 'o', 'z', 'z', 'l', 'l', 'z', 'q', 'o', 'l', 'b', 'o', 'l', 'b']
                    klavesyPoz = {'l':k.ls3k['l'],'b':k.ls3k['b'],'q':k.ls3k['q'],'o':k.ls3k['o'],'z':k.ls3k['z']}
                    return[casy,pismena,klavesyPoz,1.3,self.cislo,1]
                if self.tlacidla[2].je_keyup():
                    casy = [5.0, 7.0, 9.0, 11.0, 13.0, 15.0, 17.0, 19.0, 21.0, 23.0, 25.0, 27.0, 29.0, 31.0, 33.0, 35.0, 37.0, 39.0, 40.1, 41.2, 42.3, 43.4, 44.5, 45.6, 46.7, 47.8, 48.9, 50.0, 51.1, 52.2, 55.0, 57.0, 59.0, 61.0, 63.0, 65.0, 67.0, 69.0, 71.0, 73.0, 75.0, 77.0, 79.0, 81.0, 82.1, 83.2, 84.3, 86.0]
                    pismena = ['l', 'b', 'q', 'o', 'z', 'f', 'o', 'z', 'f', 'l', 'b', 'q', 'b', 'l', 'q', 'f', 'z', 'o', 'l', 'l', 'z', 'z', 'f', 'f', 'b', 'b', 'q', 'q', 'o', 'o', 'l', 'b', 'q', 'o', 'z', 'f', 'l', 'b', 'f', 'o', 'q', 'z', 'b', 'o', 'f', 'l', 'q', 'z']
                    klavesyPoz = {'l':k.ls3k['l'],'b':k.ls3k['b'],'q':k.ls3k['q'],'o':k.ls3k['o'],'z':k.ls3k['z'],'f':k.ls3k['f']}
                    return[casy,pismena,klavesyPoz,1.1,self.cislo,2]
                if self.tlacidla[3].je_keyup():
                    casy = [5.0, 7.0, 9.0, 11.0, 13.0, 15.0, 17.0, 19.0, 21.0, 23.0, 25.0, 27.0, 29.0, 31.0, 33.0, 35.0, 37.0, 39.0, 41.0, 43.0, 45.0, 47.0, 49.0, 51.0, 53.0, 55.0, 57.0, 59.0, 75.0, 77.0, 78.0, 79.0, 80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 92.0, 94.0, 96.0, 98.0, 100.0, 102.0, 103.0, 108.0, 112.0, 117.0, 118.0, 122.0, 125.0, 126.0, 127.0, 130.0, 133.0, 139.0, 144.0, 149.0, 154.0, 160.0, 161.0]
                    pismena = ['l', 'b', 'q', 'o', 'z', 'f', 't', 't', 'f', 'z', 'o', 'q', 'b', 'l', 't', 't', 'z', 'z', 'f', 'f', 'o', 'o', 'q', 'q', 'b', 'b', 'l', 'l', 'l', 'o', 'z', 't', 'f', 'q', 'b', 't', 'f', 'z', 'o', 'q', 'b', 'l', 'l', 'b', 'q', 'o', 'z', 'f', 't', 't', 't', 'f', 't', 'z', 'l', 'b', 'q', 'q', 'b', 'q', 'l', 'q', 'b', 'q', 'z']
                    klavesyPoz = {'l':k.ls3k['l'],'b':k.ls3k['b'],'q':k.ls3k['q'],'o':k.ls3k['o'],'z':k.ls3k['z'],'f':k.ls3k['f'],'t':k.ls3k['t']}
                    return[casy,pismena,klavesyPoz,1.0,self.cislo,3]
                if self.tlacidla[4].je_keyup():
                    casy = [1]#[5.0, 7.0, 9.0, 11.0, 13.0, 15.0, 17.0, 19.0, 21.0, 23.0, 25.0, 27.0, 29.0, 31.0, 33.0, 35.0, 35.9, 36.8, 37.7, 38.6, 39.5, 40.4, 41.3, 42.2, 47.0, 49.0, 51.0, 53.0, 58.0, 61.0, 64.0, 66.0, 74.0, 76.0, 82.0, 82.9, 88.0, 90.0, 93.0, 99.0]
                    pismena = ['l']#['l', 'b', 'q', 'o', 'z', 'f', 't', 's', 'o', 'q', 'b', 'l', 's', 't', 'f', 'z', 'l', 'b', 'q', 'o', 'z', 'f', 't', 's', 'l', 'b', 'q', 'o', 's', 't', 'f', 'z', 'l', 'q', 'b', 'o', 't', 's', 'z', 'f']
                    klavesyPoz = {'l':k.ls3k['l'],'b':k.ls3k['b'],'q':k.ls3k['q'],'o':k.ls3k['o'],'z':k.ls3k['z'],'f':k.ls3k['f'],'t':k.ls3k['t'],'s':k.ls3k['s']}
                    return[casy,pismena,klavesyPoz,0.9,self.cislo,4]

            return False#[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],['x','l','g','y','x']

        def zobraz(self):
            # pygame.zobraz(self.obrazokPozadia, (self.xP-50,self.yP-50))
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
                self.texty.append(text(pozicia[0],pozicia[1],pismeno,32,(255,255,255),g.basic_hruby_font,roh='stred'))

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
            self.naposledyPismeno = ''
            self.zobrazitSa = True

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

            if len(obrazky) == 0:
                obrazky = [o.vajce]

            return obrazky

        def update(self):
            #print(klavesy.naposledy_pismeno())
            if len(klavesy.keydown_klavesi) > 0:
                pismeno = klavesy.keydown_klavesi[0]
                if pismeno in self.klavesyPoz:
                    self.naposledyPismeno = pismeno
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

        def naposledyKlaves(self):
            return self.naposledyPismeno

        def schovajSa(self):
            self.zobrazitSa = False

        def zobraz(self):
            if self.beziAnimacia:
                self.surface = o.vajce.copy()
                pygame.zobraz(self.alr.aktualnyObrazok(),(0,0),surface=self.surface)
                pygame.zobraz(self.apr.aktualnyObrazok(),(0,0),surface=self.surface)
                pygame.zobraz(self.aln.aktualnyObrazok(),(0,0),surface=self.surface)
                pygame.zobraz(self.apn.aktualnyObrazok(),(0,0),surface=self.surface)
            if self.zobrazitSa:
                pygame.zobraz(self.surface,(k.xStenoDispleja,k.yStenoDispleja),roh='stred')

    class vtipy:
        def __init__(self):
            self.vtip = self.losujVtip()
            self.vtipoCas = 15#takto dlho zostane kazdy vtip zobrazeny
            self.casMinuleho = time.time()

        def update(self):
            if time.time() > self.casMinuleho + self.vtipoCas:
                self.vtip = self.losujVtip()
                self.casMinuleho = time.time()

        def zobraz(self):
            pygame.zobraz(self.vtip,(1250,500))

        def losujVtip(self):
            return o.vtipy[random.randint(0,len(o.vtipy)-1)]

    class bar:
        def __init__(self,celkovyCas):
            print("bar zacina, celkovy cas je",celkovyCas)
            self.celkovyCas = celkovyCas
            self.casZ = time.time()
            self.pozadie = o.bar1.copy()
            self.pozadie = pygame.prefarb(self.pozadie,(255,0,0))
            self.sirka = 1500
            self.vyska = 10

        def zobraz(self):
            castCasu = (time.time()-self.casZ)/self.celkovyCas
            # print(castCasu,"bughr")
            bar = pygame.transform.smoothscale(o.bar2,(int(castCasu*self.sirka),self.vyska))
            pygame.zobraz(bar,(0,0),surface=self.pozadie)
            pygame.zobraz(self.pozadie,(100,935))
            

    class level:
        def __init__(self,casyStien,pismenaStien,klavesyPoz,casSteny,cisloSetu,cisloLevelu):#na spusteni levelu
            self.casyStien = casyStien #casStenyPredNaburanimDoVajca je konstantny
            self.progressBar = s.bar(casyStien[-1])
            self.casyStien.append(1000000)
            self.pismenaStien = pismenaStien#pismena, ktore treba stlacit
            self.casPanvice = self.casyStien[len(pismenaStien)-1]+4
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
            self.muzika.set_volume(0.35)
            self.minulePresla = None
            self.casNaburania = None
            self.freeznutyScreen = None
            g.unlocknuteLevely = []
            klavesy.naposledyPismeno = ''
            self.panvica = None
            self.ValeboP = ''
            self.vtipy = s.vtipy()

        def update(self):#scalovanie steny, detekovanie inputu
            self.panak.update()
            self.vtipy.update()
            if (cas.cas()-self.casZ) > self.casyStien[self.indexCasu]:#+self.casSteny na lavej strane
                print(f"nadisiel cas na stenu {self.indexCasu}")
                
                print("grg",tuple(self.klavesyPoz[self.pismenaStien[self.indexCasu]]))
                self.steny.append(s.stena(o.steny[self.cisloSetu][tuple(self.klavesyPoz[self.pismenaStien[self.indexCasu]])], self.surface ,self.casSteny))#self.obrazkyStien[self.indexSteny]
                self.indexCasu += 1
            
            if (cas.cas()-self.casZ)+self.casSteny > self.casPanvice and self.panvica == None:
                self.panvica = s.stena(o.panvica,self.surface,self.casSteny,panvica=True)
                print("panvicaaaaaaa")
                


            for i,stena in enumerate(self.steny):
                supdate = stena.update()
                if supdate == False:
                    del self.steny[i]
                
                if supdate == 'presla' and stena != self.minulePresla:
                    Npismeno = self.panak.naposledyKlaves()#klavesy.naposledy_pismeno()
                    print("Npismeno",Npismeno,"malo byt",self.pismenaStien[self.indexKlavesov])
                    if Npismeno != self.pismenaStien[self.indexKlavesov]:
                        self.muzika.stop()
                        self.casNaburania = time.time()
                        self.freeznutyScreen = g.Displej.copy()
                        self.ValeboP = False
                        self.casCakania = 0.5
                        z.rozplaskvajco.play()
                        #cas.pause()
                        #return 'f'
                        #return False#nabural som

                    self.indexKlavesov += 1
                    self.minulePresla = stena

            if self.casNaburania != None:
                if time.time()-self.casNaburania > self.casCakania:
                    return self.ValeboP
            
            if self.panvica != None:
                if self.ValeboP != True:
                    if self.panvica.update() == 'presla':
                        self.updateOdomknute()
                        self.muzika.stop()
                        self.casNaburania = time.time()
                        # self.freeznutyScreen = g.Displej.copy()
                        self.ValeboP = True#updatnut odomknute
                        self.casCakania = 3#cas animacie rozplesknutia vajca na prazenicu
                        animacia(a.rozplastenieNaPanvici,self.casCakania,k.xStenoDispleja-580/2,k.yStenoDispleja-580/2)
                        self.panak.schovajSa()
                        z.rozplaskvajco.play()
            # if len(self.steny) == 0 and self.indexCasu == len(self.casyStien)-1:
                # self.updateOdomknute()
                # self.muzika.stop()
                # return True#updatnut odomknute

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
            if self.cisloLevelu+1 < 5:
                if odomknutost[self.cisloSetu][self.cisloLevelu+1] == 0:
                    odomknutost[self.cisloSetu][self.cisloLevelu+1] = 1
                    g.unlocknuteLevely.append([self.cisloSetu,self.cisloLevelu+1])
            if self.cisloLevelu == 2 and self.cisloSetu < 2:
                if odomknutost[self.cisloSetu+1][0] == 0:
                    odomknutost[self.cisloSetu+1][0] = 1
                    g.unlocknuteLevely.append([self.cisloSetu+1,0])
            print(g.unlocknuteLevely,"tutoooooooooooooooooooooooooooooooooooooooooooo")
            for i in range(3):
                subor.write(' '.join(list(map(str,odomknutost[i])))+'\n')
            subor.close()

        def zobraz(self):#reference klavesnica poz nad vajcom
            self.klavesnica.zobraz()
            pygame.zobraz(o.jama , (0,0),surface=self.surface)
            for i in range(len(self.steny)):#iterovat od konca
                self.steny[len(self.steny)-1-i].zobraz()
            if self.panvica != None:
                self.panvica.zobraz()
            pygame.zobraz(self.surface,(k.xStenoDispleja,k.yStenoDispleja),roh='stred')
            self.panak.zobraz()
            self.vtipy.zobraz()
            self.progressBar.zobraz()

            if self.freeznutyScreen != None:
                pygame.zobraz(self.freeznutyScreen,(0,0))

def init():
    global s
    s = S()