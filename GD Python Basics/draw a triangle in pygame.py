

# 
# X = 400
# Y = 400
# BLUE = (90, 90, 250)
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# ORANGE = (247, 171, 38)
# YELLOW = (247, 240, 39)
# 
# DISPLAY = pygame.display.set_mode([X, Y])
# running = True
# 
# while running:
#     DISPLAY.fill(BLUE)
#     pygame.draw.circle(DISPLAY, ORANGE, (200, 200), 25)
#     pygame.draw.polygon(DISPLAY, YELLOW,[[200, 50], [175, 160], [225, 160]])
#     pygame.draw.polygon(DISPLAY, YELLOW,[[350, 200], [240, 175], [240, 225]])
#     pygame.draw.polygon(DISPLAY, YELLOW,[[200, 350], [225, 240], [175, 240]])
#     pygame.draw.polygon(DISPLAY, YELLOW,[[50, 200], [160, 225], [160, 175]])
#     pygame.draw.polygon(DISPLAY, YELLOW,[[90, 90], [140, 170], [170, 140]])
#     pygame.draw.polygon(DISPLAY, YELLOW,[[310, 90], [260, 170], [230, 140]])
#     pygame.draw.polygon(DISPLAY, YELLOW,[[310, 310], [260, 230], [230, 260]])
#     pygame.draw.polygon(DISPLAY, YELLOW,[[90, 310], [140, 230], [170, 260]])
#     
#     pygame.display.flip()

# X = 400
# Y = 400
# BLUE = (90, 90, 250)
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# ORANGE = (247, 171, 38)
# RED = (254, 15, 16)

# DISPLAY = pygame.display.set_mode([X, Y])
# running = True

# pygame.draw.circle(DISPLAY, WHITE, (random.randint(1, 400), random.randint(1, 400)), 4)

# my_number = random.randint(1, 400)
# my_number1 = random.randint(1, 400)
# my_number2 = random.randint(1, 400)
# my_number3 = random.randint(1, 400)
# my_number4 = random.randint(1, 400)
# my_number5 = random.randint(1, 400)
# my_number6 = random.randint(1, 400)
# my_number7 = random.randint(1, 400)
# my_number8 = random.randint(1, 400)
# my_number9 = random.randint(1, 400)
# my_number = random.randint(1, 400)
# my1_number1 = random.randint(1, 400)
# my2_number2 = random.randint(1, 400)
# my3_number3 = random.randint(1, 400)
# my4_number4 = random.randint(1, 400)
# my5_number5 = random.randint(1, 400)
# my6_number6 = random.randint(1, 400)
# my7_number7 = random.randint(1, 400)
# my8_number8 = random.randint(1, 400)
# my9_number9 = random.randint(1, 400)



# while running:
#     DISPLAY.fill(BLACK)
#     pygame.draw.rect(DISPLAY, RED, [100, 75, 75, 200])
#     pygame.draw.circle(DISPLAY, WHITE, (my_number, my_number), 4)
#     pygame.draw.circle(DISPLAY, WHITE, (my_number1, my1_number1), 4)
#     pygame.draw.circle(DISPLAY, WHITE, (my_number2, my2_number2), 4)
#     pygame.draw.circle(DISPLAY, WHITE, (my_number3, my3_number3), 4)
#     pygame.draw.circle(DISPLAY, WHITE, (my_number4, my4_number4), 4)
#     pygame.draw.circle(DISPLAY, WHITE, (my_number5, my5_number5), 4)
#     pygame.draw.circle(DISPLAY, WHITE, (my_number6, my6_number6), 4)
#     pygame.draw.circle(DISPLAY, WHITE, (my_number7, my7_number7), 4)
#     pygame.draw.circle(DISPLAY, WHITE, (my_number8, my8_number8), 4)
#     pygame.draw.circle(DISPLAY, WHITE, (my_number9, my9_number9), 4)

#     pygame.display.flip()

import pygame
pygame.init()

X = 400
Y = 400
BLUE = (90, 90, 250)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (247, 171, 38)
RED = (254, 15, 16)
YELLOW = (255, 235, 15)
PURPLE = (179, 15, 255)
GREEN = (0, 255, 0)
BLUE2 = (0, 0, 255)

DISPLAY = pygame.display.set_mode([X, Y])
running = True

pygame.draw.circle(DISPLAY, WHITE, (random.randint(1, 400), random.randint(1, 400)), 4)

while running:
    DISPLAY.fill(BLACK)
    pygame.draw.polygon(DISPLAY, BLUE, [[0, 0], [5, 5], [10, 5]])
    pygame.draw.polygon(DISPLAY, WHITE, [[10, 10], [15, 15], [20, 20]])
    pygame.draw.polygon(DISPLAY, ORANGE, [[25, 25], [30, 30], [30, 35]])
    pygame.draw.polygon(DISPLAY, RED, [[25, 25], [30, 30], [30, 35]])
    pygame.draw.polygon(DISPLAY, YELLOW, [[25, 25], [30, 30], [30, 35]])
    pygame.draw.polygon(DISPLAY, PURPLE, [[25, 25], [30, 30], [30, 35]])
    pygame.draw.polygon(DISPLAY, GREEN, [[25, 25], [30, 30], [30, 35]])
    pygame.draw.polygon(DISPLAY, BLUE2, [[25, 25], [30, 30], [30, 35]])
    pygame.draw.polygon(DISPLAY, BLUE2, [[25, 25], [30, 30], [30, 35]])
    pygame.draw.polygon(DISPLAY, BLUE2, [[25, 25], [30, 30], [30, 35]])
    pygame.draw.polygon(DISPLAY, BLUE2, [[25, 25], [30, 30], [30, 35]])
    pygame.draw.polygon(DISPLAY, BLUE2, [[25, 25], [30, 30], [30, 35]])
    pygame.draw.polygon(DISPLAY, BLUE2, [[25, 25], [30, 30], [30, 35]])
    pygame.draw.polygon(DISPLAY, BLUE2, [[25, 25], [30, 30], [30, 35]])
    pygame.draw.polygon(DISPLAY, BLUE2, [[25, 25], [30, 30], [30, 35]])


    pygame.display.flip()















