import niepygame as p
#from niepygame import pygamee
import konstanty as k
import pygame

class O:
    def __init__(self):
        # testObrazok = p.loadniObrazok(200,100)
        # testObrazok2 = p.loadniObrazok(1500,1000)
        # auto = p.loadniObrazok(200,120,path='testauto2.png')
        # pozadie = p.loadniObrazok(1700,800,'pozadie.png')
        self.pixel = p.loadniObrazok(1,1,'pixel.png')
        # test1 = p.loadniObrazok(-1,-1,'test1.png')
        # test2 = p.loadniObrazok(-1,-1,'test4.png')
        # test3 = p.loadniObrazok(-1,-1,'test5.png')
        # ostryobrazok = p.loadniObrazok(-1,-1,'ostryobrazok.jpg')
        self.mys = p.loadniObrazok(50,50,'prst.png')
        # stena = p.loadniObrazok(580,580,'stena.png',bielaNaTransparent=True)
        self.panak = p.loadniObrazok(-1,-1,'panak.png')

        self.level1Panak = p.loadniObrazok(150,150,'easy.png')
        self.level1Pozadie = p.loadniObrazok(1150,250)
        self.level2Panak = p.loadniObrazok(150,150,'medium.png')
        self.level2Pozadie = p.loadniObrazok(1150,250)
        self.level3Panak = p.loadniObrazok(150,150,'hard.png')
        self.level3Pozadie = p.loadniObrazok(1150,250)
        self.zamok = p.loadniObrazok(-1,-1,"zamok/1.png")

        # kruh50 = p.loadniObrazok(100,100,'kruh.png')
        # kruh5 = p.loadniObrazok(10,10,'kruh.png')

        self.pozadieKlavesu = p.loadniObrazok(110,110,'klaves.png')

        self.pravaRuka = p.loadniAnimaciu(-1,-1,'prava ruka',polotransparent=False)
        self.lavaRuka = p.loadniAnimaciu(-1,-1,'lava ruka',polotransparent=False)
        self.pravaNoha = p.loadniAnimaciu(-1,-1,'prava noha',polotransparent=False)
        self.lavaNoha = p.loadniAnimaciu(-1,-1,'lava noha',polotransparent=False)
        self.vajce = p.loadniObrazok(-1,-1,'vajce.png',polotransparent=False)
        #region
        # pygame.image.save(pravaRuka[0],'prava ruka/1.png')
        # pygame.image.save(pravaRuka[1],'prava ruka/2.png')
        # pygame.image.save(pravaRuka[2],'prava ruka/3.png')

        # pygame.image.save(lavaRuka[0],'lava ruka/1.png')
        # pygame.image.save(lavaRuka[1],'lava ruka/2.png')
        # pygame.image.save(lavaRuka[2],'lava ruka/3.png')

        # pygame.image.save(pravaNoha[0],'prava noha/1.png')
        # pygame.image.save(pravaNoha[1],'prava noha/2.png')
        # pygame.image.save(pravaNoha[2],'prava noha/3.png')

        # pygame.image.save(lavaNoha[0],'lava noha/1.png')
        # pygame.image.save(lavaNoha[1],'lava noha/2.png')
        # pygame.image.save(lavaNoha[2],'lava noha/3.png')
        # pygame.image.save(vajce,'vajce.png')
        # endregion


        self.jama = p.loadniObrazok(580,580,'hmla.png')
        self.panvica = p.loadniObrazok(-1,-1,'panvica.png')

        self.stena1 = p.loadniObrazok(580,580)
        self.stena2 = p.loadniObrazok(580,580)
        self.stena3 = p.loadniObrazok(580,580)

        self.steny = [{
            (0,0,0,0): p.loadniObrazok(580,580,"steny1/0000.png"),
            (0,0,0,1): p.loadniObrazok(580,580,"steny1/0001.png"),
            (0,0,0,2): p.loadniObrazok(580,580,"steny1/0002.png"),
            (0,0,1,0): p.loadniObrazok(580,580,"steny1/0010.png"),
            (0,0,1,1): p.loadniObrazok(580,580,"steny1/0011.png"),
            (0,0,1,2): p.loadniObrazok(580,580,"steny1/0012.png"),
            (0,0,2,0): p.loadniObrazok(580,580,"steny1/0020.png"),
            (0,0,2,1): p.loadniObrazok(580,580,"steny1/0021.png"),
            (0,0,2,2): p.loadniObrazok(580,580,"steny1/0022.png"),
            (0,1,0,0): p.loadniObrazok(580,580,"steny1/0100.png"),
            (0,1,0,1): p.loadniObrazok(580,580,"steny1/0101.png"),
            (0,1,0,2): p.loadniObrazok(580,580,"steny1/0102.png"),
            (0,1,1,0): p.loadniObrazok(580,580,"steny1/0110.png"),
            (0,1,1,1): p.loadniObrazok(580,580,"steny1/0111.png"),
            (0,1,1,2): p.loadniObrazok(580,580,"steny1/0112.png"),
            (0,1,2,0): p.loadniObrazok(580,580,"steny1/0120.png"),
            (0,1,2,1): p.loadniObrazok(580,580,"steny1/0121.png"),
            (0,1,2,2): p.loadniObrazok(580,580,"steny1/0122.png"),
            (0,2,0,0): p.loadniObrazok(580,580,"steny1/0200.png"),
            (0,2,0,1): p.loadniObrazok(580,580,"steny1/0201.png"),
            (0,2,0,2): p.loadniObrazok(580,580,"steny1/0202.png"),
            (0,2,1,0): p.loadniObrazok(580,580,"steny1/0210.png"),
            (0,2,1,1): p.loadniObrazok(580,580,"steny1/0211.png"),
            (0,2,1,2): p.loadniObrazok(580,580,"steny1/0212.png"),
            (0,2,2,0): p.loadniObrazok(580,580,"steny1/0220.png"),
            (0,2,2,1): p.loadniObrazok(580,580,"steny1/0221.png"),
            (0,2,2,2): p.loadniObrazok(580,580,"steny1/0222.png"),
            (1,0,0,0): p.loadniObrazok(580,580,"steny1/1000.png"),
            (1,0,0,1): p.loadniObrazok(580,580,"steny1/1001.png"),
            (1,0,0,2): p.loadniObrazok(580,580,"steny1/1002.png"),
            (1,0,1,0): p.loadniObrazok(580,580,"steny1/1010.png"),
            (1,0,1,1): p.loadniObrazok(580,580,"steny1/1011.png"),
            (1,0,1,2): p.loadniObrazok(580,580,"steny1/1012.png"),
            (1,0,2,0): p.loadniObrazok(580,580,"steny1/1020.png"),
            (1,0,2,1): p.loadniObrazok(580,580,"steny1/1021.png"),
            (1,0,2,2): p.loadniObrazok(580,580,"steny1/1022.png"),
            (1,1,0,0): p.loadniObrazok(580,580,"steny1/1100.png"),
            (1,1,0,1): p.loadniObrazok(580,580,"steny1/1101.png"),
            (1,1,0,2): p.loadniObrazok(580,580,"steny1/1102.png"),
            (1,1,1,0): p.loadniObrazok(580,580,"steny1/1110.png"),
            (1,1,1,1): p.loadniObrazok(580,580,"steny1/1111.png"),
            (1,1,1,2): p.loadniObrazok(580,580,"steny1/1112.png"),
            (1,1,2,0): p.loadniObrazok(580,580,"steny1/1120.png"),
            (1,1,2,1): p.loadniObrazok(580,580,"steny1/1121.png"),
            (1,1,2,2): p.loadniObrazok(580,580,"steny1/1122.png"),
            (1,2,0,0): p.loadniObrazok(580,580,"steny1/1200.png"),
            (1,2,0,1): p.loadniObrazok(580,580,"steny1/1201.png"),
            (1,2,0,2): p.loadniObrazok(580,580,"steny1/1202.png"),
            (1,2,1,0): p.loadniObrazok(580,580,"steny1/1210.png"),
            (1,2,1,1): p.loadniObrazok(580,580,"steny1/1211.png"),
            (1,2,1,2): p.loadniObrazok(580,580,"steny1/1212.png"),
            (1,2,2,0): p.loadniObrazok(580,580,"steny1/1220.png"),
            (1,2,2,1): p.loadniObrazok(580,580,"steny1/1221.png"),
            (1,2,2,2): p.loadniObrazok(580,580,"steny1/1222.png"),
            (2,0,0,0): p.loadniObrazok(580,580,"steny1/2000.png"),
            (2,0,0,1): p.loadniObrazok(580,580,"steny1/2001.png"),
            (2,0,0,2): p.loadniObrazok(580,580,"steny1/2002.png"),
            (2,0,1,0): p.loadniObrazok(580,580,"steny1/2010.png"),
            (2,0,1,1): p.loadniObrazok(580,580,"steny1/2011.png"),
            (2,0,1,2): p.loadniObrazok(580,580,"steny1/2012.png"),
            (2,0,2,0): p.loadniObrazok(580,580,"steny1/2020.png"),
            (2,0,2,1): p.loadniObrazok(580,580,"steny1/2021.png"),
            (2,0,2,2): p.loadniObrazok(580,580,"steny1/2022.png"),
            (2,1,0,0): p.loadniObrazok(580,580,"steny1/2100.png"),
            (2,1,0,1): p.loadniObrazok(580,580,"steny1/2101.png"),
            (2,1,0,2): p.loadniObrazok(580,580,"steny1/2102.png"),
            (2,1,1,0): p.loadniObrazok(580,580,"steny1/2110.png"),
            (2,1,1,1): p.loadniObrazok(580,580,"steny1/2111.png"),
            (2,1,1,2): p.loadniObrazok(580,580,"steny1/2112.png"),
            (2,1,2,0): p.loadniObrazok(580,580,"steny1/2120.png"),
            (2,1,2,1): p.loadniObrazok(580,580,"steny1/2121.png"),
            (2,1,2,2): p.loadniObrazok(580,580,"steny1/2122.png"),
            (2,2,0,0): p.loadniObrazok(580,580,"steny1/2200.png"),
            (2,2,0,1): p.loadniObrazok(580,580,"steny1/2201.png"),
            (2,2,0,2): p.loadniObrazok(580,580,"steny1/2202.png"),
            (2,2,1,0): p.loadniObrazok(580,580,"steny1/2210.png"),
            (2,2,1,1): p.loadniObrazok(580,580,"steny1/2211.png"),
            (2,2,1,2): p.loadniObrazok(580,580,"steny1/2212.png"),
            (2,2,2,0): p.loadniObrazok(580,580,"steny1/2220.png"),
            (2,2,2,1): p.loadniObrazok(580,580,"steny1/2221.png"),
            (2,2,2,2): p.loadniObrazok(580,580,"steny1/2222.png"),
        },
        {
            (0,0,0,0): p.loadniObrazok(580,580,"steny2/0000.png"),
            (0,0,0,1): p.loadniObrazok(580,580,"steny2/0001.png"),
            (0,0,0,2): p.loadniObrazok(580,580,"steny2/0002.png"),
            (0,0,1,0): p.loadniObrazok(580,580,"steny2/0010.png"),
            (0,0,1,1): p.loadniObrazok(580,580,"steny2/0011.png"),
            (0,0,1,2): p.loadniObrazok(580,580,"steny2/0012.png"),
            (0,0,2,0): p.loadniObrazok(580,580,"steny2/0020.png"),
            (0,0,2,1): p.loadniObrazok(580,580,"steny2/0021.png"),
            (0,0,2,2): p.loadniObrazok(580,580,"steny2/0022.png"),
            (0,1,0,0): p.loadniObrazok(580,580,"steny2/0100.png"),
            (0,1,0,1): p.loadniObrazok(580,580,"steny2/0101.png"),
            (0,1,0,2): p.loadniObrazok(580,580,"steny2/0102.png"),
            (0,1,1,0): p.loadniObrazok(580,580,"steny2/0110.png"),
            (0,1,1,1): p.loadniObrazok(580,580,"steny2/0111.png"),
            (0,1,1,2): p.loadniObrazok(580,580,"steny2/0112.png"),
            (0,1,2,0): p.loadniObrazok(580,580,"steny2/0120.png"),
            (0,1,2,1): p.loadniObrazok(580,580,"steny2/0121.png"),
            (0,1,2,2): p.loadniObrazok(580,580,"steny2/0122.png"),
            (0,2,0,0): p.loadniObrazok(580,580,"steny2/0200.png"),
            (0,2,0,1): p.loadniObrazok(580,580,"steny2/0201.png"),
            (0,2,0,2): p.loadniObrazok(580,580,"steny2/0202.png"),
            (0,2,1,0): p.loadniObrazok(580,580,"steny2/0210.png"),
            (0,2,1,1): p.loadniObrazok(580,580,"steny2/0211.png"),
            (0,2,1,2): p.loadniObrazok(580,580,"steny2/0212.png"),
            (0,2,2,0): p.loadniObrazok(580,580,"steny2/0220.png"),
            (0,2,2,1): p.loadniObrazok(580,580,"steny2/0221.png"),
            (0,2,2,2): p.loadniObrazok(580,580,"steny2/0222.png"),
            (1,0,0,0): p.loadniObrazok(580,580,"steny2/1000.png"),
            (1,0,0,1): p.loadniObrazok(580,580,"steny2/1001.png"),
            (1,0,0,2): p.loadniObrazok(580,580,"steny2/1002.png"),
            (1,0,1,0): p.loadniObrazok(580,580,"steny2/1010.png"),
            (1,0,1,1): p.loadniObrazok(580,580,"steny2/1011.png"),
            (1,0,1,2): p.loadniObrazok(580,580,"steny2/1012.png"),
            (1,0,2,0): p.loadniObrazok(580,580,"steny2/1020.png"),
            (1,0,2,1): p.loadniObrazok(580,580,"steny2/1021.png"),
            (1,0,2,2): p.loadniObrazok(580,580,"steny2/1022.png"),
            (1,1,0,0): p.loadniObrazok(580,580,"steny2/1100.png"),
            (1,1,0,1): p.loadniObrazok(580,580,"steny2/1101.png"),
            (1,1,0,2): p.loadniObrazok(580,580,"steny2/1102.png"),
            (1,1,1,0): p.loadniObrazok(580,580,"steny2/1110.png"),
            (1,1,1,1): p.loadniObrazok(580,580,"steny2/1111.png"),
            (1,1,1,2): p.loadniObrazok(580,580,"steny2/1112.png"),
            (1,1,2,0): p.loadniObrazok(580,580,"steny2/1120.png"),
            (1,1,2,1): p.loadniObrazok(580,580,"steny2/1121.png"),
            (1,1,2,2): p.loadniObrazok(580,580,"steny2/1122.png"),
            (1,2,0,0): p.loadniObrazok(580,580,"steny2/1200.png"),
            (1,2,0,1): p.loadniObrazok(580,580,"steny2/1201.png"),
            (1,2,0,2): p.loadniObrazok(580,580,"steny2/1202.png"),
            (1,2,1,0): p.loadniObrazok(580,580,"steny2/1210.png"),
            (1,2,1,1): p.loadniObrazok(580,580,"steny2/1211.png"),
            (1,2,1,2): p.loadniObrazok(580,580,"steny2/1212.png"),
            (1,2,2,0): p.loadniObrazok(580,580,"steny2/1220.png"),
            (1,2,2,1): p.loadniObrazok(580,580,"steny2/1221.png"),
            (1,2,2,2): p.loadniObrazok(580,580,"steny2/1222.png"),
            (2,0,0,0): p.loadniObrazok(580,580,"steny2/2000.png"),
            (2,0,0,1): p.loadniObrazok(580,580,"steny2/2001.png"),
            (2,0,0,2): p.loadniObrazok(580,580,"steny2/2002.png"),
            (2,0,1,0): p.loadniObrazok(580,580,"steny2/2010.png"),
            (2,0,1,1): p.loadniObrazok(580,580,"steny2/2011.png"),
            (2,0,1,2): p.loadniObrazok(580,580,"steny2/2012.png"),
            (2,0,2,0): p.loadniObrazok(580,580,"steny2/2020.png"),
            (2,0,2,1): p.loadniObrazok(580,580,"steny2/2021.png"),
            (2,0,2,2): p.loadniObrazok(580,580,"steny2/2022.png"),
            (2,1,0,0): p.loadniObrazok(580,580,"steny2/2100.png"),
            (2,1,0,1): p.loadniObrazok(580,580,"steny2/2101.png"),
            (2,1,0,2): p.loadniObrazok(580,580,"steny2/2102.png"),
            (2,1,1,0): p.loadniObrazok(580,580,"steny2/2110.png"),
            (2,1,1,1): p.loadniObrazok(580,580,"steny2/2111.png"),
            (2,1,1,2): p.loadniObrazok(580,580,"steny2/2112.png"),
            (2,1,2,0): p.loadniObrazok(580,580,"steny2/2120.png"),
            (2,1,2,1): p.loadniObrazok(580,580,"steny2/2121.png"),
            (2,1,2,2): p.loadniObrazok(580,580,"steny2/2122.png"),
            (2,2,0,0): p.loadniObrazok(580,580,"steny2/2200.png"),
            (2,2,0,1): p.loadniObrazok(580,580,"steny2/2201.png"),
            (2,2,0,2): p.loadniObrazok(580,580,"steny2/2202.png"),
            (2,2,1,0): p.loadniObrazok(580,580,"steny2/2210.png"),
            (2,2,1,1): p.loadniObrazok(580,580,"steny2/2211.png"),
            (2,2,1,2): p.loadniObrazok(580,580,"steny2/2212.png"),
            (2,2,2,0): p.loadniObrazok(580,580,"steny2/2220.png"),
            (2,2,2,1): p.loadniObrazok(580,580,"steny2/2221.png"),
            (2,2,2,2): p.loadniObrazok(580,580,"steny2/2222.png"),
        },
        {
            (0,0,0,0): p.loadniObrazok(580,580,"steny3/0000.png"),
            (0,0,0,1): p.loadniObrazok(580,580,"steny3/0001.png"),
            (0,0,0,2): p.loadniObrazok(580,580,"steny3/0002.png"),
            (0,0,1,0): p.loadniObrazok(580,580,"steny3/0010.png"),
            (0,0,1,1): p.loadniObrazok(580,580,"steny3/0011.png"),
            (0,0,1,2): p.loadniObrazok(580,580,"steny3/0012.png"),
            (0,0,2,0): p.loadniObrazok(580,580,"steny3/0020.png"),
            (0,0,2,1): p.loadniObrazok(580,580,"steny3/0021.png"),
            (0,0,2,2): p.loadniObrazok(580,580,"steny3/0022.png"),
            (0,1,0,0): p.loadniObrazok(580,580,"steny3/0100.png"),
            (0,1,0,1): p.loadniObrazok(580,580,"steny3/0101.png"),
            (0,1,0,2): p.loadniObrazok(580,580,"steny3/0102.png"),
            (0,1,1,0): p.loadniObrazok(580,580,"steny3/0110.png"),
            (0,1,1,1): p.loadniObrazok(580,580,"steny3/0111.png"),
            (0,1,1,2): p.loadniObrazok(580,580,"steny3/0112.png"),
            (0,1,2,0): p.loadniObrazok(580,580,"steny3/0120.png"),
            (0,1,2,1): p.loadniObrazok(580,580,"steny3/0121.png"),
            (0,1,2,2): p.loadniObrazok(580,580,"steny3/0122.png"),
            (0,2,0,0): p.loadniObrazok(580,580,"steny3/0200.png"),
            (0,2,0,1): p.loadniObrazok(580,580,"steny3/0201.png"),
            (0,2,0,2): p.loadniObrazok(580,580,"steny3/0202.png"),
            (0,2,1,0): p.loadniObrazok(580,580,"steny3/0210.png"),
            (0,2,1,1): p.loadniObrazok(580,580,"steny3/0211.png"),
            (0,2,1,2): p.loadniObrazok(580,580,"steny3/0212.png"),
            (0,2,2,0): p.loadniObrazok(580,580,"steny3/0220.png"),
            (0,2,2,1): p.loadniObrazok(580,580,"steny3/0221.png"),
            (0,2,2,2): p.loadniObrazok(580,580,"steny3/0222.png"),
            (1,0,0,0): p.loadniObrazok(580,580,"steny3/1000.png"),
            (1,0,0,1): p.loadniObrazok(580,580,"steny3/1001.png"),
            (1,0,0,2): p.loadniObrazok(580,580,"steny3/1002.png"),
            (1,0,1,0): p.loadniObrazok(580,580,"steny3/1010.png"),
            (1,0,1,1): p.loadniObrazok(580,580,"steny3/1011.png"),
            (1,0,1,2): p.loadniObrazok(580,580,"steny3/1012.png"),
            (1,0,2,0): p.loadniObrazok(580,580,"steny3/1020.png"),
            (1,0,2,1): p.loadniObrazok(580,580,"steny3/1021.png"),
            (1,0,2,2): p.loadniObrazok(580,580,"steny3/1022.png"),
            (1,1,0,0): p.loadniObrazok(580,580,"steny3/1100.png"),
            (1,1,0,1): p.loadniObrazok(580,580,"steny3/1101.png"),
            (1,1,0,2): p.loadniObrazok(580,580,"steny3/1102.png"),
            (1,1,1,0): p.loadniObrazok(580,580,"steny3/1110.png"),
            (1,1,1,1): p.loadniObrazok(580,580,"steny3/1111.png"),
            (1,1,1,2): p.loadniObrazok(580,580,"steny3/1112.png"),
            (1,1,2,0): p.loadniObrazok(580,580,"steny3/1120.png"),
            (1,1,2,1): p.loadniObrazok(580,580,"steny3/1121.png"),
            (1,1,2,2): p.loadniObrazok(580,580,"steny3/1122.png"),
            (1,2,0,0): p.loadniObrazok(580,580,"steny3/1200.png"),
            (1,2,0,1): p.loadniObrazok(580,580,"steny3/1201.png"),
            (1,2,0,2): p.loadniObrazok(580,580,"steny3/1202.png"),
            (1,2,1,0): p.loadniObrazok(580,580,"steny3/1210.png"),
            (1,2,1,1): p.loadniObrazok(580,580,"steny3/1211.png"),
            (1,2,1,2): p.loadniObrazok(580,580,"steny3/1212.png"),
            (1,2,2,0): p.loadniObrazok(580,580,"steny3/1220.png"),
            (1,2,2,1): p.loadniObrazok(580,580,"steny3/1221.png"),
            (1,2,2,2): p.loadniObrazok(580,580,"steny3/1222.png"),
            (2,0,0,0): p.loadniObrazok(580,580,"steny3/2000.png"),
            (2,0,0,1): p.loadniObrazok(580,580,"steny3/2001.png"),
            (2,0,0,2): p.loadniObrazok(580,580,"steny3/2002.png"),
            (2,0,1,0): p.loadniObrazok(580,580,"steny3/2010.png"),
            (2,0,1,1): p.loadniObrazok(580,580,"steny3/2011.png"),
            (2,0,1,2): p.loadniObrazok(580,580,"steny3/2012.png"),
            (2,0,2,0): p.loadniObrazok(580,580,"steny3/2020.png"),
            (2,0,2,1): p.loadniObrazok(580,580,"steny3/2021.png"),
            (2,0,2,2): p.loadniObrazok(580,580,"steny3/2022.png"),
            (2,1,0,0): p.loadniObrazok(580,580,"steny3/2100.png"),
            (2,1,0,1): p.loadniObrazok(580,580,"steny3/2101.png"),
            (2,1,0,2): p.loadniObrazok(580,580,"steny3/2102.png"),
            (2,1,1,0): p.loadniObrazok(580,580,"steny3/2110.png"),
            (2,1,1,1): p.loadniObrazok(580,580,"steny3/2111.png"),
            (2,1,1,2): p.loadniObrazok(580,580,"steny3/2112.png"),
            (2,1,2,0): p.loadniObrazok(580,580,"steny3/2120.png"),
            (2,1,2,1): p.loadniObrazok(580,580,"steny3/2121.png"),
            (2,1,2,2): p.loadniObrazok(580,580,"steny3/2122.png"),
            (2,2,0,0): p.loadniObrazok(580,580,"steny3/2200.png"),
            (2,2,0,1): p.loadniObrazok(580,580,"steny3/2201.png"),
            (2,2,0,2): p.loadniObrazok(580,580,"steny3/2202.png"),
            (2,2,1,0): p.loadniObrazok(580,580,"steny3/2210.png"),
            (2,2,1,1): p.loadniObrazok(580,580,"steny3/2211.png"),
            (2,2,1,2): p.loadniObrazok(580,580,"steny3/2212.png"),
            (2,2,2,0): p.loadniObrazok(580,580,"steny3/2220.png"),
            (2,2,2,1): p.loadniObrazok(580,580,"steny3/2221.png"),
            (2,2,2,2): p.loadniObrazok(580,580,"steny3/2222.png"),
        }
        ]

        self.vyhra = p.loadniObrazok(-1,-1,'vyhra.png')
        self.prehra = p.loadniObrazok(-1,-1,'prehra.png')
        self.oblakypozadie = p.loadniObrazok(-1,-1,'oblakypozadie.png')
        self.pozadieLevel = p.loadniObrazok(-1,-1,'pozadieLevel.png')

        self.bar1 = p.loadniObrazok(1500,10)
        self.bar2 = pygame.prefarb(p.loadniObrazok(10,10),(0,255,0))

        self.vtipy = p.loadniAnimaciu(-1,-1,'vtipy')


class T:
    def __init__(self):
        self.hratN = p.loadniObrazok(-1,-1,'hrat.png')
        self.hratA = p.tlacidloA(self.hratN)
        self.restartVyhralsiN = p.loadniObrazok(-1,-1,'restartV.png')
        self.restartVyhralsiA = p.tlacidloA(self.restartVyhralsiN)
        self.restartPrehralsiN = p.loadniObrazok(-1,-1,'restartP.png')
        self.restartPrehralsiA = p.tlacidloA(self.restartPrehralsiN)

        # testtlacidloA = p.loadniObrazok(100,100)
        # testtlacidloN = p.loadniObrazok(100,100)
        # vyhralsiA = p.loadniObrazok(100,100)
        # vyhralsiN = p.loadniObrazok(100,100)
        # prehralsiA = p.loadniObrazok(100,100)
        # prehralsiN = p.loadniObrazok(100,100)
        # spetDoMenuA = p.loadniObrazok(100,100)
        # spetDoMenuN = p.loadniObrazok(100,100)
        # pauzaA = p.loadniObrazok(100,100)
        # pauzaN = p.loadniObrazok(100,100)
        # odpauzaA = p.loadniObrazok(100,100)
        # odpauzaN = p.loadniObrazok(100,100)
        self.XN = p.loadniObrazok(25,25,'cervenex.png')
        self.XA = p.tlacidloA(self.XN)
        self.fullscreenN = p.loadniObrazok(25,25)
        self.fullscreenA = p.tlacidloA(self.fullscreenN)

        self.levelyN = [
            p.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo1.png'),
            p.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo2.png'),
            p.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo3.png'),
            p.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo4.png'),
            p.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo5.png'),
            p.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo6.png'),
            p.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo7.png'),
            p.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo8.png'),
            p.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo9.png'),
            p.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo10.png'),
            p.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo11.png'),
            p.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo12.png'),
            p.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo13.png'),
            p.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo14.png'),
            p.loadniObrazok(k.sirkaLevelTlacidla,k.vyskaLevelTlacidla,'tlacidlaLevelov/tlacidlo15.png')
        ]

        self.levelyA = []
        for i in self.levelyN:
            self.levelyA.append(p.tlacidloA(i))


class A:
    def __init__(self):
        self.animacia = p.loadniAnimaciu(1000,800,path_foldera='animciaNemasDostPenazi')
        self.zaciatokLevelu = p.loadniAnimaciu(1700,960,path_foldera='rytmushadzevajce')
        self.rozplastenieNaPanvici = p.loadniAnimaciu(580,580,path_foldera='rozplesknutie')#posledny obrazok mozem potom nakopirovat este zopar krat
        self.zamok = p.loadniAnimaciu(-1,-1,'zamok')
        
        #region koncatiny
        self.pr01 = p.loadniAnimaciu(-1,-1,'pr01')
        self.pr02 = p.loadniAnimaciu(-1,-1,'pr02')
        self.pr12 = p.loadniAnimaciu(-1,-1,'pr12')

        self.lr01 = p.loadniAnimaciu(-1,-1,'lr01')
        self.lr02 = p.loadniAnimaciu(-1,-1,'lr02')
        self.lr12 = p.loadniAnimaciu(-1,-1,'lr12')

        self.pn01 = p.loadniAnimaciu(-1,-1,'pn01')
        self.pn02 = p.loadniAnimaciu(-1,-1,'pn02')
        self.pn12 = p.loadniAnimaciu(-1,-1,'pn12')

        self.ln01 = p.loadniAnimaciu(-1,-1,'ln01')
        self.ln02 = p.loadniAnimaciu(-1,-1,'ln02')
        self.ln12 = p.loadniAnimaciu(-1,-1,'ln12')
        print(self.lr02,"gheiu")
    #endregion

class Z:
    test = p.loadniZvuk('maybe-next-time-huh.wav')#zvuk.play
    testMuzika = p.loadniZvuk('muzika.wav')#existuje zvuk.set_volume() od 0 do 1
    vyhralsi = p.loadniZvuk('vyhralsi.wav')
    prehralsi = p.loadniZvuk('prehralsi.wav')
    dopozadia = p.loadniZvuk('backround music.wav')
    muzikyLevelov = [[
        p.loadniZvuk('muzikyLevelov/1.wav'),
        p.loadniZvuk('muzikyLevelov/2.wav'),
        p.loadniZvuk('muzikyLevelov/3.wav'),
        p.loadniZvuk('muzikyLevelov/4.wav'),
        p.loadniZvuk('muzikyLevelov/5.wav')
    ],
    [
        p.loadniZvuk('muzikyLevelov/6.wav'),
        p.loadniZvuk('muzikyLevelov/7.wav'),
        p.loadniZvuk('muzikyLevelov/8.wav'),
        p.loadniZvuk('muzikyLevelov/9.wav'),
        p.loadniZvuk('muzikyLevelov/10.wav')
    ],
    [
        p.loadniZvuk('muzikyLevelov/11.wav'),
        p.loadniZvuk('muzikyLevelov/12.wav'),
        p.loadniZvuk('muzikyLevelov/13.wav'),
        p.loadniZvuk('muzikyLevelov/14.wav'),
        p.loadniZvuk('muzikyLevelov/15.wav')
    ]
    ]

    klik = p.loadniZvuk('klik.wav')
    rozplaskvajco = p.loadniZvuk('rozplaskvajco.wav')
    pustivajco = p.loadniZvuk('pustivajco.wav')
    odmlevel = p.loadniZvuk('odm level.wav')

o = O()
t = T()
a = A()
z = Z()

def loadniZnovu():
    global o,t,a,z
    o = O()
    t = T()
    a = A()
    # z = Z()