""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

INT_MAX = 1000000
INT_MIN = -1000000

def checkBST(root):
    
    return (checkThatNode(root, INT_MIN, INT_MAX))

    
def checkThatNode(node, min, max):
     
    if node is None:
        return True
 
    if node.data < min or node.data > max:
        return False
 
    return (checkThatNode(node.left, min, node.data -1) and checkThatNode(node.right, node.data + 1, max))
