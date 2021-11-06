import pygame,os
from globalnepremenne import g

docasnefarby = [[226, 68, 251], [176, 182, 56], [221, 217, 80], [30, 8, 46], [100, 69, 197], [222, 31, 132], [66, 183, 130], [73, 39, 52], [140, 30, 72], [171, 51, 97], [34, 81, 55], [16, 184, 108], [227, 182, 72], [101, 24, 35], [160, 45, 248], [236, 70, 153], [72, 0, 3], [40, 106, 70], [205, 230, 228], [57, 51, 175], [52, 158, 43], [94, 78, 75], [157, 255, 207], [253, 158, 141], [234, 150, 128], [46, 63, 93], [100, 184, 113], [200, 22, 166], [80, 1, 239], [71, 192, 225], [134, 178, 92], [44, 51, 46], [195, 101, 76], [241, 241, 20], [60, 226, 91], [146, 176, 25], [59, 125, 112], [37, 18, 234], [116, 154, 228], [119, 118, 203], [116, 0, 190], [187, 216, 174], [239, 198, 21], [245, 162, 175], [80, 77, 5], [2, 184, 32], [85, 85, 229], [122, 186, 185], [189, 194, 11], [29, 88, 208], [173, 5, 104], [223, 159, 27], [252, 85, 111], [190, 5, 55], [250, 17, 215], [68, 30, 155], [206, 241, 68], [129, 217, 234], [9, 104, 251], [156, 144, 117], [3, 247, 208], [82, 10, 141], [252, 198, 58], [253, 191, 206], [195, 103, 33], [72, 217, 11], [208, 206, 186], [206, 134, 218], [124, 174, 62], [111, 250, 6], [230, 10, 194], [1, 116, 177], [78, 159, 20], [224, 111, 110], [176, 91, 62], [167, 145, 248], [22, 226, 86], [75, 133, 39], [82, 113, 22], [156, 64, 156], [0, 190, 76], [194, 184, 215], [162, 72, 237], [182, 143, 100], [122, 89, 50], [64, 9, 38], [106, 221, 254], [92, 235, 91], [12, 39, 47], [12, 112, 113], [69, 190, 75], [4, 38, 178], [148, 17, 137], [255, 211, 138], [112, 64, 127], [147, 97, 111], [143, 64, 28], [13, 206, 139], [209, 41, 245], [246, 239, 237], [140, 12, 35], [110, 24, 247], [31, 73, 12], [143, 216, 24], [243, 144, 51], [64, 224, 159], [36, 144, 238], [246, 190, 158], [163, 117, 16], [40, 140, 30], [55, 154, 92], [26, 133, 154], [199, 192, 160], [71, 246, 140], [66, 184, 179], [166, 154, 16], [205, 100, 200], [240, 92, 217], [37, 97, 143], [135, 23, 219], [197, 42, 202], [254, 245, 128], [21, 200, 15], [138, 133, 151], [239, 57, 49], [49, 48, 209], [190, 134, 73], [147, 72, 85], [162, 146, 77], [150, 234, 222], [104, 251, 104], [191, 24, 12], [159, 137, 210], [178, 63, 41], [212, 33, 52], [41, 21, 198], [243, 203, 108], [115, 85, 170], [165, 164, 203], [66, 130, 253], [50, 253, 234], [244, 11, 37], [13, 202, 212], [54, 207, 138], [181, 10, 198], [95, 51, 234], [41, 7, 87], [205, 64, 219], [175, 43, 177], [83, 250, 190], [89, 168, 136], [196, 47, 130], [23, 247, 139], [34, 201, 94], [115, 38, 65], [5, 113, 219], [147, 90, 203], [43, 191, 27], [57, 69, 143], [175, 57, 140], [72, 155, 227], [172, 55, 217], [0, 64, 240], [229, 136, 253], [200, 195, 69], [104, 209, 220], [129, 209, 50], [102, 222, 191], [250, 102, 78], [58, 225, 39], [96, 218, 31], [98, 47, 6], [202, 130, 9], [154, 198, 43], [201, 119, 95], [43, 222, 113], [102, 139, 71], [233, 155, 199], [113, 200, 1], [171, 160, 167], [11, 155, 164], [254, 230, 42], [235, 102, 49], [24, 194, 59], [162, 46, 63], [191, 157, 128], [184, 199, 199], [251, 119, 159], [96, 12, 79], [217, 67, 61], [78, 65, 109], [3, 171, 226], [253, 7, 66], [76, 207, 171], [26, 43, 75], [116, 210, 134], [220, 96, 148], [3, 106, 24], [9, 138, 62], [74, 117, 182], [222, 209, 156], [66, 217, 207], [243, 237, 72], [80, 93, 168], [151, 197, 7], [91, 167, 217], [186, 220, 250], [96, 68, 23], [30, 226, 8], [107, 153, 110], [255, 172, 38], [23, 145, 183], [169, 248, 251], [102, 255, 232], [244, 108, 0], [24, 61, 198], [33, 90, 96], [90, 222, 66], [104, 90, 247], [97, 151, 175], [149, 35, 101], [157, 108, 130], [71, 42, 96], [199, 250, 114], [118, 244, 166], [38, 161, 68], [162, 1, 157], [68, 83, 253], [33, 74, 164], [103, 133, 20], [42, 61, 229], [86, 62, 255], [141, 187, 153], [127, 130, 54], [231, 27, 237], [58, 2, 131], [240, 53, 10], [246, 145, 87], [255, 192, 246], [124, 139, 247], [31, 105, 186], [243, 22, 111], [29, 36, 144], [193, 215, 125], [228, 211, 223], [57, 49, 71], [182, 232, 49], [208, 242, 190], [48, 170, 255], [144, 233, 169], [205, 216, 47], [213, 124, 55], [99, 35, 164], [235, 255, 47], [216, 150, 82], [138, 249, 88], [215, 109, 241], [193, 69, 104], [4, 62, 5], [218, 209, 10], [0, 183, 195], [96, 120, 154], [146, 214, 81], [70, 90, 196], [183, 102, 110], [38, 47, 2], [164, 110, 175], [76, 246, 26], [198, 24, 100], [53, 147, 9], [238, 234, 158], [63, 30, 254], [21, 167, 8], [45, 193, 157], [133, 145, 30], [19, 236, 238], [207, 200, 251], [4, 60, 59], [106, 202, 159], [202, 7, 217], [20, 131, 226], [50, 31, 29], [244, 158, 243], [230, 66, 187], [110, 250, 137], [2, 75, 88], [223, 115, 212], [253, 252, 211], [255, 68, 218], [238, 225, 192], [226, 85, 94], [148, 221, 121], [243, 21, 4], [169, 173, 102], [178, 103, 236], [218, 255, 137], [110, 154, 4], [25, 1, 12], [87, 197, 251], [157, 196, 213], [27, 120, 90], [102, 193, 56], [181, 246, 11], [153, 202, 140], [158, 13, 60], [215, 166, 160], [8, 72, 134], [50, 105, 35], [81, 193, 2], [28, 167, 149], [63, 254, 104], [89, 194, 188], [74, 200, 44], [106, 249, 63], [144, 12, 194], [123, 1, 3], [36, 195, 194], [143, 189, 115], [153, 87, 42], [15, 32, 4], [225, 179, 107], [173, 208, 110], [41, 246, 54], [29, 158, 114], [28, 21, 114], [125, 104, 152], [102, 99, 109], [9, 245, 12], [213, 8, 24], [187, 65, 193], [16, 40, 231], [57, 151, 128], [26, 129, 46], [209, 51, 83], [1, 110, 141], [67, 249, 70], [198, 131, 120], [91, 218, 145], [145, 248, 14], [153, 250, 54], [253, 131, 113], [209, 81, 120], [246, 140, 16], [218, 12, 249], [170, 73, 4], [195, 94, 252], [87, 39, 190], [139, 175, 215], [180, 132, 155], [37, 135, 123]]
ktorafarba = 0

def loadniObrazok(sirka,vyska,path="",polotransparent=False,bielaNaTransparent=False):
    global ktorafarba
    try:
        obrazok = pygame.image.load(path).convert_alpha()
    except:
        if path != "":
            print('nenacital sa: ',path)
        obrazok = pygame.image.load('docasnyobrazok.png').convert_alpha()
        obrazok = prefarb(obrazok,docasnefarby[ktorafarba],ignorovaneFarby=[(0,0,0)])
        ktorafarba += 1
        # print(docasnefarby[ktorafarba])
    
    if sirka == -1:
        sirka = obrazok.get_width()
    if vyska == -1:
        vyska = obrazok.get_height()
    obrazok = zmenitRozlisenie(obrazok,(sirka,vyska))
    obrazok = pygame.transform.smoothscale( obrazok, (int(obrazok.get_width()*g.scaleObrazovky),int(obrazok.get_height()*g.scaleObrazovky)) )
    if polotransparent:
        obrazok = polotransparentnut(obrazok)
        if path != "":
            pygame.image.save(obrazok,path)
    if bielaNaTransparent:
        obrazok = bieleNaTransparentne(obrazok)
    
    return obrazok

def polotransparentnut(obrazok,a=200):
    surface = obrazok.copy()
    w, h = surface.get_size()
    for x in range(w):
        for y in range(h):
            r,g,b,aa = surface.get_at((x, y))
            if aa != 0:
                surface.set_at( (x,y) , pygame.Color(r,g,b,a) )
    return surface

def bieleNaTransparentne(obrazok):
    surface = obrazok.copy()
    w, h = surface.get_size()
    for x in range(w):
        for y in range(h):
            r,g,b,a = surface.get_at((x, y))
            if (r,g,b) == (255,255,255):
                surface.set_at( (x,y) , pygame.Color(0,0,0,0) )
    return surface

def tlacidloA(Nobrazok):
    surface = Nobrazok.copy()
    w, h = surface.get_size()
    for x in range(w):
        for y in range(h):
            # a = surface.get_at((x, y))[3]
            r,g,b,a = surface.get_at((x, y))
            surface.set_at((x,y) , pygame.Color(min(255,r+50),min(255,g+50),min(255,b+50),a) )
    return surface

def loadniAnimaciu(sirka,vyska,path_foldera='totoniejefolder',polotransparent=False,pocet_filov=-1):
    vysledok = []
    if pocet_filov == -1:
        pocet_filov = len(os.listdir(path_foldera))
    for i in range(1,pocet_filov+1):
        aktualnypath = path_foldera+'/'+str(i)+'.png'
        vysledok.append(loadniObrazok(sirka,vyska,aktualnypath,polotransparent=polotransparent))
    
    return vysledok

def loadniZvuk(path):
    try:
        return pygame.mixer.Sound(path)
    except:
        return pygame.mixer.Sound('nic.wav')

def zmenitRozlisenie(obrazok,rozmer):
    return pygame.transform.scale( obrazok,( int(rozmer[0]),int(rozmer[1]) ) )

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

def rohUpdate(pos,obrazok,roh):
    sirka = obrazok.get_width()
    vyska = obrazok.get_height()
    if(roh=="stred"):
        pos[0] -= sirka/2
        pos[1] -= vyska/2
    if(roh=="lavy_dolny"):
        pos[1] -= vyska
    if(roh=="pravy_dolny"):
        pos[0] -= sirka
        pos[1] -= vyska
    if(roh=="pravy_horny"):
        pos[0] -= sirka    #analogicky dorobit lavy_stred, pravy_stred, horny_stred,  moze sa hodit na text
    return pos

def zobraz(obrazok,pozicia,surface=g.Displej,roh="lavy_horny",ui=False):#stred: pozicia je pozicia stredu   pri scalovani stred obrazka ma ostat na tom istom mieste
    offset = g.offsetKamery
    if ui:
        offset = (0,0)

    pozicia = [pozicia[0]-offset[0],pozicia[1]-offset[1]]
    if surface == g.Displej:
        pozicia = [pozicia[0]*g.scaleObrazovky,pozicia[1]*g.scaleObrazovky]

    try:
        rohUpdate(pozicia,obrazok,roh)
    except:
        pass

    zobraz2(obrazok,pozicia,surface)

def zobraz2(obrazok,pozicia,surface):
    #surface.blit( obrazok, (int(pozicia[0]),int(pozicia[1])) )
    try:
        surface.blit( obrazok, (int(pozicia[0]),int(pozicia[1])) )
    except:
        pass

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
pygame.rohUpdate = rohUpdate
#pygame.display.blit = zobraz

