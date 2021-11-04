input = input().split()
casy = []
pismena = []
for i in range(len(input)):
    if i % 2 == 0:#je to cas
        if ':' in input[i]:
            minuty = int(input[i][0])
            cas = float(input[i][2:])
            casy.append(cas+minuty*60)
        else:
            casy.append(float(input[i]))
    else:#je to pismeno
        pismena.append(input[i])

print(casy)
print(pismena)
if len(casy) == len(pismena):
    print("huraaa")
