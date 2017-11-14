class Minigame(object):
    name=""
    author=""
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def update(self, events):
        raise NotImplementedError("You need to override the update method on your minigame.")

    def draw(self, surface):
        raise NotImplementedError("You need to override the draw method on your minigame.")