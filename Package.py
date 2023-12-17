class Package:
    def __init__(self, ID, address, city, state, zipcode, deadline, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departureTime = None
        self.deliveryTime = None
        self.truckNumber = None

    def __str__(self):
        if self.status == "Delivered":
            return "ID: %s, Address: %s, City: %s, State: %s, Zipcode: %s, Deadline: %s, Weight: %s, Delivery Time: " \
                   "%s, Status: %s, Truck Number: %s" % (self.ID, self.address, self.city, self.state, self.zipcode,
                                                         self.deadline, self.weight, self.deliveryTime, self.status,
                                                         self.truckNumber)
        else:
            return "ID: %s, Address: %s, City: %s, State: %s, Zipcode: %s, Deadline: %s, Weight: %s, Status: %s, , " \
                   "Truck Number: %s" % (self.ID, self.address, self.city, self.state, self.zipcode, self.deadline,
                                         self.weight, self.status, self.truckNumber)

    def updateStatus(self, updatedTime):
        if self.deliveryTime <= updatedTime:
            self.status = "Delivered"
        elif self.departTime >= updatedTime:
            self.status = "En-Route"
        else:
            self.status = "At Hub"
