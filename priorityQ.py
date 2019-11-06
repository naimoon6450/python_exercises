"""
Internals
function Node (data, priority) {
  this.data = data;
  this.priority = priority;
  this.next = null;
}

function PriorityQueue () {
  this.first = null;
}
API
PriorityQueue.prototype.insert = function (data, priority) {
  const newItem = new Node(data, priority);
  if (!this.first || this.first.priority < priority) {
    // First case: Check if the PQ is empty, or newItem's priority > this.first's
    newItem.next = this.first;
    this.first = newItem; // New Node (newItem) becomes new first
  } else {
    // Second case: Find where to insert newItem
    let currentNode = this.first;
    while (currentNode.next && currentNode.next.priority >= priority) {
      // Traverse queue until it finds a node with priority < search priority
      currentNode = currentNode.next;
    }
    // Here, currentNode is right before where you want to insert newItem. Point
    // newItem.next to currentNode.next, then point currentNode's next to newItem.
    newItem.next = currentNode.next;
    currentNode.next = newItem;
  }
}

PriorityQueue.prototype.peek = function () {
  return this.first.data;
}

PriorityQueue.prototype.popMax = function () {
  const maxVal = this.first;
  this.first = this.first.next;
  return maxVal.data;
}
"""


# Min Priority Queue, can easily flip to get Max PQ
"""
[1,2,3,4,  ]
         pp
"""

# Unsorted array implementation
class PriorityQ_UA:
    def __init__(self, size):
      self.q = [0] * size
      self.placement_pointer = 0
      self.max = 0

    def insert(self, item):
      # increment after the addition of the item
      self.q[self.placement_pointer] = item
      self.placement_pointer += 1
      # keep track of the max
      if self.q[self.max] < item:
        self.max = self.placement_pointer - 1


    
    def isEmpty(self):
      return self.placement_pointer == 0
    
    def size(self):
      return self.placement_pointer

    def delMax(self):
      index_of_max = 0
      # loop through entire list to find max
      for i in range(1, self.placement_pointer):
        if (self.q[index_of_max] < self.q[i]):
          index_of_max = i
      
      # exchange max and last 
      lastElem = self.q[self.placement_pointer - 1]
      # set last element to the max element
      self.q[self.placement_pointer - 1] = self.q[index_of_max]
      # set original spot of max to the last elem
      self.q[index_of_max] = lastElem
      # decrement placement pointer
      self.placement_pointer -= 1

      # if we care for O (1) findMax, then we can include some logic to restore self.max to be the new max in O(N) time, as delMax operation will already be O(N)
      return self.q[self.placement_pointer]


# Sorted array implementation
# [1, 3,    4, 6,  8, 10  ]
#           i
# insert 6
class PriorityQ_SA:
    def __init__(self, size):
      self.q = [0] * size
      self.placement_pointer = 0

    def insert(self, item):
      # increment after the addition of the item
      if self.placement_pointer == 0:
        self.q[self.placement_pointer] = item
        self.placement_pointer += 1
      else:
        # traverse backwards move everything up while elems are > than item
        i = self.placement_pointer - 1
        while (i >= 0 and self.q[i] > item):
          self.q[i + 1] = self.q[i]
          i -= 1
        # once you're out, i + 1 should be a duplicate
        self.q[i + 1] = item
        self.placement_pointer += 1

    
    def isEmpty(self):
      return self.placement_pointer == 0
    
    def size(self):
      return self.placement_pointer

    def delMax(self):
      # max is always at the end since it's sorted
      self.placement_pointer -= 1
      return self.q[self.placement_pointer]


# pq_sorted = PriorityQ_SA(10)
# pq_sorted.insert(10)
# pq_sorted.insert(11)
# pq_sorted.insert(12)
# print(pq_sorted.q)

# Linked List implementation
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class PriorityQ_LL:
  

