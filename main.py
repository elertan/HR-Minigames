import pygame
from Minigame import Minigame
from Menu import Menu
from Minigames.Dennis.Game import SuperSnake

class Game(object):
    def __init__(self):
        pygame.init()

        # PyGame Setup
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("HR MiniGames Groep 5")
        self.surface = pygame.display.get_surface()
        self.keepRunning = True
        self.currentMinigame = None
        self.minigames = [
            SuperSnake()
        ]
        self.menu = Menu(self.minigames)

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.keepRunning = False

    def update(self):
        if (self.currentMinigame is None):
            # Update Menu
            self.menu.update()
        else:
            self.currentMinigame.update()
    def draw(self):
        if (self.currentMinigame is None):
            # Draw Menu
            self.menu.draw(self.surface)
        else:
            self.minigame.draw(self.surface)
    def run(self):
        while self.keepRunning:
            self.handleEvents()
            self.update()
            self.draw()
            pygame.display.update()

game = Game()
game.run()
pygame.quit()
