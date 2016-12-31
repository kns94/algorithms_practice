from collections import deque
import sys

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):

    def __init__(self):
        """
        Initializing global variables here
        """
        self.paths = 0

    def numPath(self, root, current_sum, target, cache):
        '''
        Using Two sum method to find sum till the given node and subtracting it with the target sum
        '''

        if not root:
            return

        updated_sum = current_sum + root.val 
        if updated_sum - target in cache:
            self.paths += cache[updated_sum - target]

        cache.setdefault(updated_sum, 0)
        cache[updated_sum] += 1
        self.numPath(root.left, updated_sum, target, cache)
        self.numPath(root.right, updated_sum, target, cache)
        cache[updated_sum] -= 1
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        if not root:
            return 0

        self.numPath(root, 0, sum, {0:1})
        return self.paths

if __name__ == "__main__":
    tree = TreeNode(10)
    tree.left = TreeNode(5)
    tree.right = TreeNode(-3)
    tree.left.left = TreeNode(3)
    tree.left.left.left = TreeNode(3)
    tree.left.left.right = TreeNode(-2)
    tree.left.right = TreeNode(2)
    tree.left.right.right = TreeNode(1)
    tree.right.right = TreeNode(11)

    #dfs = Solution().depth_first(tree, [])
    #for node in dfs:
    #    print node.val

    print Solution().pathSum(tree, 8)