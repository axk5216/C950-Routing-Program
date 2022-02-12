from Package import *
from Truck import *
from HashTable import *

package_hash = HashTable(40) # Create hash table
truck1 = Truck("truck1", datetime.timedelta(hours=8, minutes=0))  # first truck
truck2 = Truck("truck2", datetime.timedelta(hours=9, minutes=5)) # second truck
truck3 = Truck("truck3", datetime.timedelta(hours=12, minutes=0)) # set truck3 depart time to truck2 delivery time

# Read in values from the CSV file as key/value pairs, iterating through the provided data
# Space-time complexity is O(N)
def package_read():
    with open('WGUInputData.csv') as isfile:
        csvRead = csv.reader(isfile, delimiter=',')  # Read CSV package data

        for row in csvRead:
            package_ID = row[0]
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            deadline = row[5]
            weight = row[6]
            note = row[7]
            status = 'AT_HUB'

            package = Package(package_ID, address, city, state, zip_code, deadline, weight, note, status)
            package_hash.insert(package_ID, package)

            if package_ID == '9':
                address = '410 S State St'
                zip_code = '84111'

    truck1.add_packages([1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40])
    truck2.add_packages([2, 3, 4, 5, 6, 7, 8, 10, 18, 27, 28, 32, 33, 36, 38, 25])
    truck3.add_packages([9, 11, 12, 17, 21, 22, 23, 24, 26, 39, 35])


def get_package_hash():
    return package_hash





