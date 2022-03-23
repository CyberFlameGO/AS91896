import asyncio
import os
from typing import Sequence, Union
import sqlite3

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

# The environment variable needs to be set before importing pygame
import pygame  # noqa: E402 isort: skip

DISPLAY_WIDTH: int = 500
DISPLAY_HEIGHT: int = 500
WHITE: tuple[int, int, int] = (255, 255, 255)
BLACK: tuple[int, int, int] = (0, 0, 0)
DEEP_RED: tuple[int, int, int] = (255, 0, 0)

pygame.init()
clock = pygame.time.Clock()

display_surface: Union[pygame.Surface, pygame.SurfaceType] = pygame.display.set_mode(
    (DISPLAY_WIDTH, DISPLAY_HEIGHT)
)


class Player(object):
    """
    Player class oh yeah
    """

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.bounding_box = None  # TODO: use this variable to detect if on platform


def main():
    """
    Main runner function
    """

    player = Player(DISPLAY_WIDTH, DISPLAY_HEIGHT - 65, 40, 60)
    pygame.display.set_caption("Jumpy Blob")
    playing: bool = True
    while playing:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.KEYDOWN:
                pass
        keys: Sequence[bool] = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pass


if __name__ == '__main__':
    main()
