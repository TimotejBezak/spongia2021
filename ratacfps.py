import pygame
from globalnepremenne import g
import queue,time
import text

class ratacfps:
    def __init__(self,vyska,ktore):
        self.fpsText = text.text(10,vyska,"",10,(0,0,0),g.basic_font)
        self.casText = text.text(10,40,"",10,(0,0,0),g.basic_font)
        self.casZ = time.time()
        self.pocet = 20
        self.sucet = 0#pocet*g.fps
        self.framy = queue.Queue()
        for _ in range(self.pocet):
            self.framy.put(0)#g.fps
        self.cas = time.time()

        self.akoCastoUpdatovat = 10 #raz za kolko framov

        self.aktualne_fps = 0
        self.ktore = ktore

    def update(self):
        global g
        if self.ktore == "F":
            g.frameF += 1
            frame = g.frameF
        else:
            g.frameZ += 1
            frame = g.frameZ
        if frame % self.akoCastoUpdatovat == 0:
            self.sucet -= self.framy.get()
            hodnota = int(1/(time.time()-self.cas))
            self.sucet += hodnota
            self.framy.put(hodnota)
            self.aktualne_fps = self.sucet/self.pocet
            #g.aktualne_fps = self.aktualne_fps
        self.cas = time.time()
        self.fpsText.zmenText(f"fps{self.ktore}: {int(self.aktualne_fps)}")
        self.casText.zmenText(f"cas: {int(time.time()-self.casZ)}")

    def zobraz(self):
        self.fpsText.zobraz()
        self.casText.zobraz()
        
