import pygame,random
from pygame.locals import *

xmax = 1000    #width of window
ymax = 600     #height of window

PARTICLES = pygame.sprite.Group()

class Dust(pygame.sprite.Sprite):
    def __init__(self, startx, starty, col, speed, chance_of_death, rattle):
        pygame.sprite.Sprite.__init__(self)
        self.x = startx
        self.y = starty
        self.col = col
        self.sx = startx
        self.sy = starty

        self.speed = speed
        self.chance_of_death = chance_of_death
        self.rattle = rattle

    def update(self, surface):
        if self.y < 0:
            self.kill()
        else:
            self.y-=1

        if random.randint(0, self.chance_of_death) == 0:
            self.kill()

        pygame.draw.circle(surface, self.col, (self.x, self.y), 2)
        self.x+=random.randint(- self.rattle, self.rattle)

def manadge_dust(surface, dust_list):
    global PARTICLES
    
    for p in PARTICLES:
            p.update(surface)

def add_dust(startx, starty, col, speed, chance_of_death, rattle):
    global PARTICLES

    PARTICLES.add(Dust(startx, starty, col, speed, chance_of_death, rattle))

class Dust(pygame.sprite.Sprite):
    def __init__(pos, speed, chance_of_death, rattle, chance_of_new):
        pygame.sprite.Sprite.__init__(self)

        self.particles = pygame.sprite.Group()
        self.chance_of_new = chance_of_new
        self.speed = speed
        self.chance_of_death = chance_of_death
        self.rattle = rattle
        self.pos = pos

    
    def update(surface):
        for n in self.particles:
            n.update
        
        if random.randint(0, chanc):
            a
        

def main():
    pygame.init()
    screen = pygame.display.set_mode((xmax,ymax))
    white = (255, 255, 255)
    black = (0,0,0)
    grey = (128,128,128)

    clock=pygame.time.Clock()

    ''''
    for part in range(300):
        if part % 2 > 0: col = black
        else: col = grey
        PARTICLES.add(Dust(515, 500, col))
    '''
    exitflag = False
    while not exitflag:
        for event in pygame.event.get():
            if event.type == QUIT:
                exitflag = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exitflag = True
        
        if random.randint(0, 1) == 0:
            if  random.randint(0, 1) == 0: 
                col = black
            else: 
                col = grey
            #PARTICLES.add(Dust(515, random.randint(500, 515), col, -1, 100, 1))
            add_dust(515, random.randint(500, 515), col, -1, 100, 1)

        screen.fill(white)
        manadge_dust(screen)

        pygame.display.flip()
        clock.tick(50)
    pygame.quit()

if __name__ == "__main__":
    main()
update