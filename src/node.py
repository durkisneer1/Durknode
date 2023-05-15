import pygame as pg
from src.const import *


class Node:
    def __init__(self, pos: pg.Vector2, size: tuple, label: str, font: pg.font.Font, layer: int):
        self.pos = pg.Vector2(pos)
        self.size = pg.Vector2(size)
        self.rect = pg.Rect(pos, size)
        self.font = font
        self.text = font.render(label, True, "black")
        self.text_offset = pg.Vector2(10, 10)
        self.border_color = "black"
        self.dragging = False
        self.selected = False
        self.mouse_offset = pg.Vector2(0, 0)

        self.layer = layer

    def set_mouse_offset(self, mouse_pos: pg.Vector2):
        self.mouse_offset = self.pos - mouse_pos

    def bound(self):
        if self.pos.x < 0:
            self.pos.x = 0
        elif self.pos.x > WIN_WIDTH - self.size.x:
            self.pos.x = WIN_WIDTH - self.size.x
        if self.pos.y < 0:
            self.pos.y = 0
        elif self.pos.y > WIN_HEIGHT - self.size.y:
            self.pos.y = WIN_HEIGHT - self.size.y

    def update(self, events: pg.event.get, mouse_pos: pg.Vector2):
        if self.dragging:
            self.pos = mouse_pos + self.mouse_offset
            self.bound()
            self.rect.topleft = self.pos

        self.border_color = "yellow" if self.selected else "black"

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, "snow", self.rect)
        pg.draw.rect(screen, self.border_color, self.rect, 2)
        screen.blit(self.text, self.pos + self.text_offset)
