import sys
import random
import pygame as pg

from helpers import *


def fill(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))
            a = (a[0] + a[1] + a[2]) / 3
            surface.set_at((x, y), (round(r + a), round(g + a), round(b + a)))
    
    return surface

def replacecolor(image, color1, color2):
    pixels = PixelArray(image)
    pixels.replace(Color(255, 255, 255, 255), Color(0, 0, 255, 255))
    return pixels

def swap_color(surf, from_, to_):
    arr = pygame.PixelArray(surf)
    from_ = tuple(from_)
    to_ = tuple(to_)

    arr.replace(from_,to_)
    huhu = arr.surface
    return huhu


def flash_up_image(image, color1, color2, operataion, initioal_look_time, up_scale, down_scale):
    if operataion <= up_scale:
        percent_now = operataion / up_scale
    elif operataion <= initioal_look_time:
        percent_now = 1
    elif operataion <= down_scale:
        percent_now = (operataion - up_scale - initioal_look_time) / -1
    else:
        percent_now = 0
    
    print(percent_now, operataion)

    #image = fill(image, transition_colors(color2, color1, percent_now))
    #replacecolor(image, color1, color2)
    print(transition_colors(color2, color1, percent_now))
    hihi = swap_color(image, (0, 0, 0), transition_colors(color2, color1, percent_now))

    return hihi

class Particle(pygame.sprite.Sprite):
    def __init__(self, starting_pos, color, target, circle_start, secret_value = 0, size = 10):
        pygame.sprite.Sprite.__init__(self)

        self.pos = starting_pos
        self.color = color
        self.target = target
        self.secret_value = secret_value
        self.size = size
        
        a = rotating_position(0, circle_start, random.randint(0, 360), [0, 0])
        self.speed = a

    def update(self, surface, new_target = 0):
        if new_target != 0:
            self.target = new_target
        
        pygame.draw.circle(surface, self.color, self.pos, self.size)

        dis = distance(self.pos, self.target)
        self.speed[0] += (self.target[0] - self.pos[0]) * 0.005
        self.speed[1] += (self.target[1] - self.pos[1]) * 0.005

        self.speed = [self.speed[0] * 0.89, self.speed[1] * 0.89]

        self.pos = [self.pos[0] + self.speed[0], self.pos[1] + self.speed[1]]

        if 15 > abs(round(self.target[0] - self.pos[0])) and 15 > abs(round(self.target[1] - self.pos[1])):
            self.kill()
            return self.secret_value
            print("kill")

        return None


def main():
    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()

    # Uncomment this for a non-translucent surface.
    # surface = pg.Surface((100, 150), pg.SRCALPHA)
    # pg.draw.circle(surface, pg.Color(40, 240, 120), (50, 50), 50)
    surface = pg.image.load("images/dragon_tail_plain_black.png").convert_alpha()
    surface = pg.transform.rotozoom(surface, 0, 0.3)

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    fill(surface, pg.Color(240, 200, 40))
                if event.key == pg.K_g:
                    fill(surface, pg.Color(250, 10, 40))
                if event.key == pg.K_h:
                    fill(surface, pg.Color(40, 240, 120))

        screen.fill(pg.Color('lightskyblue4'))
        screen.blit(surface, (10, 10))

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()