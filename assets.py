import pygame
import configs as cfg

pygame.init()

background = None
car = None
traffic = None

point_effect = None
high_score_reached_effect = None

def load_assets():
    global background, car, traffic, point_effect, high_score_reached_effect

    background = pygame.image.load(cfg.BACKGROUND).convert()
    background = pygame.transform.scale(background, cfg.SCREEN_SIZE)

    car = pygame.image.load(cfg.CAR).convert_alpha()
    car = pygame.transform.scale(car, (50, 90))

    traffic = pygame.image.load(cfg.TRAFFIC).convert_alpha()
    traffic = pygame.transform.scale(traffic, (50, 90))

    point_effect = pygame.mixer.Sound(cfg.POINT_EFFECT)
    high_score_reached_effect = pygame.mixer.Sound(cfg.HIGH_SCORE_REACHED_EFFECT)
    