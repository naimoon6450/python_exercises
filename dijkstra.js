let { Node, PriorityQueue } = require('./priorityQHeap');

class WeightedGraph {
  constructor() {
    // unidirected graph
    this.graph = {};
  }

  addVertex(name) {
    if (!this.graph[name]) {
      this.graph[name] = [];
    }
  }

  addEdge(v1, v2, weight) {
    // assuming they exist in the graph
    this.graph[v1].push({ node: v2, weight });
    this.graph[v2].push({ node: v1, weight });
  }
}

let wgraph = new WeightedGraph();
wgraph.addVertex('A');
wgraph.addVertex('B');
wgraph.addVertex('C');
wgraph.addVertex('D');
wgraph.addVertex('E');
wgraph.addVertex('F');

wgraph.addEdge('A', 'B', 4);
wgraph.addEdge('A', 'C', 2);
wgraph.addEdge('B', 'E', 3);
wgraph.addEdge('C', 'D', 2);
wgraph.addEdge('C', 'F', 4);
wgraph.addEdge('D', 'E', 3);
wgraph.addEdge('D', 'F', 1);
wgraph.addEdge('E', 'F', 1);

const dijkstra = (startVert, endVert) => {
  let path = [];
  let distanceDict = {};
  let prevDict = {};
  let priorQ = new PriorityQueue();

  // initialize the objects etc.
  for (let node in wgraph.graph) {
    if (node === startVert) {
      distanceDict[node] = 0;
      priorQ.enqueue(node, 0);
    } else {
      distanceDict[node] = Infinity;
      priorQ.enqueue(node, Infinity);
    }
    prevDict[node] = null;
  }
  let smallestVert;

  // loop through graph
  while (priorQ.values.length) {
    smallestVert = priorQ.dequeue().val;
    if (smallestVert === endVert) {
      // need to use the prevDict to build up the path to return
      while (prevDict[smallestVert]) {
        path.push(smallestVert);
        smallestVert = prevDict[smallestVert];
      }
    }
    // if there's a smallvert or if the dist is inf
    if (smallestVert || distanceDict[smallestVert] !== Infinity) {
      // calculate the distance for each node and update accordingly
      // not that neighbor will be the key of the object so for the array it's the indexes
      for (let neighbor in wgraph.graph[smallestVert]) {
        let neightborVert = wgraph.graph[smallestVert][neighbor]; // initially B node
        // current shortest way to get to anything is stored in distanceDict
        let candidateDistance =
          distanceDict[smallestVert] + neightborVert.weight;
        let neighborVertVal = neightborVert.node; // initially 'B' value
        // if new shortest way to get to neighbor node is < than the current shortest distance
        // console.log('out', neighborVertVal);
        // console.log('dictVal', distanceDict[neighborVertVal]);
        if (candidateDistance < distanceDict[neighborVertVal]) {
          // console.log('in', neighborVertVal);
          distanceDict[neighborVertVal] = candidateDistance;
          // how we got to the next neighbor
          prevDict[neighborVertVal] = smallestVert;
          priorQ.enqueue(neighborVertVal, candidateDistance);
        }
      }
    }
  }
  // while (priorQ.values.length) {
  //   smallest = priorQ.dequeue().val;
  //   if (smallest === endVert) {
  //     //WE ARE DONE
  //     //BUILD UP PATH TO RETURN AT END
  //     console.log(smallest);
  //     console.log(prevDict);
  //     while (prevDict[smallest]) {
  //       path.push(smallest);
  //       smallest = prevDict[smallest];
  //     }
  //     path.push(startVert);
  //     break;
  //   }
  //   if (smallest || distanceDict[smallest] !== Infinity) {
  //     for (let neighbor in wgraph.graph[smallest]) {
  //       //find neighboring node
  //       let nextNode = wgraph.graph[smallest][neighbor];
  //       //calculate new distance to neighboring node
  //       let candidate = distanceDict[smallest] + nextNode.weight;
  //       let nextNeighbor = nextNode.node;
  //       if (candidate < distanceDict[nextNeighbor]) {
  //         //updating new smallest distance to neighbor
  //         distanceDict[nextNeighbor] = candidate;
  //         //updating previous - How we got to neighbor
  //         prevDict[nextNeighbor] = smallest;
  //         //enqueue in priority queue with new priority
  //         priorQ.enqueue(nextNeighbor, candidate);
  //       }
  //     }
  //   }
  // }
  return path.reverse();
};

console.log(wgraph.graph);
console.log(dijkstra('A', 'E'));
