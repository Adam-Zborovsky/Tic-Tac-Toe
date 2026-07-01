# Tic-Tac-Toe

> A polished Tic-Tac-Toe game built with Pygame, featuring animated piece placement and cinematic win/tie screens.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Highlights

- **Animated piece placement** — X marks are drawn stroke-by-stroke; O circles expand outward in a smooth animation.
- **Win celebration** — a bold strike-through line animates across the winning three, followed by a victory screen.
- **Tie screen** — a clean "It's a Tie" display on match draw.
- **Auto-reset** — game restarts automatically 1.5 seconds after a result, enabling rapid play.
- **Clean OOP architecture** — polymorphic `Piece` → `X` / `O` hierarchy with a `Board` controller.

## Architecture

```
┌─────────────┐     ┌──────────────┐
│   Game.py   │────▶│  Board       │
│  (main)     │     │  (controller)│
└─────────────┘     └──────┬───────┘
                           │ owns
                    ┌──────▼───────┐
                    │  Piece[]     │
                    │  (abstract)  │
                    └──────┬───────┘
                           │ inherits
              ┌────────────┼────────────┐
              ▼            │            ▼
         ┌────────┐        │       ┌────────┐
         │   X    │        │       │   O    │
         │ (draw) │        │       │ (draw) │
         └────────┘        │       └────────┘
```

- **`Game.py`** — entry point, event loop, mouse-to-grid mapping, turn alternation.
- **`Board`** — owns the 3×3 grid state, validates moves, checks win/tie conditions, renders win/tie animations.
- **`Piece`** — abstract base class storing `(x, y)` grid coordinates.
- **`X` / `O`** — concrete subclasses implementing `draw(screen)` with per-piece animations.

## Tech Stack

| Layer         | Technology     | Notes                                      |
|---------------|----------------|--------------------------------------------|
| Language      | Python 3.8+    | No dependencies beyond the standard library |
| Rendering     | Pygame 2.0+    | Window management, 2D draw primitives       |
| Window        | 800 × 800 px   | Hardcoded; resizing not currently supported |
| Font          | David (system) | Falls back to Pygame default on non-Windows |

## Project Structure

```
Tic-Tac-Toe/
├── Game.py         # Entry point: event loop, input, turn logic
├── Boards.py       # Board controller: grid state, win check, end screens
├── Pieces.py       # Abstract Piece base class
├── Xs.py           # X piece with animated draw
├── Os.py           # O piece with animated draw
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8 or newer
- Pygame 2.0 or newer

### Installation

```bash
# Clone the repository
git clone https://github.com/Adam-Zborovsky/Tic-Tac-Toe.git
cd Tic-Tac-Toe

# (Optional) Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# Install Pygame
pip install pygame
```

### Run

```bash
python Game.py
```

Click any cell on the 3×3 grid to place your piece. X goes first, then O. The game auto-restarts after each round.

## Engineering Notes

### Design Decisions

- **Polymorphic pieces**: `X` and `O` inherit from `Piece` and each implements its own `draw()` with distinct animations. Adding a new piece type requires only a new subclass.
- **Board as state owner**: `Board` encapsulates all game logic — grid management, validation, win detection, and end-screen rendering. `Game.py` handles only the event loop and I/O mapping.
- **Mouse-to-grid mapping**: `set_position()` maps raw pixel coordinates to `(col, row)` tuples using hardcoded hit regions. A future refactor could replace this with arithmetic from cell dimensions.

### Animation Mechanics

- **X draw**: two diagonal lines grow outward simultaneously by 0.1 px per frame, creating a hand-drawn effect.
- **O draw**: concentric circles expand from radius 1 to radius 95, drawn in white with a black fill behind to erase the expanding ring.
- **Win line**: a thick (55 px) stroke is drawn from the first to the last cell of the winning triplet, with circular caps.
- All animations use `pygame.display.update()` for incremental rendering without double-buffering flicker.

### Known Limitations

- **Font portability**: `pygame.font.SysFont("David", 200)` references a Windows-specific font. On Linux/macOS, Pygame falls back to its default font, which may render at a different size.
- **Magic numbers**: grid cell positions, animation step values, and screen dimensions are hardcoded rather than derived from constants.
- **`eval()` usage**: `Game.py:62` uses `eval(f'board.{valid}(screen)')` where `valid` is `'win'` or `'tie'`. The input is controlled (not user-supplied), but `getattr(board, valid)(screen)` is preferred.
- **No input validation outside grid**: clicking outside the board returns `(0,0)` which silently fails — no visual feedback.

## Roadmap

- [ ] Replace hardcoded positions with computed grid geometry
- [ ] Support dynamic window resizing
- [ ] Add a score tracker across rounds
- [ ] Replace `eval()` with `getattr()`
- [ ] Cross-platform font fallback with configurable rendering
- [ ] Add CLI mode for headless play
- [ ] Write unit tests for `Board.check_win()`

## License

MIT — see the [LICENSE](LICENSE) file for details.
