import pygame 
pygame.init
# variables for our game
# colers
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0] 

# size of the window 
size = [700, 500]

#varibale for the screen
screen = pygame.display.set_mode(size)
#set the name of window
pygame.display.set.caption("My Game")
#control the game loop
playing = True
# Helps Controls the FPS
clock = pygame.time.Clock() 

#----GAME LOOP ----
while playing:
  # check and handle events 
  for evnt in pygame.event.get():
    if event.type == pygam.QUITE:
      playing = False

  # ---- Game logic (update varibale)

  # --- Drawing 
  screen.fill(BLACK)
  # at the end of Drawing 
  pygame.display.flip()

  # update the clock 
  clock.tick(60)