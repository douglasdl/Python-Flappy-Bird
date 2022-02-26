import pygame, sys

pygame.init()
RESIZE = 1
SCREEN_HEIGHT = 576 * RESIZE
SCREEN_WIDTH = 1024 * RESIZE
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird")

bg_surface = pygame.image.load("assets/background-day.png").convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load("assets/base.png").convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0, 0))
    floor_x_pos += 1
    screen.blit(floor_surface, (floor_x_pos, 900))

    pygame.display.update()
    clock.tick(120)
    