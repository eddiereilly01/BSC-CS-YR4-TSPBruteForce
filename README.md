# TSPBruteForce Written in Python
I wrote this to improve my understanding of the travelling salesperson problem in preparation for future projects, and also to enhance my skills with python.

The calculate_distance function:
This function calculates the distance between two positions using the math.dist() function. Using the Euclidean distance to calculate the distance between two points.

The permute function:
This function generates all possible permutations of the given string using a recursive approach, the permutations are stored in the possible_permutations list, this can be memory-intensive for long strings. And as such the algorithm takes a very long time to complete with larger problems.

The main function:
This function is where most of the TSP logic is implemented. It first generates all possible permutations of the city codes using the permute() function, then calculates the total distance for each permutation by iterating through each city in the permutation and finding the distance between it and the next city using the calculate_distance() function. The minimum distance is found and the optimal path is plotted using matplotlib.

The performance of the code:
The code is solving the problem using the brute force algorithm which is simple to implement but can be very slow for large number of cities, it will have an exponential time complexity and will not be efficient for large number of cities.
