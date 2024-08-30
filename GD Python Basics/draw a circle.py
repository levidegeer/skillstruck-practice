import pygame
pygame.init()

X = 400
Y = 400

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

sun = (249, 255, 14)
mer = (150, 150, 150)
ven = (240, 190, 49)
ear = (64, 132, 221)
mar = (200, 25, 25)
jup = (240, 190, 49)
sat = (249, 255, 19)
ura = (29, 250, 255)
nep = (165, 29, 255)
plu = (154, 71, 71)


DISPLAY = pygame.display.set_mode([X, Y])
pygame.display.set_caption("My First Game!")

running = True
while running:
    DISPLAY.fill(BLACK)
    pygame.draw.circle(DISPLAY, WHITE, (200, 200), 165, 1)
    pygame.draw.circle(DISPLAY, WHITE, (200, 200), 150, 1)
    pygame.draw.circle(DISPLAY, WHITE, (200, 200), 135, 1)
    pygame.draw.circle(DISPLAY, WHITE, (200, 200), 120, 1)
    pygame.draw.circle(DISPLAY, WHITE, (200, 200), 105, 1)
    pygame.draw.circle(DISPLAY, WHITE, (200, 200), 90, 1)
    pygame.draw.circle(DISPLAY, WHITE, (200, 200), 75, 1)
    pygame.draw.circle(DISPLAY, WHITE, (200, 200), 60, 1)
    pygame.draw.circle(DISPLAY, WHITE, (200, 200), 45, 1)
    pygame.draw.circle(DISPLAY, sun, (200, 200), 25)
    pygame.draw.circle(DISPLAY, mer, (200, 155), 4)
    pygame.draw.circle(DISPLAY, ven, (260, 200), 7)
    pygame.draw.circle(DISPLAY, ear, (200, 275), 7)
    pygame.draw.circle(DISPLAY, mar, (110, 200), 6)
    pygame.draw.circle(DISPLAY, jup, (200, 95), 18)
    pygame.draw.circle(DISPLAY, sat, (320, 200), 20)
    pygame.draw.circle(DISPLAY, BLACK, (320, 200), 19)
    pygame.draw.circle(DISPLAY, sat, (320, 200), 15)
    pygame.draw.circle(DISPLAY, ura, (200, 335), 10)
    pygame.draw.circle(DISPLAY, nep, (50, 200), 10)
    pygame.draw.circle(DISPLAY, plu, (200, 35), 3)
    pygame.display.flip()
