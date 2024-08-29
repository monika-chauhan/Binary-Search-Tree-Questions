class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None 

def Number_of_full_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0 
    
    return  Number_of_full_nodes(root.left) + Number_of_full_nodes(root.right) + (1  if root.left != None and root.right != None else 0)
    
tree = BinarySearchTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
#tree.root.right.right = Node(7)

print("Total Number of Full Nodes: ")
print(Number_of_full_nodes(tree.root))
