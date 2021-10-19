import random

farby = []
while True:
    r = random.randint(0,256)
    g = random.randint(0,256)
    b = random.randint(0,256)
    dobre = True
    for i in farby:
        sucetrozdielov = abs(r-i[0])+abs(g-i[1])+abs(b-i[2])
        if sucetrozdielov < 150:
            dobre = False
            break
    if dobre == True:
        farby.append([r,g,b])
    if len(farby) == 50:
        break

print(farby)