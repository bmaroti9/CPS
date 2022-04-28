import pygame
import math
from pygame.locals import*

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

SURFACE = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
CLOCK = pygame.time.Clock()


def filled_arc(surface, center, color, radius, width, angle1, angle2):
    angle1 = angle1 / 180 * math.pi
    angle2 = angle2 / 180 * math.pi
    points = []
    steps = 50
    for i in range(steps + 1):
        angle = angle1 + (angle2 - angle1) / steps * i
        points.append((center[0] + math.cos(angle) * radius,
                      center[1] - math.sin(angle) * radius))
    for i in range(steps + 1):
        angle = angle2 - (angle2 - angle1) / steps * i
        points.append((center[0] + math.cos(angle) * (radius - width),
                      center[1] - math.sin(angle) * (radius - width)))
    pygame.draw.polygon(surface, color, points)


RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                RUNNING = False

    SURFACE.fill((50, 0, 0))
    filled_arc(SURFACE, (250, 250), (255, 255, 0), 150, 50, 90, -270)

    pygame.display.update()
    CLOCK.tick(30)


pygame.quit()
