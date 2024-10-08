INF = 9999


def print_solution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == "INF":
                print("INF", end=" ")
            else:
                print(distance[i][j], end=" ")
        print(" ")
