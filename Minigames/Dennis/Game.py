from Minigame import Minigame
import pygame
import os
import math
from random import randint

class DennisGame(Minigame):
    SNAKE_DIRECTION_UP = 0
    SNAKE_DIRECTION_DOWN = 1
    SNAKE_DIRECTION_LEFT = 2
    SNAKE_DIRECTION_RIGHT = 3

    def __init__(self):
        super(DennisGame, self).__init__("SuperSnake", "Dennis", 1)

        self.gameOverFont = pygame.font.Font(self.getFilePath("/Shared/Fonts/neon-pixel.ttf"), 80)
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

        self.collectableBlockColor = (255, 0, 0)
        self.snakeBlockColor = (0, 255, 0)
        self.snakeHeadBlockColor = (19, 173, 19)

        self.points = 0
        self.pointsPerCollectible = 100

        self.snakeShouldGrow = False

        self.isGameOver = False

        self.snakeSpeed = 7500
        self.snakeCurrentDelay = 0
        self.snakeDelayTime = 1
        self.startGameCountdownCurrent = 0
        self.startGameCountdown = 3
        self.snakeDirection = DennisGame.SNAKE_DIRECTION_RIGHT
        self.snakeLastDirection = None

        self.snakeTailPositions = []
        self.snakeBaseTailLength = 3
        self.snakeCollectablePosition = (randint(0, self.mapWidth - 1), randint(0, self.mapHeight - 1))

    def restartGame(self):
        self.points = 0
        self.snakeCollectablePosition = (randint(0, self.mapWidth - 1), randint(0, self.mapHeight - 1))
        self.snakeSpeed = 7500
        self.snakeCurrentDelay = 0
        self.snakeDelayTime = 1
        self.startGameCountdown = 3
        self.snakeDirection = DennisGame.SNAKE_DIRECTION_RIGHT
        self.snakeLastDirection = None

        self.snakeShouldGrow = False

        self.isGameOver = False

        self.startGameCountdownCurrent = 0
        self.snakeTailPositions = []
        startX = math.floor(self.mapWidth / 2)
        startY = math.floor(self.mapHeight / 2)
        for x in range(0, self.snakeBaseTailLength + 1):
            posX = startX - x
            if posX < 0:
                posX = self.mapWidth + posX
            self.snakeTailPositions.append((posX, startY))

    def snakeCheckCollectible(self):
        currentPos = self.snakeTailPositions[0]
        collectibleX = self.snakeCollectablePosition[0]
        collectibleY = self.snakeCollectablePosition[1]
        if currentPos[0] == collectibleX and currentPos[1] == collectibleY:
            self.snakeCollectablePosition = (randint(0, self.mapWidth - 1), randint(0, self.mapHeight - 1))
            self.points += self.pointsPerCollectible
            self.snakeShouldGrow = True

    def snakeChangeDirection(self, dir):
        if dir == DennisGame.SNAKE_DIRECTION_DOWN and self.snakeLastDirection == DennisGame.SNAKE_DIRECTION_UP:
            return
        elif dir == DennisGame.SNAKE_DIRECTION_UP and self.snakeLastDirection == DennisGame.SNAKE_DIRECTION_DOWN:
            return
        elif dir == DennisGame.SNAKE_DIRECTION_LEFT and self.snakeLastDirection == DennisGame.SNAKE_DIRECTION_RIGHT:
            return
        elif dir == DennisGame.SNAKE_DIRECTION_RIGHT and self.snakeLastDirection == DennisGame.SNAKE_DIRECTION_LEFT:
            return
        else:
            self.snakeDirection = dir
            
    def snakeMove(self):
        dX = 0
        dY = 0
        if self.snakeDirection == DennisGame.SNAKE_DIRECTION_RIGHT:
            dX += 1
        elif self.snakeDirection == DennisGame.SNAKE_DIRECTION_LEFT:
            dX -= 1
        elif self.snakeDirection == DennisGame.SNAKE_DIRECTION_UP:
            dY -= 1
        elif self.snakeDirection == DennisGame.SNAKE_DIRECTION_DOWN:
            dY += 1
        
        currentPos = self.snakeTailPositions[0]
        newPos = (currentPos[0] + dX, currentPos[1] + dY)

        if newPos[0] > self.mapWidth - 1:
            newPos = (0, newPos[1])
        elif newPos[0] < 0:
            newPos = (self.mapWidth - 1, newPos[1])
        elif newPos[1] > self.mapHeight - 1:
            newPos = (newPos[0], 0)
        elif newPos[1] < 0:
            newPos = (newPos[0], self.mapHeight)

        for tailPos in self.snakeTailPositions:
            if newPos[0] == tailPos[0] and newPos[1] == tailPos[1]:
                self.isGameOver = True

        self.snakeTailPositions.insert(0, newPos)
        self.snakeLastDirection = self.snakeDirection

    def getBlockPositionByCoords(self, surface, x, y):
        blockWidth = surface.get_width() / self.mapWidth - self.blockPadding
        blockHeight = surface.get_height() / self.mapHeight - self.blockPadding

        sX = (blockWidth + self.blockPadding) * x + self.blockPadding * 2.5
        sY = (blockHeight + self.blockPadding) * y + self.blockPadding * 2.5
        sWidth = blockWidth + self.blockPadding / 2
        sHeight = blockHeight + self.blockPadding / 2

        return (sX, sY, sWidth, sHeight)
    
    def previewShown(self):
        pygame.mixer.music.load(self.getFilePath("/Shared/Music/dennis/background.ogg"))
        pygame.mixer.music.play(-1)

    # When a player starts this minigame
    def enter(self):
        self.restartGame()

    # When a player leaves this minigame
    def leave(self):
        self.isGameOver = False
        self.points = 0

    def handleEvents(self, events):
        for ev in events:
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_LEFT:
                    self.snakeChangeDirection(DennisGame.SNAKE_DIRECTION_LEFT)
                elif ev.key == pygame.K_RIGHT:
                    self.snakeChangeDirection(DennisGame.SNAKE_DIRECTION_RIGHT)
                elif ev.key == pygame.K_UP:
                    self.snakeChangeDirection(DennisGame.SNAKE_DIRECTION_UP)
                elif ev.key == pygame.K_DOWN:
                    self.snakeChangeDirection(DennisGame.SNAKE_DIRECTION_DOWN)
                elif ev.key == pygame.K_RETURN:
                    if self.isGameOver:
                        self.restartGame()

    # Gets called on every frame
    def update(self, dt):
        if self.isGameOver:
            return

        if self.startGameCountdownCurrent < self.startGameCountdown:
            self.startGameCountdownCurrent += dt
            return

        if self.snakeCurrentDelay < self.snakeDelayTime:
            self.snakeCurrentDelay += self.snakeSpeed * dt / 1000
        else:
            self.snakeCurrentDelay = 0
            self.snakeMove()
            self.snakeCheckCollectible()

            if not self.snakeShouldGrow:
                self.snakeTailPositions.pop()
            else:
                self.snakeShouldGrow = False


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
        pygame.draw.rect(snakeSurface, (0,0,0), (3, 3, snakeSurface.get_width() - 6, snakeSurface.get_height() - 6))

        # for y in range(0, self.mapHeight):
        #     for x in range(0, self.mapWidth):
        #         pygame.draw.rect(snakeSurface, 
        #             (0,0,0), 
        #             self.getBlockPositionByCoords(snakeSurface, x, y))

        isHead = True
        for part in self.snakeTailPositions:
            color = self.snakeBlockColor
            if isHead:
                color = self.snakeHeadBlockColor
                isHead = False
            pygame.draw.rect(snakeSurface, 
                    color, 
                    self.getBlockPositionByCoords(snakeSurface, part[0], part[1]))

        pygame.draw.rect(snakeSurface,
                    self.collectableBlockColor,
                    self.getBlockPositionByCoords(snakeSurface, self.snakeCollectablePosition[0], self.snakeCollectablePosition[1]))

        if self.isGameOver:
            text = self.gameOverFont.render("Game Over", True, (255,255,255))
            snakeSurface.blit(text, (snakeSurface.get_width()  / 2 - text.get_width() / 2, snakeSurface.get_height() / 2 - text.get_height() / 2))

            text = self.normalFont.render("Press [Enter] to start a new game", True, (255,255,255))
            snakeSurface.blit(text, (snakeSurface.get_width()  / 2 - text.get_width() / 2, snakeSurface.get_height() / 2 - text.get_height() / 2 + 75))

        # Menu Part
        text = self.normalFont.render(str(self.points).zfill(6), True, (255,255,255))
        surface.blit(text, (50, surface.get_height() - text.get_height() - 20))

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