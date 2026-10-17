import pygame
import configs as cfg

def draw(screen, score, high_score):
    overlay = pygame.Surface(cfg.SCREEN_SIZE, pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    screen.blit(overlay, (0, 0))

    cx = cfg.SCREEN_SIZE[0] // 2
    cy = cfg.SCREEN_SIZE[1] // 2

    title = cfg.FONT.render('GAME OVER', True, (255, 80, 80))
    result = cfg.FONT.render(f'Score {score}   Best: {high_score}', True, (255, 255, 255))
    prompt = cfg.FONT.render('Press [SPACE] to try again', True, (255, 255, 255))

    screen.blit(title, title.get_rect(center=(cx, cy - 60)))
    screen.blit(result, result.get_rect(center=(cx, cy)))
    screen.blit(prompt, prompt.get_rect(center=(cx, cy + 60)))