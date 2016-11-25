from collections import deque

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.empty(self.queue2) == 0:
            self.queue1.append(x)
        else:
            self.queue2.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        print self.queue1
        if self.empty(self.queue2) == 0:
            while self.empty(self.queue1) != 0:
                val = self.queue1.popleft()
                self.queue2.append(val)
        
        print self.queue2
        self.queue2.popleft()


    def top(self):
        """
        :rtype: int
        """
        

    def empty(self):
        """
        :rtype: bool
        """
        
        if len(self.queue2) == 0 and len(self.queue1) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    print stack.queue1
    print stack.queue2