# Aaron Kephart Student ID: 944803

from Distance import *
from ReadCSV import *

# Read in packages, and read in distance data
ReadCSV.package_read()
ReadCSV.get_package_hash()
get_distance_data()

# Deliver packages on all trucks
truck1.deliver_packages('HUB', truck1.get_packages())
truck2.deliver_packages('HUB', truck2.get_packages())
truck3.deliver_packages('HUB', truck3.get_packages())
total_mileage = float(truck1.mileage + truck2.mileage + truck3.mileage)

# Check values, depending on selection, display alternate menus
# space-time complexity:  O(1)
input_value = -1
while input_value != 4:
    if input_value == 1:
        print("Total Mileage for All Trucks:  " + str(total_mileage))
        HashTable.return_all(ReadCSV.get_package_hash())

    # Display packages by ID
    elif input_value == 2:
        package_input = input("Enter the package ID:")
        print(HashTable.find_package(ReadCSV.package_hash, package_input))

    # Display packages by time
    elif input_value == 3:
        user_end_time = input("Enter the end time in format (HH:MM) military time:  ")
        (end_hrs, end_mins) = user_end_time.split(':')
        print("\nTotal Mileage for All Trucks:  " + str(total_mileage))
        print(f"\nPackage time at {end_hrs}:{end_mins}:")
        HashTable.return_all_by_time(ReadCSV.get_package_hash(),
                                     datetime.timedelta(hours=int(end_hrs), minutes=int(end_mins)))

    input_value = int(input("\n\n*********************\n" +
                            "WGUPS Package Delivery System\n" +
                            "**********************\n\n" +
                            "Please select an option:\n" +
                            "1.  Display all packages\n" +
                            "2.  Look up package by package ID\n" +
                            "3.  Look up package status by time\n" +
                            "4.  Exit Program\n" +
                            "Selection:  "))
