# Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

# Implement these functions in your linked list class:

# get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
# addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# addAtTail(val) : Append a node of value val to the last element of the linked list.
# addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
# deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.

class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0
    
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        # if no head value
        if (self.head is None):
            return -1

        if (index > self.size or index < 0):
            return -1
        elif (index == 0):
            return self.head.value
        else:
            countInd = 0
            node = self.head
            # keep traversing until you hit index and not null
            while(node is not None and countInd != index):
                countInd += 1
                node = node.next
            
            return node.value
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        newHead = Node(val)
        self.size += 1
        # if no head exists
        if (self.head is None):
            self.head = newHead
            self.tail = newHead # stays on the first node created
        else:
            # hold head node
            temp = self.head
            # point old head prev val to new head
            temp.prev = newHead
            # point next of new head to old head
            newHead.next = temp
            # change head to new head
            self.head = newHead


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        newTail = Node(val)
        self.size += 1
        # if no node in list
        if (self.tail is None):
            self.head = newTail
            self.tail = newTail
        else:
            # store tail in temp
            temp = self.tail
            temp.next = newTail
            newTail.prev = temp
            self.tail = newTail
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        newNode = Node(val)
        # if index is = size, then add to tail
        if (self.size == index):
            self.addAtTail(val)
        elif (self.size == 0):
            self.addAtHead(val)
        elif (index > 0 and index < self.size):
            # add in the middle if size exists
            self.size += 1
            indCounter = 1
            traverseNode = self.head.next
            while (traverseNode is not None):
                # if index is hit then add the node
                if (indCounter == index):
                    temp = traverseNode
                    newNode.next = temp
                    newNode.prev = temp.prev
                    # point previous node to new node
                    temp.prev.next = newNode
                    # point prev of current node to new node
                    temp.prev = newNode
                    # still need to continue going to end so jump over newly created node
                    traverseNode = traverseNode.next
                
                indCounter += 1
                traverseNode = traverseNode.next



    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        # if index = tail
        if (index == self.size - 1):
            self.size -= 1 
            temp = self.tail
            self.tail = temp.prev
            temp.prev.next = None
            temp.prev = None
        elif (index == 0):
            self.size -= 1
            temp = self.head
            self.head = temp.next
            temp.next.prev = None
            temp.next = None
        elif (index > 0 and index < self.size):
            indCounter = 1
            traverseNode = self.head.next
            while (traverseNode is not None):
                # if index is hit then delete the node
                if (indCounter == index):
                    self.size -= 1
                    temp = traverseNode
                    # print(temp)
                    temp = traverseNode
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev

                    # change traverse node before nullified
                    traverseNode = traverseNode.next
                    temp.next = None
                    temp.prev = None
                
                indCounter += 1
                traverseNode = traverseNode.next
        



# ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
# [[],[1],[3],[1,2],[1],[1],[1]]
# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
obj.addAtHead(1)
# 1
obj.addAtTail(3)
# 1 -> 3
obj.addAtIndex(1, 2)
print(obj.head.next)
# 1 -> 2 -> 3
obj.get(1)
# 2
obj.deleteAtIndex(1)
# 1 -> 3
obj.get(1)
# 3
