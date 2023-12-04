"""Cinema Hack 110 Project - Ana Restrepo and Ashley Artica"""

name: str = input("Hello Player. Please enter your name: ")

print(f"Hello {name}, you have wandered into the mansion of Thorne Blackwood. Blackwood was once a world renown director who directed horror films. One day he read on a news article where critics were calling his newest horror film lame, boring, and mediocre. This enraged Blackwood and since he has made it his sole purpose in life to create a REAL horror movie.")


# Import statements
import pygame, sys
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
import random

from background import *
# Import from our other modules, use * to get everything (usually not a 
# good idea but since we made the files and we know what's in it it's okay)
#from constants import *

# Initialize pygame

size = width, height = 840, 680
screen = pygame.display.set_mode(size)

BLACK = (3, 1, 0)
WHITE = (253, 252, 251)
GOLD = (255, 204, 0)
BROWN = (150, 75, 0)

pygame.init()

clock = pygame.time.Clock()

player = pygame.Rect(5, height/5, 30, 30)

obstacle_top = pygame.Rect(0, -200, width, height/2)
obstacle_bottom = pygame.Rect(0, height/2 + 200, width, height/2)
obstacle_1 = pygame.Rect(200, height/3, 200, height/5)

obstacle_list = [obstacle_top, obstacle_bottom, obstacle_1]

key = pygame.Rect(width - 75, height/2, 50, 50)

running = True

pygame.mouse.set_visible(False)

collision_count = 0
key_count = 0


# Setting up the window

# Create some sprites and a background surface by calling their class constructors
background = Background()
win_zone = win_zone()


# Update the background and render separately because its not in the sprite group


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.kay == pygame.K_ESCAPE):
            running = False
            
    screen.fill(BROWN)
    background.update()
    background.render(screen)

    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, BLACK, obstacle_top)
    pygame.draw.rect(screen, BLACK, obstacle_bottom)
    pygame.draw.rect(screen, BLACK, obstacle_1)

    pygame.draw.circle(screen, GOLD, key.center, key.width/2)

    for obstacle in obstacle_list:
        if player.colliderect(obstacle):
            pygame.mouse.set_pos(5, height/2)
            collision_count += 1
            if collision_count == 3:
                running = False

    if player.colliderect(key):
        key_count += 1
        key.centerx = random.randint(10, width - 10)
        if key_count == 4:
           #check if key_count == 1 then door open and game closes 
           print("YOU WON!")
           running = False
    

    player.center = pygame.mouse.get_pos()

    pygame.display.flip()

    clock.tick(60)



