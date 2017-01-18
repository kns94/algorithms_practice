# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class LinkedList(object):
    def printList(self, head):
        while head is not None:
            print head.val
            head = head.next

class Solution(object):

    def addRecursively(self, l1, l2, carry):
        '''
        Input: Two lists
        Output: A Sum bit and a carry bit
        '''

        if l1 is not None:
            h1 = l1
            prev = h1
            current = h1.next

            if current is not None:
                while current.next is not None:
                    prev = current
                    current = current.next

                d1 = current.val
                prev.next = None
            else:
                d1 = prev.val
                l1 = None
        else:
            d1 = 0

        if l2 is not None:
            h2 = l2
            prev = h2
            current = h2.next

            if current is not None:
                while current.next is not None:
                    prev = current
                    current = current.next

                d2 = current.val
                prev.next = None
            else:
                d2 = prev.val
                l2 = None
        else:
            d2 = 0

        s = d1 + d2 + carry
        if s >= 10:
            return l1, l2, s%10, 1
        else:
            return l1, l2, s, 0

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0
        result = None

        while l1 is not None or l2 is not None:
            l1, l2, s, c = self.addRecursively(l1, l2, c)
            
            if s is not None:
                node = ListNode(s)
                node.next = result
                result = node

        if c == 1:
            node = ListNode(c)
            node.next = result
            result = node 
            
        return result

if __name__ == "__main__":
    #d14 = ListNode(3)
    #d13 = ListNode(4)
    #d12 = ListNode(2)
    d11 = ListNode(5)
    #d11.next = d12
    #d12.next = d13
    #d13.next = d14

    #d23 = ListNode(4)
    #d22 = ListNode(6)
    d21 = ListNode(5)
    #d21.next = d22
    #d22.next = d23

    lst = Solution().addTwoNumbers(d11, d21)
    LinkedList().printList(lst)