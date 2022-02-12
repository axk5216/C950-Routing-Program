# C950-Routing-Program

Using the nearest neighbor algorithm, this program delivers 40 packages spanned across three trucks with multiple constraints such as delivery deadlines, delays, and other constraints.

Using nearest neighbor algorithm, loop through packages in list on specified truck until all packages have a timestamp (indicating they are delivered)
a. After loop, determine which undelivered package is the nearest to the current location
b. Deliver package to that location, update status, and place time stamp on package, adding the time it takes to deliver package to the start delivery time of truck, assign this value to the package delivery timestamp
c. Recursively loop through checking packages, and deliver to the nearest location until all addresses have been delivered.
d. Repeat function 7 until all trucks have delivered packages.

Example: Truck – Hub
Package 1 – 3.1 miles away
Package 2 – 2.4 miles away

For example: [1,2] are not delivered. Find the nearest distance from the hub, which is package 2. From package (2) address, find the next closest package to deliver. In this case, it would be package (1). Deliver package (1). Since both packages are delivered, return to the hub from package (1) and track distance, time for the trip.



Both the self-adjusting nearest neighbor algorithm and hash table are scalable due to their ability to adjust based on the number of packages presented. The package and truck classes also scale to the demands of the program. The lists created to load the trucks are designed in such a way to manually load the trucks; there are some concerns about scalability in this regard. In this case, there were only 40 packages, so lists were manually created. However, if more packages were present, an additional sorting algorithm could be implemented to sort packages by if-else constraints and load the trucks. After careful analysis, this is the only area of the program that will not adapt well based on the number of packages and trucks.



The hash table is a self-adjusting data structure that contains key-value pairs, allowing an organized way to store and retrieve data. By pairing this data into key-value pairs inside of buckets, retrieval times are dramatically improved. Hash tables have an average complexity of O(1) and worst-case performance of O(N). However, hash tables have disadvantages, especially when there are collisions, which impacts performance negatively. Collisions occur especially when there is a large amount of data, or if the data grows to a level greater than the amount of buckets present. In addition, the data stored in the hash table is unordered, so time complexity increases as additional items are added especially when lookups occur.
The nearest neighbor algorithm is also a self-adjusting data structure that has a complexity of O(N2). The implementation of nearest neighbor algorithm is intuitive; deliver to the next nearest location until finished. Disadvantages include more optimal alternative solutions with similar space-time complexity exist, and the optimism of the nearest neighbor appears to drop as additional packages are handled
