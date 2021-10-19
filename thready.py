import threading,time

class myThread (threading.Thread):
   def __init__(self, funkcia):
      threading.Thread.__init__(self)
      self.funkcia = funkcia
   def run(self):
      self.funkcia()


pozicie = [1]

def gameloop():
    global pozicie
    while True:
        pozicie[0] += 1
        time.sleep(0.002)

def zobrazovac():
    global pozicie
    while True:
        print(f"zobrazujem na pozicie {pozicie}")
        time.sleep(0.0001)


t1 = myThread(gameloop)
t2 = myThread(zobrazovac)

t1.start()
t2.start()