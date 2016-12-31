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

    def depth_first(self, root, dfs):
        '''
        Here, I will undertake in-order tree traversal
        '''

        if not root or root is None:
            return

        dfs.append(root)

        if root.left is not None:
            self.depth_first(root.left, dfs)

        if root.right is not None:
            self.depth_first(root.right, dfs)

        return dfs

    def numPath(self, root, current_sum, target):
        '''
        To count number of paths which satisfy the sum

        Base case is when leaf is found
        '''

        if not root:
            return

        if current_sum + root.val == target:
            #print root.val
            self.paths += 1

        if root.left is not None:
            self.numPath(root.left, current_sum + root.val, target)

        if root.right is not None:
            self.numPath(root.right, current_sum + root.val, target)

        if root.left is None and root.right is None:
            return

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        if not root:
            return 0

        dfs = self.depth_first(root, [])
        count = 0

        for node in dfs:
            self.numPath(node, 0, sum)

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

    dfs = Solution().depth_first(tree, [])
    #for node in dfs:
    #    print node.val

    print Solution().pathSum(tree, 8)