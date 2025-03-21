from itertools import permutations
from collections import Counter
from icecream import ic

# Function to calculate total distance of a path
def calculate_distance(path, distance_matrix):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance_matrix[path[i]][path[i + 1]]
    total_distance += distance_matrix[path[-1]][path[0]]  # Return to start
    return total_distance


# Function to solve TSP using brute force
def tsp_brute_force(distance_matrix):
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))  # Cities labeled as 0, 1, 2, ...
    
    all_permutations = list(permutations(cities[1:]))  # Generate all possible paths
    pathes = {}  # Store paths and their distances

    shortest_distance = float("inf")
    # best_path = None

    for perm in all_permutations:
        path = [0] + list(perm)  # Always start from city 0
        current_distance = calculate_distance(path, distance_matrix)

        # Store path and its distance
        pathes[tuple(path)] = current_distance

        # Update shortest path
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            best_path = path
    
    results = []
    
    for path,distance in pathes.items():
        if distance == shortest_distance:
            results.append(path)
    
    return results


# Example distance matrix (Graph)
distance_matrix = [
    [0, 10, 15, 20],  # Distances from City 0 to others
    [10, 0, 35, 25],  # Distances from City 1 to others
    [15, 35, 0, 30],  # Distances from City 2 to others
    [20, 25, 30, 0],  # Distances from City 3 to others
]

# Run TSP
best_routes = tsp_brute_force(distance_matrix)

# Display results

print(best_routes)