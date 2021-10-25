import tlacidla,animacie
from globalnepremenne import g
import pygame

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