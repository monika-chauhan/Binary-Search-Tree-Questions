class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 
    
class BinarySearchTree:
    def __init__(self):
        self.root = None 

# [3,2,1]
#        3    [i= 0]
#     /     \
#    5       2  [i = 1]
#   /\      / \
#  6  7    9   1  [i = 2]

def Path_with_given_subsequence(root,seq,index):
    if root is None:
        return False 
    if index >= len(seq) and root.data != seq[index]:
        return False 
    
    if root.data == seq[index] and root.left is None and root.right is None:
        return True 
    
    return Path_with_given_subsequence(root.left,seq,index+1) or Path_with_given_subsequence(root.right,seq,index+1)

root = Node(3)
root.left = Node(5)
root.right = Node(2)
root.left.left = Node(6)
root.left.right = Node(7)
root.right.left = Node(9)
root.right.right = Node(1)

print("Path with Given sequence is Exists: ")
seq = [3,2,4]
print(Path_with_given_subsequence(root,seq,0))

    