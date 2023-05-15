import pygame as pg
from src.node import Node


class NumberNode(Node):
    def __init__(self, pos: pg.Vector2, font: pg.font.Font, layer: int):
        super().__init__(pos, (100, 60), "Number", font, layer)
        self.value = ["0"]
        self.output_text = self.font.render("0", True, "black")
        self.output_offset = pg.Vector2(10, 35)

    def render_text(self):
        self.output_text = self.font.render("".join(self.value), True, "black")
        self.rect.width = max(self.size.x, self.output_text.get_width() + self.output_offset.x * 2)

    def append_digit(self, event):
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

    def update(self, events: pg.event.get, mouse_pos: pg.Vector2):
        super().update(events, mouse_pos)
        if self.selected:
            for ev in events:
                if ev.type == pg.TEXTINPUT:
                    self.append_digit(ev)
                elif ev.type == pg.KEYDOWN and ev.key == pg.K_BACKSPACE:
                    self.pop_digit()

    def draw(self, screen: pg.Surface):
        super().draw(screen)
        screen.blit(self.output_text, self.pos + self.output_offset)