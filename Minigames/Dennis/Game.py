from Minigame import Minigame
import pygame
import os
import math
from random import randint

class DennisGame(Minigame):
    def __init__(self):
        super(DennisGame, self).__init__("SuperSnake", "Dennis", 1)

        self.largeFont = pygame.font.Font(self.getFilePath("/Shared/Fonts/neon-pixel.ttf"), 60)
        self.normalFont = pygame.font.Font(self.getFilePath("/Shared/Fonts/neon-pixel.ttf"), 40)

        self.previewPressToStartBlinkAnimationDelay = 0.75
        self.previewPressToStartBlinkAnimationCurrent = 0
        self.previewPressToStartBlinkAnimationIsVisible = True

        self.miniPreviewMainFont = pygame.font.Font(self.getFilePath("/Shared/Fonts/SanFrancisco.otf"), 11)
        self.miniPreviewSnakeOffsetIncrementDelayCurrent = 0
        self.miniPreviewSnakeOffsetIncrementDelay = 1
        self.miniPreviewSnakeOffset = 0

        self.mapWidth = 20
        self.mapHeight = 12
        self.blockPadding = 2

        self.collectableBlockColor = (230, 230, 230)
        self.snakeBlockColor = (0, 255, 0)

        self.startGameCountdownCurrent = 0
        self.startGameCountdown = 3
        self.snakeTailPositions = []
        self.snakeBaseTailLength = 3
        self.snakeCollectablePosition = (randint(0, self.mapWidth), randint(0, self.mapHeight))
    
    def previewShown(self):
        pygame.mixer.music.load(self.getFilePath("/Shared/Music/dennis/background.ogg"))
        pygame.mixer.music.play(-1)

    # When a player starts this minigame
    def enter(self):
        self.startGameCountdownCurrent = 0
        self.snakeTailPositions = []
        startX = math.floor(self.mapWidth / 2)
        startY = math.floor(self.mapHeight / 2)
        for x in range(0, self.snakeBaseTailLength + 1):
            posX = startX - x
            if posX < 0:
                posX = self.mapWidth + posX
            self.snakeTailPositions.append((posX, startY))

    # When a player leaves this minigame
    def leave(self):
        pass

    def handleEvents(self, events):
        pass

    # Gets called on every frame
    def update(self, dt):
        if self.startGameCountdownCurrent < self.startGameCountdown:
            self.startGameCountdownCurrent += dt
            return

    # Gets called on every frame
    def updatePreview(self, dt):
        self.previewPressToStartBlinkAnimationCurrent += dt
        if self.previewPressToStartBlinkAnimationCurrent > self.previewPressToStartBlinkAnimationDelay:
            self.previewPressToStartBlinkAnimationIsVisible = not self.previewPressToStartBlinkAnimationIsVisible
            self.previewPressToStartBlinkAnimationCurrent = 0

    def updateMiniPreview(self, dt):
        self.miniPreviewSnakeOffsetIncrementDelayCurrent += dt
        if self.miniPreviewSnakeOffsetIncrementDelayCurrent > self.miniPreviewSnakeOffsetIncrementDelay:
            self.miniPreviewSnakeOffsetIncrementDelayCurrent = 0
            self.miniPreviewSnakeOffset += 1
        
        if self.miniPreviewSnakeOffset > 8:
            self.miniPreviewSnakeOffset = 0

    # Draw the current game state
    def draw(self, surface):
        snakeSurface = surface.subsurface((20, 20, surface.get_width() - 40, surface.get_height() - 100))
        snakeSurface.fill((255,255,255))

        blockWidth = snakeSurface.get_width() / self.mapWidth - self.blockPadding
        blockHeight = snakeSurface.get_height() / self.mapHeight - self.blockPadding

        for y in range(0, self.mapHeight):
            for x in range(0, self.mapWidth):
                pygame.draw.rect(snakeSurface, 
                    (0,0,0), 
                    ((blockWidth + self.blockPadding) * x + self.blockPadding, 
                        (blockHeight + self.blockPadding) * y + self.blockPadding,
                        blockWidth + self.blockPadding / 2,
                        blockHeight + self.blockPadding / 2))

        if self.startGameCountdownCurrent < self.startGameCountdown:
            countdown = math.ceil(self.startGameCountdown - self.startGameCountdownCurrent)
            text = self.normalFont.render("Starting in " + str(countdown), True, (255,255,255))
            surface.blit(text, (surface.get_width() / 2 - text.get_width() / 2, surface.get_height() - 60))
    
    def drawPreview(self, surface):
        text = self.largeFont.render("SuperSnake", True, (255,255,255))
        surface.blit(text, (surface.get_width() / 2 - text.get_width() / 2, 40))

        text = self.largeFont.render("--------------------------", True, (255,255,255))
        surface.blit(text, (surface.get_width() / 2 - text.get_width() / 2, 80))

        if self.previewPressToStartBlinkAnimationIsVisible:
            text = self.normalFont.render("Press Enter To Start", True, (255,255,255))
            surface.blit(text, (surface.get_width() / 2 - text.get_width() / 2, surface.get_height() - 100))

    # def drawPreview(self, surface):
    #     raise NotImplementedError("You need to override the drawPreview method on your minigame.")

    def drawMiniPreview(self, surface):
        text = self.miniPreviewMainFont.render("SuperSnake", True, (255,255,255))
        surface.blit(text, (surface.get_width() / 2 - text.get_width() / 2, 5))

        # text = self.miniPreviewMainFont.render("-----------", True, (255,255,255))
        # surface.blit(text, (11, 11))

        x = 0
        y = 25
        height = 4
        width = 4

        pygame.draw.rect(surface, (230, 230, 230), (x + width * 10, y, width - 1, height))

        for i in range(0, 6):
            pygame.draw.rect(surface, (0, 200, 0), (width * (i + self.miniPreviewSnakeOffset), y, width - 1, height))