import pygame
pygame.init()

X = 400
Y = 400
BLUE = (90, 90, 250)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (251, 255, 15)
pi = 3.14

DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:

    DISPLAY.fill(BLUE)
    pygame.draw.rect(DISPLAY, YELLOW, [25, 25, 350, 225], 3)
    pygame.draw.circle(DISPLAY, BLACK, (140, 100), 20)
    pygame.draw.circle(DISPLAY, BLACK, (260, 100), 20)
    pygame.draw.polygon(DISPLAY, WHITE, [[200, 120], [170, 180], [230, 180]])
    pygame.draw.arc(DISPLAY, BLACK, [75, 125, 250, 100], pi, 2*pi, 5)
    pygame.display.flip()








