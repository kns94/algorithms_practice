# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
    
        if p == None and q == None:
            return True

        if p == None and q != None:
            return False

        if q == None and p != None:
            return False
        
        if p.val == q.val:
            return True
        else:
            return False
            

        left = isSameTree(p.left, q.left)
        right = isSameTree(p.right, q.right)

        return left and right