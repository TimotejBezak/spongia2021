import pygame,os
from globalnepremenne import g

docasnefarby = [[142, 31, 121], [206, 136, 116], [252, 87, 178], [65, 17, 252], [188, 1, 113], [44, 74, 162], [247, 149, 200], [243, 166, 236], [140, 63, 42], [81, 115, 228], [50, 102, 219], [59, 253, 182], [96, 147, 167], [188, 13, 66], [185, 147, 202], [220, 46, 8], [13, 139, 138], [175, 206, 65], [222, 16, 37], [91, 22, 6], [223, 191, 150], [129, 203, 117], [2, 68, 106], [0, 211, 45], [23, 80, 188], [196, 187, 44], [96, 142, 22], [42, 18, 120], [19, 3, 160], [59, 154, 117], [106, 149, 213], [157, 169, 232], [255, 78, 33], [213, 144, 151], [118, 210, 164], [48, 162, 179], [7, 114, 36], [20, 190, 129], [116, 79, 232], [22, 200, 88], [35, 217, 160], [93, 251, 124], [224, 41, 127], [72, 230, 37], [24, 0, 42], [237, 119, 137], [31, 178, 212], [251, 126, 71], [174, 97, 105], [197, 74, 153], [114, 247, 76], [200, 209, 89], [131, 220, 215], [162, 156, 93], [238, 185, 121], [55, 101, 99], [11, 165, 162], [28, 38, 52], [7, 227, 213], [33, 55, 5], [117, 113, 129], [212, 195, 12], [107, 102, 193], [110, 121, 5], [155, 177, 119], [133, 31, 165], [214, 65, 62], [188, 71, 16], [6, 6, 214], [113, 37, 76], [237, 92, 12], [138, 160, 194], [174, 55, 172], [18, 127, 240], [79, 137, 58], [55, 245, 17], [95, 68, 98], [86, 214, 104], [20, 255, 43], [234, 226, 95], [7, 53, 168], [254, 149, 43], [179, 16, 216], [3, 163, 97], [210, 167, 94], [188, 232, 214], [117, 41, 209], [163, 149, 3], [44, 235, 247], [248, 111, 223], [155, 212, 197], [66, 93, 47], [74, 180, 146], [219, 109, 51], [77, 5, 47], [132, 249, 255], [181, 188, 189], [241, 196, 209], [213, 176, 200], [17, 50, 128], [11, 178, 36], [46, 215, 46], [155, 47, 80], [227, 121, 247], [125, 178, 71], [208, 94, 195], [157, 32, 22], [99, 47, 160], [240, 240, 34], [166, 220, 243], [147, 233, 133], [128, 77, 118], [145, 134, 215], [134, 198, 245], [34, 151, 44], [18, 123, 1], [216, 153, 22], [128, 4, 242], [176, 74, 232], [29, 59, 216], [79, 225, 149], [214, 237, 164], [221, 23, 241], [2, 216, 123], [70, 153, 254], [156, 207, 6], [76, 250, 231], [111, 192, 10], [30, 17, 235], [74, 198, 227], [111, 235, 23], [100, 245, 208], [94, 175, 193], [69, 51, 209], [123, 67, 12], [144, 58, 236], [203, 130, 38], [38, 34, 166], [208, 54, 211], [86, 37, 131], [244, 50, 239], [130, 148, 151], [158, 103, 194], [156, 118, 42], [123, 138, 95], [10, 236, 19], [57, 20, 65], [235, 1, 95], [51, 192, 111], [137, 97, 255]]#[[26, 29, 40], [254, 190, 92], [87, 13, 44], [243, 195, 43], [98, 179, 35], [128, 135, 141], [6, 170, 99], [8, 79, 23], [81, 204, 242], [45, 142, 13], [27, 171, 141], [31, 237, 124], [198, 114, 103], [231, 172, 133], [246, 208, 121], [122, 45, 135], [69, 160, 148], [246, 31, 178], [73, 208, 199], [133, 219, 98], [250, 235, 53], [68, 192, 60], [151, 70, 102], [106, 244, 216], [237, 233, 101], [101, 92, 242], [239, 137, 105], [136, 133, 8], [118, 76, 158], [190, 243, 11], [171, 219, 179], [122, 218, 247], [190, 45, 152], [172, 8, 21], [91, 111, 45], [88, 145, 87], [40, 81, 229], [17, 223, 226], [236, 9, 55], [145, 100, 237], [241, 60, 140], [65, 85, 84], [120, 168, 203], [59, 55, 7], [89, 221, 111], [183, 89, 50], [234, 214, 243], [188, 124, 256], [146, 256, 99], [60, 39, 238], [32, 22, 216], [105, 249, 81], [135, 80, 61], [159, 13, 88], [224, 109, 83], [65, 36, 173], [89, 83, 178], [242, 213, 1], [47, 171, 196], [1, 46, 226], [71, 244, 61], [221, 251, 146], [165, 145, 134], [193, 91, 207], [189, 140, 71], [60, 185, 9], [56, 36, 113], [104, 126, 22], [42, 224, 58], [104, 243, 155], [16, 138, 62], [33, 104, 66], [53, 179, 109], [212, 101, 142], [205, 159, 160], [150, 146, 48], [92, 215, 68], [184, 154, 34], [136, 23, 166], [17, 137, 155], [189, 53, 221], [120, 162, 60], [219, 171, 188], [129, 64, 247], [131, 230, 190], [123, 247, 118], [254, 89, 215], [189, 208, 216], [59, 97, 212], [112, 27, 68], [57, 84, 139], [247, 154, 177], [92, 154, 181], [193, 30, 246], [16, 5, 167], [253, 0, 84], [168, 77, 17], [3, 79, 97], [244, 78, 25], [209, 26, 197], [135, 104, 105], [158, 163, 176], [212, 10, 88], [144, 199, 130], [160, 198, 77], [59, 111, 169], [63, 167, 240], [93, 2, 233], [230, 126, 248], [245, 99, 123], [204, 45, 20], [44, 55, 49], [20, 85, 195], [163, 9, 255], [152, 14, 215], [185, 220, 142], [127, 200, 55], [18, 201, 17], [240, 217, 200], [1, 15, 59], [185, 256, 80], [4, 132, 236], [239, 237, 171], [203, 171, 222], [40, 118, 244], [217, 39, 127], [40, 62, 88], [176, 109, 168], [42, 189, 232], [164, 80, 193], [66, 253, 212], [3, 226, 91], [190, 255, 237], [179, 140, 2], [240, 33, 15], [81, 236, 20], [196, 67, 256], [39, 101, 113], [176, 227, 105], [15, 179, 212], [66, 112, 11], [148, 256, 31], [12, 68, 132], [111, 132, 192], [169, 117, 60], [230, 3, 239], [9, 128, 193], [4, 256, 242], [215, 208, 24], [179, 12, 163]]#[[132, 137, 192], [65, 154, 30], [246, 228, 178], [105, 10, 15], [155, 30, 106], [114, 89, 243], [51, 120, 237], [214, 27, 11], [10, 246, 24], [192, 34, 227], [135, 247, 193], [95, 121, 72], [26, 49, 6], [226, 37, 131], [81, 197, 146], [193, 89, 81], [147, 215, 33], [170, 90, 3], [218, 193, 225], [235, 242, 46], [124, 87, 130], [72, 33, 61], [224, 158, 8], [54, 129, 135], [192, 254, 118], [228, 182, 86], [27, 182, 103], [14, 223, 174], [165, 206, 164], [240, 121, 206], [183, 155, 256], [235, 114, 115], [80, 4, 127], [43, 57, 162], [28, 12, 221], [251, 3, 77], [64, 251, 112], [256, 16, 192], [4, 15, 78], [73, 216, 224], [15, 109, 183], [1, 164, 228], [199, 83, 179], [0, 81, 48], [16, 253, 254], [147, 172, 102], [252, 61, 248], [140, 8, 174], [70, 223, 3], [243, 88, 28]]
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

def loadniAnimaciu(sirka,vyska,path_foldera='totoniejefolder',polotransparent=False):
    vysledok = []
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
    pozicia = [pozicia[0]*g.scaleObrazovky,pozicia[1]*g.scaleObrazovky]

    rohUpdate(pozicia,obrazok,roh)
    
    zobraz2(obrazok,pozicia,surface)

def zobraz2(obrazok,pozicia,surface):
    surface.blit( obrazok, (int(pozicia[0]),int(pozicia[1])) )
    # try:
    #     surface.blit( obrazok, (int(pozicia[0]),int(pozicia[1])) )
    # except:
    #     pass

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

