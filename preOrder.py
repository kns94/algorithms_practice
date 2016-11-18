class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Tree:

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

        if root:

            if root.left:
                for item in self.preOrder(root.left):
                    yield(item)

            if root.right:
                for item in self.preOrder(root.right):
                    yield(item)

            yield(root.val)


        #return list()

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(10)
    print list(Tree().preOrder(root))
    print list(Tree().postOrder(root))