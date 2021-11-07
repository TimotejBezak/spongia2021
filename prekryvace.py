import pygame
from globalnepremenne import g

class prekryvac:
    def __init__(self,obrazok):
        """obrazok je akokeby mask"""
        self.obrazok = pygame.transform.smoothscale(obrazok,(int(obrazok.get_width()/g.scaleObrazovky)+1,int(obrazok.get_height()/g.scaleObrazovky)+1))#+1 aby som mys nescalol na 0
        self.mask = pygame.mask.from_surface(self.obrazok)
        self.x = 0
        self.y = 0

    def prekryvaSa(self,inyPrekryvac):
        """bool, ci sa prekryvam s inyPrekryvac"""
        offset = (int(inyPrekryvac.x-self.x),int(inyPrekryvac.y-self.y))
        if self.mask.overlap(inyPrekryvac.mask,offset) is None:
            return True
        return False

    def updatePos(self,x,y):
        self.x = x
        self.y = y