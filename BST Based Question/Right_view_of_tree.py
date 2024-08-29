from collections import deque

class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None 

def Right_view_of_tree(root):
    right_view = []
    if not root:
        return right_view
    
    q = deque([root])
    while q:
        q_size = len(q)
        
        for i in range(len(q)):
            curr_node = q.popleft() 
            if i == q_size-1:
                right_view.append(curr_node.data)

            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
       
    return right_view 


tree = BinarySearchTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("Right View of the Tree")
print(Right_view_of_tree(tree.root))

