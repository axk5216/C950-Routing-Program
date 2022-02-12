import csv
from ReadCSV import *
distances = []

# Read in the CSV, read distance data and append to distances list
# Space-Time complexity:  O(N)
def get_distance_data():
    with open('WGUPSDistanceTable.csv') as csv_distance:
        csvRead = csv.reader(csv_distance, delimiter=',')
        for row in csvRead:
            distances.append(row)

# Retrieve row index for the get_distance method
# Space-Time complexity is O(N)
def get_row_index(current):
    row_index = -1
    for row in distances:
        row_index += 1
        if row[0] == current:
            return row_index


# Retrieve distance.  If nothing is in that cell, read the inverse column/row
# Space-time complexity O(1)
def get_distance(current, destination):
    current_address = get_row_index(current)
    destination_address = get_row_index(destination)

    if distances[destination_address][current_address+1] == '':
        return distances[current_address][destination_address+1]
    else:
        return distances[destination_address][current_address+1]






