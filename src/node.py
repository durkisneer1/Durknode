import pygame as pg
from src.const import *


class Node:
    def __init__(
        self, pos: pg.Vector2, size: tuple, label: str, title_font: pg.Font, layer: int
    ):
        self.pos = pg.Vector2(pos)
        self.size = pg.Vector2(size)
        self.node_rect = pg.Rect(pos, size)
        self.border_color = "black"

        self.bar_offset = pg.Vector2(0, 20)
        self.bar_pos = pos - self.bar_offset
        self.bar_rect = pg.Rect(self.bar_pos, (self.size.x, self.bar_offset.y))

        self.text = title_font.render(label, True, "snow")
        self.text_offset = pg.Vector2(5, -(self.bar_offset.y - 2.5))

        self.dragging = False
        self.selected = False
        self.mouse_offset = pg.Vector2(0, 0)

        self.layer = layer

    def set_mouse_offset(self, mouse_pos: pg.Vector2):
        self.mouse_offset.xy = self.pos - mouse_pos

    def bound(self):
        self.pos.x = min(max(self.pos.x, 0), WIN_WIDTH - self.size.x)
        self.pos.y = min(max(self.pos.y, self.bar_offset.y), WIN_HEIGHT - self.size.y)

    def manage_events(self, event: pg.Event):
        pass

    def update(self, mouse_pos: pg.Vector2):
        if self.dragging and self.selected:
            self.pos.xy = mouse_pos + self.mouse_offset
            self.bound()
            self.node_rect.topleft = self.pos
            self.bar_rect.topleft = self.pos - self.bar_offset

        self.border_color = "yellow" if self.selected else "black"

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, (20, 20, 20), self.node_rect)
        pg.draw.rect(screen, (30, 30, 30), self.bar_rect)
        pg.draw.rect(screen, self.border_color, self.node_rect, 1)
        screen.blit(self.text, self.pos + self.text_offset)
