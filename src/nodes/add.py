import pygame as pg
from src.node import Node
from src.iostream import InChannel, OutChannel


class AddNode(Node):
    def __init__(self, pos: pg.Vector2, title_font: pg.font.Font, layer: int):
        super().__init__(pos, (100, 50), "Add", title_font, layer)
        self.inputs = [InChannel(), InChannel()]
        self.output = OutChannel()

    def update(self, mouse_pos: pg.Vector2):
        super().update(mouse_pos)
        self.inputs[0].rect.center = (
            self.pos.x,
            self.pos.y + self.node_rect.height * 1 / 3,
        )
        self.inputs[1].rect.center = (
            self.pos.x,
            self.pos.y + self.node_rect.height * 2 / 3,
        )
        self.output.rect.center = (
            self.pos.x + self.node_rect.width,
            self.pos.y + self.node_rect.height / 2,
        )

    def draw(self, screen: pg.Surface):
        super().draw(screen)
        for channel in self.inputs:
            channel.draw(screen)
        self.output.draw(screen)
