import pygame
from Minigame import Minigame
from Menu import Menu
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

menu = Menu(minigames)

def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepRunning = False

def update():
    if (currentMinigame is None):
        # Update Menu
        menu.update()
    else:
        currentMinigame.update()
def draw():
    if (currentMinigame is None):
        # Draw Menu
        menu.draw(surface)
    else:
        minigame.draw(surface)

while keepRunning:
    handleEvents()
    update()
    draw()
    pygame.display.update()

pygame.quit()
