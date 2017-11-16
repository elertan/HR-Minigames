import pygame
import os

class Minigame(object):
    name=""
    author=""
    identifier = 0
    def __init__(self, name, author, identifier):
        self.name = name
        self.author = author
        self.identifier = identifier

        dirname = os.path.dirname(os.path.realpath(__file__))

        self.font16 = pygame.font.Font(dirname + "/Shared/Fonts/SanFrancisco.otf", 16)

    # When a player starts this minigame
    def enter(self):
        raise NotImplementedError("You need to override the enter method on your minigame.")

    # When a player leaves this minigame
    def leave(self):
        raise NotImplementedError("You need to override the leave method on your minigame.")

    def handleEvents(self, events):
        raise NotImplementedError("You need to override the handleEvents method on your minigame.")

    # Gets called on every frame
    def update(self, dt):
        raise NotImplementedError("You need to override the update method on your minigame.")

    # Gets called on every frame
    def updatePreview(self, dt):
        pass

    def updateMiniPreview(self, dt):
        pass

    # Draw the current game state
    def draw(self, surface):
        raise NotImplementedError("You need to override the draw method on your minigame.")

    def drawPreview(self, surface):
        pygame.draw.rect(surface, (0, 0, 230), (0,0,surface.get_width(), surface.get_height()))
        text = self.font16.render(str(surface.get_width()) + "px by " + str(surface.get_height()) + "px", True, (255, 255, 255))
        surface.blit(text, (surface.get_width() / 2 - 60, surface.get_height() / 2 - 20))

    def drawMiniPreview(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), (0, 0, surface.get_width(), surface.get_height()))