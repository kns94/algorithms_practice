'''
Reverse a LinkedList
'''

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

class Solution():

    def reverse(self, head):
        
        if not head.next or not head:
            return head

        prev = None
        current = head

        while current.next is not None:
            #temp = current.next
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        current.next = prev
        return current

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    #head.next.next.next = ListNode(3)
    rev = Solution().reverse(head)
    LinkedList().printList(rev)