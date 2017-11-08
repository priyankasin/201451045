# Implementation of find out the sum of all the nodes which are leaf nodes
 
# A Binary tree node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
# function to check if a given node is leaf or not
def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False
 

def leftLeavesSum(root):
    left_sum= 0 
    # Update result if root is not None
    if root is not None:
        # If left of root is None, then add key of left child
        if isLeaf(root.left):
            left_sum += root.left.key
        else:
            # Else iterate for left child of root
            left_sum += leftLeavesSum(root.left)
        # iterate for right child of root and update left_sum
        left_sum += leftLeavesSum(root.right)
    return left_sum
 
def rightLeavesSum(root):
    right_sum = 0 
    # Update result if root is not None
    if root is not None:
 
        # If right of root is None, then add key of right child
        if isLeaf(root.right):
            right_sum += root.right.key
        else:
            # otherwise iterate for right child of root
            right_sum += rightLeavesSum(root.right)
 
        # iterate for left child of root and update right_sum
        right_sum += rightLeavesSum(root.left)
    return right_sum

# constrcut the Binary Tree shown in the above function
root = Node(10)
root.left = Node(5)
root.right = Node(15)        
root.right.right = Node(8)
root.right.right.left = Node(5)
root.left.left = Node(10)
root.left.right = Node(12)
root.left.right.left = Node(6)
a=leftLeavesSum(root)+rightLeavesSum(root)
print("Sum of all the nodes which are leaf nodes is: ", a)
 