# Hash table to store package data in an organized fashion.

class HashTable:
    # Initialize the hash table with an input initial value
    # Space-time complexity:  O(N)
    def __init__(self, initial):
        # initialize table with empty bucket list entries
        self.table = []
        for i in range(initial):
            self.table.append([])

    # Insert method to input a key(package ID) and item(package) into the hash table
    # Space-Time complexity is O(1)
    def insert(self, key, item):
        bucket = int(key) % len(self.table)
        key_value = [key, item]
        self.table[bucket].append(key_value)

    # Find package based on package ID
    # Space-Time complexity is O(N)
    def find_package(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for index, package in bucket_list:
            return package

    # Remove package from the hash table
    # Space-Time complexity is O(1)
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        if key in bucket_list:
            bucket_list.pop(key)
            return True

    # Return all package objects from the hash table
    # Space-time complexity is O(N^2)
    def return_all(self):
        for bucket in self.table:
            for packages in bucket:
                print(packages[1])

    # Return all packages within the specified time frame.
    # Space-time complexity is O(N^2)
    def return_all_by_time(self, end_time):
        for bucket in self.table:
            for packages in bucket:
                packages[1].print_status_packages(end_time)
