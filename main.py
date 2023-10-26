import pygame

# colours
BLUE = (0,128,255)
PURPLE = (170,128,255)
RED = (194,59,34)
YELLOW = (255,234,128)
ORANGE = (255,179,71)
CREAM = (255,247,230)
VIOLET = (203,153,201)
PINK = (244,154,194)

# screen
screen = pygame.display.set_mode((1100, 713))
pygame.display.set_caption("Periodic Table Game - Lucia. S") # screen caption
screen.fill(PURPLE) 
#background = pygame.image.load('periodic-table2.jpg') # background picture of a periodic table
#screen.blit(background, (0, 0)) 
pygame.display.flip() # update full display to screen

'''
# metal colours shown on table
type_colours = {
    "Alkali Metal": "", 
    "Alkaline Earth Metal": "",
    "Transition Metal": "",
    "Nonmetal": "",
    "Halogen": "",
    "Noble Gas": "",
    "Lanthanide": "",
    "Actinide": "", 
    "Metalloid": "", 
    "Reactive Nonmetals": "", 
    "Unknown Properties": "", 
    }  
'''


# keep game loop running
running = True
# game loop 
while running: 
    
# gets events (actions)   
    for event in pygame.event.get(): 
        # check if someone close window (QUIT action)       
        if event.type == pygame.QUIT: 
            running = False