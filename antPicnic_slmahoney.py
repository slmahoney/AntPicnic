

import pygame, simpleGE, random

"ant picnic"
"slide and catch game"
"Sabrina mahoney"


class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("blanket.png")
        
def main():
    game = Game()
    game.start()
    
if __name__=="__main__":
    main()
