import pygame

pygame.init()

SCREEN_SIZE = (480, 720)
WINDOW_TITLE = 'Lane Rush'
FPS = 60
BACKGROUND = 'assets/sprites/background.png'
CAR = 'assets/sprites/car.png'
TRAFFIC = 'assets/sprites/traffic.png'

LANES = 4
ROAD_LEFT = 67
ROAD_RIGHT = 416
LANE_WIDTH = (ROAD_RIGHT - ROAD_LEFT) // LANES   # 87

TRAFFIC_SPEED = 450
SPAWN_MIN = 1.0
SPAWN_MAX = 2.0

SPEED = 300

FONT = pygame.font.Font('assets/Audiowide-Regular.ttf', 32)