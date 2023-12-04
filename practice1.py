import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Object")

# Set up object
object_size = 50
object_color = (255, 0, 0)
object_pos = [width // 2, height // 2]
object_speed = [5, 5]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update object position
    object_pos[0] += object_speed[0]
    object_pos[1] += object_speed[1]

    # Bounce off the walls
    if object_pos[0] <= 0 or object_pos[0] >= width - object_size:
        object_speed[0] = -object_speed[0]
    if object_pos[1] <= 0 or object_pos[1] >= height - object_size:
        object_speed[1] = -object_speed[1]

    # Fill the screen with a background color
    screen.fill((255, 255, 255))

    # Draw the bouncing object
    pygame.draw.rect(screen, object_color, (object_pos[0], object_pos[1], object_size, object_size))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(60)