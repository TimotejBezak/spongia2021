import pygame
from pygame.locals import *
import collections


class G:
    #region menit:
    tlacidlovy = "fonts/theboldfont.ttf"
    basic_font = 'fonts/freesansbold.ttf'
    basic_hruby_font = "fonts/theboldfont.ttf"
    hruby_pixel_font = "fonts/04B_30__.TTF"
    #endregion
    #region nemenit:
    displej_width = 1900#pygame.display.Info().current_w-100
    displej_height = 1000#pygame.display.Info().current_h-100
    Displej = pygame.display.set_mode((displej_width, displej_height))
    Hodiny = pygame.time.Clock()
    #click = pygame.mouse.get_pressed()
    #poziciamyse = pygame.mouse.get_pos()
    frameF = 0
    framez = 0
    offsetKamery = [0,0]
    scaleKamery = 1
    #endregion

    class farby:
        cierna = (0,0,0)
        modra = (0,0,255)
        zelena = (0,255,0)
        cervena = (255,0,0)

def init():
    global g
    g = G()