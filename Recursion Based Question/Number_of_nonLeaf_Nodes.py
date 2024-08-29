class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None 

def count_number_of_nonLeaf_node(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    return 1 + count_number_of_nonLeaf_node(root.left) + count_number_of_nonLeaf_node(root.right)

tree = BinarySearchTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("Total number of non leaf node")
print(count_number_of_nonLeaf_node(tree.root))