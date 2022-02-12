import datetime

import Distance
import ReadCSV
import HashTable
from Distance import *


class Truck:
    def __init__(self, truck, depart_time):
        self.truck = truck
        self.depart_time = depart_time
        self.packages = []
        self.delivery = depart_time
        self.mileage = 0

    def add_packages(self, package_list):
        self.packages = package_list

    def get_packages(self):
        return self.packages

    def get_delivery(self):
        return self.delivery

    def set_delivery(self, delivery_time):
        self.delivery = delivery_time

    # Determine if package is delivered or not
    # Space-time complexity:  O(N)
    def packages_delivered(self):
        for package_id in self.packages:
            if ReadCSV.package_hash.find_package(package_id).is_not_delivered:
                return False
        return True

    def mileage_truck(self):
        return self.mileage

    # Deliver packages algorithm determines current address, starting at the hub, and loops through the package list
    # to determine which package is nearest, if and only if the package is not yet delivered.
    # once the nearest location is determined in the package list, deliver the package.
    #
    # If the package is delivered, update the current location to the delivery address, and check remaining packages
    # to determine if remaining packages are delivered or not.  If package is not delivered, compare the distances
    # until the closest is found.  Deliver the package until all packages are delivered in the package list.
    # Space-time complexity:  O(N)
    def deliver_packages(self, current_address, package_list):
        minimum_package_id = -1
        minimum_distance = 99.0

        for package_index in package_list:
            package = ReadCSV.package_hash.find_package(package_index)
            package.departure_time = self.depart_time
            if package.is_not_delivered():
                d = Distance.get_distance(current_address, package.address)
                if float(d) < minimum_distance:
                    minimum_distance = float(d)
                    minimum_package_id = package_index

        if minimum_package_id != -1:
            package = ReadCSV.package_hash.find_package(minimum_package_id)
            package.delivery_time = datetime.timedelta(minutes=minimum_distance * (60/18)) + self.delivery
            self.delivery = package.delivery_time

            package.mileage = minimum_distance
            self.mileage += package.mileage

            package.status = "DELIVERED at " + str(package.delivery_time)
            self.deliver_packages(package.address, package_list)

        else:
            self.mileage += float(Distance.get_distance('HUB', package.address))
            self.delivery = datetime.timedelta(minutes=self.mileage * (60/18)) + self.depart_time


