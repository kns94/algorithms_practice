from collections import deque

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = deque()
        self.stack_top = None
        self.min_top = None
        self.min_stack = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.isEmpty(self.min_stack):
            self.min_stack.append(x)
            self.min_top = x 
        else:
            if self.min_top >= x:
                self.min_stack.append(x)
                self.min_top = x

        self.stack_top = x

    def pop(self):
        """
        :rtype: void
        """

        self.stack.pop()
        if self.stack_top == self.min_top:
            self.min_stack.pop()
            if not self.isEmpty(self.min_stack):
                self.min_top = self.min_stack.pop()
                self.min_stack.append(self.min_top)
            else:
                self.min_top = None

        if not self.isEmpty(self.stack):
                self.stack_top = self.stack.pop()
                self.push(self.stack_top)
        else:
            self.stack_top = None

    def top(self):
        """
        :rtype: int
        """
        return self.stack_top

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_top

    def isEmpty(self, stack):
        '''
        If the stack is empty
        '''

        return len(stack) == 0

    def out(self, stack):
        for ele in stack:
            print ele

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
obj.push(0)
obj.push(2)
obj.push(0)
obj.out(obj.min_stack)
obj.pop()
obj.out(obj.min_stack)
obj.pop()
obj.pop()
print '\n'
obj.out(obj.stack)
print '\n'
obj.out(obj.min_stack)