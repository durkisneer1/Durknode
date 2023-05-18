import pygame as pg
import numpy as np
from src.const import *
from src.utils import calculate_bezier_points


t = np.linspace(0, 1)

t = t[:, np.newaxis]

inverse_t = 1 - t
inverse_t2 = inverse_t**2
t2 = t**2


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
        self.in_out_radius = 5

        self.make_connection = False
        self.has_connection = False
        self.wire_points = []

        self.input_connection = None
        self.output_connection = None

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

        if self.make_connection and self.selected:
            if not self.node_rect.collidepoint(mouse_pos.xy):
                self.calculate_wire(mouse_pos.x, mouse_pos.y)
            else:
                self.wire_points = [self.node_rect.midright, self.node_rect.midright]

        if self.has_connection:
            self.calculate_wire(
                self.output_connection.node_rect.left,
                self.output_connection.node_rect.centery,
            )

    def calculate_wire(self, end_point_x: int, end_point_y: int):
        dx = (end_point_x - self.node_rect.right) // 2
        dy = (end_point_y - self.node_rect.centery) // 2

        if end_point_x <= self.node_rect.right:
            control_1 = (end_point_x + dx, end_point_y - dy)
            control_2 = (self.node_rect.right - dx, self.node_rect.centery + dy)
        else:
            control_1 = (end_point_x - abs(dx), end_point_y + dy)
            control_2 = (self.node_rect.right + abs(dx), self.node_rect.centery - dy)

        self.wire_points = calculate_bezier_points(
            (end_point_x, end_point_y),
            control_1,
            control_2,
            self.node_rect.midright,
            t,
            inverse_t,
            inverse_t2,
            t2,
        )

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, (20, 20, 20), self.node_rect)
        pg.draw.rect(screen, (30, 30, 30), self.bar_rect)
        pg.draw.rect(screen, self.border_color, self.node_rect, 1)
        screen.blit(self.text, self.pos + self.text_offset)

        pg.draw.circle(screen, "red", self.node_rect.midleft, self.in_out_radius)
        pg.draw.circle(screen, "red", self.node_rect.midright, self.in_out_radius)

        if (self.make_connection and self.selected) or self.has_connection:
            pg.draw.aalines(screen, "lightgrey", False, self.wire_points)
