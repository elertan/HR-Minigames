import os
import pygame
from random import randint

class GamePlayer(object):
    def __init__(self, minigame):
        self.minigame = minigame
    def handleEvents(self, events):
        for ev in events:
            pass
        self.minigame.handleEvents(events)
    def update(self, dt):
        self.minigame.update(dt)
    def draw(self, surface):
        s = surface.subsurface((20, 20, surface.get_width() - 40, surface.get_height() - 40))
        pygame.draw.rect(s, (0, 255, 0), (0,0,500,500))
        self.minigame.draw(s)