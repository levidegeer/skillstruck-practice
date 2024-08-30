import pygame
pygame.init()

X = 200
Y = 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

DISPLAY = pygame.display.set_mode([X, Y])
pygame.display.set_caption("My First Game!")

running = True
while running:

    DISPLAY.fill(WHITE)
    pygame.display.flip()














