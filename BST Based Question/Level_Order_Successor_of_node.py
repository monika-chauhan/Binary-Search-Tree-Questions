#The Level Order successor is the node that appers right after the given node in the level order traversal in the level order traversal.

from collections import deque
class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None 

def Level_order_successor(root,node):
    result = []
    if not root:
        return result 
    q = deque([root])
    while q:
        curr_node = q.popleft()
           
        if curr_node.data == node: # If matches then Break
            break
                
        if curr_node.left:
            q.append(curr_node.left)
        if curr_node.right:
            q.append(curr_node.right)

    ans = q.popleft() # Store the successor by poping the next value from queue
    return ans.data # Return the data 
 

tree = BinarySearchTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("Level Order successor Of Node")
print(Level_order_successor(tree.root,4))

    
