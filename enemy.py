import pygame as pg

class Enemy(pg.sprite.Sprite):
    def __init__(self):
       pg.sprite.Sprite.__init__(self) 
       self.image = pg.image.load('Assets/Sprites/Invaders/space__0000_A1.png').convert()
       self.rect = self.image.get_rect()
       self.time_since_move = 0
       self.move_timeout = 1


    def update_position(self, dt):
        if self.rect != None:
            self.time_since_move += dt

            if self.time_since_move > self.move_timeout:
                self.time_since_move = 0
                self.rect = self.rect.move(20, 0)
                print(self.rect)
