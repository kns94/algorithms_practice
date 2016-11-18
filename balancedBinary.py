"""
Find whether tree is balanced or not
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):

    def checkHeight(self, root, h):

        if not root.left and not root.right:
            return 0

        if root.left:
            rec = self.checkHeight(root.left, h)
            if rec == -1:
                return -1
            else:
                lh = 1 + rec
        else:
            lh = 0

        if root.right:
            rec = self.checkHeight(root.right, h)
            if rec == -1:
                return -1
            else:
                rh = 1 + rec
        else:
            rh = 0

        new_height = max(lh,rh)
        if lh - rh >= 2 or lh - rh <= -2:
            return -1
        else:
            return new_height

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        height = self.checkHeight(root, 0)
        if height == -1:
            return False
        else:
            return True

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    #root.left.right.right = TreeNode(9)
    root.right = TreeNode(2)
    root.right.right = TreeNode(5)

    print Solution().isBalanced(root)        

