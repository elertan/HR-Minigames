import pygame


class map(object):
    def __init__(self, dirname):
        self.mapSpriteInfo = [dirname + '/Shared/Images/GavinGame/world/ground.png', [56, 59]]
        self.mapStartSpriteInfo = 'ground-start.png'
        self.mapEndSpriteInfo = 'ground-end.png'
        self.location = [0, 56, 112, 168, 224, 280, 336, 392, 448, 504, 560, 616, 672, 728, 784, 840]
        self.bgLocation = [0, 420, 840]
        self.highestLocation = 15
        self.bghighestLocation = 2
        self.mapSprite = pygame.image.load(self.mapSpriteInfo[0])
        self.bgSprite = pygame.image.load(dirname + '/Shared/Images/GavinGame/world/game-bg.jpg')

    def draw(self, screen):
        i = 0
        while i < int(len(self.location)):
            screen.blit(self.mapSprite, (self.location[i], 300))
            i += 1
        j = 0
        while j < int(len(self.bgLocation)):
            screen.blit(self.bgSprite, (self.bgLocation[j], 0))
            j += 1

    def map(self):
        i = 0
        while i < int(len(self.location)):
            if self.location[i] == -56:
                self.location[i] = self.location[self.highestLocation] + 56
                if self.highestLocation == 15:
                    self.highestLocation = 0
                else:
                    self.highestLocation += 1

            self.location[i] = self.location[i] - 2

            i += 1
        j = 0
        while j < int(len(self.bgLocation)):
            if self.bgLocation[j] == -420:
                self.bgLocation[j] = self.bgLocation[self.bghighestLocation] + 420
                if self.bghighestLocation == 2:
                    self.bghighestLocation = 0
                else:
                    self.bghighestLocation += 1

            self.bgLocation[j] = self.bgLocation[j] - 2
            j += 1
