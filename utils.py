import os
import sys
import configs as cfg
import states as st

# next to the .exe when bundled, next to this file when running from source
if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HIGH_SCORE_FILE = os.path.join(BASE_DIR, "high_score.txt")

START_SPEED = cfg.SPEED
START_SPAWN_MIN = cfg.SPAWN_MIN
START_SPAWN_MAX = cfg.SPAWN_MAX


def load_high_score():
    try:
        with open(HIGH_SCORE_FILE, "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0


def save_high_score(high_score):
    with open(HIGH_SCORE_FILE, "w") as f:
        f.write(str(high_score))


def reset_game(bg, car, high_score):
    save_high_score(high_score)

    cfg.SPEED = START_SPEED
    cfg.SPAWN_MIN = START_SPAWN_MIN
    cfg.SPAWN_MAX = START_SPAWN_MAX
    bg.speed = cfg.SPEED

    car.rect.center = (cfg.SCREEN_SIZE[0] // 2, cfg.SCREEN_SIZE[1] - 100)
    car.x = float(car.rect.x)

    st.STATE_GAME_OVER = False

    # score, score_timer, spawn_timer, beat_high_score, traffic
    return 0, 0, 0, False, []