# WGUPS 

## Overview
The WGUPS  Program is a Python-based solution designed to address the routing and delivery challenges faced by WGUPS. The primary goal of the project is to determine efficient routes and distribution for daily local deliveries (DLD), ensuring on-time delivery of 40 packages with specific criteria and constraints.

## Algorithm
The project employs a nearest neighbor algorithm to optimize the delivery routes. The algorithm prioritizes selecting the nearest neighbor (package) at each step, minimizing the overall travel distance and ensuring timely deliveries. This heuristic approach is effective for solving vehicle routing problems, especially when finding an optimal solution is computationally expensive.

## Features
1. Efficient Routing Algorithm:
- Implemented a routing algorithm using the nearest neighbor heuristic.
- Ensured on-time delivery of all 40 packages while limiting the combined total distance traveled by two trucks to under 140 miles.

2. Object-Oriented Design:
- Developed a modular and maintainable solution using object-oriented design principles.
- Created classes such as Package, PackageHashTable, and Truck to encapsulate data and functionality, promoting code reusability.

3. User-Friendly Package Tracking System:
- Integrated a user-friendly package tracking system to monitor the progress of each truck and its packages.
- Provided the supervisor with visibility into the status of packages at assigned points, enhancing overall logistics management.

## Assumptions and Constraints
The project carefully considered and managed various assumptions and constraints, including:

- Maximum package capacity per truck.
- Driver-truck assignments and departure/loading times.
- Instantaneous delivery and loading times.
- Special case handling for package #9 address correction at 10:20 a.m.

## Usage
1. CSV Data Loading:
- Ensure CSV files (address.csv, distance.csv, package.csv) are available in the designated csv directory.
- Run the program to load package data and initialize the routing system.

2. Algorithm Execution:
- The program employs a nearest neighbor algorithm to optimize package delivery.
- Trucks are assigned packages based on the algorithm, ensuring efficient and on-time deliveries.

3. Package Tracking:
- Users can check the status of packages at specific times using the provided interface.
- Enter a time in the format HH:MM to view the status of individual or all packages.

## Author
- Email - [Jason Zeng](mailto:officialjasonzeng@gmail.com?subject=[GitHub]%20iFitness%20App)
- Website - [Jason Zeng](https://mister-zeng.github.io/Portfolio-Website/)
- Twitter - [Misterzeng](https://www.twitter.com/misterzeng)