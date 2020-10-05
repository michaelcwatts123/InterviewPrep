# Find the sum of all left leaves in a given binary tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, parent = None, sum = 0):
        if(node.left != None):
            sum = self.traverse(node.left, 'l', sum)
        if(node.right != None):
            sum = self.traverse(node.right, 'r', sum)
        if(node.left == None and node.right == None and parent == 'l'):
            return sum + node.val
        else:
            return sum 
        
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        val = self.traverse(root)
        return val