def floydWarshall(distances, keys):
    n = len(distances)

    # Setting initial values for the path array

    path = [[None for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                path[i][j] = 0
            else:
                path[i][j] = i

    # Floyd-Warshall algorithm

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if distances[j][k] > distances[j][i] + distances[i][k]:
                    path[j][k] = path[i][k]
                    print("New Path from " + keys[j] + " to " + keys[k] +
                          " value: " + str(distances[j][i] + distances[i][k]) +
                          " path: ",
                          end="")
                    currentPath = [keys[j]]
                    findPath(path, j, k, currentPath, keys)
                    currentPath.append(keys[k])
                    for l in range(len(currentPath)):
                        print(currentPath[l], end="")
                        if l != len(currentPath) - 1:
                            print(" -> ", end="")
                    print()
                    distances[j][k] = distances[j][i] + distances[i][k]
    print()


# Recursive function for saving the path from start to destination


def findPath(path, start, destination, currentPath, keys):
    if path[start][destination] == start:
        return
    findPath(path, start, path[start][destination], currentPath, keys)
    currentPath.append(keys[path[start][destination]])


def printMatrix(matrix, keys):
    for i in range(len(matrix)):
        print("\t" + keys[i], end="")
    print()
    for i in range(len(matrix)):
        print(keys[i], end="\t")
        for j in range(len(matrix)):
            print(matrix[i][j], end="\t")
        print()


def inputData():

    adjencyList = {
        'A': set([('B', 10), ('D', 2)]),
        'B': set([('E', 9)]),
        'C': set([('A', 5), ('D', 2)]),
        'D': set([('C', 1), ('E', 9)]),
        'E': set([('A', 13), ('B', 4), ('C', 7)]),
    }

    distances = [[float('inf') for x in range(len(adjencyList))]
                 for y in range(len(adjencyList))]
    for i in range(len(adjencyList)):
        distances[i][i] = 0

    keys = []
    for key, val in adjencyList.items():
        keys.append(key)

    i = 0
    for key, val in adjencyList.items():
        for to, weight in val:
            for j in range(len(distances)):
                if keys[j] == to:
                    distances[i][j] = weight
        i += 1
    print("Paths:")
    floydWarshall(distances, keys)
    print("Distance matrix:")
    printMatrix(distances, keys)


inputData()