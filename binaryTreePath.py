# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.ans = []

    def paths(self, root, path):

        if root.left is None and root.right is None:
            self.ans.append(path)
            return None

        if root.left:
            self.paths(root.left, path+'->'+str(root.left.val))

        if root.right:
           self.paths(root.right, path+'->'+str(root.right.val))

    def binaryTreePaths(self, root):
        if not root:
            return None

        self.paths(root, str(root.val))
        return self.ans

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(8)
    root.left.right = TreeNode(5)
    root.left.left = TreeNode(3)
    #root.left.right.right = TreeNode(9)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)

    print Solution().binaryTreePaths(root)        