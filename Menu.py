import pygame

class Menu(object):
    isIncreasing = False
    menuOffset = 45
    minigames = []
    def __init__(self, minigames):
        self.minigames = minigames

    def update(self):
        

    def draw(self, surface):
        pygame.draw.rect(
            surface, 
            (255, 255, 255), 
            (self.menuOffset, 
            self.menuOffset, 
            surface.get_width() - self.menuOffset * 2,
            surface.get_height() - self.menuOffset * 2)
        )