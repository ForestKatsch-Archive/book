#!/usr/bin/python3

import universe
import error

class Book:
    
    def __init__(self,theme={}):
        self.theme=theme
        self.universe=universe.Universe(self.theme)
        
    def set_theme(self,theme):
        self.theme=theme

    def gen(self):
        self.universe.set_theme(self.theme)
        self.universe.gen()

if __name__ == "__main__":
    b=Book()
    b.gen()
