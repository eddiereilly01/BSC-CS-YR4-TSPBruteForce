

import math
import matplotlib.pyplot as plt
possible_permutations = []
startPos = [(0,0)]
positions = [(1,3), (3,7), (9,6), (12,13), (15,18)]

def calculate_distance(pos1, pos2):
    """
       Calculate the distance between two points using Euclidean distance
       :param pos1: a tuple of x and y coordinates (x1, y1)
       :param pos2: a tuple of x and y coordinates (x2, y2)
       :return: distance as float
    """
    dist = math.dist(pos1, pos2)
    print("Distance between " + str(pos1) + " and " + str(pos2) + " is " + str(dist))
    return str(math.dist(pos1, pos2))



def permute(string, start, end):
    """
       Generate all possible permutations of a string using a recursive approach
       :param string: a string to permute
       :param start: starting index
       :param end: ending index
    """
    current = 0;
    if start == end-1:
        possible_permutations.append(string)
    else:
        for current in range(start, end):
            x = list(string);
            temp = x[start]
            x[start] = x[current];
            x[current] = temp;
            permute("".join(x), start + 1, end);

def main():

    city_codes = "12345"
    n = len(city_codes);
    permute(city_codes, 0, n); #generate all permutations

    print("All the permutations of the string are: ");
    print(possible_permutations)
    print("--------------------------------")

    total_distances = [] # list to store total distance of each permutation

    for permutation in possible_permutations:

        print("-----------------------------")
        print("NEW PERMUTATION")
        print("-----------------------------")

        current_permutation = permutation

        print("List: " + str(current_permutation))
        print("-----------------------------")

        first_pos = positions[int(current_permutation[0]) - 1]
        distances = [] # list to store distance of each city in the permutation
        distances.append(calculate_distance((0, 0), first_pos)) # calculate distance from start position to the first city

        for number in range(0, len(current_permutation)):
            print("Current Number: " + str(current_permutation[number]))
            index = int(current_permutation[number]) - 1
            print("Index: " + str(index) + ", Position: " + str(positions[index]))
            if (number < len(current_permutation) - 1):
                next_index = int(current_permutation[number + 1]) - 1
                print("Next Index: " + str(next_index) + " Next Position: " + str(positions[next_index]))
                distances.append(calculate_distance(positions[index], positions[next_index]))
            else:
                print("Next Number: Reached Final Number")
                distances.append(calculate_distance(positions[index], (0, 0)))
            print("=================")
        print("Distances: " + str(distances))
        total = 0
        for d in distances:
            total += float(d)
        print("Total Distance: " + str(total))
        total_distances.append(total)

    print(total_distances)

    min_distance = min(total_distances)
    min_index = total_distances.index(min_distance)
    min_permutation = possible_permutations[min_index]

    print("Minimum Distance: ", min_distance)
    print("Optimal Path: ", min_permutation)

    # Plotting the optimal path
    x = [startPos[0][0]] + [positions[int(i) - 1][0] for i in min_permutation] + [startPos[0][0]]
    y = [startPos[0][1]] + [positions[int(i) - 1][1] for i in min_permutation] + [startPos[0][1]]
    plt.plot(x, y, 'bo-')
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

