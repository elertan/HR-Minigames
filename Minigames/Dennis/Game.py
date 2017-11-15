from Minigame import Minigame
import pygame
import os

class DennisGame(Minigame):
    def __init__(self):
        super(DennisGame, self).__init__("SuperSnake", "Dennis")
        dirname = os.path.dirname(os.path.realpath(__file__))

        self.miniPreviewMainFont = pygame.font.Font(dirname + "/../../Shared/Fonts/SanFrancisco.otf", 11)
        self.miniPreviewSnakeOffsetIncrementDelayCurrent = 0
        self.miniPreviewSnakeOffsetIncrementDelay = 1
        self.miniPreviewSnakeOffset = 0
    
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
        raise NotImplementedError("You need to override the updatePreview method on your minigame.")

    def updateMiniPreview(self, dt):
        self.miniPreviewSnakeOffsetIncrementDelayCurrent += dt
        if self.miniPreviewSnakeOffsetIncrementDelayCurrent > self.miniPreviewSnakeOffsetIncrementDelay:
            self.miniPreviewSnakeOffsetIncrementDelayCurrent = 0
            self.miniPreviewSnakeOffset += 1
        
        if self.miniPreviewSnakeOffset > 8:
            self.miniPreviewSnakeOffset = 0

    # Draw the current game state
    def draw(self, surface):
        raise NotImplementedError("You need to override the draw method on your minigame.")

    def drawPreview(self, surface):
        raise NotImplementedError("You need to override the drawPreview method on your minigame.")

    def drawMiniPreview(self, surface):
        text = self.miniPreviewMainFont.render("SuperSnake", True, (255,255,255))
        surface.blit(text, (9, 5))

        # text = self.miniPreviewMainFont.render("-----------", True, (255,255,255))
        # surface.blit(text, (11, 11))

        x = 0
        y = 25
        height = 4
        width = 4

        pygame.draw.rect(surface, (230, 230, 230), (x + width * 10, y, width - 1, height))

        for i in range(0, 6):
            pygame.draw.rect(surface, (0, 200, 0), (width * (i + self.miniPreviewSnakeOffset), y, width - 1, height))