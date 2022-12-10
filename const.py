import pygame

# GAME STATE
GAME_OVER = -1
GAME_INIT = 0
GAME_START = 1
GAME_STAGE1 = 2
GAME_STAGE2 = 3

# game options/settings
TITLE = "TEST"
WIDTH = 800
HEIGHT = 600
FPS = 60

# Player properties
PLAYER_ACC = 1.5
PLAYER_FRICTION = -0.2
PLAYER_GRAVITY = 0.8

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (WIDTH/2 - 50, HEIGHT*3/4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]


# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


STANDING_SURFACE = pygame.transform.scale(pygame.image.load("assets/mario_standing.png"), (33, 35))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("assets/mario_jumping.png"), (33, 35))
