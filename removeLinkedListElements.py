# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class LinkedList():
    def printList(self, head):

        if not head:
            return None

        runner = head
        while runner:
            print runner.val
            runner = runner.next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
    
        while head and head.val == val:
            head = head.next

        if not head:
            return None

        prev = head
        n = head.next 
        #print prev.val
        ##print n.val
        #print n.next

        while n:

            if n.val == val:
                while n and n.val == val:
                    n = n.next

                prev.next = n

            prev = n
            if n:
                n = n.next

        return head

if __name__ == "__main__":
    head = ListNode(9)
    head.next = ListNode(9)
    head.next.next = ListNode(8)
    head.next.next.next = ListNode(9)
    head.next.next.next.next = ListNode(8)
    head.next.next.next.next.next = ListNode(9)
    head.next.next.next.next.next.next = ListNode(8)
    #head.next.next = ListNode(9)
    #head.next.next.next = ListNode(3)
    rev = Solution().removeElements(head, 9)
    LinkedList().printList(rev)