#                              ---------------------  
#                              |left | root | right|
#                              ---------------------
#                              ---------------------  
#                              |     |   1   |      |
#                              ---------------------  
#                           /                           \
#                          /                             \
#               -------------                           --------------
#               |   | 2 |   |                           |   | 3 |    |
#               -------------                           --------------
#                  /     \                               /        \
#                 /       \                             /          \
#        -------------     --------------       ------------     -------------
#        |   | 4 |   |     |   | 5  |   |       |  | 6 |   |     |   | 7  |  |
#        -------------     --------------       ------------     -------------
#
#
# Nodes contains -> Three fields 
# 1. Data Field  (root)
# 2. Left Node (left child)
# 3. Right Node (right child)

class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 
    
class BinarySearchTree:
    def __init__(self):
        self.root = None 
    
def preOrder(root):
    if root is None:
        return 
    print(root.data, end = ' ')
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if not root:
        return 
    inOrder(root.left)
    print(root.data,end = ' ')
    inOrder(root.right)


def postOrder(root):
    if not root:
        return 
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end = ' ')

tree = BinarySearchTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5) 
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("Pre Order Traversal: ")
preOrder(tree.root)

print("\nInorder Traversal: ")
inOrder(tree.root)

print("\nPostOrder Traversal: ")
postOrder(tree.root)

