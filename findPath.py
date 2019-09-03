
def findPath(graph, start, end):
    tasks = graph[start] # initialize with the starting array
    visited = []
    # while there are still paths to go and the end hasn't been reached
    endBool = end not in visited
    # can't have visit bool up here bc the changes are happening inside loop
    while (len(tasks)):
        # this bool will say whether or not the children have already been visited
        visitBool = tasks[0] not in visited

        if (tasks[0] == end):
            # append the final node
            visited.append(tasks[0])
            return True

        # if the current task node already visited can pop it
        if (not visitBool):
            tasks.pop(0)
        
        if (tasks[0] != end and endBool):
            # append visited node
            visited.append(tasks[0])
            # concat the children
            tasks += graph[tasks[0]]
            # pop off the first item
            tasks.pop(0)
        
    return False

graph = {
    'a': ['b', 'c'],
    'b': ['c'],
    'c': ['d'],
    'd': ['b'],
    # 'e': []
}

# print(graph['a'] + graph['c'])
print(findPathDict(graph, 'a', 'd'))