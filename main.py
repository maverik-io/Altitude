import pygame as pg
from utils import Game

class Altitude(Game):
    def __init__(self):
        super().__init__()
    def main_menu(self):
        pos = self.ev_handler()

        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.logo, self.logo_rect)

        if self.btn_play.update(self.screen, pos):
            self.active_window = self.game
        if self.btn_settings.update(self.screen, pos):
            self.active_window = self.settings
            print('ss')

    def game(self):
        pos = self.ev_handler()

        self.screen.blit(self.bg,(0,0))




def main():
    game = Altitude()

    while True:
        game.run()
        pg.display.update()


if __name__ == "__main__":
    main()
