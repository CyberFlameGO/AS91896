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

window_size: tuple[int, int] = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
display_surface: Union[pygame.Surface, pygame.SurfaceType] = pygame.display.set_mode(
    (DISPLAY_WIDTH, DISPLAY_HEIGHT)
)


class Player(object):
    """
    Player class oh yeah
    """

    # TODO: add display width/height as params here
    def __init__(self, display_size, width, height):
        self.width: int = width
        self.height: int = height
        self.display_width, self.display_height = display_size
        self.x = (self.display_width - self.width) // 2
        self.y = (self.display_height - self.height) - 4
        self.velocity = 5
        self.bounding_box = None  # TODO: use this variable to detect if on platform


def main():
    """
    Main runner function
    """

    player = Player(window_size, 40, 60)
    velocity = 5
    width: int = 40
    height: int = 60
    pygame.display.set_caption("Jumpy Blob")
    playing: bool = True
    while playing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.KEYDOWN:
                pass

        keys: Sequence[bool] = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if player.x > velocity:
                player.x -= velocity
        if keys[pygame.K_RIGHT]:
            if player.x < DISPLAY_WIDTH - width - velocity:
                player.x += velocity
        display_surface.fill(BLACK)
        red_rectangle = (
            pygame.draw.rect(display_surface, DEEP_RED, (player.x, player.y, player.width, player.height))
        )
        if (
                red_rectangle  # remove this later when there's a proper use for the variable.
        ):
            pass
        pygame.display.update()


if __name__ == '__main__':
    main()
