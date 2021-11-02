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
    stena = pygame.loadniObrazok(580,580,'stena.png',bielaNaTransparent=True)
    panak = pygame.loadniObrazok(-1,-1,'panak.png')

    level1Panak = pygame.loadniObrazok(150,150)
    level1Pozadie = pygame.loadniObrazok(1150,250)
    level2Panak = pygame.loadniObrazok(150,150)
    level2Pozadie = pygame.loadniObrazok(1150,250)
    level3Panak = pygame.loadniObrazok(150,150)
    level3Pozadie = pygame.loadniObrazok(1150,250)
    zamknutyLevel = pygame.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla)

    kruh50 = pygame.loadniObrazok(100,100,'kruh.png')

    pozadieKlavesu = pygame.loadniObrazok(120,120)

    pravaRuka = pygame.loadniAnimaciu(-1,-1,'prava ruka',polotransparent=False)
    lavaRuka = pygame.loadniAnimaciu(-1,-1,'lava ruka',polotransparent=False)
    pravaNoha = pygame.loadniAnimaciu(-1,-1,'prava noha',polotransparent=False)
    lavaNoha = pygame.loadniAnimaciu(-1,-1,'lava noha',polotransparent=False)

    vajce = pygame.loadniObrazok(-1,-1,'vajce.png',polotransparent=False)
    jama = pygame.loadniObrazok(580,580)

    steny = {
        (0,0,0,0): pygame.loadniObrazok(580,580,"0000.png"),
        (0,0,0,1): pygame.loadniObrazok(580,580,"0001.png"),
        (0,0,0,2): pygame.loadniObrazok(580,580,"0002.png"),
        (0,0,1,0): pygame.loadniObrazok(580,580,"0010.png"),
        (0,0,1,1): pygame.loadniObrazok(580,580,"0011.png"),
        (0,0,1,2): pygame.loadniObrazok(580,580,"0012.png"),
        (0,0,2,0): pygame.loadniObrazok(580,580,"0020.png"),
        (0,0,2,1): pygame.loadniObrazok(580,580,"0021.png"),
        (0,0,2,2): pygame.loadniObrazok(580,580,"0022.png"),
        (0,1,0,0): pygame.loadniObrazok(580,580,"0100.png"),
        (0,1,0,1): pygame.loadniObrazok(580,580,"0101.png"),
        (0,1,0,2): pygame.loadniObrazok(580,580,"0102.png"),
        (0,1,1,0): pygame.loadniObrazok(580,580,"0110.png"),
        (0,1,1,1): pygame.loadniObrazok(580,580,"0111.png"),
        (0,1,1,2): pygame.loadniObrazok(580,580,"0112.png"),
        (0,1,2,0): pygame.loadniObrazok(580,580,"0120.png"),
        (0,1,2,1): pygame.loadniObrazok(580,580,"0121.png"),
        (0,1,2,2): pygame.loadniObrazok(580,580,"0122.png"),
        (0,2,0,0): pygame.loadniObrazok(580,580,"0200.png"),
        (0,2,0,1): pygame.loadniObrazok(580,580,"0201.png"),
        (0,2,0,2): pygame.loadniObrazok(580,580,"0202.png"),
        (0,2,1,0): pygame.loadniObrazok(580,580,"0210.png"),
        (0,2,1,1): pygame.loadniObrazok(580,580,"0211.png"),
        (0,2,1,2): pygame.loadniObrazok(580,580,"0212.png"),
        (0,2,2,0): pygame.loadniObrazok(580,580,"0220.png"),
        (0,2,2,1): pygame.loadniObrazok(580,580,"0221.png"),
        (0,2,2,2): pygame.loadniObrazok(580,580,"0222.png"),
        (1,0,0,0): pygame.loadniObrazok(580,580,"1000.png"),
        (1,0,0,1): pygame.loadniObrazok(580,580,"1001.png"),
        (1,0,0,2): pygame.loadniObrazok(580,580,"1002.png"),
        (1,0,1,0): pygame.loadniObrazok(580,580,"1010.png"),
        (1,0,1,1): pygame.loadniObrazok(580,580,"1011.png"),
        (1,0,1,2): pygame.loadniObrazok(580,580,"1012.png"),
        (1,0,2,0): pygame.loadniObrazok(580,580,"1020.png"),
        (1,0,2,1): pygame.loadniObrazok(580,580,"1021.png"),
        (1,0,2,2): pygame.loadniObrazok(580,580,"1022.png"),
        (1,1,0,0): pygame.loadniObrazok(580,580,"1100.png"),
        (1,1,0,1): pygame.loadniObrazok(580,580,"1101.png"),
        (1,1,0,2): pygame.loadniObrazok(580,580,"1102.png"),
        (1,1,1,0): pygame.loadniObrazok(580,580,"1110.png"),
        (1,1,1,1): pygame.loadniObrazok(580,580,"1111.png"),
        (1,1,1,2): pygame.loadniObrazok(580,580,"1112.png"),
        (1,1,2,0): pygame.loadniObrazok(580,580,"1120.png"),
        (1,1,2,1): pygame.loadniObrazok(580,580,"1121.png"),
        (1,1,2,2): pygame.loadniObrazok(580,580,"1122.png"),
        (1,2,0,0): pygame.loadniObrazok(580,580,"1200.png"),
        (1,2,0,1): pygame.loadniObrazok(580,580,"1201.png"),
        (1,2,0,2): pygame.loadniObrazok(580,580,"1202.png"),
        (1,2,1,0): pygame.loadniObrazok(580,580,"1210.png"),
        (1,2,1,1): pygame.loadniObrazok(580,580,"1211.png"),
        (1,2,1,2): pygame.loadniObrazok(580,580,"1212.png"),
        (1,2,2,0): pygame.loadniObrazok(580,580,"1220.png"),
        (1,2,2,1): pygame.loadniObrazok(580,580,"1221.png"),
        (1,2,2,2): pygame.loadniObrazok(580,580,"1222.png"),
        (2,0,0,0): pygame.loadniObrazok(580,580,"2000.png"),
        (2,0,0,1): pygame.loadniObrazok(580,580,"2001.png"),
        (2,0,0,2): pygame.loadniObrazok(580,580,"2002.png"),
        (2,0,1,0): pygame.loadniObrazok(580,580,"2010.png"),
        (2,0,1,1): pygame.loadniObrazok(580,580,"2011.png"),
        (2,0,1,2): pygame.loadniObrazok(580,580,"2012.png"),
        (2,0,2,0): pygame.loadniObrazok(580,580,"2020.png"),
        (2,0,2,1): pygame.loadniObrazok(580,580,"2021.png"),
        (2,0,2,2): pygame.loadniObrazok(580,580,"2022.png"),

        

    }
    
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
    testMuzika = pygame.loadniZvuk('muzika.wav')#existuje zvuk.set_volume() od 0 do 1

o = O()
t = T()
a = A()
z = Z()