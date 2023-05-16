import pygame as pg
from src.const import *
from src.editor import NodeEditor


pg.init()
screen = pg.display.set_mode(WIN_SIZE)
pg.display.set_caption("Node Editor")
node_body_font = pg.font.SysFont("Calibri", 20, True, False)
node_title_font = pg.font.SysFont("Calibri", 15, True, False)

editor = NodeEditor(node_title_font, node_body_font)

add_key_text = node_body_font.render("Shift + A: Add Node", True, "snow")
number_key_text = node_body_font.render("Shift + N: Number Node", True, "snow")
delete_key_text = node_body_font.render("Selected + X: Delete Node", True, "snow")


def main() -> None:
    mouse_vec = pg.Vector2()
    while True:
        keys = pg.key.get_pressed()
        mouse_vec.xy = pg.mouse.get_pos()

        for event in pg.event.get():
            editor.manage_events(event, mouse_vec, keys)
            if event.type == pg.QUIT:
                pg.quit()
                return

        screen.fill((60, 60, 60))

        editor.update(mouse_vec)
        editor.draw(screen)

        screen.blit(add_key_text, (10, 10))
        screen.blit(number_key_text, (10, 30))
        screen.blit(delete_key_text, (10, 50))

        pg.display.flip()


if __name__ == "__main__":
    main()
