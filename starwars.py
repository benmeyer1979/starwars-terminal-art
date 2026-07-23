#!/usr/bin/env python3
"""Render Star Wars ASCII art in the terminal.

Usage:
    python starwars.py            # pick a random scene
    python starwars.py vader      # a specific scene by name
    python starwars.py --list     # show available scenes
"""

import random
import sys

# ANSI color helpers -------------------------------------------------------
RESET = "\033[0m"


def color(text, code):
    return f"\033[{code}m{text}{RESET}"


YELLOW = "38;5;226"
CYAN = "38;5;51"
RED = "38;5;196"
GREY = "38;5;250"
DIM = "38;5;240"
BLUE = "38;5;39"

# Scenes -------------------------------------------------------------------

DEATH_STAR = color(r"""
                 .-'''''-.
              .'  * * *  `.
             /  *  _____  *  \
            |  * .'     `. *  |
            | * /  .---.  \ * |
            |* |  / .-. \  | *|
            |* |  | | | |  | *|
            |* |  \ `-' /  | *|
            | * \  `---'  / * |
            |  * `.____.'  * |
             \  *  ` ` `  *  /
              `.  * * * *  .'
                `-.......-'
""", GREY) + color("\n        That's no moon...\n", DIM)


VADER = color(r"""
                 ______
              .-'      `-.
            .'            `.
           /   .------.     \
          ;   /  ____  \     ;
          |  |  / __ \  |    |
          |  | | /  \ | |    |
          ;  | | \__/ | |    ;
           \ |  \____/  |   /
            \|          |  /
          .--|  ||||||  |--.
         /   |  ||||||  |   \
        /    `.________.'    \
       |     /|        |\     |
       |    / |        | \    |
        \  /  |________|  \  /
         `'   |  |  |  |   `'
              |  |  |  |
""", RED) + color("\n     I find your lack of faith disturbing.\n", DIM)


TIE_FIGHTER = color(r"""
        |\                    /|
        | \                  / |
        |  \                /  |
        |   \    ______    /   |
        |    \  /      \  /    |
        |     \|  .--.  |/     |
        |======|  |()|  |======|
        |     /|  `--'  |\     |
        |    /  \      /  \    |
        |   /    `----'    \   |
        |  /                \  |
        | /                  \ |
        |/                    \|
""", CYAN) + color("\n              TIE Fighter incoming.\n", DIM)


R2D2 = color(r"""
             .-------.
            /  .---.  \
           /  / .-. \  \
          |  | | O | |  |
          |  | `-'  |  |
          |  |======|  |
          |  | .--. |  |
          |  | |[]| |  |
          |  | |  | |  |
          |  | `--' |  |
          |  |======|  |
          \  \______/  /
           \  .-''-.  /
            `.______.'
           .' | || | `.
          (___|_||_|___)
""", BLUE) + color("\n              Beep boop. R2-D2 reporting.\n", DIM)


LIGHTSABER = color(r"""
   o=========================================>
""", CYAN) + color("""   [ ][ ][ ][ ]
""", GREY) + color("\n         An elegant weapon for a more civilized age.\n", DIM)


YODA = color(r"""
              ____
           .-'    '-.
          /  ^    ^  \
         |   (o)(o)   |
         |     <      |
          \   \__/   /
       .---'--....--'---.
      /   /  ~~~~~~  \   \
     |   |  ~~~~~~~~  |   |
     |    \  ~~~~~~  /    |
      \    '-.____.-'    /
       '-.___________.-'
""", "38;5;120") + color('\n     Do. Or do not. There is no try.\n', DIM)


SCENES = {
    "deathstar": DEATH_STAR,
    "vader": VADER,
    "tie": TIE_FIGHTER,
    "r2d2": R2D2,
    "lightsaber": LIGHTSABER,
    "yoda": YODA,
}


def crawl_banner():
    """A little Star Wars-style intro banner."""
    lines = [
        "        A long time ago in a terminal far, far away....",
        "",
        "                   S T A R   W A R S",
    ]
    print()
    print(color(lines[0], YELLOW))
    print()
    print(color(lines[2], YELLOW))
    print()


def main(argv):
    if "--list" in argv or "-l" in argv:
        print("Available scenes:")
        for name in SCENES:
            print(f"  - {name}")
        return

    crawl_banner()

    args = [a for a in argv if not a.startswith("-")]
    if args:
        key = args[0].lower()
        scene = SCENES.get(key)
        if scene is None:
            print(color(f"Unknown scene '{key}'.", RED))
            print("Try one of: " + ", ".join(SCENES))
            return
    else:
        scene = random.choice(list(SCENES.values()))

    print(scene)
    print(color("      May the Force be with you.", YELLOW))
    print()


if __name__ == "__main__":
    main(sys.argv[1:])
