import pygame
import math
from pygame.locals import*
import time
import random
import sys
import json

from helpers import *
from gradient import *
from arc import *
from designs import *
from colors_and_images import *
from particle_effects import *

pygame.init()

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 712

SCREEN_XC = SCREEN_WIDTH // 2
SCREEN_YC = SCREEN_HEIGHT // 2

SURFACE = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
#SURFACE = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
CLOCK = pygame.time.Clock()

SURFACE.fill((200, 200, 200))
gradientRect_w(SURFACE, (0, 0, 10), (83, 132, 255),
                     Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
image = pygame.image.load(
    "images/dragon_tail_white_shadow.png").convert_alpha()
image = pygame.transform.rotozoom(image, 0, 0.3)
rect = image.get_rect()
rect.center = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
SURFACE.blit(image, rect)
pygame.display.update()
time.sleep(1)

print("hello")
print(pygame.font.get_fonts())

FONT_SCRIPT = pygame.font.SysFont('simsun', 20)
FONT1 = pygame.font.SysFont('snapitc', 65)
FONT2 = pygame.font.SysFont('segoeprint', 45)
FONT3 = pygame.font.SysFont('showcardgothic', 20)
FONT4 = pygame.font.SysFont('twcen', 50)
FONT5 = pygame.font.SysFont('copperplategothic', 25)

GRAY_GREEN = (150, 220, 150)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (50, 50, 50)

class Home_page(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.money = 1000
        self.security_strength = 23
        self.safety_percautions = ('password', 'warning')

    def update(self, surface):
        blit_text(surface, GRAY_GREEN, "$" + str(self.money), [SCREEN_XC, 50], FONT1, 1)
        
        a = blit_text(surface, GRAY_GREEN, 'security', [SCREEN_XC, 550], FONT2, 1)
        security_color = transition_colors((0, 250, 0), (250, 0, 0), self.security_strength / 100)
        bar_display(surface, security_color, 
        [a[0] - 100, a[1] + a[3] + 10], a[2] + 200,  5, self.security_strength / 100, (200, 200, 200))
        
        list_content(surface, self.safety_percautions, FONT_SCRIPT, GRAY_GREEN, 20, 
                [SCREEN_XC, a[1] + 120], 0, 0, 1)

        button(surface, FONT4, DARK_GRAY, 'HACK', [SCREEN_XC - 50, 200], GRAY_GREEN, 
                BLACK, 0)


RUNNING = True
HOME_PAGE = Home_page()

DELTA_TIME = 53

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                RUNNING = False

    SURFACE.fill((50, 50, 50))
    HOME_PAGE.update(SURFACE)
    
    pygame.display.update()
    CLOCK.tick(DELTA_TIME)

pygame.quit()
