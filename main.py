import pygame

# colours
BLUE = (0,128,255)
PURPLE = (170,128,255)
RED = (204,34,0)
YELLOW = (255,234,128)

# screen
screen = pygame.display.set_mode((1100, 713))
pygame.display.set_caption("Periodic Table Game - Lucia. S") # screen caption
screen.fill(YELLOW) 
background = pygame.image.load('periodic-table2.jpg') 
screen.blit(background, (0, 0)) 
pygame.display.flip() # update full display to screen
  

# keep game loop running
running = True
# game loop 
while running: 
    
# gets events (actions)   
    for event in pygame.event.get(): 
        # check if someone close window (QUIT action)       
        if event.type == pygame.QUIT: 
            running = False