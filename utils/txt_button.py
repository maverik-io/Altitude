import pygame as pg

"""
This file contains the Ui classes.
"""


class TxtButton:
    """
    INITALIZE THE BUTTON
    Syntax: TxtButton(x, y, txt, color, font)

    :param x: x position of the button
    :param y: y position of the button
    :param txt: text to be displayed on the button
    :param color: color of the text
    :param font: font of the text
    """

    def __init__(self, x, y, txt, color, font):
        self.txt = txt
        self.label = font.render(txt, True, color)
        self.rect = self.label.get_rect(center=(x, y))
        self.bgrect = self.rect.inflate(30, 30)
        self.clicked = False
        self.color = color
        self.font = font

        self.bg_surf = pg.Surface(self.bgrect.size)
        self.bg_surf.set_alpha(128)
        pg.draw.rect(self.bg_surf, '#000000',(0,0,*self.bgrect.size), 0,30)

    def update(self, surface, pos):
        action = False

        mp = pg.mouse.get_pos()
        if self.rect.collidepoint(mp):
            surface.blit(self.bg_surf, self.bgrect)
        if self.rect.collidepoint(pos):
            action = True
        surface.blit(self.label, self.rect)
        return action
