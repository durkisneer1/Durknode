import pygame as pg
from src.node import Node


class AddNode(Node):
    def __init__(self, pos: pg.Vector2, title_font: pg.font.Font, layer: int):
        super().__init__(pos, (100, 50), "Add", title_font, layer)

    def update(self, mouse_pos: pg.Vector2):
        super().update(mouse_pos)

    def draw(self, screen: pg.Surface):
        super().draw(screen)
