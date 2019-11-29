class BinaryHeap {
  constructor() {
    this.values = [];
  }

  insert(val) {
    this.values.push(val);
    this.bubbleUp();
  }

  bubbleUp() {
    let currInd = this.values.length - 1;
    let parentInd = Math.floor((currInd - 1) / 2);
    while (this.values[currInd] > this.values[parentInd]) {
      // swap
      let temp = this.values[currInd];
      this.values[currInd] = this.values[parentInd];
      this.values[parentInd] = temp;
      // move currInd to parent and find new parent
      currInd = parentInd;
      parentInd = Math.floor((currInd - 1) / 2);
    }
  }

  extractMax() {
    // replace max with last val and remove last val
    let temp = this.values[0];
    // swap
    this.values[0] = this.values[this.values.length - 1];
    this.values[this.values.length - 1] = temp;
    // pop
    let max = this.values.pop();
    this.bubbleDown();
    return max;
  }

  bubbleDown() {
    let valToBubb = 0,
      heapLen = this.values.length,
      valueToBubb = this.values[valToBubb],
      leftIdx = 2 * valToBubb + 1,
      rightIdx = 2 * valToBubb + 2,
      leftChild = this.values[leftIdx],
      rightChild = this.values[rightIdx];
    // keep looping if valueToBubb is less than children
    // or if the indexes are inbound
    while (
      (valueToBubb < leftChild || valueToBubb < rightChild) &&
      (this.values[leftIdx] || this.values[rightIdx])
    ) {
      // if left child is greater or if there's only a left child
      if (leftChild > rightChild || this.values[leftIdx]) {
        // swap with left child
        let left = 2 * valToBubb + 1;
        let temp = this.values[left];
        this.values[left] = this.values[valToBubb];
        this.values[valToBubb] = temp;
        valToBubb = left;
      } else if (rightChild > leftChild) {
        // swap with right child
        let right = 2 * valToBubb + 2;
        let temp = this.values[right];
        this.values[right] = this.values[valToBubb];
        this.values[valToBubb] = temp;
        valToBubb = right;
      } else {
        break;
      }
      leftIdx = 2 * valToBubb + 1;
      rightIdx = 2 * valToBubb + 2;
    }
  }
}

let bh = new BinaryHeap();
bh.insert(10);
bh.insert(12);
bh.insert(2);
bh.insert(100);
bh.extractMax();
bh.extractMax();
bh.extractMax();

module.exports = BinaryHeap;
