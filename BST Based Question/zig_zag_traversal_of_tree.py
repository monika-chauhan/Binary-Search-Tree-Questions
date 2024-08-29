from collections import deque

class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 
    
class BinarySearchTree:
    def __init__(self):
        self.root = None 

def zigZagTraversal(root):
    result = []
    leftToRight = True
    if not root:
        return result 
    q = deque([root])
    while q:
        q_size = len(q)
        curr_level = deque()
        for i in range(q_size):
            curr_node = q.popleft()

            if leftToRight == True:
                curr_level.append(curr_node.data)
            else:
                curr_level.appendleft(curr_node.data)

            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)

        
        result.append(list(curr_level))
        leftToRight = False 

    return result 

tree = BinarySearchTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("Zig Zag traversal of Tree: ")
print(zigZagTraversal(tree.root))