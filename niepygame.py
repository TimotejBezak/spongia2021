import pygame,os
from globalnepremenne import g


docasnefarby = [[132, 137, 192], [65, 154, 30], [246, 228, 178], [105, 10, 15], [155, 30, 106], [114, 89, 243], [51, 120, 237], [214, 27, 11], [10, 246, 24], [192, 34, 227], [135, 247, 193], [95, 121, 72], [26, 49, 6], [226, 37, 131], [81, 197, 146], [193, 89, 81], [147, 215, 33], [170, 90, 3], [218, 193, 225], [235, 242, 46], [124, 87, 130], [72, 33, 61], [224, 158, 8], [54, 129, 135], [192, 254, 118], [228, 182, 86], [27, 182, 103], [14, 223, 174], [165, 206, 164], [240, 121, 206], [183, 155, 256], [235, 114, 115], [80, 4, 127], [43, 57, 162], [28, 12, 221], [251, 3, 77], [64, 251, 112], [256, 16, 192], [4, 15, 78], [73, 216, 224], [15, 109, 183], [1, 164, 228], [199, 83, 179], [0, 81, 48], [16, 253, 254], [147, 172, 102], [252, 61, 248], [140, 8, 174], [70, 223, 3], [243, 88, 28]]
ktorafarba = 0

def loadniObrazok(sirka,vyska,path="totoniejenazovnicoho.png"):
    global ktorafarba
    try:
        obrazok = pygame.image.load(path).convert_alpha()
    except:
        obrazok = pygame.image.load('docasnyobrazok.png').convert_alpha()
        obrazok = prefarb(obrazok,docasnefarby[ktorafarba],ignorovaneFarby=[(0,0,0)])
        ktorafarba += 1
    
    if sirka == -1:
        sirka = obrazok.get_width()
    if vyska == -1:
        vyska = obrazok.get_height()
    vysledok = zmenitRozlisenie(obrazok,(sirka,vyska))
    return vysledok

def loadniAnimaciu(sirka,vyska,path_foldera='totoniejefolder'):
    vysledok = []
    pocet_filov = len(os.listdir(path_foldera))
    for i in range(1,pocet_filov):
        aktualnypath = path_foldera+'/'+str(i)+'.png'
        try:
            vysledok.append(loadniObrazok(sirka,vyska,aktualnypath))
        except:
            print('nenacital sa: ',aktualnypath)
            break
    return vysledok

def loadniZvuk(path):
    return pygame.mixer.Sound(path)

def zmenitRozlisenie(obrazok,rozmer):
    return pygame.transform.scale(obrazok,rozmer)

def prefarb(surface, color, ignorovaneFarby=[]):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b = color
    for x in range(w):
        for y in range(h):
            # a = surface.get_at((x, y))[3]
            rr,gg,bb,a = surface.get_at((x, y))
            if (rr,gg,bb) not in ignorovaneFarby:
                surface.set_at((x, y), pygame.Color(r, g, b, a))
    return surface

def zobraz(obrazok,pozicia,surface=g.Displej,roh="lavy_horny",ui=False):#stred: pozicia je pozicia stredu   pri scalovani stred obrazka ma ostat na tom istom mieste
    offset = g.offsetKamery
    scale = g.scaleKamery
    if ui:
        offset = (0,0)
        scale = 1
        #surface.blit(obrazok,pozicia)
        #return
    pozicia = [pozicia[0],pozicia[1]]
    pozicia[0] -= offset[0]
    pozicia[1] -= offset[1]#posunutie
    sirka = obrazok.get_width()*scale
    vyska = obrazok.get_height()*scale
    #print(roh,pozicia)
    if(roh=="stred"):
        pozicia[0] -= sirka/2
        pozicia[1] -= vyska/2
    if(roh=="lavy_horny"):
        pozicia[0] -= (sirka-obrazok.get_width())/2#(g.scaleKamery*obrazok.get_width()-obrazok.get_width())/2#(pixle o ktore som narastol)/2
        pozicia[1] -= (vyska-obrazok.get_height())/2
    if(roh=="lavy_dolny"):
        pozicia[0] -= (sirka-obrazok.get_width())/2
        pozicia[1] -= (vyska-obrazok.get_height())/2+obrazok.get_height()
    if(roh=="pravy_dolny"):
        pozicia[0] -= (sirka-obrazok.get_width())/2+obrazok.get_width()
        pozicia[1] -= (vyska-obrazok.get_height())/2+obrazok.get_height()
    if(roh=="pravy_horny"):
        pozicia[0] -= (sirka-obrazok.get_width())/2+obrazok.get_width()
        pozicia[1] -= (vyska-obrazok.get_height())/2
    #analogicky dorobit lavy_stred, pravy_stred, horny_stred,  moze sa hodit na text
    

    zobraz2(obrazok,pozicia,surface) #surface.blit(pygame.transform.smoothscale(obrazok,(obrazok.get_width()*g.scaleKamery,obrazok.get_height()*g.scaleKamery)),(pozicia[0]-g.offsetKamery[0],pozicia[1]-g.offsetKamery[1]))

def zobraz2(obrazok,pozicia,surface):
    surface.blit(pygame.transform.smoothscale(obrazok,(int(obrazok.get_width()*g.scaleKamery),int(obrazok.get_height()*g.scaleKamery))),(int(pozicia[0]),int(pozicia[1])))

#def zobraz(surface,co,pozicia):
#    surface.blit(co,pozicia)

#def zobraz(obrazok):
#    g.pozicieZobrazovania[obrazok.meno] = [obrazok.surface,[obrazok.pos_x,obrazok.pos_y]]
#
#def zmenSkin(obrazok,novySkin):
#    obrazok.skin = novySkin


pygame.loadniObrazok = loadniObrazok
pygame.loadniAnimaciu = loadniAnimaciu
pygame.zmenitRozlisenie = zmenitRozlisenie
pygame.prefarb = prefarb
pygame.zobraz = zobraz
pygame.loadniZvuk = loadniZvuk
#pygame.display.blit = zobraz

