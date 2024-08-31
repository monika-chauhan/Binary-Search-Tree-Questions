from collections import deque

class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 
    
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None 

def minimum_depth_of_tree(root):
    minimum_depth = 0 
    q = deque([root])
    while q:
        minimum_depth += 1
        for i in range(len(q)):
            curr_node = q.popleft()

            if curr_node.left is None and curr_node.right is None:
                return minimum_depth
            
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
    return minimum_depth

#tree = BinarySearchTree()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Minimum depth Of Tree")
print(minimum_depth_of_tree(root))
