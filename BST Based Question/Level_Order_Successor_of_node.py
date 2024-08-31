#The Level Order successor is the node that appers right after the given node in the level order traversal in the level order traversal.

from collections import deque
class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None 

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
 

#tree = BinarySearchTree()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Level Order successor Of Node")
print(Level_order_successor(root,4))

    
