# Author: Jason Zeng
# Student ID: 011745518

import csv
import datetime

from Package import Package
from PackageHashTable import PackageHashTable
from Truck import Truck


# Read the CSV files
def readCsv(filePath):
    with open(filePath) as csvFile:
        CSVReader = csv.reader(csvFile)
        CSVReader = list(CSVReader)
        return CSVReader


# Loading the CSV files
AddressCSV = readCsv("csv/address.csv")
DistanceCSV = readCsv("csv/distance.csv")
PackageCSV = readCsv("csv/package.csv")

# Initialize the package data hash table
packageData = PackageHashTable()


# Loading all the packages into the hash table
def loadPackageData():
    for p in PackageCSV:
        package = Package(*p[:7], "At Hub")
        packageData.insert(int(p[0]), package)


loadPackageData()


# Calculate the distance between two addresses
def distanceBetweenAddress(addressOne, addressTwo):
    distance = DistanceCSV[addressOne][addressTwo] or DistanceCSV[addressTwo][addressOne]
    return float(distance) if distance else 0.0


# Get the address ID based on the address string
def getAddress(address):
    return next(int(row[0]) for row in AddressCSV if address in row[2])


# Create 3 trucks with initial package assignment
truck1 = Truck("4001 South 700 East", 16, datetime.timedelta(hours=8), 0.0,
               [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40, 11, 33], 18, 1)
truck2 = Truck("4001 South 700 East", 16, datetime.timedelta(hours=10, minutes=20), 0.0,
               [3, 18, 36, 38, 9, 12, 17, 21, 22, 23, 24, 26, 27, 35, 39], 18, 2)
truck3 = Truck("4001 South 700 East", 16, datetime.timedelta(hours=9, minutes=5), 0.0,
               [2, 4, 5, 6, 7, 8, 10, 25, 28, 32], 18, 3)


# Function to deliver packages for a given truck using a nearest neighbor algorithms
def deliverPackage(truck):
    # Get the list of packages to be delivered from the truck
    notDelivered = []

    for packageID in truck.packages:
        package = packageData.lookup(packageID)
        notDelivered.append(package)

    # Clear the package list of the truck for depopulation in the order of nearest neighbors
    truck.packages.clear()

    # Iterate until all packages are delivered
    while notDelivered:
        # Find the nearest neighbor based on distance
        nextAddress = 9999
        nextPackage = None

        for package in notDelivered:
            if distanceBetweenAddress(getAddress(truck.address), getAddress(package.address)) <= nextAddress:
                nextAddress = distanceBetweenAddress(getAddress(truck.address), getAddress(package.address))
                nextPackage = package

        # Add the next closest package to the truck package list
        truck.packages.append(nextPackage.ID)

        # Remove the same package from the not_delivered list
        notDelivered.remove(nextPackage)

        # Update the truck's miles, address, truck time, and the truck that the package is loaded on
        truck.miles += nextAddress
        truck.address = nextPackage.address
        nextPackage.truckNumber = truck.truckNumber
        truck.time += datetime.timedelta(hours=nextAddress / truck.speed)

        # Update the delivery and departure times for the next package
        nextPackage.deliveryTime, nextPackage.departTime = truck.time, truck.departTime


# Deliver packages for each truck
deliverPackage(truck1)
deliverPackage(truck2)
deliverPackage(truck3)


# Function to check the status of packages at a given time
def checkPackageStatus(userInputTime):
    try:
        (h, m) = userInputTime.split(":")
        time = datetime.timedelta(hours=int(h), minutes=int(m))

        # Get status for individual or all package(s)
        secondInput = input("Type 'single' to view the status of a individual package. Type 'all' to view the status "
                            "of all the packages.")

        # Get status for individual package based on package ID
        if secondInput == "single":
            try:
                packageID = input("Enter the package ID")
                package = packageData.lookup(int(packageID))
                package.updateStatus(time)
                print(str(package))
            except ValueError:
                print("Invalid input. Please enter a valid package ID from 1-40.")
        # Get status for all packages
        elif secondInput == "all":
            for packageID in range(1, 41):
                package = packageData.lookup(packageID)
                package.updateStatus(time)
                print(str(package))
        else:
            print("Invalid input. Please enter either 'single' or 'all'.")
    except ValueError:
        print("Invalid time format. Please enter the time in the format HH:MM.")


class Main:
    print("Welcome to WGUPS")
    totalMiles = truck1.miles + truck2.miles + truck3.miles
    print(f"The overall mileage for the route is: {totalMiles}")

    # Get package(s) status by asking user for the time
    userInputTime = input("Please enter a time to check the status of the package(s). Use the following format: HH:MM ")
    checkPackageStatus(userInputTime)
