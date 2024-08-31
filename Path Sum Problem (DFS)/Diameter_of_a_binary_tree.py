class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 



def findDiameter(root):
    diameter = [0]
    
    def findHeight(root):
        if root is None:
            return 0 
        
        leftHeight = findHeight(root.left)
        rightHeight = findHeight(root.right)

        curr_diameter = leftHeight + rightHeight + 1
        diameter[0] = max(diameter[0],curr_diameter)

        return 1 + max(leftHeight,rightHeight) 
    findHeight(root)
    return diameter[0]



root = Node(3)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(6)
root.right.left = Node(7)
root.right.right = Node(8)
root.right.right.left = Node(2)

print("Diameter of the Binary Tree: ")
print(findDiameter(root))