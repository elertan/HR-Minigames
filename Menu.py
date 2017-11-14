import os
import pygame

class Menu(object):
    def __init__(self, minigames):
        self.headerColor = (255,255,255)
        self.footerColor = (255,255,255)
        self.minigameTextColor = (255,255,255)
        self.minigameTextActiveColor = (255,0,0)

        dirname = os.path.dirname(os.path.realpath(__file__))
        self.headerFont = pygame.font.Font(dirname + "/Shared/Fonts/SanFrancisco.otf", 21)
        self.mainFont = pygame.font.Font(dirname + "/Shared/Fonts/SanFrancisco.otf", 20)
        self.minigameFont = pygame.font.Font(dirname + "/Shared/Fonts/SanFrancisco.otf", 18)
        self.footerFont = pygame.font.Font(dirname + "/Shared/Fonts/SanFrancisco.otf", 16)

        self.menuOffset = 45
        self.minigames = minigames

        self.gameSelectedIndex = 1

    def drawMainSection(self, surface):
        pygame.draw.rect(
            surface, 
            (150, 150, 150), 
            (self.menuOffset,
            self.menuOffset, 
            surface.get_width() - self.menuOffset * 2,
            surface.get_height() - self.menuOffset * 2)
        )

        text = self.mainFont.render("Select a minigame to start!", True, (0, 0, 0))
        surface.blit(text, (self.menuOffset + 10, self.menuOffset + 10))

        x = 1
        for minigame in self.minigames:
            content = minigame.name + " by " + minigame.author
            color = None
            if self.gameSelectedIndex == x:
                content = "> " + content
                color = self.minigameTextActiveColor
            else:
                color = self.minigameTextColor
            text = self.minigameFont.render(content, True, color)
            surface.blit(text, (self.menuOffset + 30, self.menuOffset + 20 + 30 * x))
            x += 1

    def update(self, events):
        pass

    def draw(self, surface):
        # Header Text
        text = self.headerFont.render("Minigame Masters", True, self.headerColor)
        surface.blit(text, (10, 10))

        # Main Section
        self.drawMainSection(surface)

        # Footer Text
        text = self.footerFont.render("Made by Dennis, Jasper, Gavin, Ties and Vincent", True, self.footerColor)
        surface.blit(text, (10, surface.get_height() - 30))