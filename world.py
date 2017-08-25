import pygame as pg
import sys

#Global variables
import globals as gb

#import planets
from planet import Planet

class World:

    def __init__(self):

        #initialise pygame
        pg.init()

        # Initialise the planets and sun
        self.sun = Planet("sprites/sun.png", 0, 0, True)
        self.earth = Planet("sprites/earth.png", 250, 1, False)
        self.mercury = Planet("sprites/mercury.png", 150, 3, False)

        # Initialise the screen and set screem size
        self.screen = pg.display.set_mode(gb.WORLD_SIZE)

        # Initialise clock to keep track of FPS
        self.clock = pg.time.Clock()

    def start(self): 

        # Animation Loop
        while True:

            # Event loop to read for events
            for event in pg.event.get():

                # Quit button Condition
                if event.type == pg.QUIT:
                    sys.exit()
            
            # Render the background
            self.screen.fill(gb.SPACE_BLUE)
            
            # Render sun and planets
            self.sun.render(self.screen)
            self.mercury.render(self.screen)
            self.earth.render(self.screen)

            # Keep track of FPS
            self.clock.tick(gb.FPS)

            # Flip the buffer (Refresh the screen)
            pg.display.flip()




