from Minigame import Minigame

class VincentGame(Minigame):
    def __init__(self):
        super(VincentGame, self).__init__("VincentGame", "Vincent", 6)
    
    # When a player starts this minigame
    def enter(self):
        raise NotImplementedError("You need to override the enter method on your minigame.")

    # When a player leaves this minigame
    def leave(self):
        raise NotImplementedError("You need to override the leave method on your minigame.")

    def handleEvents(self, events):
        raise NotImplementedError("You need to override the handleEvents method on your minigame.")

    # Gets called on every frame
    def update(self, dt):
        raise NotImplementedError("You need to override the update method on your minigame.")

    # Gets called on every frame
    def updatePreview(self, dt):
        raise NotImplementedError("You need to override the updatePreview method on your minigame.")

    # Draw the current game state
    def draw(self, surface):
        raise NotImplementedError("You need to override the draw method on your minigame.")

    def drawPreview(self, surface):
<<<<<<< HEAD
        x=5
=======
        x=20
>>>>>>> aed9ca7b57b372948ff310d66cf292b270c154f0
        raise NotImplementedError("You need to override the drawPreview method on your minigame.")