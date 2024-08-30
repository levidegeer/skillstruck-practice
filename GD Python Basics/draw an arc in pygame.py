import pygame
pygame.init()

X = 400
Y = 400
BLUE = (90, 90, 250)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (124, 25, 245)
GREEN = (0, 255, 0)
YELLOW = (221, 224, 0)
ORANGE = (224, 142, 0)
RED = (255, 0, 0)
BLUE2 = (0, 0, 255)

pi = 3.14

DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:
    DISPLAY.fill(PURPLE)
    pygame.draw.circle(DISPLAY, WHITE, [137, 160], 5)
    pygame.draw.circle(DISPLAY, BLACK, [213, 180], 5)
    pygame.draw.arc(DISPLAY, YELLOW, [100, 100, 150, 150], 2*pi, pi, 3)
    pygame.draw.arc(DISPLAY, YELLOW, [100, 100, 150, 150], pi, 2*pi, 3)
    pygame.draw.arc(DISPLAY, YELLOW, [100, 133, 75, 75], 2*pi, pi, 3)
    pygame.draw.arc(DISPLAY, YELLOW, [175, 133, 75, 75], pi, 2*pi, 3)
    pygame.display.flip()