import math
import random
import sys
import pygame
from pygame.locals import *
import time
import json

from helpers import *
from arc import *

pygame.init()

PARCTICLES = pygame.sprite.Group()

def gradientRect(surface, left_colour, right_colour, target_rect):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface(
        (2, 2))                                   # tiny! 2x2 bitmap
    pygame.draw.line(colour_rect, left_colour,  (0, 0),
                     (0, 1))            # left colour line
    pygame.draw.line(colour_rect, right_colour, (1, 0),
                     (1, 1))            # right colour line
    colour_rect = pygame.transform.smoothscale(
        colour_rect, (target_rect.width, target_rect.height))  # stretch!
    # paint it
    surface.blit(colour_rect, target_rect)


class Particle(pygame.sprite.Sprite):
    def __init__(self, starting_pos, color, target, secret_value = 0):
        pygame.sprite.Sprite.__init__(self)

        self.pos = starting_pos
        self.color = color
        self.target = target
        self.secret_value = secret_value
        
        a = rotating_position(0, 50, random.randint(0, 360), [0, 0])
        self.speed = a

    def update(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, 10)

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

def draw_arc(surface, percent, radius, color, center_pos, width):
    angle = 0
    old_pos = rotating_position(0, radius, angle, center_pos)

    for n in range(round(180 * percent)):
        angle -= 2
        new_pos = rotating_position(0, radius, angle, center_pos)
        pygame.draw.line(surface, color, old_pos, new_pos, width)
        old_pos = new_pos
    
def arc_circle(surface, percent, radius, color, center_pos, width, number, font, font_color, add, back):
    angle = 0

    pygame.draw.circle(surface, back, [center_pos[0] - 1, center_pos[1] - 1], radius + 6, (width * 2) + 2)

    for n in range(round(120 * percent)):
        angle -= 3
        pygame.draw.circle(surface, color, rotating_position(0, radius, angle, center_pos), width)

    blit_text(surface, font_color, str(number), center_pos, font, 1)
    
def arc_circle2(surface, center, font, number, radius, width, percent, color, t_color, add):
    filled_arc(surface, center, color, radius, width, 90, 90 + (-360 * percent))
    blit_text(surface, t_color, str(number), center, font, 1)