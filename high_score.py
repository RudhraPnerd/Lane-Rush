import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HIGH_SCORE_FILE = os.path.join(BASE_DIR, "high_score.txt")


def load_high_score():
    try:
        with open(HIGH_SCORE_FILE, "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0


def save_high_score(high_score):
    with open(HIGH_SCORE_FILE, "w") as f:
        f.write(str(high_score))