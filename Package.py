import datetime


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
        if self.deliveryTime is None or updatedTime < self.departureTime:
            self.status = "At Hub"
        elif self.deliveryTime >= updatedTime:
            self.status = "En-Route"
        else:
            self.status = "Delivered"

        # Update package 9 with correct address on 10:20
        if self.ID == "9":
            if updatedTime >= datetime.timedelta(hours=10, minutes=20):
                self.address = "410 S State St"
                self.city = "Salt Lake City"
                self.state = "UT"
                self.zipcode = "84111"

        # Package 6, 25, 28, 32 are on flight until 9:05
        if self.ID == "6" or self.ID == "25" or self.ID == "28" or self.ID == "32":
            if updatedTime < datetime.timedelta(hours=9, minutes=5):
                self.status = "On Flight"
                self.truckNumber = None
