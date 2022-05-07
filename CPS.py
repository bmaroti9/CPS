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
from colors_and_images import *

pygame.init()

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 712

SURFACE = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
#SURFACE = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
CLOCK = pygame.time.Clock()

SURFACE.fill((200, 200, 200))
gradientRect(SURFACE, (0, 0, 10), (83, 132, 255),
                     Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
image = pygame.image.load(
    "images/dragon_tail_white_shadow.png").convert_alpha()
image = pygame.transform.rotozoom(image, 0, 0.3)
rect = image.get_rect()
rect.center = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
SURFACE.blit(image, rect)
pygame.display.update()
time.sleep(3)

CLICKING_OPTIONS = ['everything', 'no_right-click']
CLICKING_SETTING = 0

'''
for n in range(120):
    SURFACE.fill((200, 200, 200))
    flashed = flash_up_image(image, (0, 0, 0), (0, 70, 100),
                             n, 70, 30, 20)
    SURFACE.blit(flashed, rect)
    pygame.display.update()
    CLOCK.tick(30)
'''

print("hello")
print(pygame.font.get_fonts())
print(len(pygame.key.name(K_UP)), 'GGGGGGGGGGGGGGGGGG')

SCREEN_CENTER = [SURFACE.get_width() // 2, SURFACE.get_height() // 2]

FONT1 = pygame.font.SysFont('snapitc', 40)
FONT2 = pygame.font.SysFont('segoeprint', 45)
FONT3 = pygame.font.SysFont('showcardgothic', 20)
FONT4 = pygame.font.SysFont('copperplategothic', 30)
#FONT3 = pygame.font.SysFont('tempussansitc', 20)


class Home_page(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.money = 0
        self.clicks = []
        self.cps = 1
        self.rapid_cool = 0
        self.speed_color = (0, 0, 0)
        self.slowly_add = 0
        self.fontsize = 60
        self.flash = 0

    def update(self):
        gradientRect(SURFACE, (64, 93, 148), (83, 132, 224),
                     Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

        if len(self.clicks) > DELTA_TIME * 5:
            del self.clicks[0]

        self.cps = add_values(self.clicks) / 5

        if pygame.mouse.get_pressed(3)[2] and CLICKING_SETTING == 0:
            PARTICLES.add(Particle(SCREEN_CENTER, self.speed_color, [
                          SCREEN_CENTER[0], 90], 50, self.cps))
            self.clicks.append(1)
            self.rapid_cool = (self.rapid_cool + 5) * ((self.cps * 0.08) + 2)

        if check_released(0) or check_released(K_SPACE) or check_released(K_UP):
            PARTICLES.add(Particle(SCREEN_CENTER, self.speed_color, [
                          SCREEN_CENTER[0], 90], 50, self.cps))
            self.clicks.append(1)
            self.rapid_cool = (self.rapid_cool + 5) * ((self.cps * 0.05) + 1)
        else:
            self.clicks.append(0)
            self.rapid_cool = self.rapid_cool * 0.73
            self.rapid_cool = min(self.rapid_cool, SCREEN_HEIGHT * 0.07)

        for n in PARTICLES:
            if n.update(SURFACE) != None:
                self.slowly_add += n.secret_value * 5

        self.fontsize = (self.slowly_add + (self.fontsize) * 2.5) * 0.1
        self.money += self.fontsize
        self.slowly_add -= self.fontsize

        sizedfont = pygame.font.SysFont(
            'rage', 60 + (round(min(self.fontsize, 23)) * 5))

        self.speed_color = transition_colors(
            (250, 0, 0), (224, 208, 75), 1 - self.cps * 0.06)

        pygame.draw.circle(SURFACE, self.speed_color, SCREEN_CENTER,
                           60 + (self.cps * 2) + (self.rapid_cool * 0.8))

        size = blit_text(SURFACE, (250, 250, 250), "$" +
                  str('{:,}'.format(round(self.money))), [SCREEN_CENTER[0], 90], sizedfont, 1)

        blit_text(SURFACE, (0, 0, 0), "{:.1f}".format(
            self.cps), SCREEN_CENTER, FONT1, 1)
        blit_text(SURFACE, (0, 0, 0), 'CPS', [
                  SCREEN_CENTER[0], SCREEN_CENTER[1] + 35], FONT3, 1)

        self.display_coolness()

    def display_coolness(self):
        global CLICKING_SETTING

        # arc_circle(SURFACE, 0.8, 50, (121, 34, 148), [
        # 1000, 100], 5, 50, FONT2, (250, 250, 250), 1, (187, 63, 224))
        
        #arc_circle2(SURFACE, [1000, 100], FONT2, 50, 70,
                    #14, 0.7, (245, 194, 36), (230, 180, 143), 1)
        
        change_setting = button(SURFACE, FONT4, (150, 0, 0), CLICKING_OPTIONS[CLICKING_SETTING],
                    [10, 10], (150, 0, 0), (80, 0, 0), 2)
        
        if change_setting:
            self.clicks = []
            CLICKING_SETTING += 1
            if CLICKING_SETTING > len(CLICKING_OPTIONS) - 1:
                CLICKING_SETTING = 0



RUNNING = True
PARTICLES = pygame.sprite.Group()

HOME_PAGE = Home_page()
DELTA_TIME = 53

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                RUNNING = False

    SURFACE.fill((0, 0, 0))

    HOME_PAGE.update()
    
    pygame.display.update()
    CLOCK.tick(DELTA_TIME)


pygame.quit()
