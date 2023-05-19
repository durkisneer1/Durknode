import pygame as pg
import numpy as np
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
        self.spawn_point = pg.Vector2()

        self.receive_linking = False
        self.link_sending_node = None

    def manage_events(
        self, event: pg.Event, mouse_pos: np.array, keys: pg.key.get_pressed
    ):
        [node.manage_events(event) for node in self.nodes if node.selected]

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_x:  # Delete selected node
                self.nodes = [node for node in self.nodes if not node.selected]
            elif keys[pg.K_LSHIFT]:
                self.spawn_point.xy = mouse_pos
                match event.key:
                    case pg.K_a:  # Add node
                        self.nodes.append(
                            AddNode(
                                self.spawn_point, self.title_font, len(self.nodes) + 1
                            )
                        )
                    case pg.K_n:  # Number node
                        self.nodes.append(
                            NumberNode(
                                self.spawn_point,
                                self.title_font,
                                self.body_font,
                                len(self.nodes) + 1,
                            )
                        )

        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            sorted_nodes = sorted(
                [
                    node
                    for node in self.nodes
                    if node.bar_rect.collidepoint(event.pos)
                    or node.node_rect.collidepoint(event.pos)
                ],
                key=lambda node: node.layer,
                reverse=True,
            )  # Sort nodes by layer, so that the topmost node is selected first

            if sorted_nodes:
                selected_node = sorted_nodes[0]
                selected_node.set_mouse_offset(event.pos)
                selected_node.dragging = True
                for node in self.nodes:
                    node.selected = False
                selected_node.selected = True

                selected_node.layer = self.nodes[-1].layer + 1  # Set layer to topmost
                index = self.nodes.index(selected_node)
                for node in self.nodes[
                    index:
                ]:  # Move all nodes above selected node down
                    node.layer = max(1, node.layer - 1)  # Don't go below layer 1
                self.nodes = sorted(self.nodes, key=lambda node: node.layer)

                for node in self.nodes:
                    if (
                        any([i.rect.collidepoint(event.pos) for i in node.inputs])
                        and self.link_sending_node is not None
                        and node != self.link_sending_node
                    ):
                        self.link_sending_node.output_connection = node
                        node.input_connection = self.link_sending_node
                        self.link_sending_node.make_connection = False
                        self.link_sending_node.has_connection = True

                    elif node.output.rect.collidepoint(event.pos):
                        selected_node.make_connection = True
                        self.link_sending_node = selected_node

        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            for n in self.nodes:
                n.dragging = False

    def update(self, mouse_pos: np.array):
        [node.update(mouse_pos) for node in self.nodes]

    def draw(self, screen: pg.Surface):
        [node.draw(screen) for node in self.nodes]
