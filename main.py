import pygame
from Minigame import Minigame
from Menu import Menu
from Minigames.Dennis.Game import DennisGame
from Minigames.Gavin.Game import GavinGame
from Minigames.Jasper.Game import JasperGame
from Minigames.Ties.Game import TiesGame
from Minigames.Vincent.Game import VincentGame

class Game(object):
    def __init__(self):
        pygame.init()

        # PyGame Setup
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Minigame Masters")
        self.surface = pygame.display.get_surface()
        self.keepRunning = True
        self.currentMinigame = None
        self.minigames = [
            DennisGame(),
            GavinGame(),
            JasperGame(),
            TiesGame(),
            VincentGame()
        ]
        self.menu = Menu(self.minigames)

    # def handleEvents(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             self.keepRunning = False

    def update(self):
        events = []
        for event in pygame.event.get():
            events.append(event)
        if (self.currentMinigame is None):
            # Update Menu
            self.menu.update(events)
        else:
            self.currentMinigame.update(events)
    def draw(self):
        if (self.currentMinigame is None):
            # Draw Menu
            self.menu.draw(self.surface)
        else:
            self.minigame.draw(self.surface)
    def run(self):
        while self.keepRunning:
            # self.handleEvents()
            self.update()
            self.draw()
            pygame.display.update()

game = Game()
game.run()
pygame.quit()
