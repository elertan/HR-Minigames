from Minigame import Minigame
import pygame
import os


class GavinGame(Minigame):
    def __init__(self):
        super(GavinGame, self).__init__("Platformer Python", "Gavin", 1)

        self.largeFont = pygame.font.Font(self.getFilePath("/Shared/Fonts/neon-pixel.ttf"), 60)
        self.normalFont = pygame.font.Font(self.getFilePath("/Shared/Fonts/neon-pixel.ttf"), 40)

        self.previewPressToStartBlinkAnimationDelay = 0.75
        self.previewPressToStartBlinkAnimationCurrent = 0
        self.previewPressToStartBlinkAnimationIsVisible = True

        self.miniPreviewMainFont = pygame.font.Font(self.getFilePath("/Shared/Fonts/SanFrancisco.otf"), 11)

    def previewShown(self):
        pygame.mixer.music.load(self.getFilePath("/Shared/Music/dennis/background.ogg"))
        pygame.mixer.music.play(-1)

    # When a player starts this minigame
    def enter(self):
        pass

    # When a player leaves this minigame
    def leave(self):
        pass

    def handleEvents(self, events):
        pass

    # Gets called on every frame
    def update(self, dt):
        pass

    # Gets called on every frame
    def updatePreview(self, dt):
        pass

    def updateMiniPreview(self, dt):
        pass

    # Draw the current game state
    def draw(self, surface):
        pass

    def drawPreview(self, surface):
        text = self.largeFont.render("Python Platformer", True, (255, 255, 255))
        surface.blit(text, (surface.get_width() / 2 - text.get_width() / 2, 40))

        text = self.largeFont.render("--------------------------", True, (255, 255, 255))
        surface.blit(text, (surface.get_width() / 2 - text.get_width() / 2, 80))

        if self.previewPressToStartBlinkAnimationIsVisible:
            text = self.normalFont.render("Press Enter To Start", True, (255, 255, 255))
            surface.blit(text, (surface.get_width() / 2 - text.get_width() / 2, surface.get_height() - 100))

    # def drawPreview(self, surface):
    #     raise NotImplementedError("You need to override the drawPreview method on your minigame.")

    def drawMiniPreview(self, surface):
        text = self.miniPreviewMainFont.render("Platformer", True, (255, 255, 255))
        surface.blit(text, (surface.get_width() / 2 - text.get_width() / 2, 5))

