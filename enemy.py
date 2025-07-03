import pygame as pg

class Enemy(pg.sprite.Sprite):

    def __init__(self, image_array):
       pg.sprite.Sprite.__init__(self) 
       self.current_image_array_index = 0 
       self.image_array = image_array         
       self.updateSprite()
       self.rect = self.image.get_rect()
       self.time_since_move = 0
       self.move_timeout = 1

    def update_position(self, dt):
        if self.rect != None:
            self.time_since_move += dt

            if self.time_since_move > self.move_timeout:
                self.time_since_move = 0
                self.rect = self.rect.move(10, 0)
                self.updateSprite()
                
    def updateSprite(self):
       self.image = pg.image.load(self.image_array[self.current_image_array_index]).convert()
#       self.image = pg.transform.scale2x(self.image) 
       self.current_image_array_index = 1 if self.current_image_array_index == 0 else 0 
