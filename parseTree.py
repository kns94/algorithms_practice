# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):

    def __init__(self):
        self.childs = []

    def parse(self, root):

        self.childs.append(root.val)

        if root.left is None and root.right is None:
            return None

        if root.left:
            self.parse(root.left)

        if root.right:
            self.parse(root.right)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        else:
            self.parse(root)
            print self.childs

            if len(self.childs) % 2 == 0:
                return False
            else:
                for i in range(1, len(self.childs)/2 + 1):
                    if self.childs[i] != self.childs[len(self.childs)/2 + i]:
                        return False
            
            return True


if __name__ == "__main__":
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(2)
    head.left.left = TreeNode(3)
    head.left.left.left = TreeNode(5)
    head.left.right = TreeNode(4)
    head.right.left = TreeNode(3)
    head.right.right = TreeNode(4)
    head.right.right.right = TreeNode(6)
    print Solution().isSymmetric(head)