import pygame, math
from .settings import Settings

class Player:
    
    def __init__(self):
        self._st = Settings()
        self._speed = 10
        self._x = self._st._screen_width / 2 - self._st._player_width / 2
        self._y = (self._st._screen_height * (2 / 3)) - self._st._player_height / 2
        self._rect = (self._x, self._y, self._st._player_width, self._st._player_height)
    
    def move_left(self):
        self._x -= self._speed
    
    def move_right(self):
        self._x += self._speed

    def player(self):
        self._rect = (self._x, self._y, self._st._player_width, self._st._player_height)
        return self._rect
