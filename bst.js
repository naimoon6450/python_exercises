class Node {
  constructor(val) {
    this.val = val;
    this.right = null;
    this.left = null;
  }
}

class BinarySearchTree {
  constructor(root = null) {
    this.root = root;
  }

  find(rootNode, val) {
    if (rootNode.val === val) {
      return true;
    }
    if (!this.root) {
      return false;
    } else {
      if (rootNode.val > val && rootNode.left) {
        return this.find(rootNode.left, val);
      } else if (rootNode.val < val && rootNode.right) {
        return this.find(rootNode.right, val);
      } else {
        return false;
      }
    }
  }

  insert(val) {
    let node = new Node(val);
    if (!this.root) {
      this.root = node;
    } else {
      this.insertNode(this.root, node);
    }
  }

  insertNode(node, newNode) {
    if (node.val > newNode.val) {
      if (!node.left) {
        node.left = newNode;
      } else {
        this.insertNode(node.left, newNode);
      }
    } else {
      if (!node.right) {
        node.right = newNode;
      } else {
        this.insertNode(node.right, newNode);
      }
    }
  }
}

let bst = new BinarySearchTree();
bst.insert(10);
bst.insert(20);
bst.insert(8);
bst.insert(9);
bst.insert(25);
bst.insert(4);
bst.insert(18);

const BFS = root => {
  let visited = [];
  let q = [root];

  // key is to understand that you can traverse what gets added into the QUEUE vs thinking recursively

  while (q.length > 0) {
    // ref to the curr top elem in q
    let deqNode = q.shift();
    // push deqNode into visited
    visited.push(deqNode.val);
    // check if deqNode has right or left children
    if (deqNode.left || deqNode.right) {
      q.push(deqNode.left);
      q.push(deqNode.right);
    }
  }

  return visited;
};

// console.log(BFS(bst.root));

const DFS = root => {
  let visited = [];

  if (!root) {
    return;
  } else {
    if (root.left) {
      visited = visited.concat(DFS(root.left));
    }
    visited.push(root.val);
    if (root.right) {
      visited = visited.concat(DFS(root.right));
    }
  }
  return visited;
};

console.log(DFS(bst.root));
