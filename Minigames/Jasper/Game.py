from Minigame import Minigame
import pygame
import random

class JasperGame(Minigame):
    def __init__(self):
        super(JasperGame, self).__init__("JasperGame", "Jasper", 3)

        self.largeFont = pygame.font.Font(self.getFilePath("/Shared/Fonts/neon-pixel.ttf"), 60)
        self.normalFont = pygame.font.Font(self.getFilePath("/Shared/Fonts/neon-pixel.ttf"), 40)

        self.previewPressToStartBlinkAnimationDelay = 0.75
        self.previewPressToStartBlinkAnimationCurrent = 0
        self.previewPressToStartBlinkAnimationIsVisible = True

        self.miniPreviewMainFont = pygame.font.Font(self.getFilePath("/Shared/Fonts/SanFrancisco.otf"), 11)
        self.playerImage = pygame.image.load(self.getFilePath("/Shared/Images/Jaspergame/skaterV2.png"))
        self.enemyImage = pygame.image.load(self.getFilePath("/Shared/Images/Jaspergame/EnemySkater.png"))

        self.playerX = 0
        self.playerY = 0

        self.enemyX = 0
        self.enemyY = 2

        self.playerDirection_UP = 0
        self.playerDirection_DOWN = 1
        self.playerDirection_RIGHT = 2
        self.playerDirection_LEFT = 3
        self.playerDirection = 0

        self.mapWidth = 10
        self.mapHeight = 7
        self.availableColors = [(45, 185, 7), (170, 11, 148), (255, 34, 34), (64, 120, 218), (180, 225, 225)]

        self.backgroundColors = [[0 for x in range(self.mapWidth)] for y in range(self.mapHeight)]

    def getRandomColor(self):
        index = random.randint(0, len(self.availableColors) - 1)
        return self.availableColors[index]

    def getTileWidth(self, surface):
        width = surface.get_width()
        return width / self.mapWidth

    def getTileHeight(self, surface):
        height = surface.get_height()
        return height / self.mapHeight

    def generateBackground(self):
        for y in range(self.mapHeight):
            for x in range(self.mapWidth):
                if y > self.mapHeight * 0.8:
                    self.backgroundColors[y][x] = (0, 0, 0)
                else:
                    self.backgroundColors[y][x] = self.getRandomColor()


    def drawBackground(self, surface):
        tileWidth = self.getTileWidth(surface)
        tileHeight = self.getTileHeight(surface)

        for y in range(self.mapHeight):
            for x in range(self.mapWidth):
                pygame.draw.rect(surface, self.backgroundColors[y][x], (x * tileWidth + 1, y * tileHeight + 1, tileWidth - 2, tileHeight - 2))

      # When a player starts this minigame
    def enter(self):
        self.generateBackground()

    # When a player leaves this minigame
    def leave(self):
        pass

    def handleEvents(self, events):
        for ev in events:
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RIGHT:
                    self.playerX += 1
                    if self.playerDirection == 0:
                        self.playerImage = pygame.transform.rotate(self.playerImage, -90)
                        self.playerDirection += 2
                    elif self.playerDirection == 1:
                        self.playerImage = pygame.transform.rotate(self.playerImage, 90)
                        self.playerDirection += 1
                    elif self.playerDirection == 2:
                        pass
                    elif self.playerDirection == 3:
                        self.playerImage = pygame.transform.rotate(self.playerImage, 180)
                        self.playerDirection -= 1
                elif ev.key == pygame.K_LEFT:
                    self.playerX -= 1
                    if self.playerDirection == 0:
                        self.playerImage = pygame.transform.rotate(self.playerImage, 90)
                        self.playerDirection += 3
                    elif self.playerDirection == 1:
                        self.playerImage = pygame.transform.rotate(self.playerImage, -90)
                        self.playerDirection += 2
                    elif self.playerDirection == 2:
                        self.playerImage = pygame.transform.rotate(self.playerImage, 180)
                        self.playerDirection += 1
                    elif self.playerDirection == 3:
                        pass
                elif ev.key == pygame.K_UP:
                    self.playerY -= 1
                    if self.playerDirection == 0:
                        pass
                    elif self.playerDirection == 1:
                        self.playerImage = pygame.transform.rotate(self.playerImage, 180)
                        self.playerDirection -= 1
                    elif self.playerDirection == 2:
                        self.playerImage = pygame.transform.rotate(self.playerImage, 90)
                        self.playerDirection -= 2
                    elif self.playerDirection == 3:
                        self.playerImage = pygame.transform.rotate(self.playerImage, -90)
                        self.playerDirection -=3
                elif ev.key == pygame.K_DOWN:
                    self.playerY += 1
                    if self.playerDirection == 0:
                        self.playerImage = pygame.transform.rotate(self.playerImage, 180)
                        self.playerDirection += 1
                    elif self.playerDirection == 1:
                        pass
                    elif self.playerDirection == 2:
                        self.playerImage = pygame.transform.rotate(self.playerImage, -90)
                        self.playerDirection -= 1
                    elif self.playerDirection == 3:
                        self.playerImage = pygame.transform.rotate(self.playerImage, 90)
                        self.playerDirection -= 2

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
        self.drawBackground(surface)
        surface.blit(self.playerImage, (self.playerX * self.getTileWidth(surface), self.playerY * self.getTileHeight(surface)))
        surface.blit(self.enemyImage, (self.enemyX * self.getTileWidth(surface), self.enemyY * self.getTileHeight(surface)))

    def drawPreview(self, surface):
        text = self.largeFont.render("Roller-Coder", True, (255, 255, 255))
        surface.blit(text, (surface.get_width() / 2 - text.get_width() / 2, 40))

        text = self.largeFont.render("--------------------------", True, (255, 255, 255))
        surface.blit(text, (surface.get_width() / 2 - text.get_width() / 2, 80))

        if self.previewPressToStartBlinkAnimationIsVisible:
            text = self.normalFont.render("Press Enter To Start", True, (255, 255, 255))
            surface.blit(text, (surface.get_width() / 2 - text.get_width() / 2, surface.get_height() - 100))

    def drawMiniPreview(self, surface):
        text = self.miniPreviewMainFont.render("Roller-Coder", True, (255, 255, 255))
        surface.blit(text, (surface.get_width() / 2 - text.get_width() / 2, 5))