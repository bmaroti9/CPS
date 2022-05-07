import pygame,random
from pygame.locals import *

from helpers import *
from gradient import *

xmax = 1000    #width of window
ymax = 600     #height of window

PARTICLES = pygame.sprite.Group()
MOOD_PHASES = ['peacefull', 'calm', 'angry', 'rage']

class Dust(pygame.sprite.Sprite):
    def __init__(self, startx, starty, col, speed, chance_of_death, rattle):
        pygame.sprite.Sprite.__init__(self)
        self.x = startx
        self.y = starty
        self.col = col
        self.sx = startx
        self.sy = starty
        self.size = random.randint(1, 2)
        self.life = 0

        self.speed = speed
        self.chance_of_death = chance_of_death
        self.rattle = rattle

    def update(self, surface):
        self.life += 1
        if self.y < 0:
            self.kill()
        else:
            self.y-=1

        if random.randint(self.life, self.chance_of_death) == self.chance_of_death:
            self.kill()

        pygame.draw.circle(surface, self.col, (self.x, self.y), self.size)
        self.x+=random.randint(- self.rattle, self.rattle)

def manadge_dust(surface, dust_list):
    global PARTICLES
    
    for p in PARTICLES:
            p.update(surface)

def add_dust(startx, starty, col, speed, chance_of_death, rattle):
    global PARTICLES

    PARTICLES.add(Dust(startx, starty, col, speed, chance_of_death, rattle))

class Dust_monster(pygame.sprite.Sprite):
    def __init__(self, pos, speed, rattle):
        pygame.sprite.Sprite.__init__(self)

        self.particles = pygame.sprite.Group()
        self.chance_of_new = 2
        self.speed = speed
        self.chance_of_death = 200
        self.rattle = rattle
        self.pos = pos
        self.color1 = (200, 100, 100)
        self.color2 = (0, 0, 0)

        self.new_pos = self.pos
        
        self.mood = 0
    
    def update(self, surface):
        changed_pos = [self.pos[0] + sin_pos(10, 750, 0.2)[1], self.pos[1]]
        #pygame.draw.circle(surface, (250, 0, 0), changed_pos, 2)
        
        if [round(self.pos[0]), round(self.pos[1])] != [round(self.new_pos[0]), round(self.new_pos[1])]:
            angle = calculate_angle(self.new_pos, self.pos)
            moving = rotating_position(0, 0.7, angle, [0, 0])
            self.pos = [self.pos[0] + moving[0], self.pos[1] + moving[1]]

        self.think(surface)   
    
        for n in self.particles:
            n.update(surface)
        
        if random.randint(0, self.chance_of_new) == 0:
            color = transition_colors(self.color1, self.color2, random.randint(0, 2) * 0.5)
            self.particles.add(Dust(changed_pos[0], changed_pos[1], color, 
                    self.speed, self.chance_of_death, self.rattle))
    
    def think(self, surface):
        if random.randint(0, 600) == 0:
            a = random.randint(-1, 1) + self.mood
            self.mood = max(min(a, 3), 0)
            if self.mood == 0:
                #calm
                self.color1 = (250, 250, 250)
                self.color2 = (100, 100, 100)
                self.chance_of_new = 3
            elif self.mood == 1:
                #peacefull
                self.color1 = (250, 250, 250)
                self.color2 = (100, 100, 100)
                self.chance_of_death = 150
            elif self.mood == 2:
                #angry
                self.color1 = (250, 100, 100)
                self.color2 = (0, 0, 0)
                self.chance_of_new = 2
            elif self.mood == 3:
                #rage
                self.color1 = (250, 0, 0)
                self.color2 = (0, 0, 0)
                self.chance_of_death = 300
                self.chance_of_new = 1
        
        if random.randint(0, 900) == 0:
            self.new_pos = [random.randint(30, surface.get_width() - 30), 
                    random.randint(surface.get_height() - 120, surface.get_height() - 50)]
            print(self.new_pos)

class Waves(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.group_list = []

    def update(self, surface):
        if random.randint(0, 8) == 0:
            randi = random.randint(0, 5)
            if randi == 0:
                a = [40, random.randint(surface.get_height() - 140, surface.get_height() - 50)]
                self.group_list.append([a, 1])
            elif randi == 1 and False:
                del self.group_list[random.randint(0, len(self.group_list) - 1)]
            elif randi > 1 and len(self.group_list) > 0:
                self.group_list[random.randint(0, len(self.group_list) - 1)][1] += 1
        
        for n in self.group_list:
            n[0][0] += 0.5
            n[0][1] += 0.03
            pos = n[0]
            for w in range(n[1]):
                blit_image(surface, "images/single_wave4.png", [pos[0] - w * 5, pos[1] + w * 3], 0.1)
            
            if pos[0] > surface.get_width():
                del self.group_list[self.group_list.index(n)]



def main():
    pygame.init()
    screen = pygame.display.set_mode((xmax,ymax))
    white = (240, 240, 240)
    black = (0,0,0)
    grey = (128,128,128)
    MONSTER = Dust_monster([200, 550], 1, 1)
    WAVES = Waves()

    whited = []
    for n in range(8):
        a = pygame.Surface([screen.get_width(), 150])
        a.fill((200, 230, 255))
        for n in range(300):
            #a.set_at([random.randint(0, a.get_width()), random.randint(0, a.get_height())], 
                    #(0, 0, 0))
            pygame.draw.rect(a, (255, 255, 255), 
                    [random.randint(0, a.get_width()), random.randint(0, a.get_height()), 4, 2])
        whited.append(a)
    current_ocean = 0

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
            add_dust(515, random.randint(500, 515), col, -1, 200, 1)

        screen.fill(white)

        #pygame.draw.rect(screen, (200, 230, 255), (0, screen.get_height() - 150, 
                #screen.get_width(), screen.get_height()))
        screen.blit(whited[current_ocean], [0, screen.get_height() - 150])

        current_ocean = (pygame.time.get_ticks() // 101) % 8
        
        pygame.draw.line(screen, (150, 150, 150), [0, screen.get_height() - 150], 
                [screen.get_width(), screen.get_height() - 150])
        WAVES.update(screen)

        manadge_dust(screen, PARTICLES)
        MONSTER.update(screen)

        pygame.draw.circle(screen, (250, 250, 250), sin_pos(100, 2000, 1), 2)
        pygame.display.flip()
        clock.tick(50)
    pygame.quit()

if __name__ == "__main__":
    main()