# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

import random 

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """

        """
        The methodology applied is called reservoir sampling, where you create a reservoir and then randomly select a number from the reservoir. Since, we cannot 
        use an extra space - we will randomly select a number with 1/n probability.
        """
        
        if self.head == None:
            return

        result = self.head.val
        current = self.head.next
        n = 2

        while current is not None:

            rnd = random.randrange(n)

            if rnd == 0:
                result = current.val  

            current = current.next
            n += 1

        return result

# Your Solution object will be instantiated and called as such:
if __name__ == "__main__":
    d14 = ListNode(3)
    d13 = ListNode(4)
    d12 = ListNode(2)
    d11 = ListNode(5)
    d11.next = d12
    d12.next = d13
    d13.next = d14

    obj = Solution(d11)
    param_1 = obj.getRandom()
    print param_1