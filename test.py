import pygame
import random

# TODO Replace block black fill color with asteriod image - DONE
# TODO Replace player block red fill color with spaceship image - DONE
# TODO Make asteriods move in random directions - Done

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Block(pygame.sprite.Sprite):
"""
This class represents the ball.
It derives from the "Sprite" class in Pygame
"""

# changed color parameter to a filename for the image
def __init__(self, image_name, width, height, isPlayer):
""" Constructor. Pass in the color of the block,
and its size."""

super().__init__()

# Create an image of the block, and fill it with a color.
# This could also be an image loaded from the disk.
self.image = pygame.Surface([width, height])
# changed this line to have it hold an image
self.image = pygame.image.load(image_name)

self.xVel = random.randrange(-2, 2)
self.yVel = random.randrange(-2, 2)
self.player = isPlayer

# Fetch the rectangle object that has the dimensions of the image
# Update the position of this object by setting the values
# of rect.x and rect.y
self.rect = self.image.get_rect()

def moveBlock(self):
self.rect.x += self.xVel
self.rect.y += self.yVel

def playerCharacter(self):
return self.player


# initialize pygame
pygame.init()

# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# This is a list of 'sprites'. Each block in the program is
# added to this list. The list is managed by a class called 'Group'.
block_list = pygame.sprite.Group()

# This is a list of every sprite.
# All the blocks and the player block as well.

all_sprites_list = pygame.sprite.Group()

for i in range(50):
# This represents a block
block = Block("asteriod2.png", 20, 20, False)

# Set a random location for the block
block.rect.x = random.randrange(screen_width)
block.rect.y = random.randrange(screen_height)

# Add the block to the list of objects
block_list.add(block)
all_sprites_list.add(block)

# Create a RED player block
player = Block("spaceShip.png", 39, 32, True)
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0

# ------- Main Program Loop --------
while not done:
for event in pygame.event.get():
if event.type == pygame.QUIT:
done = True

# Clear the screen
screen.fill(BLACK)

# Get the current mouse position. This returns the position
# as a list of two numbers.
pos = pygame.mouse.get_pos()

# Fetch the x and y out of the list
# Set the player object to the mouse location
player.rect.x = pos[0]
player.rect.y = pos[1]

# See if the player block has collided with anything
# The third parameter will remove the sprite
blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

# Check the list of collisions
for block in blocks_hit_list:
score += 1
print(score)

# update the position
for block in all_sprites_list:
if not block.playerCharacter():
block.moveBlock()

# Draw all the sprites
all_sprites_list.draw(screen)

# Go ahead and update the screen with what we've drawn.
pygame.display.flip()

# Limit to 60 frames per second
clock.tick(60)

pygame.quit()