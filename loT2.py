# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):

    def __init__(self):
        self.levels = {}

    def parse(self, root, h):

        if root is None:
            return None

        if h not in self.levels:
            self.levels[h] = [root.val]
        else:
            self.levels[h].append(root.val)

        if root.left:
            self.parse(root.left, h + 1)

        if root.right:
            self.parse(root.right, h + 1)

        if not root.left and not root.right:
            return None

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return None

        if not root.left and not root.right:
            return [[root]]

        self.parse(root, 0)
        vals = self.levels.values()
        return vals[::-1]

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    #root.left.left = TreeNode(1)
    #root.left.right = TreeNode(3)
    #root.right.left = TreeNode(6)
    #root.right.right = TreeNode(9)

    print Solution().levelOrderBottom(root)
    #print tree.left.val
    #print tree.right\