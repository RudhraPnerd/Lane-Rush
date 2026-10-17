import pygame
import random
import configs as cfg
import objects as obj
import assets as ast

pygame.init()

score = 0
high_score = 0
score_timer = 0

screen = pygame.display.set_mode(cfg.SCREEN_SIZE)
pygame.display.set_caption(cfg.WINDOW_TITLE)
ast.load_assets()

bg = obj.Background(cfg.SPEED)
car = obj.Car(cfg.SCREEN_SIZE[0] // 2, cfg.SCREEN_SIZE[1] - 100)

traffic = []
spawn_timer = 0

clock = pygame.time.Clock()
running = True

while running:
    dt = clock.tick(cfg.FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bg.update(dt)
    car.update(dt, pygame.key.get_pressed())

    score_timer += dt
    if score_timer >= 1:
        score_timer -= 1
        score += 1
        cfg.SPEED += 1
        bg.speed = cfg.SPEED
        cfg.SPAWN_MIN -= 0.001
        cfg.SPAWN_MAX -= 0.001
        print(score)

    if score > high_score:
        high_score = score

    spawn_timer -= dt
    if spawn_timer <= 0:
        traffic.append(obj.Traffic(random.randrange(cfg.LANES), speed=cfg.TRAFFIC_SPEED))
        spawn_timer = random.uniform(cfg.SPAWN_MIN, cfg.SPAWN_MAX)

    for t in traffic:
        t.update(dt)
    traffic = [t for t in traffic if t.rect.top < cfg.SCREEN_SIZE[1]]

    for t in traffic:
        if car.rect.colliderect(t.rect):
            running = False

    bg.draw(screen)
    for t in traffic:
        t.draw(screen)
    car.draw(screen)

    score_text = cfg.FONT.render(str(score), True, (255, 255, 255))

    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()