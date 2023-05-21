import pygame as pg
import numpy as np
from src.const import *


class Node:
    def __init__(
        self, pos: pg.Vector2, size: tuple, label: str, title_font: pg.Font, layer: int
    ):
        self.pos = pos.copy()
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

        self.make_connection = False
        self.has_connection = False
        self.wire_points = []

        self.input_connection = None
        self.output_connection = None

        self.layer = layer

    def set_mouse_offset(self, mouse_pos: np.array):
        self.mouse_offset.xy = self.pos.xy - mouse_pos

    def bound(self):
        self.pos.x = min(max(self.pos.x, 0), WIN_WIDTH - self.size.x)
        self.pos.y = min(max(self.pos.y, self.bar_offset.y), WIN_HEIGHT - self.size.y)

    def manage_events(self, event: pg.Event):
        pass

    def update(self, mouse_pos: np.array):
        if self.dragging and self.selected:
            self.pos.xy = mouse_pos + self.mouse_offset.xy
            self.bound()
            self.node_rect.topleft = self.pos
            self.bar_rect.topleft = self.pos - self.bar_offset

        self.border_color = "yellow" if self.selected else "black"

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, (20, 20, 20), self.node_rect)
        pg.draw.rect(screen, (30, 30, 30), self.bar_rect)
        pg.draw.rect(screen, self.border_color, self.node_rect, 1)
        screen.blit(self.text, self.pos + self.text_offset)

        if (self.make_connection and self.selected) or self.has_connection:
            pg.draw.aalines(screen, "lightgray", False, self.wire_points)
