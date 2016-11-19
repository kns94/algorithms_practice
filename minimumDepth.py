# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):

    def __init__(self):
        self.mn = -1

    def calculateHeight(self, root, h):

        if root.left is None and root.right is None:
            if self.mn == -1:
                self.mn = h
            else:
                self.mn = min(self.mn, h)
            return h

        lh = None
        rh = None

        if root.left:
            lh = self.calculateHeight(root.left, 1 + h)

        if root.right:
            rh = self.calculateHeight(root.right, 1 + h)

        if lh and rh:
            mn = min(lh, rh)
            mx = max(lh,rh)
        else:
            mn = lh or rh
            mx = lh or rh
        if self.mn == -1:
            self.mn = mn
        else:
            self.mn = min(self.mn, mn)

        return mx


    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        height = self.calculateHeight(root, 1)
        #print height
        return self.mn

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(8)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.left.left = TreeNode(3)
    #root.left.right.right = TreeNode(9)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)

    print Solution().minDepth(root)

