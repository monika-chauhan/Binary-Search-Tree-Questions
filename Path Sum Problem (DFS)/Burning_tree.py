# Output:
# 2
# 7 4 5
# 6 3
# 1 
# 0 8 

from collections import deque
class Node:
    def __init__(self,data):
        self.data = data 
        self.left = self.right = None 

class BurningTree:
    def __init__(self):
        self.root = None 
    
    q = deque()
    def Burning_tree(self,root, target):
        
        if root is None:
            return 0 
        if root.data == target:
            print(root.data)
            if root.left:
                self.q.append(root.left)
            if root.right:
                self.q.append(root.right)
            return 1 
        
        left = self.Burning_tree(root.left,target)
        if left == 1:
            qSize = len(self.q)
            for i in range(qSize):
                curr = self.q.popleft()
                print(curr.data, end = ' ')
                if curr.left:
                    self.q.append(curr.left)
                if curr.right:
                    self.q.append(curr.right)
            if root.right is not None:
                self.q.append(root.right)
            
            print(root.data)
            return 1 
        
        right = self.Burning_tree(root.right, target)
        if right == 1:
            qSize = len(self.q)
            for i in range(qSize):
                curr = self.q.popleft()
                print(curr.data, end = ' ')
                if curr.left:
                    self.q.append(curr.left)
                if curr.right:
                    self.q.append(curr.right)
            
            if root.left is not None:
                self.q.append(root.left)
            print(root.data)
            return 1

tree = BurningTree()
tree.root = Node(3)
tree.root.left = Node(5)
tree.root.right = Node(1)
tree.root.left.left = Node(6)
tree.root.left.right = Node(2)

tree.root.right.left = Node(0)
tree.root.right.right = Node(8)

tree.root.left.right.left = Node(7)
tree.root.left.right.right = Node(4)

print("Burning Tree Seqeuence:")
tree.Burning_tree(tree.root, 2)
while tree.q:
    qSize = len(tree.q)
    for i in range(qSize):
        curr = tree.q.popleft()
        print(curr.data, end = ' ')
        if curr.left:
            tree.q.append(curr.left)
        if curr.right:
            tree.q.append(curr.right)
    print()