import pygame as pg
from src.nodes.add import AddNode
from src.nodes.number import NumberNode


class NodeEditor:
    def __init__(self, font):
        self.nodes = []
        self.font = font
        self.dragging_node = None

    def update(
        self, events: pg.event.get, mouse_pos: pg.Vector2, keys: pg.key.get_pressed
    ):
        for ev in events:
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_x:
                    self.nodes = [node for node in self.nodes if not node.selected]
                elif keys[pg.K_LSHIFT]:
                    match ev.key:
                        case pg.K_a:
                            self.nodes.append(AddNode(mouse_pos, self.font))
                        case pg.K_n:
                            self.nodes.append(NumberNode(mouse_pos, self.font))

        for node in reversed(self.nodes):
            node.update(events, mouse_pos)
            for ev in events:
                if ev.type == pg.MOUSEBUTTONDOWN and ev.button == 1:
                    if node.rect.collidepoint(ev.pos):
                        node.set_mouse_offset(ev.pos)
                        node.dragging = True
                        [n.__setattr__("selected", False) for n in self.nodes]
                        node.selected = True
                        break
                elif ev.type == pg.MOUSEBUTTONUP and ev.button == 1:
                    node.dragging = False
                    break

    def draw(self, screen):
        for node in self.nodes:
            node.draw(screen)
