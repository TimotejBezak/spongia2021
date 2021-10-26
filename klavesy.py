import pygame
from globalnepremenne import g
from pygame.locals import *

stlacene_klavesi = set()
keyup_klavesi = []
keydown_klavesi = []
klavesy_vsetky = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','u','v','w','x','y','z']
koniec = False

def je_stlaceny(klaves):
    if klaves in stlacene_klavesi:
        return True
    return False

def je_keydown(klaves):
    if klaves in keydown_klavesi:
        return True
    return False

def je_keyup(klaves):
    if klaves in keyup_klavesi:
        return True
    return False

def je_koniec():
    return koniec


def update():
    global keydown_klavesi,keyup_klavesi,stlacene_klavesi, koniec
    keydown_klavesi = []
    keyup_klavesi = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            koniec = True
            # pygame.display.quit()
            # pygame.quit()
            #exit(0)
        if event.type == pygame.KEYDOWN:
            for pismeno in klavesy_vsetky:
                if event.key == eval('pygame.K_'+pismeno):
                    keydown_klavesi.append(pismeno)
                    if pismeno not in stlacene_klavesi:
                        stlacene_klavesi.add(pismeno)
        
        if event.type == pygame.KEYUP:
            for pismeno in klavesy_vsetky:
                if event.key == eval('pygame.K_'+pismeno):
                    keyup_klavesi.append(pismeno)
                    if pismeno in stlacene_klavesi:
                        stlacene_klavesi.remove(pismeno)