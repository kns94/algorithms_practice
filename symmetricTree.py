# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

from collections import deque

class Solution(object):

    def isSymmetric(self, root):
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
        head = True
        elements = 1

        while queue:
            counter = 0
            sub = []

            while elements > 0:
                ele = queue.popleft()
                
                if ele:

                    sub.append(ele.val)

                    if ele.left:
                        queue.append(ele.left)
                        counter += 1
                    else:
                        queue.append(None)
                        counter += 1

                    if ele.right:
                        queue.append(ele.right)
                        counter += 1 
                    else:
                        queue.append(None)
                        counter += 1

                else:
                    sub.append(None)

                elements -= 1


            if not head:
                if len(sub) % 2 != 0:
                    return False

                if sub != sub[::-1]:
                    return False

            head = False
            elements = counter
            
        return True


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(2)
    root.right.right = TreeNode(5)

    print Solution().isSymmetric(root)