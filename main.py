import pygame
import csv
from data_to_dict import elements_data
pygame.font.init()

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
BLACK = (0, 0, 0)
DARK_GREY = (85,85,85)
EMERALD = (49,145,119)
DARK_PINK = (171,39,79)
TEAL = (0,128,128)

# other constants
FONT = pygame.font.Font('freesansbold.ttf', 16)
WIDTH = 800
HEIGHT = 600

# screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Periodic Table Game - Lucia. S") # screen caption




'''
def element_file(file="data_elements.csv"):
    #prints csv
    with open('eggs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))
'''

class Element:
    def __init__(self, element_name, data): # data is dictionary of elements.
        element_data = data[element_name]
        self.name = elements_data
        self.atomic_number = element_data["AtomicNumber"]
        self.symbol = element_data["Symbol"]
        self.column = element_data["Group"]
        self.row = element_data["Period"]
        self.type = element_data["Type"]
        self.width = WIDTH / 17
        self.height = HEIGHT / 7
        self.drawable = True
        if self.column == "":
            self.drawable = False
            return
        if int(self.column) < 3:
            self.x_pos = (int(self.column) - 1) * self.width
        else:
            self.x_pos = (int(self.column) - 2) * self.width
        self.y_pos = (int(self.row) - 2) * self.height + self.height
        self.hitbox = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)


    def draw_element(self):
        # element colours shown on table
        if not self.drawable:
            return
        
        # print(self.symbol)
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
        # print(self.drawable)
        if self.type in type_colours:
            pygame.draw.rect(SCREEN, type_colours[self.type], self.hitbox)
        else:
            pygame.draw.rect(SCREEN, GREY, self.hitbox)
        # print(self.x_pos, self.y_pos, self.width, self.height)
        SCREEN.blit(FONT.render(self.atomic_number, True, 'black'), (self.x_pos + 5, self.y_pos + 5))
        SCREEN.blit(FONT.render(self.symbol, True, 'black'), (self.x_pos + 5, self.y_pos + 20))

    def draw_info_box(self):
        pygame.draw.rect(SCREEN, GREY, pygame.Rect(self.width * 3, self.height * 0.5, self.width * 8, self.height * 2))
        pygame.draw.rect(SCREEN, BLACK, pygame.Rect(self.width * 3, self.height * 1.5, self.width * 8, self.height * 0.8))
        pygame.draw.rect(SCREEN, DARK_GREY, pygame.Rect(self.width * 3, self.height * 0.5, self.width * 8, self.height * 2))
        
         



"""
background = pygame.image.load('periodic-table2.jpg') # background picture of a periodic table
screen.blit(background, (0, 0)) 
"""




#hydrogen = elements("Carbon", elements_data)
#hydrogen.draw_element()

# Creates objects of elements and puts them in a list
elements = []
for e in elements_data:
    element = Element(e, elements_data)
    if element.drawable:
        elements.append(element)



# keep game loop running
running = True
# game loop 
while running: 
    # gets events (actions)   
    for event in pygame.event.get(): 
        # check if someone close window (QUIT action)       
        if event.type == pygame.QUIT: 
            running = False
    
    SCREEN.fill(CREAM)    
    # Draws periodic table
    for element in elements: 
        element.draw_element()
    
    # Checks if mouse has hit an element
    mouse_pos = pygame.mouse.get_pos()
    for element in elements:
        if pygame.Rect.collidepoint(element.hitbox, mouse_pos[0], mouse_pos[1]):
            highlight = True
            element.draw_info_box()

    pygame.display.flip()
       
        