import os
import pygame
from random import randint
from GamePlayer import GamePlayer

class Menu(object):
    IMAGE_ARCADE_MACHINE_WIDTH = 160
    IMAGE_ARCADE_MACHINE_HEIGHT = 250

    def __init__(self, minigames):
        self.headerColor = (255,255,255)
        self.footerColor = (255,255,255)
        self.minigameTextColor = (255,255,255)
        self.minigameTextActiveColor = (255,0,0)

        self.dirname = os.path.dirname(os.path.realpath(__file__))

        self.backgroundImage = pygame.image.load(self.getFilePath("/Shared/Images/menu/background.jpg"))
        self.headerFont = pygame.font.Font(self.getFilePath("/Shared/Fonts/SanFrancisco.otf"), 21)
        self.mainFont = pygame.font.Font(self.getFilePath("/Shared/Fonts/SanFrancisco.otf"), 20)
        self.minigameFont = pygame.font.Font(self.getFilePath("/Shared/Fonts/SanFrancisco.otf"), 18)
        self.footerFont = pygame.font.Font(self.getFilePath("/Shared/Fonts/SanFrancisco.otf"), 16)

        pygame.mixer.music.load(self.getFilePath("/Shared/Music/menu/music" + str(randint(1,2)) + ".ogg"))
        pygame.mixer.music.play(-1)

        self.minigames = minigames
        self.gamePlayer = None

        self.minigameArcadeMachineImages = []
        for i in range(0, 6):
            self.minigameArcadeMachineImages.append(pygame.image.load(self.getFilePath("/Shared/Images/menu/arcade-machine-" + str(i + 1) + ".png")))
        self.minigameArcadeMachineGlowImage = pygame.image.load(self.getFilePath("/Shared/Images/menu/arcade-machine-glow.png"))
        self.minigameArcadeMachineActiveArrow = pygame.image.load(self.getFilePath("/Shared/Images/menu/arrow.png"))

        self.arrowAnimationIncreasing = True
        self.arrowAnimationCurrent = 0
        self.arrowAnimationMax = 15
        self.arrowAnimationSpeed = 15
        self.gameSelectedIndex = 0

        self.curtainAnimationIsPlaying = False
        self.curtainAnimationIncreasing = True
        self.curtainAnimationSpeed = 750
        self.curtainAnimationMiddleTimeoutDelayCurrent = 0
        self.curtainAnimationMiddleTimeoutDelay = 0.6
        self.curtainAnimationCurrent = 0

    def getFilePath(self, relativePath):
        return self.dirname + relativePath

    def handleEvents(self, events):
        if (self.gamePlayer != None):
            self.gamePlayer.handleEvents(events)
            return
        if (self.curtainAnimationIsPlaying):
            return
        for ev in events:
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_LEFT:
                    if self.gameSelectedIndex == 0:
                        self.gameSelectedIndex = len(self.minigames) - 1
                    else:
                        self.gameSelectedIndex -= 1
                elif ev.key == pygame.K_RIGHT:
                    if self.gameSelectedIndex == len(self.minigames) - 1:
                        self.gameSelectedIndex = 0
                    else:
                        self.gameSelectedIndex += 1
                elif ev.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    self.curtainAnimationIsPlaying = True
    def update(self, dt):
        if self.curtainAnimationIsPlaying:
            if self.curtainAnimationIncreasing:
                self.curtainAnimationCurrent += self.curtainAnimationSpeed * dt
                if self.curtainAnimationCurrent > 400:
                    self.curtainAnimationIncreasing = False
                    self.curtainAnimationCurrent = 400
            else:
                if self.gamePlayer is None:
                    self.gamePlayer = GamePlayer(self.minigames[self.gameSelectedIndex], self)
                if self.curtainAnimationMiddleTimeoutDelayCurrent < self.curtainAnimationMiddleTimeoutDelay:
                    self.curtainAnimationMiddleTimeoutDelayCurrent += dt
                else:
                    self.curtainAnimationCurrent -= self.curtainAnimationSpeed * dt
                    if self.curtainAnimationCurrent < 0:
                        self.curtainAnimationMiddleTimeoutDelayCurrent = 0
                        self.curtainAnimationIncreasing = True
                        self.curtainAnimationIsPlaying = False
                        self.curtainAnimationCurrent = 0

        if (self.gamePlayer != None):
            self.gamePlayer.update(dt)
            return

        animationDelta = self.arrowAnimationSpeed * dt
        if self.arrowAnimationIncreasing:
            self.arrowAnimationCurrent += animationDelta
            if self.arrowAnimationCurrent > self.arrowAnimationMax:
                self.arrowAnimationIncreasing = False
                self.arrowAnimationCurrent = self.arrowAnimationMax
        else:
            self.arrowAnimationCurrent -= animationDelta
            if self.arrowAnimationCurrent < 0:
                self.arrowAnimationIncreasing = True
                self.arrowAnimationCurrent = 0

        for minigame in self.minigames:
            minigame.updateMiniPreview(dt)


    def draw(self, surface):
        if (self.gamePlayer != None):
            self.gamePlayer.draw(surface)
            if (self.curtainAnimationIsPlaying):
                pygame.draw.rect(surface, (0,0,0), (0,0,self.curtainAnimationCurrent,surface.get_height()))
                pygame.draw.rect(surface, (0,0,0), (surface.get_width() - self.curtainAnimationCurrent, 0, self.curtainAnimationCurrent,surface.get_height()))
            return

        surface.blit(self.backgroundImage, (0, 0))

        # Header Text
        text = self.headerFont.render("Minigame Masters", True, self.headerColor)
        surface.blit(text, (10, 10))

        # Help Text
        text = self.mainFont.render("Use the arrow/enter key(s)", True, self.headerColor)
        surface.blit(text, (260, 230))

        # Render arcade machines
        for i in range(0, 6):
            # Draw small preview
            previewSurface = surface.subsurface((40 + 129 * i, 410,
                                Menu.IMAGE_ARCADE_MACHINE_WIDTH - 86,
                                Menu.IMAGE_ARCADE_MACHINE_HEIGHT - 202))
            pygame.draw.rect(previewSurface, (0, 0, 0), (0, 0, previewSurface.get_width(), previewSurface.get_height()))
            self.minigames[i].drawMiniPreview(previewSurface)

            s = surface.subsurface((124 * i, 350, 
            Menu.IMAGE_ARCADE_MACHINE_WIDTH, 
            Menu.IMAGE_ARCADE_MACHINE_HEIGHT))
            #pygame.transform.scale(s, (100, 250), s)
            s.blit(self.minigameArcadeMachineImages[i], (15 + 5 * i, 0))

            # Is Hovered game?
            if self.gameSelectedIndex == i:
                s.blit(self.minigameArcadeMachineGlowImage, (-15 + (5 * i), -30))
                s = surface.subsurface((124 * i, 250,
                    Menu.IMAGE_ARCADE_MACHINE_WIDTH,
                    Menu.IMAGE_ARCADE_MACHINE_HEIGHT))
                s.blit(self.minigameArcadeMachineActiveArrow, (50 + 5 * i, self.arrowAnimationCurrent))


        # Footer Text
        text = self.footerFont.render("Made by Dennis, Jasper, Gavin, Ties, Vincent and Quinten", True, self.footerColor)
        surface.blit(text, (10, surface.get_height() - 30))

        if (self.curtainAnimationIsPlaying):
            pygame.draw.rect(surface, (0,0,0), (0,0,self.curtainAnimationCurrent,surface.get_height()))
            pygame.draw.rect(surface, (0,0,0), (surface.get_width() - self.curtainAnimationCurrent, 0, self.curtainAnimationCurrent,surface.get_height()))

    def leaveGame(self):
        self.gamePlayer = None
        pygame.mixer.music.load(self.getFilePath("/Shared/Music/menu/music" + str(randint(1,2)) + ".ogg"))
        pygame.mixer.music.play(-1)