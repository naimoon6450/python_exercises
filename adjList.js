class Graph {
  constructor() {
    // unidirected graph
    this.graph = {};
  }

  addVertex(name) {
    if (!this.graph[name]) {
      this.graph[name] = [];
    }
  }

  addEdge(v1, v2) {
    // assuming they exist in the graph
    this.graph[v1].push(v2);
    this.graph[v2].push(v1);
  }

  removeEdge(v1, v2) {
    this.graph[v1] = this.graph[v1].filter(elem => {
      if (elem !== v2) {
        return elem;
      }
    });
    this.graph[v2] = this.graph[v2].filter(elem => {
      if (elem !== v1) {
        return elem;
      }
    });
  }

  removeVertex(vert) {
    this.graph[vert].forEach(edge => {
      this.removeEdge(vert, edge);
    });

    delete this.graph[vert];
  }
}

let graph = new Graph();
graph.addVertex('New York');
graph.addVertex('Hong Kong');
graph.addVertex('China');
graph.addVertex('Bangladesh');
graph.addEdge('New York', 'Hong Kong');
graph.addEdge('China', 'Hong Kong');
graph.addEdge('Bangladesh', 'Hong Kong');

// console.log(graph);

const DFSRec = vertex => {
  let vertSeen = {};
  let visited = [];

  const dfs = vertex => {
    if (!vertex) {
      return;
    }
    vertSeen[vertex] = true;
    visited.push(vertex);
    // if there are children and the vertex hasn't been visited
    graph.graph[vertex].forEach(vertChild => {
      if (!vertSeen[vertChild]) {
        return helper(vertChild);
      }
    });
  };
  dfs(vertex);
  return visited;
};

// console.log(DFSRec('New York'));

const BFS = vertex => {
  let vertSeen = {};
  let visited = [];
  let queue = [vertex];

  while (queue.length) {
    let deqNode = queue.shift();
    if (!vertSeen[deqNode]) {
      vertSeen[deqNode] = true;
      visited.push(deqNode);
      // if there are children and the vertex hasn't been visited
      graph.graph[deqNode].forEach(vertChild => {
        queue.push(vertChild);
      });
    }
  }

  return visited;
};
console.log(graph.graph);
console.log(BFS('New York'));
