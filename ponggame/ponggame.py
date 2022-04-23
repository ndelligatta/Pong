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
        self._disp = self._st.run()
        self._space_toggle = False

    def process_input(self):
        pl = self._pl
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            pass
        elif keys[pygame.K_LEFT]:
            pl.move_left()
        elif keys[pygame.K_RIGHT]:
            pl.move_right()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self._space_toggle = not self._space_toggle
        if not self._space_toggle:
            self.process_input()


    def draw_screen(self):
        self._disp.fill(self._black)
        pygame.draw.rect(self._disp, self._white, self._pl.player())
        pygame.display.update()

    def run(self):
        while True:
            self.handle_events()
            self.draw_screen()
            