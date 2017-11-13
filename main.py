import pygame
from Minigame import Minigame
from Minigames.Dennis.Game import SuperSnake

pygame.init()

# PyGame Setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("HR MiniGames Groep 5")
surface = pygame.display.get_surface()
keepRunning = True
currentMinigame = None

# Our Minigames
minigames = [
    SuperSnake()
]

def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepRunning = False

def update():
    if (currentMinigame is None):
        # Update Menu
    else:
        currentMinigame.update()
def draw():
    if (currentMinigame is None):
        # Draw Menu
    else:
        
        minigame.draw(surface)
    pygame.display.update()

while keepRunning:
    handleEvents()
    update()
    draw()