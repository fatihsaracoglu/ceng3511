import re, sys


def BFS(graphDict, initialState, goalState):
    expandedVertices = []
    queue = [[initialState]]
    if (initialState == goalState):
        return [initialState]
    while queue:
        path = queue.pop(0)
        vertex = path[-1]
        if vertex not in expandedVertices:
            adjacencies = graphDict[vertex]
            for adjacent in adjacencies:
                otherPath = list(path)
                otherPath.append(adjacent)
                queue.append(otherPath)
                if (adjacent == goalState):
                    return otherPath
            expandedVertices.append(vertex)
    print("There is no path b/w these two vertices!")


def DFS(graphDict, initialState, goalState):
    stack = [(initialState, [initialState])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if (vertex == goalState):
                return path
            visited.add(vertex)
            for neighbor in sorted(graphDict[vertex], reverse=True):
                stack.append((neighbor[0], path + [neighbor[0]]))
    print("There is no path b/w these two vertices!")


def UCS(graphDict, initialState, goalState, expandedVertices=[], distances={}, predecessors={}):
    if (initialState == goalState):
        path = []
        pred = goalState
        while pred != None:
            path.append(pred)
            pred = predecessors.get(pred, None)
        result = path[0]
        for index in range(1, len(path)):
            result = path[index] + ' - ' + result
        print(result)
    else:
        if not expandedVertices:
            distances[initialState] = 0
        for adjacent in graphDict[initialState]:
            if adjacent not in expandedVertices:
                new_distance = distances[initialState] + graphDict[initialState][adjacent]
                if new_distance < distances.get(adjacent, float('inf')):
                    distances[adjacent] = new_distance
                    predecessors[adjacent] = initialState
        expandedVertices.append(initialState)

        unexpandedVertices = {}
        for k in graphDict:
            if k not in expandedVertices:
                unexpandedVertices[k] = distances.get(k, float('inf'))
        x = min(unexpandedVertices, key=unexpandedVertices.get)
        UCS(graphDict, x, goalState, expandedVertices, distances, predecessors)


def printResult(l):
    result = ""
    for i in range(len(l)):
        result += l[i]
        if (i != len(l) - 1):
            result += " - "
    print(result)


if __name__ == "__main__":

    adjacencyDictionaryForUCS = {}
    adjacencyDictionaryForBFSAndDFS = {}

    try:
        file_name = str(sys.argv[1])

        with open(file_name) as f:
            content = f.readlines()
        content = [x.strip() for x in content]

        for line in content:
            label = line[0]
            onlyLetters = re.sub('[^A-Z-z]+', '', line[3:])
            onlyDigits = re.sub('[^0-9]+', '', line[3:])
            weightDictionary = {}
            adjacencyList = []
            for x, y in zip(onlyLetters, onlyDigits):
                if (int(y) == 0):
                    continue
                weightDictionary.update({x: int(y)})
                adjacencyList.append(x)
            adjacencyDictionaryForUCS.update({label: weightDictionary})
            adjacencyDictionaryForBFSAndDFS.update({label: adjacencyList})
    except:
        print("An unexpected error occurred while reading and parsing the file!")

    initialState = input("Please enter the start state : ")
    goalState = input("Please enter the goal state  : ")


    try:
        print("BFS : ", end='')
        printResult(BFS(adjacencyDictionaryForBFSAndDFS, initialState, goalState))
        print("DFS : ", end='')
        printResult(DFS(adjacencyDictionaryForBFSAndDFS, initialState, goalState))
        print("UCS : ", end='')
        UCS(adjacencyDictionaryForUCS, initialState, goalState)
    except:
        print("An unexpected error occurred while printing the result!")
