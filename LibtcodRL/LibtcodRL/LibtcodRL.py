import libtcodpy as ltc

WIDTH = 800
HEIGHT = 600
STR_TITLE = "Libtcod RL"
TITLE = bytearray()
TITLE.extend(STR_TITLE)

ltc.console_init_root(WIDTH, HEIGHT, TITLE)
console = ltc.console_new(WIDTH, HEIGHT)
ltc.console_blit(console, 0, 0, WIDTH, HEIGHT, 0, 0, 0)

# MAIN GAME LOOP

ltc.console_flush()
ltc.console_fill_background(console, 100, 100, 100)
ltc.console_blit(console, 0, 0, WIDTH, HEIGHT, 0, 0, 0)
ltc.console_clear(console)
