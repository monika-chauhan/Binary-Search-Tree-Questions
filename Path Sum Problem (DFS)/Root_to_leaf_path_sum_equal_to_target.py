class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 
    
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None 
    

def Path_sum_root_to_left_equal_target(root,target):
    if root is None:
        return False 
    if root.data == target and not root.left and not root.right:
        return True 
    return Path_sum_root_to_left_equal_target(root.left,target - root.data) or Path_sum_root_to_left_equal_target(root.right,target-root.data)

#tree = BinarySearchTree()
root = Node(12)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.left.right = Node(5)
root.right.left = Node(10)
root.right.right = Node(5)
root.left.left.left = Node(3)

print("Path Sum is equal to target: ")
target = 23
print(Path_sum_root_to_left_equal_target(root,target))
