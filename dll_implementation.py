class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


    def insert(self, val):
        # if there's nothing in the list
        if self.length == 0:
            self.head = Node(val)
            self.tail = self.head
            self.length += 1
        # otherwise adds to end
        else:
            newNode = Node(val)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1
        
        return self
    
    def pop(self):
        # check for head
        if self.length == 0:
            return None
        
        deleteNode = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        # remove linkages of list from deletedNode
        deleteNode.prev = None
        self.length -= 1
        return deleteNode

node1 = Node(5)
node2 = Node(6)
node3 = Node(10)

dll = DoublyLinkedList()
dll.insert(node1)
dll.insert(node2)
dll.insert(node3)
# print(dll.pop().val)
print(dll.head.next)





