
# create the node
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    
    def __repr__(self):
        return "Node: %s" % self.value
    # def __str__(self):
    #     return str(self.__class__) + ": " + str(self.__dict__)

class BST:
    def __init__(self, root):
        self.root = root
        self.size = 1

    def __str__(self):
        return "BST " + str(self.__dict__)

    def insert(self, node):
        if(node is None):
            return 'Insert a valid node'
        
        # if there's right children or left children then must check accordingly starting from root
        if(self.root.value < node.value):
            # now check for children
            if (self.root.right is None):
                self.root.right = BST(node)
            else:
                self.root.right.insert(node)
        else:
            if (self.root.left is None):
                self.root.left = BST(node)
            else:
                self.root.left.insert(node)
        
        self.size += 1
        return node



def maxDepthGivenNode(bstNode):
    depth = 0
    # if there's no left or right child then return 0 count
    if(bstNode is None or (bstNode.root.left is None and bstNode.root.right is None)):
        return depth

    # no traverse left or right to find depth
    depth += 1
    leftDepth = maxDepthGivenNode(bstNode.root.left)
    rightDepth = maxDepthGivenNode(bstNode.root.right)

    if(leftDepth > rightDepth):
        depth += leftDepth
    else:
        depth += rightDepth
    
    return depth
        
root = Node(5)
node2 = Node(4)
node3 = Node(2)
node4 = Node(1)
print(root)

newBST = BST(root)
newBST.insert(node2)
newBST.insert(node3)
newBST.insert(node4)

print(newBST)
# print(maxDepthGivenNode(newBST.root.left))
