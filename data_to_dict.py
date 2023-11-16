import csv

elements_data = {}

with open("data_elements.csv") as file_data_elements:
    for line in csv.DictReader(file_data_elements):
        elements_data[line["Element"]] = dict(line) # adds each row of CSV file into the dictionary "elements_data"

print(elements_data) # it works!!!

"""
element = input("What element do you want to access? ").title()
while True:
    what_data = input(f"What would you like to know about the element {element}? (if nothing type 'nothing'): ")
    if what_data.lower() == "nothing":
        break
    answer = elements_data[element][what_data]
    print(f"The {what_data} of {element} is {answer}!")
"""