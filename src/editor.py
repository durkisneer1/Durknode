import pygame as pg
from src.nodes.add import AddNode
from src.nodes.number import NumberNode


# CANVASX = 0
# CANVASY = 0
class NodeEditor:
    def __init__(self, title_font: pg.Font, body_font: pg.Font):
        self.nodes = []
        self.title_font = title_font
        self.body_font = body_font
        self.dragging_node = None

    def manage_events(self, event: pg.Event, mouse_pos: pg.Vector2, keys: pg.key.get_pressed):
        [node.manage_events(event) for node in self.nodes if node.selected]

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_x:
                self.nodes = [node for node in self.nodes if not node.selected]
            elif keys[pg.K_LSHIFT]:
                match event.key:
                    case pg.K_a:
                        self.nodes.append(
                            AddNode(mouse_pos, self.title_font, len(self.nodes) + 1)
                        )
                    case pg.K_n:
                        self.nodes.append(
                            NumberNode(mouse_pos, self.title_font, self.body_font, len(self.nodes) + 1)
                        )

        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            sorted_overlapping_nodes = sorted(
                [
                    node
                    for node in self.nodes
                    if node.bar_rect.collidepoint(event.pos)
                    or node.node_rect.collidepoint(event.pos)
                ],
                key=lambda node: node.layer,
                reverse=True,
            )

            if sorted_overlapping_nodes:
                selected_node = sorted_overlapping_nodes[0]

                selected_node.set_mouse_offset(event.pos)
                selected_node.dragging = True
                for node in self.nodes:
                    node.selected = False
                selected_node.selected = True

                # Put everything that's on top of the selected node one layer down -> the selected ends up on top

                selected_node.layer = self.nodes[-1].layer + 1

                index = self.nodes.index(selected_node)
                for node in self.nodes[index:]:
                    node.layer = max(1, node.layer - 1)

                self.nodes = sorted(self.nodes, key=lambda node: node.layer)

        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            for n in self.nodes:
                n.dragging = False

    def update(self, mouse_pos: pg.Vector2):
        [node.update(mouse_pos) for node in self.nodes]

    def draw(self, screen: pg.Surface):
        [node.draw(screen) for node in self.nodes]
