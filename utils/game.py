import pygame as pg
from sys import exit

from .txt_button import TxtButton


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((640, 960))
        self.clock = pg.time.Clock()

        # Assets
        self.bg = pg.image.load("assets/images/background.png").convert()
        self.logo = pg.image.load("assets/images/logo.png").convert_alpha()
        self.logo_rect = self.logo.get_rect(center=(320, 250))
        self.icon = pg.image.load("assets/images/icon.png").convert_alpha()

        self.big_font = pg.font.Font("assets/fonts/Roboto.ttf", 40)

        # Buttons
        self.btn_play = TxtButton(320, 500, "Play", "#ffffff", self.big_font)
        self.btn_settings = TxtButton(320, 600, "Settings", "#ffffff", self.big_font)

        self.active_window = self.main_menu

        pg.display.set_caption("Altitude")
        pg.display.set_icon(self.icon)

    def run(self):
        self.active_window()

    def ev_handler(self):
        pos = (0, 0)
        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()

        return pos

    def game(self):
        self.active_window = self.main_menu

    def main_menu(self):
        self.ev_handler()
        self.screen.fill('#333333')
        txt = self.big_font.render('Game',True,'#FFFFFF')
        self.screen.blit(txt,txt.get_rect(center = (320,480)))

    def settings(self):
        self.active_window = self.main_menu
