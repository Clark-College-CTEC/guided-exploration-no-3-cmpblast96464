# Guided Exploration No. 3
# Carlos Mercado Perez

# to generate a random number
import random

# This list was declared empty for later to be used to store values later
possible_names = []

# this line of code going to open a new file named 'rap-names-output.txt'
outputFile = open('rap-names-output.txt', 'w')

# this opens the file as the varaible dataFile
with open('rap-names.txt', 'r') as dataFile:
    # it well itrate every name within the file
    for name in dataFile:
        # then it well be added to the empty list
        possible_names.append(name.rstrip())

# ask the count of names you want to create
count = int(input('How many rap names would you like to create? '))
# ask the amount of part each name should have
parts = int(input('How many parts should the name contain? '))

# this loop only by the number of names wanted by the user
for i in range(count):
    # this is a empty list
    name_parts = []
    # this loops only by the number of parts for each names
    for j in range(parts):
        # then for each part it will be add to the empty list
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])


# this will format the outputfile evey name that was made in the new file
outputFile.write(f"{' '.join(name_parts)}\n")
# this well print and display the names in the terminal
print(f"{' '.join(name_parts)}")


# this close the output file
outputFile.close()
