import pygame as pg
from src.const import *


class Node:
    def __init__(
        self, pos: pg.Vector2, size: tuple, label: str, font: pg.font.Font, layer: int
    ):
        self.pos = pg.Vector2(pos)
        self.size = pg.Vector2(size)
        self.rect = pg.Rect(pos, size)

        self.zindex = 0
        self.bar = 20
        self.bar_pos = pg.Vector2((pos[0],pos[1]-self.bar))
        self.bar_rect = pg.Rect(self.bar_pos, (size[0],20))
        self.bar_font = pg.font.Font(None,22)
        self.font_colour = "#DDDDDD"
        self.node_bg = "#111111"
        self.bar_bg = "#222222"
        self.text = self.bar_font.render(label, True, self.font_colour)
        # self.text_offset = pg.Vector2(x,y=0-self.bar_height - (self.bar_height - self.bar_font_height)/2)
        self.text_offset = pg.Vector2(5, 0 - (self.bar-2.5))
        self.border_color = "black"
        self.dragging = False
        self.selected = False
        self.mouse_offset = pg.Vector2(0, 0)

        self.layer = layer

    def set_mouse_offset(self, mouse_pos: pg.Vector2):
        self.mouse_offset = self.pos - mouse_pos 

    def bound(self):
        if self.pos.x < 0:
            self.pos.x = 0
        elif self.pos.x > WIN_WIDTH - self.size.x:
            self.pos.x = WIN_WIDTH - self.size.x
        if self.pos.y+-(self.bar) < 0:
            self.pos.y = 0+self.bar
        elif self.pos.y+self.bar > WIN_HEIGHT - self.size.y:
            self.pos.y = WIN_HEIGHT - self.size.y

    def update(self, events: pg.event.get, mouse_pos: pg.Vector2):
        if self.dragging and self.selected:
            self.pos = mouse_pos + self.mouse_offset
            self.bound()
            self.rect.topleft = self.pos
            self.bar_rect.topleft = (self.pos[0],self.pos[1]-20)
            

        self.border_color = "yellow" if self.selected else "black"

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.node_bg, self.rect)
        pg.draw.rect(screen,self.bar_bg,self.bar_rect)
        pg.draw.rect(screen, self.border_color, self.rect, 1)
        screen.blit(self.text, self.pos + self.text_offset)
