import pygame
import math
from pygame.locals import*
import time
import random
import sys
import json

pygame.init()

NAME_OF_RELEASE = []
STATE_OF_RELEASE = []

IMAGE_NAMES = []
IMAGE_IMAGES = []


def rotating_position(x, y, direction, pos):
    """
    Rotates (x,y) by direction angles and adds it to pos.
    """
    a = pos[0] + (x * math.cos(-direction / 180.0 * math.pi) +
                  y * math.sin(-direction / 180.0 * math.pi))
    b = pos[1] + (-y * math.cos(-direction / 180.0 * math.pi) +
                  x * math.sin(-direction / 180.0 * math.pi))

    return [a, b]


def calculate_angle(pos1, pos2):
    x = pos1[0] - pos2[0]
    y = pos1[1] - pos2[1]
    return 0 - (math.atan2(y, x) / math.pi * 180) - 90


def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def retrogade(x, y):
    x = 0 - (math.atan2(y, x) / math.pi * 180) - 90
    return x


def add_speed(original, new):
    return [original[0] + new[0], original[1] + new[1]]


def multiply_speed(original, multiply):
    return [original[0] * multiply, original[1] * multiply]


def speed_in_direction(speed, direction, original_real_speed):
    valami = rotating_position(0, speed, direction, [0, 0])
    return add_speed(original_real_speed, valami)


def button(surface, font, color, text, pos, rect_color, tuch_color, width, mouse_add=[0, 0]):
    clicked = False
    
    wrighting = font.render(text, True, color)
    rect = wrighting.get_rect()
    rect.topleft = pos
    saint_rect = Rect(rect[0], rect[1], rect[2], rect[3])

    saint_rect[0] -= 5
    saint_rect[2] += 10
    saint_rect[1] -= 5
    saint_rect[3] += 10

    pygame.draw.rect(surface, rect_color, saint_rect, width)

    mouse_pos = [pygame.mouse.get_pos()[0] + mouse_add[0],
                 pygame.mouse.get_pos()[1] + mouse_add[1]]

    hihi = mouse_pos[0] > saint_rect[0] and mouse_pos[1] > saint_rect[1]
    haha = mouse_pos[0] < (saint_rect[0] + saint_rect[2]
                           ) and mouse_pos[1] < (saint_rect[1] + saint_rect[3])

    if hihi and haha:
        a = button_release(3)
        print(a, 'hhhhhhhhhhhhhhhhhhhhh')
        if a:
            clicked = True
        wrighting = font.render(text, True, tuch_color)

    surface.blit(wrighting, rect)
    return clicked


def blit_text(surface, color, text, pos, font, center = 0):
    wrighting = font.render(text, True, color)
    rect = wrighting.get_rect()
    
    if center == 0:
        rect.topleft = pos
    if center == 1:
        rect.center = pos
    
    surface.blit(wrighting, rect)
    return rect


def detect_click_rect(which_click, rect, mouse_add=[0, 0]):
    if pygame.mouse.get_pressed()[which_click]:
        mouse_pos = [pygame.mouse.get_pos()[0] + mouse_add[0],
                     pygame.mouse.get_pos()[1] + mouse_add[1]]

        hihi = mouse_pos[0] > rect[0] and mouse_pos[1] > rect[1]
        haha = mouse_pos[0] < (
            rect[0] + rect[2]) and mouse_pos[1] < (rect[1] + rect[3])

        return hihi and haha

    return False

def spaceless_string(text):
    new = ""
    
    for n in text:
        if n == "J":
            new = new + " "
        elif n != " ":
            new = new + n

    return new

def blit_sprite(sprite, pos, surface, font):
    split = sprite.splitlines()
    y = pos[1]

    for n in split:
        blit_text(surface, (0, 0, 0), spaceless_string(
            n), [pos[0], y], font, 1)
        y += 23

def blit_image(surface, directory, pos, zoom):
    if IMAGE_NAMES.__contains__(directory):
        index = IMAGE_NAMES.index(directory)
        image = IMAGE_IMAGES[index]
    else:
        image = pygame.image.load(directory).convert_alpha()
        image = pygame.transform.rotozoom(image, 0, zoom)
        IMAGE_NAMES.append(directory)
        IMAGE_IMAGES.append(image)
        index = IMAGE_NAMES.index(directory)
    
    rect = image.get_rect()
    rect.center = pos
    surface.blit(image, rect)           

def determine_biggest_width(sprite, font):
    split = sprite.splitlines()

    greatest = 0

    for n in split:
        wrighting = font.render(n, True, (0, 0, 0))

        if wrighting.get_width() / 2 > greatest:
            greatest = wrighting.get_width() / 2

    return greatest

def button_release(name):
    if NAME_OF_RELEASE.__contains__(name):
        index = NAME_OF_RELEASE.index(name)
    else:
        NAME_OF_RELEASE.append(name)
        STATE_OF_RELEASE.append(False)
        index = NAME_OF_RELEASE.index(name)
    
    print(ditinguish_button_and_number(name), 'dist', name)
    
    if name == 0 or name == 1 or name == 2 or name == 3:
        pressed = pygame.mouse.get_pressed(3)[name % 3]

        if pressed:
            if STATE_OF_RELEASE[index] == False:
                STATE_OF_RELEASE[index] = True
                return True
        else:
            STATE_OF_RELEASE[index] = False
    else:
        key = pygame.key.get_pressed()

        if key[name]:
            if STATE_OF_RELEASE[index] == False:
                STATE_OF_RELEASE[index] = True
                return True
        else:
            STATE_OF_RELEASE[index] = False
    
    return False

def transition_colors(color1, color2, percent):
    percent = max(percent, 0)
    percent = min(percent, 1)
    a = list(color2)
    b = list(color1)

    for n in range(3):
        a[n] = a[n] * percent
        b[n] = b[n] * (1 - percent)

    for n in range(3):
        a[n] = round(b[n] + a[n])
    
    return a

def add_values(listy):
    a = 0
    for n in listy:
        a += n
    return a

def ditinguish_button_and_number(value):
    try:
        a = value * 1
    except:
        return False
    return True

def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False




    