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
                            self.nodes.append(
                                AddNode(mouse_pos, self.font, len(self.nodes) + 1)
                            )
                        case pg.K_n:
                            self.nodes.append(
                                NumberNode(mouse_pos, self.font, len(self.nodes) + 1)
                            )

            if ev.type == pg.MOUSEBUTTONDOWN and ev.button == 1:
                sorted_overlapping_nodes = sorted(
                    [node for node in self.nodes if node.rect.collidepoint(ev.pos)],
                    key=lambda node: node.layer,
                    reverse=True,
                )

                if sorted_overlapping_nodes:
                    selected_node = sorted_overlapping_nodes[0]

                    selected_node.set_mouse_offset(ev.pos)
                    selected_node.dragging = True
                    for node in self.nodes:
                        node.selected = False
                    selected_node.selected = True

                    # Put everything that's on top of the selected node one layer down -> the selected ends up on top

                    selected_node.layer = self.nodes[-1].layer + 1

                    index = self.nodes.index(selected_node)
                    for node in self.nodes[index:]:
                        node.layer = max(1, node.layer - 1)

                    self.nodes = sorted(self.nodes, key=lambda n: n.layer)

            elif ev.type == pg.MOUSEBUTTONUP and ev.button == 1:
                for n in self.nodes:
                    n.dragging = False

        for node in self.nodes:
            node.update(events, mouse_pos)
            
        # print([node.layer for node in self.nodes])

    def draw(self, screen):
        for node in self.nodes:
            node.draw(screen)
