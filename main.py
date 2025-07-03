# Example file showing a circle moving on screen
import pygame
import random
from threading import Timer
#import game_timer
from enemy import Enemy
from particle import Particle
from player import Player

#game_timer = game_timer.GameTimer(print('In Game Timer'), 3)
#game_timer.start()

#TODO: Maybe have a row factory
invaders_row_1_image_array = [
    'Assets/Sprites/Invaders-32/space__0000_A1.png',
    'Assets/Sprites/Invaders-32/space__0001_A2.png'
]
invaders_row_2_image_array = [
    'Assets/Sprites/Invaders-32/space__0002_B1.png',
    'Assets/Sprites/Invaders-32/space__0003_B2.png'
] 
  
 
# pygame setup
pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
dt = 0
colors = ["red", "blue", "yellow", "orange", "purple"]

row_1_invaders = []
row_2_invaders = []

particle_array = []
particle_spawner_timer = .25
time_since_last_circle = 0

player = Player()

for i in range(0,11):
    invader = Enemy(invaders_row_1_image_array)
    invader.rect.topleft = (100 + i*60, 200)
    row_1_invaders.append(invader)


for i in range(0,11):
    invader = Enemy(invaders_row_2_image_array)
    invader.rect.topleft = (100 + i*60, 250)
    row_2_invaders.append(invader)


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
        particle.update_position(dt)
        pygame.draw.circle(screen, particle.color, particle.position, particle.radius)

#    particle_array = list(map(lambda particle: particle.update_position(), particle_array))

    for invader in row_1_invaders:
        invader.update_position(dt)
        screen.blit(invader.image, invader.rect)

    for invader in row_2_invaders:
        invader.update_position(dt)
        screen.blit(invader.image, invader.rect)


    screen.blit(player.image, player.rect)
    pygame.display.flip()

    dt = clock.tick(60) / 1000
    time_since_last_circle += dt

pygame.quit()
