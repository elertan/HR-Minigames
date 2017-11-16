import pygame
from Minigame import Minigame
from Menu import Menu
from Minigames.Dennis.Game import DennisGame
from Minigames.Gavin.Game import GavinGame
from Minigames.Jasper.Game import JasperGame
from Minigames.Ties.Game import TiesGame
from Minigames.Vincent.Game import VincentGame
from Minigames.Quinten.Game import QuintenGame

class Game(object):
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
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
            VincentGame(),
            QuintenGame()
        ]
        self.menu = Menu(self.minigames)

    def handleEvents(self):
        events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.keepRunning = False
                return
            events.append(event)
        # Update Menu
        self.menu.handleEvents(events)

    def update(self, dt):
        # Update Menu
        self.menu.update(dt)
    def draw(self):
        # Draw Menu
        self.menu.draw(self.surface)
    def run(self):
        getTicksLastFrame = 0
        deltaTime = 16
        while self.keepRunning:
            t = pygame.time.get_ticks()

            self.handleEvents()
            self.update(deltaTime)
            self.draw()
            pygame.display.update()

            # deltaTime in seconds.
            deltaTime = (t - getTicksLastFrame) / 1000.0
            getTicksLastFrame = t

game = Game()
game.run()
pygame.quit()
