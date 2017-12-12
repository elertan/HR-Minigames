import pygame


class player(object):
    def __init__(self, dirname):
        self.playerDir = dirname + '/Shared/Images/GavinGame/player/'
        self.playerSmileSprite = self.playerDir + 'p-smile.png'
        self.playerMadSprite = self.playerDir + 'p-mad.png'
        self.playerSprites = [self.playerDir + 'p-walk-0.png', self.playerDir + 'p-walk-1.png']
        self.mapStartSpriteInfo = 'ground-start.png'
        self.mapEndSpriteInfo = 'ground-end.png'

        self.playerWalk0 = pygame.image.load(self.playerSprites[0])
        self.playerWalk1 = pygame.image.load(self.playerSprites[1])
        self.playerSmile = pygame.image.load(self.playerSmileSprite)
        self.playerMad = pygame.image.load(self.playerMadSprite)

        self.playerWalkCount = 0

    def draw(self, screen):
        if self.playerWalkCount < 4:
            screen.blit(self.playerWalk0, (300, 220))
        elif self.playerWalkCount < 8 :
            screen.blit(self.playerWalk1, (300, 220))
        else:
            screen.blit(self.playerWalk0, (300, 220))
            self.playerWalkCount = 0

    def smile(self, screen):
        screen.blit(self.playerSmile, (300, 220))

    def mad(self, screen):
        screen.blit(self.playerMad, (300, 220))


    def walk(self):
        self.playerWalkCount += 1
