# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

from collections import deque

class Solution(object):

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        result = []

        if not root:
            return []

        if not root.left and not root.right:
            return [root]

        queue = deque()
        queue.append(root)
        elements = 1

        while queue:
            counter = 0
            sub = []

            while elements > 0:
                ele = queue.popleft()
                sub.append(ele.val)

                if ele.left:
                    queue.append(ele.left)
                    counter += 1

                if ele.right:
                    queue.append(ele.right)
                    counter += 1 

                elements -= 1

            elements = counter
            result.append(sub)


        return result[::-1]

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