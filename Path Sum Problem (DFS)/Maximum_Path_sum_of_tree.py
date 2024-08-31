class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None 

def find_Max_Path_sum_of_tree(root):
    maxSum = [0]
    def findMaxSum(root):
        if root is None:
            return 0 

        leftSum = findMaxSum(root.left)
        rightSum = findMaxSum(root.right)
         
        leftSum = max(leftSum, 0)
        rightSum = max(rightSum, 0) 
        currSum = leftSum + rightSum + root.data 
       
        maxSum[0] = max(maxSum[0], currSum)

        return max(leftSum,rightSum) + root.data
    findMaxSum(root)
    return maxSum[0]

root = Node(10)
root.left = Node(5)
root.right = Node(6)

root.left.left = Node(-6)
root.left.right = Node(-9)

root.right.left = Node(-7)
root.right.left.left = Node(3)
root.right.left.right = Node(4)

print("Maximum Sum Path of binary Tree: ")
print(find_Max_Path_sum_of_tree(root))