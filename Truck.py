# Create class for freight trucks
class Truck:
    def __init__(self, address, capacity, departureTime, miles, packages, speed, truckNumber):
        self.address = address
        self.capacity = capacity
        self.departureTime = departureTime
        self.miles = miles
        self.packages = packages
        self.speed = speed
        self.time = departureTime
        self.truckNumber = truckNumber

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.address, self.capacity, self.departureTime, self.miles,
                                               self.packages, self.speed, self.truckNumber)
