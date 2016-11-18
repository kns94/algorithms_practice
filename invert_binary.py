# Definition for a binary tree node.

class Tree():

    def __init__(self):
        self.queue = []

    def calculateDFS(self, root):
        '''
        DFS of tree
        '''

        if not root:
            return []

        self.queue.append(root.val)

        if not root.left and not root.right:
            return None

        if root.left and root.right:
            #self.queue.append(root.val)
            #self.queue.append(root.left.val)
            self.calculateDFS(root.left)

            #self.queue.append(root.right.val)
            self.calculateDFS(root.right)

        if not root.right:
            #self.queue.append(root.val)
            self.calculateDFS(root.left)

        if not root.left:
            #self.queue.append(Noone)
            self.calculateDFS(root.right)

        return self.queue

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if not root:
            return None

        #if not root.left and not root.right:
        #    return root

        temp = TreeNode(root.val)

        if root.right:
            temp.left = self.invertTree(root.right)
        else:
            temp.left = None

        if root.left:
            temp.right = self.invertTree(root.left)
        else:
            temp.right = None

        return temp

        #if not root.right:
        #    root.right = root.left
        #    root.left = None
        #    self.invertTree(root.right)

        #if not root.left:
        #    root.left = root.right
        #    root.right = None
        #    self.invertTree(root.left)

        #if root.left and root.right:
        #    temp = root.left
        #    root.left = root.right
        #    root.right = temp

         #   self.invertTree(root.left)
         #   self.invertTree(root.right)

        #return root

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    #root.right = TreeNode(7)
    #root.left.left = TreeNode(1)
    #root.left.right = TreeNode(3)
    #root.right.left = TreeNode(6)
    #root.right.right = TreeNode(9)

    tree = Solution().invertTree(root)
    #print tree.left.val
    #print tree.right
    print Tree().calculateDFS(tree)
