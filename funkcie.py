import tlacidla,animacie
from globalnepremenne import g

def resetScreen():# toto by chcelo byt rovnake vo vsetkych screenoch
    global g
    g.koniec = False
    tlacidla.tlacidla = []
    animacie.animacie = []
    #g.Displej = pygame.display.set_mode((g.displej_width, g.displej_height))
    g.frameF = 0
    g.frameZ = 0