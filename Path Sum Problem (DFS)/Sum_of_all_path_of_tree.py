class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None 

def findPathSum(root,pathSum):
    if root is None:
        return 0 
    
    pathSum = 10 * pathSum + root.data 

    if root.left is None and root.right is None:
        return pathSum

    return findPathSum(root.left,pathSum) + findPathSum(root.right,pathSum)


root = Node(3)
root.left = Node(7)
root.right = Node(1)
root.left.left = Node(9)
root.right.left = Node(4)
root.right.right = Node(5)

print("All Path sum of tree: ")
print(findPathSum(root,0))