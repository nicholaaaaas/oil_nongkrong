from __future__ import annotations
from ast import List, Tuple
from typing import Optional
import pygame

FPS = 60
METAL_PLATE = 'oil_nongkrong/assets/metal_plate.png'


class Game():
    """
    Class representing the simulation.
    """
    size: Tuple[int, int]
    width: int
    height: int
    screen: Optional[pygame.Surface]

    _running: bool
    _metal_plate: pygame.Surface

    def __init__(self) -> None:
        """
        Initialize variables for this Class.
        """
        self.width, self.height = 1000, 750
        self.size = (self.width, self.height)
        self.screen = None
        self._running = True
        
        

    def new(self):
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill((190, 180, 164))
        pygame.display.flip()
        
        # sprites
        self._metal_plate = pygame.image.load(METAL_PLATE).convert_alpha()
        self._metal_plate = pygame.transform.scale(self._metal_plate, (600, 50))
        self.screen.blit(self._metal_plate, (30, 10))
        self.screen.blit(self._metal_plate, (30, 690))
        
    def run(self) -> None:
        """
        Run the Game until it ends or player quits.
        """
        while self._running:
            # pygame.time.wait(1000 // FPS)
            # set background color
            
            self._events()
            self._update()
            self._draw()

    def _update(self) -> None:
        """
        Updates sprite positions
        """
        pass  # TODO

    def _events(self) -> None:
        """
        Event handling of the game window
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)

    def _draw(self) -> None:
        """
        Draws the screen, grid, and objects/players on the screen
        """
        # TODO : Implement

        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.new()
    game.run()



