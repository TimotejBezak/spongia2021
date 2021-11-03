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

    # kruh50 = pygame.loadniObrazok(100,100,'kruh.png')
    # kruh5 = pygame.loadniObrazok(10,10,'kruh.png')

    pozadieKlavesu = pygame.loadniObrazok(110,110)

    pravaRuka = pygame.loadniAnimaciu(-1,-1,'prava ruka',polotransparent=False)
    lavaRuka = pygame.loadniAnimaciu(-1,-1,'lava ruka',polotransparent=False)
    pravaNoha = pygame.loadniAnimaciu(-1,-1,'prava noha',polotransparent=False)
    lavaNoha = pygame.loadniAnimaciu(-1,-1,'lava noha',polotransparent=False)

    vajce = pygame.loadniObrazok(-1,-1,'vajce.png',polotransparent=True)
    jama = pygame.loadniObrazok(580,580)

    stena1 = pygame.loadniObrazok(580,580)
    stena2 = pygame.loadniObrazok(580,580)
    stena3 = pygame.loadniObrazok(580,580)

    steny = [{
        (0,0,0,0): pygame.loadniObrazok(580,580,"steny1/0000.png"),
        (0,0,0,1): pygame.loadniObrazok(580,580,"steny1/0001.png"),
        (0,0,0,2): pygame.loadniObrazok(580,580,"steny1/0002.png"),
        (0,0,1,0): pygame.loadniObrazok(580,580,"steny1/0010.png"),
        (0,0,1,1): pygame.loadniObrazok(580,580,"steny1/0011.png"),
        (0,0,1,2): pygame.loadniObrazok(580,580,"steny1/0012.png"),
        (0,0,2,0): pygame.loadniObrazok(580,580,"steny1/0020.png"),
        (0,0,2,1): pygame.loadniObrazok(580,580,"steny1/0021.png"),
        (0,0,2,2): pygame.loadniObrazok(580,580,"steny1/0022.png"),
        (0,1,0,0): pygame.loadniObrazok(580,580,"steny1/0100.png"),
        (0,1,0,1): pygame.loadniObrazok(580,580,"steny1/0101.png"),
        (0,1,0,2): pygame.loadniObrazok(580,580,"steny1/0102.png"),
        (0,1,1,0): pygame.loadniObrazok(580,580,"steny1/0110.png"),
        (0,1,1,1): pygame.loadniObrazok(580,580,"steny1/0111.png"),
        (0,1,1,2): pygame.loadniObrazok(580,580,"steny1/0112.png"),
        (0,1,2,0): pygame.loadniObrazok(580,580,"steny1/0120.png"),
        (0,1,2,1): pygame.loadniObrazok(580,580,"steny1/0121.png"),
        (0,1,2,2): pygame.loadniObrazok(580,580,"steny1/0122.png"),
        (0,2,0,0): pygame.loadniObrazok(580,580,"steny1/0200.png"),
        (0,2,0,1): pygame.loadniObrazok(580,580,"steny1/0201.png"),
        (0,2,0,2): pygame.loadniObrazok(580,580,"steny1/0202.png"),
        (0,2,1,0): pygame.loadniObrazok(580,580,"steny1/0210.png"),
        (0,2,1,1): pygame.loadniObrazok(580,580,"steny1/0211.png"),
        (0,2,1,2): pygame.loadniObrazok(580,580,"steny1/0212.png"),
        (0,2,2,0): pygame.loadniObrazok(580,580,"steny1/0220.png"),
        (0,2,2,1): pygame.loadniObrazok(580,580,"steny1/0221.png"),
        (0,2,2,2): pygame.loadniObrazok(580,580,"steny1/0222.png"),
        (1,0,0,0): pygame.loadniObrazok(580,580,"steny1/1000.png"),
        (1,0,0,1): pygame.loadniObrazok(580,580,"steny1/1001.png"),
        (1,0,0,2): pygame.loadniObrazok(580,580,"steny1/1002.png"),
        (1,0,1,0): pygame.loadniObrazok(580,580,"steny1/1010.png"),
        (1,0,1,1): pygame.loadniObrazok(580,580,"steny1/1011.png"),
        (1,0,1,2): pygame.loadniObrazok(580,580,"steny1/1012.png"),
        (1,0,2,0): pygame.loadniObrazok(580,580,"steny1/1020.png"),
        (1,0,2,1): pygame.loadniObrazok(580,580,"steny1/1021.png"),
        (1,0,2,2): pygame.loadniObrazok(580,580,"steny1/1022.png"),
        (1,1,0,0): pygame.loadniObrazok(580,580,"steny1/1100.png"),
        (1,1,0,1): pygame.loadniObrazok(580,580,"steny1/1101.png"),
        (1,1,0,2): pygame.loadniObrazok(580,580,"steny1/1102.png"),
        (1,1,1,0): pygame.loadniObrazok(580,580,"steny1/1110.png"),
        (1,1,1,1): pygame.loadniObrazok(580,580,"steny1/1111.png"),
        (1,1,1,2): pygame.loadniObrazok(580,580,"steny1/1112.png"),
        (1,1,2,0): pygame.loadniObrazok(580,580,"steny1/1120.png"),
        (1,1,2,1): pygame.loadniObrazok(580,580,"steny1/1121.png"),
        (1,1,2,2): pygame.loadniObrazok(580,580,"steny1/1122.png"),
        (1,2,0,0): pygame.loadniObrazok(580,580,"steny1/1200.png"),
        (1,2,0,1): pygame.loadniObrazok(580,580,"steny1/1201.png"),
        (1,2,0,2): pygame.loadniObrazok(580,580,"steny1/1202.png"),
        (1,2,1,0): pygame.loadniObrazok(580,580,"steny1/1210.png"),
        (1,2,1,1): pygame.loadniObrazok(580,580,"steny1/1211.png"),
        (1,2,1,2): pygame.loadniObrazok(580,580,"steny1/1212.png"),
        (1,2,2,0): pygame.loadniObrazok(580,580,"steny1/1220.png"),
        (1,2,2,1): pygame.loadniObrazok(580,580,"steny1/1221.png"),
        (1,2,2,2): pygame.loadniObrazok(580,580,"steny1/1222.png"),
        (2,0,0,0): pygame.loadniObrazok(580,580,"steny1/2000.png"),
        (2,0,0,1): pygame.loadniObrazok(580,580,"steny1/2001.png"),
        (2,0,0,2): pygame.loadniObrazok(580,580,"steny1/2002.png"),
        (2,0,1,0): pygame.loadniObrazok(580,580,"steny1/2010.png"),
        (2,0,1,1): pygame.loadniObrazok(580,580,"steny1/2011.png"),
        (2,0,1,2): pygame.loadniObrazok(580,580,"steny1/2012.png"),
        (2,0,2,0): pygame.loadniObrazok(580,580,"steny1/2020.png"),
        (2,0,2,1): pygame.loadniObrazok(580,580,"steny1/2021.png"),
        (2,0,2,2): pygame.loadniObrazok(580,580,"steny1/2022.png"),
        (2,1,0,0): pygame.loadniObrazok(580,580,"steny1/2100.png"),
        (2,1,0,1): pygame.loadniObrazok(580,580,"steny1/2101.png"),
        (2,1,0,2): pygame.loadniObrazok(580,580,"steny1/2102.png"),
        (2,1,1,0): pygame.loadniObrazok(580,580,"steny1/2110.png"),
        (2,1,1,1): pygame.loadniObrazok(580,580,"steny1/2111.png"),
        (2,1,1,2): pygame.loadniObrazok(580,580,"steny1/2112.png"),
        (2,1,2,0): pygame.loadniObrazok(580,580,"steny1/2120.png"),
        (2,1,2,1): pygame.loadniObrazok(580,580,"steny1/2121.png"),
        (2,1,2,2): pygame.loadniObrazok(580,580,"steny1/2122.png"),
        (2,2,0,0): pygame.loadniObrazok(580,580,"steny1/2200.png"),
        (2,2,0,1): pygame.loadniObrazok(580,580,"steny1/2201.png"),
        (2,2,0,2): pygame.loadniObrazok(580,580,"steny1/2202.png"),
        (2,2,1,0): pygame.loadniObrazok(580,580,"steny1/2210.png"),
        (2,2,1,1): pygame.loadniObrazok(580,580,"steny1/2211.png"),
        (2,2,1,2): pygame.loadniObrazok(580,580,"steny1/2212.png"),
        (2,2,2,0): pygame.loadniObrazok(580,580,"steny1/2220.png"),
        (2,2,2,1): pygame.loadniObrazok(580,580,"steny1/2221.png"),
        (2,2,2,2): pygame.loadniObrazok(580,580,"steny1/2222.png"),
    },
    {
        (0,0,0,0): pygame.loadniObrazok(580,580,"steny2/0000.png"),
        (0,0,0,1): pygame.loadniObrazok(580,580,"steny2/0001.png"),
        (0,0,0,2): pygame.loadniObrazok(580,580,"steny2/0002.png"),
        (0,0,1,0): pygame.loadniObrazok(580,580,"steny2/0010.png"),
        (0,0,1,1): pygame.loadniObrazok(580,580,"steny2/0011.png"),
        (0,0,1,2): pygame.loadniObrazok(580,580,"steny2/0012.png"),
        (0,0,2,0): pygame.loadniObrazok(580,580,"steny2/0020.png"),
        (0,0,2,1): pygame.loadniObrazok(580,580,"steny2/0021.png"),
        (0,0,2,2): pygame.loadniObrazok(580,580,"steny2/0022.png"),
        (0,1,0,0): pygame.loadniObrazok(580,580,"steny2/0100.png"),
        (0,1,0,1): pygame.loadniObrazok(580,580,"steny2/0101.png"),
        (0,1,0,2): pygame.loadniObrazok(580,580,"steny2/0102.png"),
        (0,1,1,0): pygame.loadniObrazok(580,580,"steny2/0110.png"),
        (0,1,1,1): pygame.loadniObrazok(580,580,"steny2/0111.png"),
        (0,1,1,2): pygame.loadniObrazok(580,580,"steny2/0112.png"),
        (0,1,2,0): pygame.loadniObrazok(580,580,"steny2/0120.png"),
        (0,1,2,1): pygame.loadniObrazok(580,580,"steny2/0121.png"),
        (0,1,2,2): pygame.loadniObrazok(580,580,"steny2/0122.png"),
        (0,2,0,0): pygame.loadniObrazok(580,580,"steny2/0200.png"),
        (0,2,0,1): pygame.loadniObrazok(580,580,"steny2/0201.png"),
        (0,2,0,2): pygame.loadniObrazok(580,580,"steny2/0202.png"),
        (0,2,1,0): pygame.loadniObrazok(580,580,"steny2/0210.png"),
        (0,2,1,1): pygame.loadniObrazok(580,580,"steny2/0211.png"),
        (0,2,1,2): pygame.loadniObrazok(580,580,"steny2/0212.png"),
        (0,2,2,0): pygame.loadniObrazok(580,580,"steny2/0220.png"),
        (0,2,2,1): pygame.loadniObrazok(580,580,"steny2/0221.png"),
        (0,2,2,2): pygame.loadniObrazok(580,580,"steny2/0222.png"),
        (1,0,0,0): pygame.loadniObrazok(580,580,"steny2/1000.png"),
        (1,0,0,1): pygame.loadniObrazok(580,580,"steny2/1001.png"),
        (1,0,0,2): pygame.loadniObrazok(580,580,"steny2/1002.png"),
        (1,0,1,0): pygame.loadniObrazok(580,580,"steny2/1010.png"),
        (1,0,1,1): pygame.loadniObrazok(580,580,"steny2/1011.png"),
        (1,0,1,2): pygame.loadniObrazok(580,580,"steny2/1012.png"),
        (1,0,2,0): pygame.loadniObrazok(580,580,"steny2/1020.png"),
        (1,0,2,1): pygame.loadniObrazok(580,580,"steny2/1021.png"),
        (1,0,2,2): pygame.loadniObrazok(580,580,"steny2/1022.png"),
        (1,1,0,0): pygame.loadniObrazok(580,580,"steny2/1100.png"),
        (1,1,0,1): pygame.loadniObrazok(580,580,"steny2/1101.png"),
        (1,1,0,2): pygame.loadniObrazok(580,580,"steny2/1102.png"),
        (1,1,1,0): pygame.loadniObrazok(580,580,"steny2/1110.png"),
        (1,1,1,1): pygame.loadniObrazok(580,580,"steny2/1111.png"),
        (1,1,1,2): pygame.loadniObrazok(580,580,"steny2/1112.png"),
        (1,1,2,0): pygame.loadniObrazok(580,580,"steny2/1120.png"),
        (1,1,2,1): pygame.loadniObrazok(580,580,"steny2/1121.png"),
        (1,1,2,2): pygame.loadniObrazok(580,580,"steny2/1122.png"),
        (1,2,0,0): pygame.loadniObrazok(580,580,"steny2/1200.png"),
        (1,2,0,1): pygame.loadniObrazok(580,580,"steny2/1201.png"),
        (1,2,0,2): pygame.loadniObrazok(580,580,"steny2/1202.png"),
        (1,2,1,0): pygame.loadniObrazok(580,580,"steny2/1210.png"),
        (1,2,1,1): pygame.loadniObrazok(580,580,"steny2/1211.png"),
        (1,2,1,2): pygame.loadniObrazok(580,580,"steny2/1212.png"),
        (1,2,2,0): pygame.loadniObrazok(580,580,"steny2/1220.png"),
        (1,2,2,1): pygame.loadniObrazok(580,580,"steny2/1221.png"),
        (1,2,2,2): pygame.loadniObrazok(580,580,"steny2/1222.png"),
        (2,0,0,0): pygame.loadniObrazok(580,580,"steny2/2000.png"),
        (2,0,0,1): pygame.loadniObrazok(580,580,"steny2/2001.png"),
        (2,0,0,2): pygame.loadniObrazok(580,580,"steny2/2002.png"),
        (2,0,1,0): pygame.loadniObrazok(580,580,"steny2/2010.png"),
        (2,0,1,1): pygame.loadniObrazok(580,580,"steny2/2011.png"),
        (2,0,1,2): pygame.loadniObrazok(580,580,"steny2/2012.png"),
        (2,0,2,0): pygame.loadniObrazok(580,580,"steny2/2020.png"),
        (2,0,2,1): pygame.loadniObrazok(580,580,"steny2/2021.png"),
        (2,0,2,2): pygame.loadniObrazok(580,580,"steny2/2022.png"),
        (2,1,0,0): pygame.loadniObrazok(580,580,"steny2/2100.png"),
        (2,1,0,1): pygame.loadniObrazok(580,580,"steny2/2101.png"),
        (2,1,0,2): pygame.loadniObrazok(580,580,"steny2/2102.png"),
        (2,1,1,0): pygame.loadniObrazok(580,580,"steny2/2110.png"),
        (2,1,1,1): pygame.loadniObrazok(580,580,"steny2/2111.png"),
        (2,1,1,2): pygame.loadniObrazok(580,580,"steny2/2112.png"),
        (2,1,2,0): pygame.loadniObrazok(580,580,"steny2/2120.png"),
        (2,1,2,1): pygame.loadniObrazok(580,580,"steny2/2121.png"),
        (2,1,2,2): pygame.loadniObrazok(580,580,"steny2/2122.png"),
        (2,2,0,0): pygame.loadniObrazok(580,580,"steny2/2200.png"),
        (2,2,0,1): pygame.loadniObrazok(580,580,"steny2/2201.png"),
        (2,2,0,2): pygame.loadniObrazok(580,580,"steny2/2202.png"),
        (2,2,1,0): pygame.loadniObrazok(580,580,"steny2/2210.png"),
        (2,2,1,1): pygame.loadniObrazok(580,580,"steny2/2211.png"),
        (2,2,1,2): pygame.loadniObrazok(580,580,"steny2/2212.png"),
        (2,2,2,0): pygame.loadniObrazok(580,580,"steny2/2220.png"),
        (2,2,2,1): pygame.loadniObrazok(580,580,"steny2/2221.png"),
        (2,2,2,2): pygame.loadniObrazok(580,580,"steny2/2222.png"),
    },
    {
        (0,0,0,0): pygame.loadniObrazok(580,580,"steny3/0000.png"),
        (0,0,0,1): pygame.loadniObrazok(580,580,"steny3/0001.png"),
        (0,0,0,2): pygame.loadniObrazok(580,580,"steny3/0002.png"),
        (0,0,1,0): pygame.loadniObrazok(580,580,"steny3/0010.png"),
        (0,0,1,1): pygame.loadniObrazok(580,580,"steny3/0011.png"),
        (0,0,1,2): pygame.loadniObrazok(580,580,"steny3/0012.png"),
        (0,0,2,0): pygame.loadniObrazok(580,580,"steny3/0020.png"),
        (0,0,2,1): pygame.loadniObrazok(580,580,"steny3/0021.png"),
        (0,0,2,2): pygame.loadniObrazok(580,580,"steny3/0022.png"),
        (0,1,0,0): pygame.loadniObrazok(580,580,"steny3/0100.png"),
        (0,1,0,1): pygame.loadniObrazok(580,580,"steny3/0101.png"),
        (0,1,0,2): pygame.loadniObrazok(580,580,"steny3/0102.png"),
        (0,1,1,0): pygame.loadniObrazok(580,580,"steny3/0110.png"),
        (0,1,1,1): pygame.loadniObrazok(580,580,"steny3/0111.png"),
        (0,1,1,2): pygame.loadniObrazok(580,580,"steny3/0112.png"),
        (0,1,2,0): pygame.loadniObrazok(580,580,"steny3/0120.png"),
        (0,1,2,1): pygame.loadniObrazok(580,580,"steny3/0121.png"),
        (0,1,2,2): pygame.loadniObrazok(580,580,"steny3/0122.png"),
        (0,2,0,0): pygame.loadniObrazok(580,580,"steny3/0200.png"),
        (0,2,0,1): pygame.loadniObrazok(580,580,"steny3/0201.png"),
        (0,2,0,2): pygame.loadniObrazok(580,580,"steny3/0202.png"),
        (0,2,1,0): pygame.loadniObrazok(580,580,"steny3/0210.png"),
        (0,2,1,1): pygame.loadniObrazok(580,580,"steny3/0211.png"),
        (0,2,1,2): pygame.loadniObrazok(580,580,"steny3/0212.png"),
        (0,2,2,0): pygame.loadniObrazok(580,580,"steny3/0220.png"),
        (0,2,2,1): pygame.loadniObrazok(580,580,"steny3/0221.png"),
        (0,2,2,2): pygame.loadniObrazok(580,580,"steny3/0222.png"),
        (1,0,0,0): pygame.loadniObrazok(580,580,"steny3/1000.png"),
        (1,0,0,1): pygame.loadniObrazok(580,580,"steny3/1001.png"),
        (1,0,0,2): pygame.loadniObrazok(580,580,"steny3/1002.png"),
        (1,0,1,0): pygame.loadniObrazok(580,580,"steny3/1010.png"),
        (1,0,1,1): pygame.loadniObrazok(580,580,"steny3/1011.png"),
        (1,0,1,2): pygame.loadniObrazok(580,580,"steny3/1012.png"),
        (1,0,2,0): pygame.loadniObrazok(580,580,"steny3/1020.png"),
        (1,0,2,1): pygame.loadniObrazok(580,580,"steny3/1021.png"),
        (1,0,2,2): pygame.loadniObrazok(580,580,"steny3/1022.png"),
        (1,1,0,0): pygame.loadniObrazok(580,580,"steny3/1100.png"),
        (1,1,0,1): pygame.loadniObrazok(580,580,"steny3/1101.png"),
        (1,1,0,2): pygame.loadniObrazok(580,580,"steny3/1102.png"),
        (1,1,1,0): pygame.loadniObrazok(580,580,"steny3/1110.png"),
        (1,1,1,1): pygame.loadniObrazok(580,580,"steny3/1111.png"),
        (1,1,1,2): pygame.loadniObrazok(580,580,"steny3/1112.png"),
        (1,1,2,0): pygame.loadniObrazok(580,580,"steny3/1120.png"),
        (1,1,2,1): pygame.loadniObrazok(580,580,"steny3/1121.png"),
        (1,1,2,2): pygame.loadniObrazok(580,580,"steny3/1122.png"),
        (1,2,0,0): pygame.loadniObrazok(580,580,"steny3/1200.png"),
        (1,2,0,1): pygame.loadniObrazok(580,580,"steny3/1201.png"),
        (1,2,0,2): pygame.loadniObrazok(580,580,"steny3/1202.png"),
        (1,2,1,0): pygame.loadniObrazok(580,580,"steny3/1210.png"),
        (1,2,1,1): pygame.loadniObrazok(580,580,"steny3/1211.png"),
        (1,2,1,2): pygame.loadniObrazok(580,580,"steny3/1212.png"),
        (1,2,2,0): pygame.loadniObrazok(580,580,"steny3/1220.png"),
        (1,2,2,1): pygame.loadniObrazok(580,580,"steny3/1221.png"),
        (1,2,2,2): pygame.loadniObrazok(580,580,"steny3/1222.png"),
        (2,0,0,0): pygame.loadniObrazok(580,580,"steny3/2000.png"),
        (2,0,0,1): pygame.loadniObrazok(580,580,"steny3/2001.png"),
        (2,0,0,2): pygame.loadniObrazok(580,580,"steny3/2002.png"),
        (2,0,1,0): pygame.loadniObrazok(580,580,"steny3/2010.png"),
        (2,0,1,1): pygame.loadniObrazok(580,580,"steny3/2011.png"),
        (2,0,1,2): pygame.loadniObrazok(580,580,"steny3/2012.png"),
        (2,0,2,0): pygame.loadniObrazok(580,580,"steny3/2020.png"),
        (2,0,2,1): pygame.loadniObrazok(580,580,"steny3/2021.png"),
        (2,0,2,2): pygame.loadniObrazok(580,580,"steny3/2022.png"),
        (2,1,0,0): pygame.loadniObrazok(580,580,"steny3/2100.png"),
        (2,1,0,1): pygame.loadniObrazok(580,580,"steny3/2101.png"),
        (2,1,0,2): pygame.loadniObrazok(580,580,"steny3/2102.png"),
        (2,1,1,0): pygame.loadniObrazok(580,580,"steny3/2110.png"),
        (2,1,1,1): pygame.loadniObrazok(580,580,"steny3/2111.png"),
        (2,1,1,2): pygame.loadniObrazok(580,580,"steny3/2112.png"),
        (2,1,2,0): pygame.loadniObrazok(580,580,"steny3/2120.png"),
        (2,1,2,1): pygame.loadniObrazok(580,580,"steny3/2121.png"),
        (2,1,2,2): pygame.loadniObrazok(580,580,"steny3/2122.png"),
        (2,2,0,0): pygame.loadniObrazok(580,580,"steny3/2200.png"),
        (2,2,0,1): pygame.loadniObrazok(580,580,"steny3/2201.png"),
        (2,2,0,2): pygame.loadniObrazok(580,580,"steny3/2202.png"),
        (2,2,1,0): pygame.loadniObrazok(580,580,"steny3/2210.png"),
        (2,2,1,1): pygame.loadniObrazok(580,580,"steny3/2211.png"),
        (2,2,1,2): pygame.loadniObrazok(580,580,"steny3/2212.png"),
        (2,2,2,0): pygame.loadniObrazok(580,580,"steny3/2220.png"),
        (2,2,2,1): pygame.loadniObrazok(580,580,"steny3/2221.png"),
        (2,2,2,2): pygame.loadniObrazok(580,580,"steny3/2222.png"),
    }
    ]
    
    vyhra = pygame.loadniObrazok(-1,-1,'vyhra.png')
    prehra = pygame.loadniObrazok(-1,-1,'prehra.png')

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
    levelyN = [
        pygame.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo1.png'),
        pygame.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo2.png'),
        pygame.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo3.png'),
        pygame.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo4.png'),
        pygame.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo5.png'),
        pygame.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo6.png'),
        pygame.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo7.png'),
        pygame.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo8.png'),
        pygame.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo9.png'),
        pygame.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo10.png'),
        pygame.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo11.png'),
        pygame.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo12.png'),
        pygame.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo13.png'),
        pygame.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo14.png'),
        pygame.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo15.png')
    ]

    levelyA = []
    for i in levelyN:
        levelyA.append(pygame.tlacidloA(i))


class A:
    animacia = pygame.loadniAnimaciu(1000,800,path_foldera='animciaNemasDostPenazi')

class Z:
    test = pygame.loadniZvuk('maybe-next-time-huh.wav')#zvuk.play
    testMuzika = pygame.loadniZvuk('muzika.wav')#existuje zvuk.set_volume() od 0 do 1

o = O()
t = T()
a = A()
z = Z()