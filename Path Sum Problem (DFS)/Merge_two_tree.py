class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 

def traversal(root):
    if root:
        print(root.data , end = ' ')
        traversal(root.left)
        traversal(root.right)

def merge_two_tree(root1,root2):
    if root1 is None:
        return root2 
    if root2 is None:
        return root2
    
    root1.data += root2.data 

    root1.left = merge_two_tree(root1.left,root2.left)
    root1.right = merge_two_tree(root1.right,root2.right)
    
    return root1

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.right.left = Node(4)
root1.right.right = Node(5)

root2 = Node(2)
root2.left = Node(4)
root2.right = Node(5)
root2.left.left = Node(3)
root2.left.right = Node(1)
root2.right.left = Node(6)

print("Merge the Tree: ")
root = merge_two_tree(root1,root2)
traversal(root)
