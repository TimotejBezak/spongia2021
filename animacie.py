from globalnepremenne import g
import time
import pygame

animacie = []
akyFrameBezi = 0
def update():
    global akyFrameBezi
    akyFrameBezi += 1
    for i in animacie:
        i.update()

def zobraz():
    for i in animacie:
        i.zobraz()

class obrazky_v_case:
    def __init__(self,obrazky,cas,loop=False):
        """cas: s"""
        global animacie
        self.obrazky = obrazky

        self.cas = cas
        self.loop = loop

        self.reset()

        animacie.append(self)

    def reset(self):
        interval = self.cas/len(self.obrazky)
        self.kedy_zobrazit = []
        for i in range(len(self.obrazky)):
            self.kedy_zobrazit.append((i+1)*interval)

        self.kolkatyObrazok = 0
        self.zaciatocnyCas = time.time()


    def update(self):
        global animacie
        # print(self.kolkatyObrazok,len(self.obrazky))
        if self.kedy_zobrazit[self.kolkatyObrazok] <= time.time() - self.zaciatocnyCas:
            self.kolkatyObrazok += 1
            if self.kolkatyObrazok == len(self.obrazky):
                if self.loop == True:
                    self.reset()
                else:
                    print("animacia trvala:",time.time()-self.zaciatocnyCas,"mala trvat:",self.cas)
                    self.koniec()
                    return
        
        # self.zobraz()

    def zobraz(self):
        pass

    def koniec(self):
        animacie.remove(self)

    def aktualnyObrazok(self):
        if self.kolkatyObrazok == len(self.obrazky):
            return
        return self.obrazky[self.kolkatyObrazok]
        
class animacia(obrazky_v_case):
    def __init__(self, obrazky, cas,x,y, loop=False):
        obrazky_v_case.__init__(self,obrazky, cas, loop=loop)
        self.x = x
        self.y = y

    def zobraz(self):
        print("teraz je ",self.kolkatyObrazok)
        obrazok = self.aktualnyObrazok()
        if obrazok != None:
            pygame.zobraz(obrazok,(self.x,self.y))