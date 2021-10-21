from globalnepremenne import g
import pygame

pygame.mouse.set_visible(False)
predosly_click,predosla_pozicia = None,None
pozicia = (0,0)
click = (0,0,0)
def update():
    global predosly_click,predosla_poziciamyse, pozicia, click
    predosly_click = click
    predosla_poziciamyse = pozicia
    click = pygame.mouse.get_pressed()
    pozicia = pygame.mouse.get_pos()

def jeKeyDown():
    if predosly_click[0] == False and g.click[0] == True:
        return True
    return False

def jeKeyUp():
    if predosly_click[0] == True and g.click[0] == False:
        return True
    return False