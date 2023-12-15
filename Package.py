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

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zipcode,
                                                       self.deadline, self.weight, self.deliveryTime,
                                                       self.status)

    def updateStatus(self, updatedTime):
        if self.deliveryTime < updatedTime:
            self.status = "Delivered"
        elif self.departTime > updatedTime:
            self.status = "En-Route"
        else:
            self.status = "At Hub"
