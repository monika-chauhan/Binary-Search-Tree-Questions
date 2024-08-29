Tree : A Data structure composed on Nodes.
                 2    ---- Level 1 (root Node)
            /    |    \       ------edges 
           3     4     9       ------ Level 2 
        /    \   /\     \       -- edges 
       5      6  7 8     10    ----- Level 3 (leaf Nodes)
    
Binary Tree : A tree which has upto two children. (either zero node, one node or two nodes) 
               1
            /     \
          2         3
        /   \         \   
      9      8          6

Complete Binary Tree : A Tree is a tree in which every level of the tree s fully filled, except for perhaps the last level. 
                        To extent that the last level is filled, It is filled from left to right.
Order of filling -> Left to Right
Tree 1: Complete Binary tree-> filled from left to right 
                1
            /     \
          2         3
        /   \      /   
      9      8    6    -> Last level Left to right filled 

Tree 2: Not complete Binary Tree
              1
            /     \
          2         3
        /   \         \   
      9      8          6 -> Last level not filled from left to right so it is not complete binary tree

Full Binary Tree : A Tree in which every node has either zero or two children.
Tree 1: Full Binary Tree 
               1
            /     \
          2         3
        /   \      /  \   
      9      8    5    6

Tree 2: Not fully 
               1
            /     \
          2         3
        /   \         \   
      9      8          6 (contains one node it should be zero or two)

Perfect Binary Tree: A Tree is one which is complete and full. All leaf nodes will be at the same level. 
                    and this level has the maximum number of nodes. 

Tree 1: 
               1
            /     \
          2         3
        /   \      /  \   
      9      8    5    6  (leaf node at same level)

Binary Search Tree: A Tree is a binary tree in which every node fits a specific ordering property. 
1 : all left descendents < n < all right descendents
2 : This must be tree for each node n. 
              10
            /     \
          5         15
        /   \      /  \   
       2     3    12    20
