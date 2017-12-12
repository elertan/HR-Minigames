import os
import pygame
from random import randint

class GamePlayer(object):
    def __init__(self, minigame, menu):
        self.menu = menu
        self.minigame = minigame
        self.isInPreview = True

        dirname = os.path.dirname(os.path.realpath(__file__))

        self.borderImages = []
        for i in range(0, 6):
            self.borderImages.append(pygame.image.load(dirname + "/Shared/Images/game/game-border-" + str(i + 1) + ".png"))

        self.minigame.previewShown()
    def handleEvents(self, events):
        for ev in events:
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    # Go to preview or go to home menu
                    if self.isInPreview:
                        self.menu.leaveGame()
                    else:
                        self.minigame.leave()
                        self.isInPreview = True
                elif ev.key == pygame.K_RETURN and self.isInPreview:
                    self.isInPreview = False
                    # pygame.mixer.music.stop()
                    self.minigame.enter()
        if not self.isInPreview:
            self.minigame.handleEvents(events)
    def update(self, dt):
        if self.isInPreview:
            self.minigame.updatePreview(dt)
            return
        self.minigame.update(dt)
    def draw(self, surface):
        s = surface
        if not self.minigame.gameRequiresFullscreen:
            s = surface.subsurface((5, 5, surface.get_width() - 10, surface.get_height() - 10))
        if self.isInPreview:
            self.minigame.drawPreview(s)
        else:
            self.minigame.draw(s)
        surface.blit(self.borderImages[self.minigame.identifier], (0,0))
        self.minigame.endFrame()