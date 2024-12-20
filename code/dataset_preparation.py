import math

def create_distnce_matrix(input_path: str):
    # TODO: read data from file and create distance matrix
    coords = []
    with open("tsp.txt", "r") as f:
        for line in f:
            # each line: "x, y"
            line = line.strip()
            if not line:
                continue
            x_str, y_str = line.split(",")
            x = float(x_str)
            y = float(y_str)
            coords.append((x, y))

    n = len(coords)
    distance_matrix = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dx = coords[i][0] - coords[j][0]
                dy = coords[i][1] - coords[j][1]
                distance_matrix[i][j] = math.sqrt(dx*dx + dy*dy)
            else:
                distance_matrix[i][j] = 0.0

    return distance_matrix
