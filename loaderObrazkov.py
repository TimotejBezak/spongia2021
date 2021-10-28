import niepygame as pygame
#from niepygame import pygamee
import konstanty as k

class O:
    testObrazok = pygame.loadniObrazok(200,100)
    testObrazok2 = pygame.loadniObrazok(1500,1000)
    auto = pygame.loadniObrazok(200,120,path='testauto2.png')
    pozadie = pygame.loadniObrazok(1700,800,'pozadie.png')
    pixel = pygame.loadniObrazok(1,1,'pixel.png')
    test1 = pygame.loadniObrazok(-1,-1,'test1.png')
    test2 = pygame.loadniObrazok(-1,-1,'test4.png')
    test3 = pygame.loadniObrazok(-1,-1,'test5.png')
    ostryobrazok = pygame.loadniObrazok(-1,-1,'ostryobrazok.jpg')
    mys = pygame.loadniObrazok(50,50,'mys.png')
    stena = pygame.loadniObrazok(1000,1000,'stena.png',bielaNaTransparent=False)
    panak = pygame.loadniObrazok(-1,-1,'panak.png')

    level1Panak = pygame.loadniObrazok(150,150)
    level1Pozadie = pygame.loadniObrazok(1150,250)

    kruh50 = pygame.loadniObrazok(100,100,'kruh.png')

    pozadieKlavesu = pygame.loadniObrazok(120,120)

    pravaRuka = pygame.loadniAnimaciu(-1,-1,'prava ruka',polotransparent=False)
    lavaRuka = pygame.loadniAnimaciu(-1,-1,'lava ruka',polotransparent=False)
    pravaNoha = pygame.loadniAnimaciu(-1,-1,'prava noha',polotransparent=False)
    lavaNoha = pygame.loadniAnimaciu(-1,-1,'lava noha',polotransparent=False)

    vajce = pygame.loadniObrazok(-1,-1,'vajce.png',polotransparent=False)
    jama = pygame.loadniObrazok(580,580)
    
class T:
    testtlacidloA = pygame.loadniObrazok(100,100)
    testtlacidloN = pygame.loadniObrazok(100,100)
    vyhralsiA = pygame.loadniObrazok(100,100)
    vyhralsiN = pygame.loadniObrazok(100,100)
    prehralsiA = pygame.loadniObrazok(100,100)
    prehralsiN = pygame.loadniObrazok(100,100)
    spetDoMenuA = pygame.loadniObrazok(100,100)
    spetDoMenuN = pygame.loadniObrazok(100,100)
    pauzaA = pygame.loadniObrazok(100,100)
    pauzaN = pygame.loadniObrazok(100,100)
    odpauzaA = pygame.loadniObrazok(100,100)
    odpauzaN = pygame.loadniObrazok(100,100)
    XA = pygame.loadniObrazok(25,25)
    XN = pygame.loadniObrazok(25,25)

    levelA = pygame.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla)
    levelN = pygame.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla)

class A:
    animacia = pygame.loadniAnimaciu(1000,800,path_foldera='animciaNemasDostPenazi')

class Z:
    test = pygame.loadniZvuk('maybe-next-time-huh.wav')#zvuk.play
    testMuzika = pygame.loadniZvuk('muzikaaa.wav')#existuje zvuk.set_volume() od 0 do 1

o = O()
t = T()
a = A()
z = Z()