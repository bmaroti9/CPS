import pygame
import math
from pygame.locals import*

def filled_arc(surface, center, color, radius, width, angle1, angle2, quality = 201):
    angle1 = angle1 / 180 * math.pi
    angle2 = angle2 / 180 * math.pi
    points = []
    steps = quality
    for i in range(steps + 1):
        angle = angle1 + (angle2 - angle1) / steps * i
        points.append((center[0] + math.cos(angle) * radius,
                      center[1] - math.sin(angle) * radius))
    for i in range(steps + 1):
        angle = angle2 - (angle2 - angle1) / steps * i
        points.append((center[0] + math.cos(angle) * (radius - width),
                      center[1] - math.sin(angle) * (radius - width)))
    pygame.draw.polygon(surface, color, points)