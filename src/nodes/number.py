import pygame as pg
from src.node import Node


class NumberNode(Node):
    def __init__(self, pos: pg.Vector2, font: pg.Font, layer: int):
        super().__init__(pos, (100, 40), "Number", font, layer)
        self.font = font
        self.value = ["0"]
        self.output_text = self.font.render("0", True, "snow")
        self.output_offset = pg.Vector2(10, 10)

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
            if event.type == pg.TEXTINPUT:
                self.append_digit(event)
            elif event.type == pg.KEYDOWN and event.key == pg.K_BACKSPACE:
                self.pop_digit()

    def draw(self, screen: pg.Surface):
        super().draw(screen)
        screen.blit(self.output_text, self.pos + self.output_offset)
