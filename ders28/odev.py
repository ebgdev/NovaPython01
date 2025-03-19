# gorev1: en kisa yollari gosteren bir fonksiyon gelistiriniz :

# ------------------------------------

# Path: [0, 1, 2, 3]
# total_distance = 0 + distance_matrix[path[0]][path[1]] = 0 + 10 → 10
# total_distance = 10 + distance_matrix[path[1]][path[2]] = 10 + 35 → 45
# total_distance = 45 + distance_matrix[path[2]][path[3]] = 45 + 30 → 75
# total_distance = 75 + distance_matrix[path[-1]][path[0]] = 75 + 20 → 95 (Returning to start)
# Total Distance for [0, 1, 2, 3]: 95
# ----------------------------------------

# Path: [0, 1, 3, 2]
# total_distance = 0 + distance_matrix[path[0]][path[1]] = 0 + 10 → 10
# total_distance = 10 + distance_matrix[path[1]][path[2]] = 10 + 25 → 35
# total_distance = 35 + distance_matrix[path[2]][path[3]] = 35 + 30 → 65
# total_distance = 65 + distance_matrix[path[-1]][path[0]] = 65 + 15 → 80 (Returning to start)
# Total Distance for [0, 1, 3, 2]: 80
# ----------------------------------------

# Path: [0, 2, 1, 3]
# total_distance = 0 + distance_matrix[path[0]][path[1]] = 0 + 15 → 15
# total_distance = 15 + distance_matrix[path[1]][path[2]] = 15 + 35 → 50
# total_distance = 50 + distance_matrix[path[2]][path[3]] = 50 + 25 → 75
# total_distance = 75 + distance_matrix[path[-1]][path[0]] = 75 + 20 → 95 (Returning to start)
# Total Distance for [0, 2, 1, 3]: 95
# ----------------------------------------

# Path: [0, 2, 3, 1]
# total_distance = 0 + distance_matrix[path[0]][path[1]] = 0 + 15 → 15
# total_distance = 15 + distance_matrix[path[1]][path[2]] = 15 + 30 → 45
# total_distance = 45 + distance_matrix[path[2]][path[3]] = 45 + 25 → 70
# total_distance = 70 + distance_matrix[path[-1]][path[0]] = 70 + 10 → 80 (Returning to start)
# Total Distance for [0, 2, 3, 1]: 80
# ----------------------------------------

# Path: [0, 3, 1, 2]
# total_distance = 0 + distance_matrix[path[0]][path[1]] = 0 + 20 → 20
# total_distance = 20 + distance_matrix[path[1]][path[2]] = 20 + 25 → 45
# total_distance = 45 + distance_matrix[path[2]][path[3]] = 45 + 35 → 80
# total_distance = 80 + distance_matrix[path[-1]][path[0]] = 80 + 15 → 95 (Returning to start)
# Total Distance for [0, 3, 1, 2]: 95
# ----------------------------------------

# Path: [0, 3, 2, 1]
# total_distance = 0 + distance_matrix[path[0]][path[1]] = 0 + 20 → 20
# total_distance = 20 + distance_matrix[path[1]][path[2]] = 20 + 30 → 50
# total_distance = 50 + distance_matrix[path[2]][path[3]] = 50 + 35 → 85
# total_distance = 85 + distance_matrix[path[-1]][path[0]] = 85 + 10 → 95 (Returning to start)
# Total Distance for [0, 3, 2, 1]: 95
# ----------------------------------------


# gorev2:
# linked list sinifina search fonksiyonu eklenecek


def search(self, item):
    pass
