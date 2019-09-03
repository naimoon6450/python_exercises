const findPathDict = (graph, start, end) => {
    let visited = {}
    let tasksQ = graph[start]

    while (tasksQ.length) {
        // either initiate or increment the current node
        if (visited[tasksQ[0]]) {
            visited[tasksQ[0]]++
        } else {
            visited[tasksQ[0]] = 0
        }
        if (tasksQ[0] === end) {
            visited[tasksQ[0]] = 1
            console.log(visited)
            return True
        }

        if (tasksQ[0] !== end && visited[tasksQ[0]] === 0) {
            visited[tasksQ[0]]++
            tasksQ = tasksQ.concat(graph[tasksQ[0]])
            console.log(tasksQ)
            tasksQ.shift()
        }
    }
    return false
}


graph = {
    'a': ['b', 'c'],
    'b': ['c'],
    'c': ['d'],
    'd': ['b'],
}

console.log(findPathDict(graph, 'a', 'd'))