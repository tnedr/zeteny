import pygame
import sys

pygame.init()
size = (480,320)
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print('jozsi')
            pygame.quit()
            sys.exit()
    pygame.display.update()