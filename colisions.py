import pygame
import random 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Block(pygame.sprite.Sprite)
    def _init_(self, color, width, height):
        SUPER()._init_()
        self.image = pygame.Surface([width, height])
        self.image = fill(color)
        self.rect = self.image.get_rect()

pygame.init()

screen_width = 700
scree_heoght
screen = pygame.display.set_mode([screen_wodth, screen_hight])

blcok_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite,Groupe()

for i in range(50):
    blcok = Blcok(black, 20, 15)
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    blcok_list.add(blcok)
    all_sprites_list(block)

player = block(red, 20, 15)
all_sprites_list.add(player)

done = Fales
clock = pygame.time.Clock()

score = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT
            done = True

    screen fill(WHITE)
    pos = pygame.mouse.get_pos()
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    blocks_hits_list=pygame.sprite.spritecollide(player, blcok_list, true)