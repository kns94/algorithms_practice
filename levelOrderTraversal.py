# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.hash = {}

    def calculateHeight(self, root):

        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        return 1 + max(self.calculateHeight(root.left), self.calculateHeight(root.right))

    def addDict(self, root, level):
        if not root:
            return

        if level == 1:
            try:
                self.hash[ ]


    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        

