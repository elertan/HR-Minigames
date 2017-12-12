from Minigame import Minigame
from Minigames.Gavin.gameElements.map import map
from Minigames.Gavin.gameElements.textImput import code
from Minigames.Gavin.gameElements.buttons import button
from Minigames.Gavin.gameElements.player import player
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
        self.done = False
        self.started = 0

        self.map = map(self.getFilePath(""))
        self.player = player(self.getFilePath(""))
        self.code = code()
        self.button = button()

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
        self.code.imput(events)
        if self.button.click(events):
            self.code.check()

    # Gets called on every frame
    def update(self, dt):
        if self.code.gameRank == 1:
            self.map.map()
            self.player.walk()

    # Gets called on every frame
    def updatePreview(self, dt):
        pass

    def updateMiniPreview(self, dt):
        pass

    # Draw the current game state
    def draw(self, surface):
        self.map.draw(surface)
        self.code.render(surface)
        self.button.draw(surface)
        self.player.draw(surface)
        #if self.code.playerSmile < 20:
        #    self.player.smile(surface)
        #    self.code.playerSmile += 1
        #elif self.code.playerMad < 20:
        #    self.player.mad(surface)
        #    self.code.playerMad += 1

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

