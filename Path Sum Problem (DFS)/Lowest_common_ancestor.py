class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 

def lowest_common_ancestor(root, p, q):
    if root is None:
        return None 
    
    if root.data == p.data or root.data == q.data:
        return root.data 
    
    left = lowest_common_ancestor(root.left,p,q)
    right = lowest_common_ancestor(root.right,p,q)

    # If left have non null value and right also have non null value return root.data
    if left is not None and right is not None:
        return root.data 
    
    # If left is the node equal to either P or Q return return left. 
    #IF right is the node equal to either P and Q return right.
    return left if left is not None else right 
root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)

root.right.left = Node(0)
root.right.right = Node(8)

root.left.right.left = Node(7)
root.left.right.right = Node(4)

p = root.left 
q = root.right
print("Lowest common Ancestor: ")
print(lowest_common_ancestor(root,p,q))

