# Create class for freight trucks
class Truck:
    def __init__(self, address, capacity, departTime, miles, packages, speed, truckNumber):
        self.address = address
        self.capacity = capacity
        self.departTime = departTime
        self.miles = miles
        self.packages = packages
        self.speed = speed
        self.time = departTime
        self.truckNumber = truckNumber

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.address, self.capacity, self.departTime, self.miles, self.packages,
                                               self.speed, self.truckNumber)
