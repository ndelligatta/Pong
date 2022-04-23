import pygame, sys
from .settings import Settings
from .player import Player

class PongGame:
    def __init__(self):
        self._st = Settings()
        self._pl = Player()
        self._white = (255, 255, 255)
        self._black = (0, 0, 0)
        self._red = (255, 0, 0)
        self._instance = None

    def process_input(self):
        pl = self._pl
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            pass
        elif keys[pygame.K_LEFT]:
            pl.move_left()
        elif keys[pygame.K_RIGHT]:
            pl.move_right()
    def run(self):
        st = self._st
        disp = st.run()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.process_input()
            disp.fill(self._black)
            pygame.draw.rect(disp, self._white, self._pl.player())
            pygame.display.update()