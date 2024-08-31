from collections import deque

class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None 
    
def left_view_of_tree(root):
    left_view = []
    if not root:
        return left_view 
    q = deque([root])
    while q:
        q_size = len(q)
        for i in range(q_size):
            curr_node = q.popleft()
            if i == 0:
                left_view.append(curr_node.data)
            
            if curr_node.left:
                q.append(curr_node.left)
            
            if curr_node.right:
                q.append(curr_node.right)
    return left_view


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Left View of Tree: ")
print(left_view_of_tree(root))


