from Minigame import Minigame
import pygame

class VincentGame(Minigame):

    #colors
    purple = 28, 28, 122
    pink = 242, 72, 158
    white = 255, 255, 255

    display_width = 800
    display_height = 600
    screen = pygame.display.set_mode((display_width, display_height))

    x_change = 0

    def __init__(self):
        super(VincentGame, self).__init__("VincentGame", "Vincent", 6)

        self.miniPreviewMainFont = pygame.font.Font(self.getFilePath("/Shared/Fonts/SanFrancisco.otf"), 11)

        self.largeFont = pygame.font.Font(self.getFilePath("/Shared/Fonts/neon-pixel.ttf"), 60)
        self.normalFont = pygame.font.Font(self.getFilePath("/Shared/Fonts/neon-pixel.ttf"), 40)

        self.previewPressToStartBlinkAnimationDelay = 0.75
        self.previewPressToStartBlinkAnimationCurrent = 0
        self.previewPressToStartBlinkAnimationIsVisible = True

        self.characterImage = pygame.image.load(self.getFilePath("/Shared/Images/Vincentgame/omega.png"))
        self.backgroundImage = pygame.image.load(self.getFilePath("/Shared/Images/Vincentgame/omegabackground.png"))

        self.characterX = 400
        self.characterY = 300



    def player(x,y):
        screen.blit(self.characterImage, (x,y))

    x = (display_width * 0.45)
    y = (display_height * 0.8)


    # When a player starts this minigame
    def enter(self):
        pass

    # When a player leaves this minigame
    def leave(self):
        pass

    def handleEvents(self, events):
        #player movement

        x_change = 0
        left = False
        right = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            elif event.key == pygame.K_RIGHT:
                right = True
        if event.type == pygame.KEYUP:
            if left and event.key == pygame.K_LEFT:
                left = False
            if right and event.key == pygame.K_RIGHT:
                right = False
        if left and right:
            x_change *= 1
        elif left:
            x_change= -5
        elif right:
            x_change = 5
        else:
            x_change = 0

    x += x_change

    # Gets called on every frame
    def update(self, dt):
        pass

    # Gets called on every frame
    def updatePreview(self, dt):
        pass

    def updateMiniPreview(self, dt):
        pass

    # Draw the current game state
    def draw(self, surface):
        pass

    def drawPreview(self, surface):
        text = self.largeFont.render("OmegaInvaders", True, (255, 255, 255))
        surface.blit(text, (surface.get_width() / 2 - text.get_width() / 2, 40))

        text = self.largeFont.render("--------------------------", True, (255, 255, 255))
        surface.blit(text, (surface.get_width() / 2 - text.get_width() / 2, 80))

        if self.previewPressToStartBlinkAnimationIsVisible:
            text = self.normalFont.render("Press Enter To Start", True, (255, 255, 255))
            surface.blit(text, (surface.get_width() / 2 - text.get_width() / 2, surface.get_height() - 100))

    def drawMiniPreview(self, surface):
        text = self.miniPreviewMainFont.render("OmegaInvaders", True, (255, 255, 255))
        surface.blit(text, (surface.get_width() / 2 - text.get_width() / 2, 5))