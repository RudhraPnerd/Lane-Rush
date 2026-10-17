# Contributing to Lane Rush

Thanks for your interest in contributing! Lane Rush is a small Pygame project where you dodge traffic on a scrolling road, and all kinds of help are welcome: bug fixes, new features, art, sound, and documentation.

## Getting started

1. **Fork** the repository and clone your fork:

   ```bash
   git clone https://github.com/RudhraPnerd/Lane-Rush.git
   cd Lane-Rush
   ```

2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS / Linux
   ```

3. **Install Pygame**:

   ```bash
   pip install pygame
   ```

4. **Run the game** from the project root:

   ```bash
   python main.py
   ```

> [!NOTE]
> Always run the game from the project root so relative imports and asset paths resolve correctly.

## Project structure

| Path | Purpose |
|------|---------|
| `main.py` | Game loop, input, scoring, and drawing |
| `configs.py` | Settings such as screen size, lanes, speeds, and file paths |
| `assets.py` | Loads images, sounds, and fonts (call `load_assets()` after `set_mode()`) |
| `objects.py` | Game classes: `Background`, `Car`, `Traffic` |
| `utils.py` | Helpers: high score load/save and game reset |
| `states.py` | Game state flags |
| `displays/` | Screens such as the game over overlay |
| `assets/` | Sprites, audio, and fonts |

## How to contribute

### Reporting bugs

Open an issue and include:

- What you expected to happen and what actually happened
- Steps to reproduce the problem
- Your operating system and Python and Pygame versions
- The full error message or traceback, if there is one

### Suggesting features

Open an issue describing the idea and why it would improve the game. Small, focused ideas (a new power-up, a new traffic type, a menu screen) are easiest to review.

### Submitting a pull request

1. Create a branch from `main`:

   ```bash
   git checkout -b feature/short-description
   ```

2. Make your changes and **play-test them**. There's no automated test suite yet, so run the game and check that nothing else broke.
3. Commit with a clear message:

   ```bash
   git commit -m "Add fuel pickups"
   ```

4. Push your branch and open a pull request describing what you changed and why. Screenshots or a short GIF help a lot for visual changes.

Keep pull requests small and focused on one thing. If you're planning something big, open an issue first so we can talk it through.

## Code guidelines

- Follow [PEP 8](https://peps.python.org/pep-0008/) and use clear, descriptive names.
- Put tunable values (speeds, sizes, spawn rates, paths) in `configs.py` instead of hardcoding them.
- Load images, fonts, and sounds **once**, in `assets.load_assets()`, never inside the game loop.
- Multiply movement by `dt` so the game runs at the same speed on every computer.
- Don't create fonts or load images at the top level of a module. They need `pygame.init()` and a display to exist first.
- Keep new screens or overlays in the `displays/` folder.

## Assets

- Use only images, sounds, and fonts you created or that are licensed for reuse, and credit the source in your pull request.
- Prefer `.png` for sprites, `.wav` for sound effects, and `.ogg` for music.
- Keep file sizes small so the repository stays light.

> [!IMPORTANT]
> Don't commit `high_score.txt`, `__pycache__/`, or virtual environment folders. They are listed in `.gitignore`.

## Questions

Not sure where to start? Open an issue with the question label, and we'll point you in the right direction.