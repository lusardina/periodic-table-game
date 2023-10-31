import pygame
import csv

# colours
BLUE = (0,128,255)
PURPLE = (170,128,255)
RED = (194,59,34)
YELLOW = (255,234,128)
ORANGE = (255,179,71)
CREAM = (255,247,230)
VIOLET = (203,153,201)
PINK = (244,154,194)

'''
def element_file(file="data_elements.csv"):
    #prints csv
    with open('eggs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))
'''

class elements:
    def __init__(self, name, atomic_num, symbol, weight, col, row):
        self.name = name
        self.atomic_number = atomic_num
        self.symbol = symbol
        self.column = col
        self.row = row
    def draw_element(self):
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