import pygame as pg
import numpy as np
from src.node import Node
from src.iostream import InChannel, OutChannel
from src.utils import calculate_bezier_points


class AddNode(Node):
    def __init__(self, pos: pg.Vector2, title_font: pg.font.Font, layer: int):
        super().__init__(pos, (100, 50), "Add", title_font, layer)
        self.inputs = [InChannel(), InChannel()]
        self.output = OutChannel()

    def update(self, mouse_pos: np.array) -> None:
        super().update(mouse_pos)
        self.inputs[0].update(self.pos.x, self.pos.y + self.node_rect.height * 1 / 3)
        self.inputs[1].update(self.pos.x, self.pos.y + self.node_rect.height * 2 / 3)
        self.output.update(
            self.pos.x + self.node_rect.width, self.pos.y + self.node_rect.height / 2
        )

        if self.has_connection:
            self.wire_points = calculate_bezier_points(
                self.output.pos, self.output_connection.inputs[0].pos
            )
            return

        if self.make_connection and self.selected:
            self.wire_points = calculate_bezier_points(self.output.pos, mouse_pos)

    def draw(self, screen: pg.Surface):
        super().draw(screen)
        for channel in self.inputs:
            channel.draw(screen)
        self.output.draw(screen)
