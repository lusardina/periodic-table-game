import pygame
import csv
from data_to_dict import elements_data

# colours
BLUE = (0,128,255)
PURPLE = (170,128,255)
RED = (194,59,34)
YELLOW = (255,234,128)
ORANGE = (255,179,71)
CREAM = (255,247,230)
VIOLET = (203,153,201)
PINK = (244,154,194)
GREY = (132,132,130)
EMERALD = (49,145,119)
DARK_PINK = (171,39,79)
TEAL = (0,128,128)

'''
def element_file(file="data_elements.csv"):
    #prints csv
    with open('eggs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))
'''

class elements:
    def __init__(self, element_name, data): # data is dictionary of elements.
        element_data = data[element_name]
        self.name = elements_data
        self.atomic_number = element_data["AtomicNumber"]
        self.symbol = element_data["Symbol"]
        self.column = element_data["Group"]
        self.row = element_data["Period"]
    def draw_element(self):
        # element colours shown on table
        print(self.symbol)
        type_colours = {
            "Alkali Metal": RED, 
            "Alkaline Earth Metal": ORANGE,
            "Transition Metal": YELLOW,
            "Nonmetal": BLUE,
            "Halogen": VIOLET,
            "Noble Gas": PURPLE,
            "Lanthanide": PINK,
            "Actinide": TEAL, 
            "Metalloid": DARK_PINK, 
            "Reactive Nonmetals": EMERALD, 
            "Unknown Properties": GREY, 
            }  
        pygame.draw.rect(screen, type_colours["Alkali Metal"], pygame.Rect(30, 30, 60, 60))
        pygame.display.flip()
        pass

# screen
screen = pygame.display.set_mode((1100, 713))
pygame.display.set_caption("Periodic Table Game - Lucia. S") # screen caption
screen.fill(CREAM) 
'''
background = pygame.image.load('periodic-table2.jpg') # background picture of a periodic table
screen.blit(background, (0, 0)) 
'''
pygame.display.flip() # update full display to screen


hydrogen = elements("Hydrogen", elements_data)
hydrogen.draw_element()

# keep game loop running
running = True
# game loop 
while running: 
    
# gets events (actions)   
    for event in pygame.event.get(): 
        # check if someone close window (QUIT action)       
        if event.type == pygame.QUIT: 
            running = False