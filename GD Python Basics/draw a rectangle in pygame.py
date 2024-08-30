#import pygame
# pygame.init()
# 
# X = 400
# Y = 400
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# PURPLE = (145, 9, 236)
# ORANGE = (255, 123, 0)
# 
# DISPLAY = pygame.display.set_mode([X, Y])
# running = True
# 
# while running:
# 
#     DISPLAY.fill(PURPLE)
#     pygame.draw.rect(DISPLAY, ORANGE, [50, 0, 25, 200])
#     pygame.draw.rect(DISPLAY, ORANGE, [50, 200, 25, 150])
#     pygame.draw.rect(DISPLAY, ORANGE, [125, 200, 25, 200])
#     pygame.draw.rect(DISPLAY, ORANGE, [125, 50, 25, 150])
#     pygame.draw.rect(DISPLAY, ORANGE, [200, 50, 250, 25])
#     pygame.draw.rect(DISPLAY, ORANGE, [200, 275, 25, 125])
#     pygame.draw.rect(DISPLAY, ORANGE, [275, 325, 125, 25])
#     pygame.draw.rect(DISPLAY, ORANGE, [200, 125, 25, 150])
#     pygame.draw.rect(DISPLAY, ORANGE, [50, 0, 150, 25])
#     pygame.draw.rect(DISPLAY, ORANGE, [225, 125, 125, 25])
#     pygame.draw.rect(DISPLAY, ORANGE, [275, 200, 125, 25])
#     pygame.draw.rect(DISPLAY, ORANGE, [225, 275, 125, 25])
#     pygame.draw.circle(DISPLAY, WHITE, (25, 25), 7)
#     pygame.draw.circle(DISPLAY, BLACK, (375, 375), 7)
# 
#     pygame.display.flip()


#import pygame
#pygame.init()
# 
# X = 400
# Y = 400
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)
# 
# DISPLAY = pygame.display.set_mode([X, Y])
# running = True
# 
# while running:
#     DISPLAY.fill(GREEN)
#     
#     pygame.draw.rect(DISPLAY, BLACK, [50, 50, 150, 150], 2)
#     pygame.draw.rect(DISPLAY, BLACK, [198, 50, 150, 150], 2)
#     pygame.draw.rect(DISPLAY, BLACK, [50, 198, 150, 150], 2)
#     pygame.draw.rect(DISPLAY, BLACK, [198, 198, 150, 150], 2)
#     pygame.draw.rect(DISPLAY, BLACK, [124, 124, 150, 150], 2)
# 
#     pygame.display.flip()


import pygame
pygame.init()

X = 400
Y = 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 30)
PINK = (236, 177, 231)
BLUE = (0, 125, 255)

DISPLAY = pygame.display.set_mode([X, Y])
running = True

while running:
    DISPLAY.fill(BLUE)
    pygame.draw.rect(DISPLAY, GREEN, [0, 275, 400, 125])
    pygame.draw.rect(DISPLAY, BLACK, [150, 200, 100, 100])
    pygame.draw.rect(DISPLAY, WHITE, [152, 202, 96, 96])
    pygame.draw.rect(DISPLAY, BLACK, [195, 202, 45, 28])
    pygame.draw.rect(DISPLAY, BLACK, [152, 252, 29, 23])
    pygame.draw.rect(DISPLAY, BLACK, [210, 276, 40, 24])
    pygame.draw.rect(DISPLAY, BLACK, [181, 278, 21, 17])
    pygame.draw.rect(DISPLAY, BLACK, [195, 245, 35, 22])
    pygame.draw.rect(DISPLAY, BLACK, [120, 175, 55, 73])
    pygame.draw.rect(DISPLAY, WHITE, [122, 177, 51, 69])
    pygame.draw.rect(DISPLAY, BLACK, [122, 215, 51, 32])
    pygame.draw.rect(DISPLAY, PINK, [122, 216, 51, 30])
    pygame.draw.rect(DISPLAY, BLACK, [152, 225, 6, 12])
    pygame.draw.rect(DISPLAY, BLACK, [138, 225, 6, 12])
    pygame.draw.rect(DISPLAY, BLACK, [108, 175, 14, 22])
    pygame.draw.rect(DISPLAY, WHITE, [110, 177, 10, 18])
    pygame.draw.rect(DISPLAY, BLACK, [173, 175, 14, 22])
    pygame.draw.rect(DISPLAY, WHITE, [175, 177, 10, 18])
    pygame.draw.circle(DISPLAY, BLACK, (155, 195), 4)
    pygame.draw.circle(DISPLAY, BLACK, (140, 195), 4)

    pygame.display.flip()








