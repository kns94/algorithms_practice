# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def calculateSum(self, root, leaf_sum, sum):
        if not root:
            return False

        if not root.left and not root.right:
            if root.val + leaf_sum == sum:
                return True
            else:
                return False
                
        left = False
        right = False

        if root.left:
            left = self.calculateSum(root.left, root.val + leaf_sum, sum)
        
        if root.right:
            right = self.calculateSum(root.right, root.val + leaf_sum, sum)
            
        return right or left

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.calculateSum(root, 0, sum)