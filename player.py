import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('Assets/Sprites/Invaders/space__0006_Player.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (300, 300)
