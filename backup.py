docasnefarby = [[132, 137, 192], [65, 154, 30], [246, 228, 178], [105, 10, 15], [155, 30, 106], [114, 89, 243], [51, 120, 237], [214, 27, 11], [10, 246, 24], [192, 34, 227], [135, 247, 193], [95, 121, 72], [26, 49, 6], [226, 37, 131], [81, 197, 146], [193, 89, 81], [147, 215, 33], [170, 90, 3], [218, 193, 225], [235, 242, 46], [124, 87, 130], [72, 33, 61], [224, 158, 8], [54, 129, 135], [192, 254, 118], [228, 182, 86], [27, 182, 103], [14, 223, 174], [165, 206, 164], [240, 121, 206], [183, 155, 256], [235, 114, 115], [80, 4, 127], [43, 57, 162], [28, 12, 221], [251, 3, 77], [64, 251, 112], [256, 16, 192], [4, 15, 78], [73, 216, 224], [15, 109, 183], [1, 164, 228], [199, 83, 179], [0, 81, 48], [16, 253, 254], [147, 172, 102], [252, 61, 248], [140, 8, 174], [70, 223, 3], [243, 88, 28]]
ktorafarba = 0
def loadniObrazok(path,sirka,vyska):
    global ktorafarba
    try:
        obrazok = pygame.image.load(path)
    except:
        obrazok = pygame.image.load('docasnyobrazok.png')
        obrazok = prefarb(obrazok,docasnefarby[ktorafarba])
        ktorafarba += 1
    return zmenitRozlisenie(obrazok,(sirka,vyska))

jedenkratjeden = loadniObrazok('jedenkratjeden.png',1,1)