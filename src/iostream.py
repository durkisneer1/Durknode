import pygame as pg


class InChannel:
    def __init__(self):
        self.value = None
        self.rect = pg.Rect(0, 0, 12, 12)

    def draw(self, screen):
        pg.draw.rect(screen, "red", self.rect)
        pg.draw.circle(screen, "snow", self.rect.center, 5)


class OutChannel:
    def __init__(self):
        self.value = None
        self.rect = pg.Rect(0, 0, 12, 12)

    def draw(self, screen):
        pg.draw.rect(screen, "green", self.rect)
        pg.draw.circle(screen, "snow", self.rect.center, 5)
