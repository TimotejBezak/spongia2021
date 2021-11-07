#tu budu konstanty
import pygame
sirkaLevelTlacidla = 100
vyskaLevelTlacidla = 100
xStenoDispleja = 580/2+100
yStenoDispleja = 660

sirkaPocitaca = pygame.display.Info().current_w
vyskaPocitaca = pygame.display.Info().current_h

sirkaVajca = 400
vyskaVajca = 450

ls1k = {'x':[0,1,2,1],'l':[1,2,1,1],'g':[0,0,2,2],'y':[1,1,1,2],'i':[2,1,1,2],'e':[1,1,0,1]}
ls2k = {'k':[2,1,2,1],'v':[2,0,0,0],'a':[1,2,2,0],'p':[2,2,0,1],'j':[1,2,0,2],'x':[2,1,1,0],'r':[0,2,2,1]}
ls3k = {'l':[0,0,2,0],'b':[0,2,1,1],'q':[1,1,0,2],'o':[2,0,1,1],'z':[1,0,2,1],'f':[2,0,2,2],'t':[1,2,1,2],'s':[0,1,1,2]}