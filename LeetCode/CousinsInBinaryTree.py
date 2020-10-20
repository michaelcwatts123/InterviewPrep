# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

# Return true if and only if the nodes corresponding to the values x and y are cousins.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, par, node, val, level):
        if(node == None):
            return (0,None)
        if(val == node.val):
            return (level,par)
        level += 1
        level1, level2 = self.traverse(node,node.left, val, level), self.traverse(node,node.right, val, level)
        if(level1[0]>level2[0]):
            level = level1
        else:
            level = level2
        
        return level 
        
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        a,b = self.traverse(None, root, x,0), self.traverse(None, root,y,0)
        if(a[0]==b[0]):
            if(a[1].val != b[1].val):
                return True
            else:
                return False
        else:
            return False
        