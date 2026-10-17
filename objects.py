import pygame
import assets as ast
import configs as cfg

class Background:
    def __init__(self, speed):
        self.image = ast.background
        self.height = self.image.get_height()
        self.speed = speed
        self.y = 0.0

    def update(self, dt):
        self.y = (self.y + self.speed * dt) % self.height

    def draw(self, screen):
        screen.blit(self.image, (0, self.y))
        screen.blit(self.image, (0, self.y - self.height))



class Car:
    def __init__(self, x, y):
        self.image = ast.car
        self.rect = self.image.get_rect(center=(x, y))
        self.x = float(self.rect.x)
        self.speed = 400

    def update(self, dt, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed * dt

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed * dt


        self.x = max(cfg.ROAD_LEFT, min(self.x, cfg.ROAD_RIGHT - self.rect.width))
        self.rect.x = round(self.x)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Traffic:
    def __init__(self, lane, speed):
        self.image = ast.traffic
        x = cfg.ROAD_LEFT + lane * cfg.LANE_WIDTH + cfg.LANE_WIDTH // 2
        self.rect = self.image.get_rect(midbottom=(x, 0))
        self.y = float(self.rect.y)
        self.speed = speed
        self.passed = False

    def update(self, dt):
        self.y += self.speed * dt
        self.rect.y = round(self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)