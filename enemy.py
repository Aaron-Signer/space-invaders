import pygame

class Enemy:
    def update_position(self, dt):
        if self.position != None:
            self.time_since_move += dt

            if self.time_since_move > self.move_timeout:
                self.time_since_move = 0
                self.position = pygame.Vector2(self.position.x + 20, self.position.y)


    def __init__(self, sprite_path) -> None:
        self.sprite = pygame.image.load(sprite_path).convert()
        self.position = None
        self.time_since_move = 0
        self.move_timeout = 1

        
