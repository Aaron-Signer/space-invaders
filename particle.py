import random
import pygame

class Particle:
    time_on_screen = 0
    color = "red"
    radius = 5

    def update_position(self, dt):
        self.position = pygame.Vector2(self.position.x, self.position.y + dt*200)

    def __init__(self):
        self.show_time = random.randint(5, 10)    
        self.position = None

        self.move_timeout = 1




