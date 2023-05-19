import pygame as pg
import numpy as np


class InChannel:
    def __init__(self):
        self.pos = np.array([0, 0])
        self.value = None
        self.rect = pg.Rect(self.pos[0], self.pos[1], 12, 12)

    def update(self, x, y):
        self.pos[0], self.pos[1] = x, y
        self.rect.center = self.pos

    def draw(self, screen):
        pg.draw.rect(screen, "red", self.rect)
        pg.draw.circle(screen, "snow", self.rect.center, 5)


class OutChannel:
    def __init__(self):
        self.pos = np.array([0, 0])
        self.value = None
        self.rect = pg.Rect(self.pos[0], self.pos[1], 12, 12)

    def update(self, x, y):
        self.pos[0], self.pos[1] = x, y
        self.rect.center = self.pos

    def draw(self, screen):
        pg.draw.rect(screen, "green", self.rect)
        pg.draw.circle(screen, "snow", self.rect.center, 5)
