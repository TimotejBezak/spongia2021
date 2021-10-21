import time

casPauz = 0

def pause():
    global casPauz,casPauzy
    casPauzy = time.time()

def unpause():
    global casPauz,casPauzy
    casPauz += (time.time() - casPauzy)#tak dlho trvala pauza

def cas():
    return time.time() - casPauz