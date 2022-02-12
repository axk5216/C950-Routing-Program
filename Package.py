# Package class to store package objects and information about packages
from Truck import *
from ReadCSV import *


class Package:

    # Initialize method, constructor for package object
    def __init__(self, package_id, address, city, state, zipcode, deadline, weight, note, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.note = note
        self.status = status
        self.delivery_time = None
        self.mileage = 0
        self.departure_time = None

    def getpackageid(self):
        return self.package_id

    def getaddress(self):
        return self.address

    def get_mileage(self):
        return self.mileage

    def set_status(self, status):
        self.status = status

    def get_status(self, status):
        return self.status

    def deliver_package(self, delivery_time, mileage):
        self.delivery_time = delivery_time
        self.mileage = mileage

    def is_delivered(self):
        return self.delivery_time is not None

    def is_not_delivered(self):
        return not self.is_delivered()

    # Override string class to include package information
    def __str__(self):
        package = f"{self.package_id}\t{self.address}\t{self.city}\t{self.state}\t{self.zipcode}\t{self.deadline}" \
                  f"\t{self.weight}\t{self.note}\t{self.status}"
        return package

    # Print the status of package based on time
    # Simulated times based on package delivery time, and truck departure times
    # Time-complexity O(1)
    def print_status_packages(self, end_time):
        status_code = "DELIVERED"

        if self.delivery_time <= end_time:
            status_code = "DELIVERED at " + str(self.delivery_time)
        elif self.departure_time < end_time:
            status_code = "EN_ROUTE"
        else:
            status_code = "AT HUB"

        package = f"{self.package_id}\t{self.address}\t{self.city}\t{self.state}\t{self.zipcode}\t{self.deadline}" \
                  f"\t{self.weight}\t{self.note}\t{status_code}"

        print(package)
