
import error
import name

class Actor:

    def __init__(self,theme={}):
        self.theme=theme
        self.name=""

    def set_theme(self,theme):
        self.theme=theme

    def gen(self):
        self.actors.gen()

class Actors:
    
    def __init__(self,theme={}):
        self.theme=theme
        self.actors=[]

    def set_theme(self,theme):
        self.theme=theme

    def gen(self):
        pass

