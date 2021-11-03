import pygame,os
pygame.init()
pygame.display.init()
Displej = pygame.display.set_mode((10,10))

def loadniObrazok(sirka,vyska,path=""):
    global ktorafarba
    try:
        obrazok = pygame.image.load(path).convert_alpha()
    except:
        if path != "":
            print('nenacital sa: ',path)
        obrazok = pygame.image.load('docasnyobrazok.png').convert_alpha()
    
    if sirka == -1:
        sirka = obrazok.get_width()
    if vyska == -1:
        vyska = obrazok.get_height()
    obrazok = zmenitRozlisenie(obrazok,(sirka,vyska))
    #obrazok = pygame.transform.smoothscale( obrazok, (int(obrazok.get_width()*g.scaleObrazovky),int(obrazok.get_height()*g.scaleObrazovky)) )
    return obrazok

def loadniAnimaciu(sirka,vyska,path_foldera='totoniejefolder'):
    vysledok = []
    pocet_filov = len(os.listdir(path_foldera))
    for i in range(1,pocet_filov+1):
        aktualnypath = path_foldera+'/'+str(i)+'.png'
        vysledok.append(loadniObrazok(sirka,vyska,aktualnypath))
    
    return vysledok

def zmenitRozlisenie(obrazok,rozmer):
    return pygame.transform.scale( obrazok,( int(rozmer[0]),int(rozmer[1]) ) )

def poziciaZKoncatin(rozmiestnenieKoncatin):
    surface = vajce.copy()
    lr,pr,ln,pn = rozmiestnenieKoncatin
    # print(o.lavaRuka,o.pravaRuka)
    zobraz(lavaRuka[lr],(0,0),surface=surface)
    zobraz(pravaRuka[pr],(0,0),surface=surface)#pygame.zobraz(o.pravaRuka[pr],(1000,850))
    zobraz(lavaNoha[ln],(0,0),surface=surface)
    zobraz(pravaNoha[pn],(0,0),surface=surface)
    return surface

def zobraz(obrazok,pozicia,surface=Displej,roh="lavy_horny",ui=False):#stred: pozicia je pozicia stredu   pri scalovani stred obrazka ma ostat na tom istom mieste

    #rohUpdate(pozicia,obrazok,roh)
    
    zobraz2(obrazok,pozicia,surface)

def zobraz2(obrazok,pozicia,surface):
    surface.blit( obrazok, (int(pozicia[0]),int(pozicia[1])) )

vajce = loadniObrazok(-1,-1,'vajce.png')
pravaRuka = loadniAnimaciu(-1,-1,'prava ruka')
lavaRuka = loadniAnimaciu(-1,-1,'lava ruka')
pravaNoha = loadniAnimaciu(-1,-1,'prava noha')
lavaNoha = loadniAnimaciu(-1,-1,'lava noha')

sirkaT = 5#sirka transparentneho obvodu
sirkaF = 8#sirka farebneho obvodu
stenaOriginal = loadniObrazok(580,580,'stenatextura1.png')
kruhT = loadniObrazok(sirkaT*2,sirkaT*2,'kruh.png')
kruhF = loadniObrazok((sirkaF+sirkaT)*2,(sirkaF+sirkaT)*2,'kruh.png')

def zrob(koncatiny):#[0,0,1,0]
    poza = poziciaZKoncatin(koncatiny)
    stena = stenaOriginal.copy()
    pw,ph = poza.get_size()
    sw,sh = stena.get_size()
    offset = [int((sw-pw)/2),int((sh-ph)/2)]

    for x in range(pw):
        for y in range(ph):
            r,g,b,a = poza.get_at((x,y))
            if a != 0:#ak tam nieje poza transparentna
                stena.set_at((x+offset[0],y+offset[1]), pygame.Color(0,0,0,0))#0

    for x in range(pw):
        # break
        for y in range(ph):
            r,g,b,a = poza.get_at((x,y))
            if a != 0:#ak tam nieje poza transparentna
                a1,a2,a3,a4 = 0,0,0,0
                # print(x,y,pw,ph)
                if x+1 < pw:
                    a1 = poza.get_at((x+1,y))[3]
                if y+1 < ph:
                    a2 = poza.get_at((x,y+1))[3]
                if x > 0:
                    a3 = poza.get_at((x-1,y))[3]
                if y > 0:
                    a4 = poza.get_at((x,y-1))[3]
                if a1==0 or a2==0 or a3==0 or a4==0:#ci je na obvode panaka
                    for xk in range((sirkaT+sirkaF)*2):
                        for yk in range((sirkaT+sirkaF)*2):
                            ak = kruhF.get_at((xk,yk))[3]
                            if ak != 0:#ak to je v kruhu
                                pos = (x+offset[0]+xk-(sirkaT+sirkaF), y+offset[1]+yk-(sirkaT+sirkaF))
                                if stena.get_at(pos) != (0,0,0,0):
                                    stena.set_at(pos, pygame.Color(255,215,0,255))
                    # for xk in range(sirkaT*2):
                    #     for yk in range(sirkaT*2):
                    #         ak = kruhT.get_at((xk,yk))[3]
                    #         if ak != 0:#ak to je v kruhu
                    #             stena.set_at((x+offset[0]+xk-sirkaT-2,y+offset[1]+yk-sirkaT-2), pygame.Color(0,0,0,0))

    for x in range(pw):
        for y in range(ph):
            r,g,b,a = poza.get_at((x,y))
            if a != 0:#ak tam nieje poza transparentna
                a1,a2,a3,a4 = 0,0,0,0
                # print(x,y,pw,ph)
                if x+1 < pw:
                    a1 = poza.get_at((x+1,y))[3]
                if y+1 < ph:
                    a2 = poza.get_at((x,y+1))[3]
                if x > 0:
                    a3 = poza.get_at((x-1,y))[3]
                if y > 0:
                    a4 = poza.get_at((x,y-1))[3]
                if a1==0 or a2==0 or a3==0 or a4==0:#ci je na obvode panaka
                    for xk in range(sirkaT*2):
                        for yk in range(sirkaT*2):
                            ak = kruhT.get_at((xk,yk))[3]
                            if ak != 0:#ak to je v kruhu
                                pos = (x+offset[0]+xk-sirkaT, y+offset[1]+yk-sirkaT)
                                # if stena.get_at(pos) != (0,0,0,255):
                                stena.set_at(pos, pygame.Color(0,0,0,0))

    pygame.image.save(stena,f"steny1/{''.join(list(map(str,koncatiny)))}.png")

for a in range(3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                zrob([a,b,c,d])
                print(f"{[a,b,c,d]} hotovo")
# zrob([0,0,0,0])
