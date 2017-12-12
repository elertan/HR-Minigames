import pygame
from Minigames.Gavin.gameElements.includes.textField import TextInput

myfont = pygame.font.SysFont("monospace", 18)
class code:
    gameRank = 0
    playerSmile = 20
    playerMad = 20

    def __init__(self):

        self.input = TextInput()
        self.error = ""

    def imput(self, events):
        self.input.update(events)
        # Blit its surface onto the screen

    def render(self,screen):
        screen.blit(self.input.get_surface(), (10, 400))
        self.howto(screen)

    def howto(self, screen):
        guide = ["", ""]

        if self.gameRank == 0:
            guide[0] = "First we have to start the game."
            guide[1] = "we have a class 'game' with the function 'run'"
        elif self.gameRank == 1:
            guide[0] = "Congrats! now we are walking!"
            guide[0] = "Now we need a jump function Lets create one"
        elif self.gameRank == 2:
            guide[0] = ""
        elif self.gameRank == 3:
            guide[0] = ""

        i = 0
        text = myfont.render(self.error, 1, (255, 0, 0))
        screen.blit(text, (10, 530))

        while i < int(len(guide)):
            text = myfont.render(guide[i], 1, (255, 255, 0))
            screen.blit(text, (500, 400 + (i * 20)))
            i += 1

    def check(self):
        if self.gameRank == 0 and self.input.input_string == "game.run()":
            self.gameRank = 1
            self.input.input_string = ""
            #self.playerSmile = 0
        elif self.gameRank == 0:
            self.error = self.checkCode(self.input.input_string)
            #self.playerMad = 0

    def checkCode(self, input):
        if '(' in input and ')' not in input:
            return "unexpected end. expecting ')' instead"
        elif 'game.' in input:
            return "Undifined variable '" + str(input.replace('game.','')) + "' is not a member of game."
        else:
            return "Syntax error!"


