# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):

    def __init__(self):
        self.l2r = []
        self.r2l = []

    def rightToLeft(self, root):
        self.r2l.append(root.val)

        if not root.right and not root.left:
            return None

        if root.right:
            self.rightToLeft(root.right)

        if root.left:
            self.rightToLeft(root.left)

    def leftToRight(self, root):
        self.l2r.append(root.val)

        if not root.right and not root.left:
            return None

        if root.left:
            self.leftToRight(root.left)

        if root.right:
            self.leftToRight(root.right)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True

        if not root.left and not root.right:
            return True

        if not root.left or not root.right:
            return False

        self.rightToLeft(root.left)
        self.leftToRight(root.right)

        return self.l2r == self.r2l

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.left.left = TreeNode(5)
    root.right = TreeNode(9)
    root.right.right = TreeNode(5)

    print Solution().isSymmetric(root)