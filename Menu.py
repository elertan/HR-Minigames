import os
import pygame

class Menu(object):
    IMAGE_ARCADE_MACHINE_WIDTH = 160
    IMAGE_ARCADE_MACHINE_HEIGHT = 250

    def __init__(self, minigames):
        self.headerColor = (255,255,255)
        self.footerColor = (255,255,255)
        self.minigameTextColor = (255,255,255)
        self.minigameTextActiveColor = (255,0,0)

        dirname = os.path.dirname(os.path.realpath(__file__))
        self.backgroundImage = pygame.image.load(dirname + "/Shared/Images/menu/background.jpg")
        self.headerFont = pygame.font.Font(dirname + "/Shared/Fonts/SanFrancisco.otf", 21)
        self.mainFont = pygame.font.Font(dirname + "/Shared/Fonts/SanFrancisco.otf", 20)
        self.minigameFont = pygame.font.Font(dirname + "/Shared/Fonts/SanFrancisco.otf", 18)
        self.footerFont = pygame.font.Font(dirname + "/Shared/Fonts/SanFrancisco.otf", 16)

        self.minigames = minigames
        self.minigameArcadeMachineImages = []
        for i in range(0, 6):
            self.minigameArcadeMachineImages.append(pygame.image.load(dirname + "/Shared/Images/menu/arcade-machine-" + str(i + 1) + ".png"))
        self.minigameArcadeMachineGlowImage = pygame.image.load(dirname + "/Shared/Images/menu/arcade-machine-glow.png")

        self.gameSelectedIndex = 1

    def handleEvents(self, events):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.blit(self.backgroundImage, (0, 0))

        # Header Text
        text = self.headerFont.render("Minigame Masters", True, self.headerColor)
        surface.blit(text, (10, 10))

        # Render arcade machines
        for i in range(0, 3):
            s = surface.subsurface((175 * i, 35, Menu.IMAGE_ARCADE_MACHINE_WIDTH, Menu.IMAGE_ARCADE_MACHINE_HEIGHT))
            #pygame.transform.scale(s, (100, 250), s)
            s.blit(self.minigameArcadeMachineImages[i], (0,0))
            
        for i in range(0, 3):
            s = surface.subsurface((175 * i, 35 + Menu.IMAGE_ARCADE_MACHINE_HEIGHT, Menu.IMAGE_ARCADE_MACHINE_WIDTH, Menu.IMAGE_ARCADE_MACHINE_HEIGHT))
            #pygame.transform.scale(s, (100, 250), s)
            s.blit(self.minigameArcadeMachineImages[i + 3], (0,0))

        # Footer Text
        text = self.footerFont.render("Made by Dennis, Jasper, Gavin, Ties and Vincent", True, self.footerColor)
        surface.blit(text, (10, surface.get_height() - 30))