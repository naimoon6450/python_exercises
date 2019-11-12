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
console.log(bst.find(bst.root, 200));
// console.log(bst);
