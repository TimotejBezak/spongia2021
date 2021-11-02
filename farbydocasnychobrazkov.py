import random

farby = []
while True:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    dobre = True
    for i in farby:
        sucetrozdielov = abs(r-i[0])+abs(g-i[1])+abs(b-i[2])
        if sucetrozdielov < 50:
            dobre = False
            break
    if dobre == True:
        farby.append([r,g,b])
    if len(farby) == 150:
        break

print(farby)