import pygame as pg
from src.const import *
from src.editor import NodeEditor


pg.init()
screen = pg.display.set_mode(WIN_SIZE)
pg.display.set_caption("Node Editor")
font = pg.font.SysFont("Calibri", 20, True, False)

editor = NodeEditor(font)

add_key_text = font.render("Shift + A: Add Node", True, "snow")
number_key_text = font.render("Shift + N: Number Node", True, "snow")


def main() -> None:
    mouse_vec = pg.Vector2()
    while True:
        keys = pg.key.get_pressed()
        mouse_vec.xy = pg.mouse.get_pos()
        events = pg.event.get()
        for ev in events:
            if ev.type == pg.QUIT or (ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE):
                pg.quit()
                return

        screen.fill((60, 60, 60))

        editor.update(events, mouse_vec, keys)
        editor.draw(screen)

        screen.blit(add_key_text, (10, 10))
        screen.blit(number_key_text, (10, 30))

        pg.display.flip()


if __name__ == "__main__":
    main()
