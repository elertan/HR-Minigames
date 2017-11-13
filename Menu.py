import os
import pygame

class Menu(object):
    def __init__(self, minigames):
        self.menuOffset = 45
        self.minigames = minigames
        dirname = os.path.dirname(os.path.realpath(__file__))
        self.headerFont = pygame.font.Font(dirname + "/Shared/Fonts/SanFrancisco.otf", 21)
        self.normalFont = pygame.font.Font(dirname + "/Shared/Fonts/SanFrancisco.otf", 16)

    def update(self):
        pass

    def draw(self, surface):
        text = self.headerFont.render("Groep 5: Minigames", True, (255,255,255))
        surface.blit(text, (10, 10))
        pygame.draw.rect(
            surface, 
            (255, 255, 255), 
            (self.menuOffset, 
            self.menuOffset, 
            surface.get_width() - self.menuOffset * 2,
            surface.get_height() - self.menuOffset * 2)
        )
        text = self.normalFont.render("Made by Dennis, Jasper, Gavin, Ties and Vincent", True, (255,255,255))
        surface.blit(text, (10, surface.get_height() - 30))