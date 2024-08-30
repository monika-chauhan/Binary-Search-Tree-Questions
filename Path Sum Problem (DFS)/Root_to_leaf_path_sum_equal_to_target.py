class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 
    
class BinarySearchTree:
    def __init__(self):
        self.root = None 
    

def Path_sum_root_to_left_equal_target(root,target):
    if root is None:
        return False 
    if root.data == target and not root.left and not root.right:
        return True 
    return Path_sum_root_to_left_equal_target(root.left,target - root.data) or Path_sum_root_to_left_equal_target(root.right,target-root.data)

tree = BinarySearchTree()
tree.root = Node(12)
tree.root.left = Node(7)
tree.root.right = Node(1)
tree.root.left.left = Node(9)
tree.root.left.right = Node(5)
tree.root.right.left = Node(10)
tree.root.right.right = Node(5)
tree.root.left.left.left = Node(3)

print("Path Sum is equal to target: ")
target = 12
print(Path_sum_root_to_left_equal_target(tree.root,target))
