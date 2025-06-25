# Example file showing a circle moving on screen
import pygame
import random
from threading import Timer
import game_timer

class Particle:
    time_on_screen = 0
    color = "red"
    radius = 5

    def __init__(self):
        self.show_time = random.randint(5, 10)    
        self.position = None

class Enemy:
    def update_position(self):
        print('In update postion')
        if self.position != None:
            print('Updating')

    def __init__(self, sprite_path) -> None:
        self.sprite = pygame.image.load(sprite_path)
        self.position = None

game_timer = game_timer.GameTimer(print('In Game Timer'), 3)
game_timer.start()

# pygame setup
pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
dt = 0
colors = ["red", "blue", "yellow", "orange", "purple"]

particle_array = []
particle_spawner_timer = .25
time_since_last_circle = 0

enemy_move_timer = 1
time_since_last_enemy_move = 0

player = pygame.image.load('Assets/Sprites/Invaders/space__0006_Player.png')
enemy_1 = Enemy('Assets/Sprites/Invaders/space__0000_A1.png')
enemy_1.position = pygame.Vector2(200, 200)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if time_since_last_circle > particle_spawner_timer : 
        new_particle = Particle()
        new_particle.color = colors[random.randint(0,len(colors)) - 1] 
        new_particle.position = pygame.Vector2(random.random()*width, random.random()*height)

        particle_array.append(new_particle)
        time_since_last_circle = 0

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
 
    particle_array = list(filter(lambda particle : particle.time_on_screen < particle.show_time,particle_array))

    for particle in particle_array:
        particle.time_on_screen += dt
        particle.position = pygame.Vector2(particle.position.x, particle.position.y + dt*200)
        pygame.draw.circle(screen, particle.color, particle.position, particle.radius)

    if time_since_last_enemy_move > enemy_move_timer :
        enemy_1.position = pygame.Vector2(enemy_1.position.x + 20, enemy_1.position.y)
        time_since_last_enemy_move = 0

    screen.blit(player, pygame.Vector2(100, 100))
    screen.blit(enemy_1.sprite, enemy_1.position)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    time_since_last_circle += dt
    time_since_last_enemy_move += dt

pygame.quit()
