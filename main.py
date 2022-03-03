import pygame, sys, random


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 900))
    screen.blit(floor_surface, (floor_x_pos + 576, 900))


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(700, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(700, random_pipe_pos - 300))
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)

RESIZE = 1
SCREEN_HEIGHT = 576 * RESIZE
SCREEN_WIDTH = 1024 * RESIZE
pygame.init()
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird")

# Game variables
gravity = 0.25
bird_movement = 0

bg_surface = pygame.image.load("assets/background-day.png").convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load("assets/base.png").convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

# Bird
bird_surface = pygame.image.load("assets/bluebird-midflap.png").convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center=(100, SCREEN_WIDTH / 2))

# Pipes
pipe_surface = pygame.image.load("assets/pipe-green.png").convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWN_PIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWN_PIPE, 1200)
pipe_height = [400, 600, 800]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Check for space bar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 12
        
        # Spawn pipes
        if event.type == SPAWN_PIPE:
            pipe_list.extend(create_pipe())
            SPAWN_PIPE += 1
            pygame.time.set_timer(SPAWN_PIPE, 1200)

    screen.blit(bg_surface, (0, 0))

    # Bird
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)

    # Move pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)
    
    # Floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
    