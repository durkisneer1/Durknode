import pygame as pg
import numpy as np
from src.const import *
from src.editor import NodeEditor


pg.init()
screen = pg.display.set_mode(WIN_SIZE)
pg.display.set_caption("Node Editor")
cat_img = pg.transform.scale(pg.image.load("assets/cat.png").convert(), WIN_SIZE)

node_body_font = pg.font.SysFont("Calibri", 20, True, False)
node_title_font = pg.font.SysFont("Calibri", 15, True, False)

editor = NodeEditor(node_title_font, node_body_font)

add_key_text = node_body_font.render("Shift + A: Add Node", True, "snow")
number_key_text = node_body_font.render("Shift + N: Number Node", True, "snow")
delete_key_text = node_body_font.render("Selected + X: Delete Node", True, "snow")


def main() -> None:
    mouse_pos = np.array([0, 0])
    while True:
        keys = pg.key.get_pressed()
        mouse_pos[0], mouse_pos[1] = pg.mouse.get_pos()

        for event in pg.event.get():
            editor.manage_events(event, mouse_pos, keys)
            if event.type == pg.QUIT:
                pg.quit()
                return

        screen.fill((50, 50, 50))
        # screen.blit(cat_img, (0, 0))

        editor.update(mouse_pos)
        editor.draw(screen)

        screen.blit(add_key_text, (10, 10))
        screen.blit(number_key_text, (10, 30))
        screen.blit(delete_key_text, (10, 50))

        pg.display.flip()


if __name__ == "__main__":
    main()
