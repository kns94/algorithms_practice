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
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or not head.next:
            return True

        prev = None
        tortoise = head
        hare = head
        begin = True
        #hare

        while hare and hare.next:
            temp = tortoise.next
            tortoise.next = prev
            prev = tortoise
            tortoise = temp
            #print hare.val
            if begin:
                hare = temp.next
                begin = False
            else:
                hare = hare.next.next
        
        #Even
        if not hare:
            hare = prev
        else:
            hare = prev
            tortoise = tortoise.next
        
        while hare and tortoise:
            if hare.val != tortoise.val:
                return False
            hare = hare.next
            tortoise = tortoise.next

        return True

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)

    #LinkedList().printList(head)
    print Solution().isPalindrome(head)
    #LinkedList().printList(rev)