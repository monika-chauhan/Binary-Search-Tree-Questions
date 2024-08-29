from collections import deque

class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 
    
class BinarySearchTree:
    def __init__(self):
        self.root = None 
    

def BFS(root):
    result = []
    if not root:
        return result 
    q = deque([root])
    while q:
        level = []
        for i in range(len(q)):
            curr = q.popleft()
            level.append(curr.data)

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        result.append(level)
    return result 

tree = BinarySearchTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5) 
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("Breadth First Search: ")
print(BFS(tree.root))