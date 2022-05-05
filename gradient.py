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

def integer_to_english(number):
    if number>=1 and number<=1000:
        a = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty ','thirty ','fourty ','fifty ','sixty ','seventy ','eighty ','ninty ']
        if number<=20:
            if number%10==0: return a[number]
            else: return a[number]
        elif number<100:
            b=number-20
            r=b%10
            b//=10
            return a[20+b]+a[r]
        elif number<1000:
            if number%100==0:
                b=number//100
                return a[b]+' hundred'
            else:
                r=number%100
                b=number//100
                if r<=20:
                    return a[b]+' hundred'+' and '+a[r]
                else:
                    r=r-20
                    d=r//10
                    r%=10
                    return a[b]+' hundred'+' and '+a[20+d]+a[r]
        elif number==1000:
            return 'one thousand'
        else:
            return -1