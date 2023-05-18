import pygame as pg
from src.node import Node
from src.iostream import InChannel, OutChannel


class NumberNode(Node):
    def __init__(
        self, pos: pg.Vector2, title_font: pg.Font, body_font: pg.Font, layer: int
    ):
        super().__init__(pos, (100, 40), "Number", title_font, layer)
        self.font = body_font
        self.value = ["0"]
        self.output_text = self.font.render("0", True, "snow")
        self.output_offset = pg.Vector2(10, 10)
        self.inputs = [InChannel()]
        self.output = OutChannel()

    def render_text(self):
        self.output_text = self.font.render("".join(self.value), True, "snow")
        self.node_rect.width = max(
            self.size.x, self.output_text.get_width() + self.output_offset.x * 2
        )
        self.bar_rect.width = self.node_rect.width

    def append_digit(self, event: pg.Event):
        if event.text.isdigit() or event.text == ".":
            self.value.append(event.text)
            if len(self.value) > 1 and self.value[0] == "0" and "." not in self.value:
                self.value.pop(0)
            self.render_text()

    def pop_digit(self):
        if self.value:
            self.value.pop()
        if not self.value:
            self.value.append("0")
        self.render_text()

    def manage_events(self, event: pg.Event):
        if self.selected:
            if event.type == pg.TEXTINPUT and len(self.value) < 20:
                self.append_digit(event)
            elif event.type == pg.KEYDOWN and event.key == pg.K_BACKSPACE:
                self.pop_digit()

    def update(self, mouse_pos: pg.Vector2):
        super().update(mouse_pos)
        self.inputs[0].rect.center = (
            self.pos.x,
            self.pos.y + self.node_rect.height / 2,
        )
        self.output.rect.center = (
            self.pos.x + self.node_rect.width,
            self.pos.y + self.node_rect.height / 2,
        )

    def draw(self, screen: pg.Surface):
        super().draw(screen)
        screen.blit(self.output_text, self.pos + self.output_offset)
        for channel in self.inputs:
            channel.draw(screen)
        self.output.draw(screen)
