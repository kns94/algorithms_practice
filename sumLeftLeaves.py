# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isLeaf(self, node):
        if node is None:
            return False
        if node.left is None and node.right is None:
            return True
        return False

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        result = 0

        if root is not None:

            if self.isLeaf(root.left):
                result += root.left.val
            else:
                result += self.sumOfLeftLeaves(root.left)
            
            result += self.sumOfLeftLeaves(root.right)
           
        return result
