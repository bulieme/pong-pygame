import pygame
import sys

pygame.init()
screenSize = (512, 300)

screen = pygame.display.set_mode(screenSize)
scroll = 0

def font(size):
    return pygame.font.Font("assets/fonts/font.ttf", size)

while True:

    screen.fill((0, 0, 0))
    about = font(15).render("This game its just an hobby project.", False, (255, 255, 255))

    screen.blit(about, (screenSize[0]/2 - about.get_width()/2, screenSize[1]/2 - about.get_height()/2 + scroll))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEWHEEL:
            scroll += event.y * 20
            print(scroll)
