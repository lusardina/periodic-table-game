import csv

elements_data = {}

with open("data_elements.csv") as file_data_elements:
    for line in csv.DictReader(file_data_elements):
        elements_data[line["Element"]] = line # adds each row of CSV file into the dictionary "elements_data"

# print(elements_data) # it works!!!

"""
element = input("What element do you want to access? ").title()
while True:
    what_data = input(f"What would you like to know about the element {element}? ('nothing' to finish; 'list' to print possible properties ): ")
    if what_data.lower() == "nothing":
        break
    elif what_data.lower() == "list":
        print("here is a list of the properties you can choose from:")
        for key in elements_data[element]:
            print(f"- {key}")
    else:       
        answer = elements_data[element][what_data]
        print(f"The {what_data} of {element} is {answer}!")
"""
