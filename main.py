import pygame
import random
import configs as cfg
import objects as obj
import assets as ast
import utils as ut
from displays import gameover
import states as st

pygame.init()

score = 0
high_score = ut.load_high_score()
beat_high_score = False
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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and st.STATE_GAME_OVER:
            score, score_timer, spawn_timer, beat_high_score, traffic = ut.reset_game(bg, car, high_score)

    if not st.STATE_GAME_OVER:
        bg.update(dt)
        car.update(dt, pygame.key.get_pressed())

        score_timer += dt
        if score_timer >= 1:
            score_timer -= 1
            score += 1
            cfg.SPEED = min(cfg.SPEED + 1, 900)
            bg.speed = cfg.SPEED
            cfg.SPAWN_MIN = max(0.15, cfg.SPAWN_MIN - 0.001)
            cfg.SPAWN_MAX = max(0.4, cfg.SPAWN_MAX - 0.001)
            ast.point_effect.play()

        if score > high_score:
            if not beat_high_score and high_score > 0:
                ast.high_score_reached_effect.play()
            beat_high_score = True
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
                st.STATE_GAME_OVER = True

    bg.draw(screen)
    for t in traffic:
        t.draw(screen)
    car.draw(screen)

    score_text = cfg.FONT.render(str(score), True, (255, 255, 255))
    high_score_text = cfg.FONT.render(f"Best: {high_score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(high_score_text, high_score_text.get_rect(topright=(cfg.SCREEN_SIZE[0] - 10, 10)))

    if st.STATE_GAME_OVER:
        gameover.draw(screen, score, high_score)

    pygame.display.flip()

ut.save_high_score(high_score)
pygame.quit()