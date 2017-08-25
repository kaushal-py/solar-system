import pygame as pg
import math

import globals as gb

class Planet:

    def __init__(self, displayImage,
                 revolveRadius, revolveSpeed, isSun):
        self.displayImage = displayImage
        self.revolveRadius = revolveRadius
        self.revolveSpeed = revolveSpeed
        self.isSun = isSun

        self.theta = 90

        # Planet Position
        if self.isSun:
            self.position = gb.WORLD_CENTER
        else:
            self.position = (gb.WORLD_WIDTH//2, gb.WORLD_HEIGHT//2 - self.revolveRadius)

        self.planetSurface = pg.image.load(displayImage)
        self.planetRect = self.planetSurface.get_rect()

        self.planetRect.center = self.position

    def render(self, screen):

        #render Orbit
        if not self.isSun:
            pg.draw.circle(screen, gb.WHITE, gb.WORLD_CENTER, self.revolveRadius, 1)

        #render planet
        screen.blit(self.planetSurface, self.planetRect)

        # revolution of the planet
        self.revolve()

        # self.planetSurface, self.planetRect = self.rotate(self.planetSurface, self.planetRect, 1)

    def revolve(self):

        xPosition = gb.WORLD_WIDTH//2 + self.revolveRadius * math.cos(math.radians(self.theta))
        yPosition = gb.WORLD_HEIGHT//2 - self.revolveRadius * math.sin(math.radians(self.theta))

        self.planetRect.center = (xPosition, yPosition)

        self.theta = (self.theta + self.revolveSpeed) % 360

    def rotate(self, image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pg.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

