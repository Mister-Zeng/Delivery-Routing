class PackageHashTable:
    def __init__(self, initialCapacity=40):
        self.list = []
        for i in range(initialCapacity):
            self.list.append([])

    # Private method to calculate the hash index for a given package ID
    def _hash(self, packageID):
        # Use the modulo operator to ensure the hash index is within the size of the table
        return hash(packageID) % len(self.list)

    # Method to insert a package into the hash table
    def insert(self, packageID, packageData):
        hashIndex = self._hash(packageID)
        bucketList = self.list[hashIndex]
        # Iterate over the list to check if the package ID already exists
        for keyValue in bucketList:
            if keyValue[0] == packageID:
                keyValue[1] = packageData  # If the package ID exists, update the corresponding package data
                return True
        # If the package ID does not exist, append a new key-value pair to the list
        bucketList.append([packageID, packageData])
        return True

    # Method to search for a package in the hash table
    def lookup(self, packageID):
        hashIndex = self._hash(packageID)
        # Iterate over the list at the hash index
        for data in self.list[hashIndex]:
            if data[0] == packageID:  # If the package ID is found, return the package data
                return data[1]
        return None  # If the package ID is not found, return None

    # Method to remove a package from the hash table
    def remove(self, packageID):
        hashIndex = self._hash(packageID)
        bucketList = self.list[hashIndex]
        # remove package by the packageID if it is found in the bucketList
        if packageID in bucketList:
            bucketList.remove(packageID)
        return False  # If the package ID is not found, return False
