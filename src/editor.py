import pygame as pg
from src.nodes.add import AddNode
from src.nodes.number import NumberNode

CANVASX = 0
CANVASY = 0
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
                    if node.bar_rect.collidepoint(ev.pos):
                        node.set_mouse_offset(ev.pos)
                        node.dragging = True
                        [n.__setattr__("selected", False) for n in self.nodes]
                        node.selected = True
                        self.nodes[self.nodes.index(node)],self.nodes[len(self.nodes)-1] = self.nodes[len(self.nodes)-1],self.nodes[self.nodes.index(node)]
                        break
                elif ev.type == pg.MOUSEBUTTONUP and ev.button == 1:
                    node.dragging = False
                    node.zindex = 0
                    break

    def draw(self, screen):
        for node in self.nodes:
            node.draw(screen)
