# import pygame
# pygame.init()
# 
# X = 400
# Y = 400
# BLUE = (90, 90, 250)
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# 
# DISPLAY = pygame.display.set_mode([X, Y])
# running = True
# 
# while running:
#     DISPLAY.fill(BLUE)
#     pygame.draw.line(DISPLAY, WHITE, [100, 100], [200, 200], 3)
#     pygame.draw.line(DISPLAY, WHITE, [80, 120], [200, 200], 3)
#     pygame.draw.line(DISPLAY, WHITE, [100, 100], [80, 120], 3)
#     pygame.draw.line(DISPLAY, WHITE, [300, 100], [200, 200], 3)
#     pygame.draw.line(DISPLAY, WHITE, [300, 100], [100, 100], 3)
#     pygame.draw.line(DISPLAY, WHITE, [320, 120], [200, 200], 3)
#     pygame.draw.line(DISPLAY, WHITE, [300, 100], [320, 120], 3)
#     pygame.draw.line(DISPLAY, WHITE, [80, 120], [320, 120], 3)
#     pygame.display.flip()

import pygame
pygame.init()

X = 400
Y = 400
BLUE = (90, 90, 250)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:
    DISPLAY.fill(BLUE)
    pygame.draw.line(DISPLAY, WHITE, [50, 50], [50, 100], 10)
    pygame.draw.line(DISPLAY, WHITE, [50, 100], [100, 100], 10)
    pygame.draw.line(DISPLAY, WHITE, [125, 50], [175, 50], 10)
    pygame.draw.line(DISPLAY, WHITE, [125, 75], [175, 75], 10)
    pygame.draw.line(DISPLAY, WHITE, [125, 100], [175, 100], 10)
    pygame.draw.line(DISPLAY, WHITE, [125, 50], [125, 100], 10)
    pygame.draw.line(DISPLAY, WHITE, [200, 50], [235, 100], 10)
    pygame.draw.line(DISPLAY, WHITE, [270, 50], [235, 100], 10)
    pygame.draw.line(DISPLAY, WHITE, [295, 50], [295, 60], 10)
    pygame.draw.line(DISPLAY, WHITE, [295, 70], [295, 100], 10)

    pygame.display.flip()