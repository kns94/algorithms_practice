# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root == None:
            return 0

        depth = 1
        #depth = max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
        #return depth
        ldepth = self.maxDepth(root.left)
        rdepth = self.maxDepth(root.right)

        return 1 + max(ldepth, rdepth)