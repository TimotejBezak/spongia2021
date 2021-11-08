import pygame
from pygame.locals import *
import collections

class G:
    global nefullscreen
    #region menit:
    tlacidlovy = "fonts/LEMONMILK-Medium.otf"#fonts/theboldfont.ttf"
    basic_font = 'fonts/freesansbold.ttf'
    basic_hruby_font = "fonts/theboldfont.ttf"
    hruby_pixel_font = "fonts/Mostwasted.ttf"#fonts/04B_30__.TTF"
    #endregion
    #region nemenit:
    moj_width = 1700
    moj_height = 960
    sirkaPocitaca = pygame.display.Info().current_w
    vyskaPocitaca = pygame.display.Info().current_h
    
    displej_width = moj_width
    displej_height = moj_height
    Displej = pygame.display.set_mode((displej_width, displej_height))
    scaleObrazovky = 1

    
    # scaleSirka = sirkaPocitaca/moj_width
    # scaleVyska = vyskaPocitaca/moj_height
    # scaleObrazovky = min(scaleSirka,scaleVyska)#ratam s tym, ze moja obrazovka je najmensia
    # displej_width = int(moj_width*scaleObrazovky)
    # displej_height = int(moj_height*scaleObrazovky)
    # Displej = pygame.display.set_mode((displej_width, displej_height),FULLSCREEN)
    # print(sirkaPocitaca,vyskaPocitaca)
    
    Hodiny = pygame.time.Clock()

    unlocknuteLevely = []
    #click = pygame.mouse.get_pressed()
    #poziciamyse = pygame.mouse.get_pos()
    frameF = 0
    frameZ = 0
    offsetKamery = [0,0]

    koniec = False
    #endregion

    class farby:
        cierna = (0,0,0)
        modra = (0,0,255)
        zelena = (0,255,0)
        cervena = (255,0,0)




def init():
    global g
    g = G()