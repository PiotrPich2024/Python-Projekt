from game.particles.snow import Snow
from random import randint

class SnowGenerator:
    def __init__(self,map_w,map_h):
        self.snow_arr = []
        self.map_w = map_w
        self.map_h = map_h

    def generate_one(self):
        pos = (randint(0,self.map_w),5)
        h = randint(6,12)
        w = h
        vel = randint(1,5)
        d = (randint(1,5),randint(1,5))
        snow_particle = Snow(pos,h,w,d,vel)
        return snow_particle

    def render(self,surf):
        self.snow_arr.append(self.generate_one())
        w,h = surf.get_width(),surf.get_height()

        for particle in self.snow_arr:
            particle.render(surf)
            if w < particle.pos[0] < 0 or h < particle.pos[1] < 0:
                self.snow_arr.remove(particle)



