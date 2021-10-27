import tlacidla,animacie
from globalnepremenne import g
import pygame
from loaderObrazkov import o,t,a,z

def resetScreen():# toto by chcelo byt rovnake vo vsetkych screenoch
    global g
    pygame.event.clear()
    g.koniec = False
    g.Displej = pygame.display.set_mode((g.displej_width, g.displej_height))
    tlacidla.tlacidla = []
    animacie.animacie = []
    #g.Displej = pygame.display.set_mode((g.displej_width, g.displej_height))
    g.frameF = 0
    g.frameZ = 0

def poziciaZKoncatin(rozmiestnenieKoncatin):
    surface = o.vajce.copy()
    lr,pr,ln,pn = rozmiestnenieKoncatin
    # print(o.lavaRuka,o.pravaRuka)
    pygame.zobraz(o.lavaRuka[lr],(0,0),surface=surface)
    pygame.zobraz(o.pravaRuka[pr],(0,0),surface=surface)#pygame.zobraz(o.pravaRuka[pr],(1000,850))
    pygame.zobraz(o.pravaNoha[ln],(0,0),surface=surface)
    pygame.zobraz(o.lavaNoha[pn],(0,0),surface=surface)
    return surface