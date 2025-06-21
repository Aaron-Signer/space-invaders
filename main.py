# Example file showing a circle moving on screen
import pygame
import random

class Particle:
    time_on_screen = 0
    position = None
    color = "red"
    radius = 5

    def __init__(self):
        self.show_time = random.randint(5, 10)    


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

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

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
 
    new_random_pos = pygame.Vector2(random.random()*width, random.random()*height)
    particle_array = list(filter(lambda particle : particle.time_on_screen < particle.show_time,particle_array))

    for particle in particle_array:
        particle.time_on_screen += dt
        particle.position = pygame.Vector2(particle.position.x, particle.position.y + dt*200)
        pygame.draw.circle(screen, particle.color, particle.position, particle.radius)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    time_since_last_circle += dt

pygame.quit()
