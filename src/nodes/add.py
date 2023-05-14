import pygame as pg
from src.node import Node


class AddNode(Node):
    def __init__(self, pos: pg.Vector2, font: pg.font.Font):
        super().__init__(pos, (100, 50), "Add", font)

    def update(self, events: pg.event.get, mouse_pos: pg.Vector2):
        super().update(events, mouse_pos)

    def draw(self, screen: pg.Surface):
        super().draw(screen)
