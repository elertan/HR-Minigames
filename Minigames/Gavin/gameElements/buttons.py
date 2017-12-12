import pygame

myfont = pygame.font.SysFont("monospace", 18)
class button(object):
    def __init__(self):
        self.buttons = ['Check Answer', 'Give Hint']

    def draw(self, screen):

        i = 0
        while i < int(len(self.buttons)):
            pygame.draw.rect(screen, [100, 100, 100], (10 + (i * 160), 550, 150, 30))
            text = myfont.render(self.buttons[i], 1, (255, 255, 0))
            screen.blit(text, (20 + (i * 160), 560))
            i += 1


    def click(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                i = 0
                mousepos = pygame.mouse.get_pos()
                if 10 < mousepos[0] < 160 and 550 < mousepos[1] < 580:
                    return True
