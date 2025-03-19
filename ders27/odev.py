from itertools import permutations

# Example distance matrix (Graph)
distance_matrix = [
    [0, 10, 15, 20],  # Distances from City 0 to others
    [10, 0, 35, 25],  # Distances from City 1 to others
    [15, 35, 0, 30],  # Distances from City 2 to others
    [20, 25, 30, 0],  # Distances from City 3 to others
]

# our start point is city 0

# # Run TSP
# best_path, best_distance = tsp_brute_force(distance_matrix)

# # Display results
# print(f"🚀 Best Path: {best_path} with Distance: {best_distance}")


# output:
# 🚀 Best Path: [0, 1, 3, 2] with Distance: 80
