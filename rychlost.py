import math
import cas

class rychlost:
    def __init__(self,rychlost):
        """pixel za sekundu"""
        self.rychlost = rychlost
        self.cas = cas.cas()

    def vzdialenost(self):
        novyCas = cas.cas()
        dt = novyCas - self.cas
        self.cas = novyCas
        return self.rychlost*dt

class linearnyPohyb:
    def __init__(self,z_pos,k_pos,rychlost):
        """pixel za sekundu"""
        self.z_pos = z_pos
        self.k_pos = k_pos
        self.rychlost = rychlost
        self.cas = cas.cas()
        self.dx, self.dy = k_pos[0]-z_pos[0], k_pos[1]-z_pos[1]
        self.vzdialenost = math.sqrt(abs(self.dx)**2 + abs(self.dy)**2)
        self.x = z_pos[0]
        self.y = z_pos[1]

    def update(self):
        novyCas = cas.cas()
        dt = novyCas - self.cas
        self.cas = novyCas
        ds = self.rychlost*dt
        #print(dt)
        k = self.vzdialenost/ds
        self.x += self.dx/k
        self.y += self.dy/k
        return self.x,self.y
        
    def koniec(self):
        if self.x > self.k_pos[0]:
            return True
        return False