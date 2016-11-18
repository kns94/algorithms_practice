# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):

    def preOrder(self, root):

        if root:

            yield(root.val)

            if root.left:
                for item in self.preOrder(root.left):
                    yield(item)

            if root.right:
                for item in self.preOrder(root.right):
                    yield(item)

    def postOrder(self, root):

        """
        if root:

            if root.left:
                for item in self.preOrder(root.left):
                    yield(item)

            if root.right:
                for item in self.preOrder(root.right):
                    yield(item)

            yield(root.val)
        """

        if root:

            for item in self.postOrder(root.left):
                yield(item)

            for item in self.postOrder(root.right):
                yield(item)

            yield(root.val)

    def inOrder(self, root):

        if root:

            for item in self.inOrder(root.left):
                yield(item)

            yield(root.val)

            for item in self.inOrder(root.right):
                yield(item)

    def postOrder_recursive(self, root):

        if not root:
            return []

        return self.postOrder_recursive(root.left) + self.postOrder_recursive(root.right) + [root.val]

    def isSymmetric(self, root):

        if not root:
            return True

        pre = list(self.preOrder(root))
        #post = list(self.postOrder(root))
        #ino = list(self.inOrder(root))
        print self.postOrder_recursive(root)[::-1]
        print pre
       #print post
        #print ino

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    #root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right = TreeNode(2)
    #root.right.left = TreeNode(6)
    root.right.right = TreeNode(3)
    Solution().isSymmetric(root)