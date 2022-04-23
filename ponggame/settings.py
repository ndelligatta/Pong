import pygame 

class Settings:

    def __init__(self):
        self._screen_width = 800
        self._screen_height = 800
        self._player_width = 140
        self._player_height = 20

    def run(self):
        pygame.init()
        self._disp = pygame.display.set_mode((self._screen_width, self._screen_height))
        pygame.display.set_caption("Pong 22")
        return self._disp