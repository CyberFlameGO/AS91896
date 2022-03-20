import os
from typing import Union

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

# (explain why it's not ordered correct)
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

def main():
    pass




if __name__ == '__main__':
    main()

