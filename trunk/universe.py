
import error
import actors

class Universe:
    
    def __init__(self,theme={}):
        self.theme=theme
        self.actors=actors.Actors(self.theme)

    def set_theme(self,theme):
        self.theme=theme

    def gen(self):
        self.actors.gen()
