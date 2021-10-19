import pygame
#from niepygame import pygamee

class O:
    testObrazok = pygame.loadniObrazok(200,100)
    testObrazok2 = pygame.loadniObrazok(1500,1000)
    auto = pygame.loadniObrazok(200,120,path='testauto2.png')
    pozadie = pygame.loadniObrazok(1500,800,'pozadie.png')
    pixel = pygame.loadniObrazok(1,1,'pixel.png')
    test1 = pygame.loadniObrazok(-1,-1,'test1.png')
    test2 = pygame.loadniObrazok(-1,-1,'test4.png')
    test3 = pygame.loadniObrazok(-1,-1,'test5.png')
    ostryobrazok = pygame.loadniObrazok(-1,-1,'ostryobrazok.jpg')
    mys = pygame.loadniObrazok(50,50,'mys.png')
    
class T:
    testtlacidloA = pygame.loadniObrazok(100,100)
    testtlacidloN = pygame.loadniObrazok(100,100)
    vyhralsiA = pygame.loadniObrazok(100,100)
    vyhralsiN = pygame.loadniObrazok(100,100)
    prehralsiA = pygame.loadniObrazok(100,100)
    prehralsiN = pygame.loadniObrazok(100,100)

class A:
    animacia = pygame.loadniAnimaciu(1000,800,path_foldera='animciaNemasDostPenazi')

class Z:
    test = pygame.loadniZvuk('maybe-next-time-huh.wav')#zvuk.play
    testMuzika = pygame.loadniZvuk('muzika.wav')#existuje zvuk.set_volume() od 0 do 1

o = O()
t = T()
a = A()
z = Z()