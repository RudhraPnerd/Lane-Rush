import os
import sys

import pygame

pygame.init()


def resource_path(relative):
    # PyInstaller's temp folder when running as an exe, the project folder otherwise
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative)


SCREEN_SIZE = (480, 720)
WINDOW_TITLE = 'Lane Rush'
FPS = 60

BACKGROUND = resource_path('assets/sprites/background.png')
CAR = resource_path('assets/sprites/car.png')
TRAFFIC = resource_path('assets/sprites/traffic.png')
ICON = resource_path('assets/icon.png')

POINT_EFFECT = resource_path('assets/audio/point.wav')
HIGH_SCORE_REACHED_EFFECT = resource_path('assets/audio/high_score_reached.wav')

LANES = 4
ROAD_LEFT = 67
ROAD_RIGHT = 416
LANE_WIDTH = (ROAD_RIGHT - ROAD_LEFT) // LANES   # 87

TRAFFIC_SPEED = 450
SPAWN_MIN = 1.0
SPAWN_MAX = 2.0

SPEED = 300

FONT = pygame.font.Font(resource_path('assets/Audiowide-Regular.ttf'), 32)