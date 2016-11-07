'''
Here I have to remove duplicates in an unsorted linkedList
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

    def removeDups(self, head):
        
        if not head or not head.next:
            return head

        #previous = None
        n = head
        runner = head.next
        prev = head

        while n:
            current = n.val 
            prev = n
            runner = n.next

            while runner:
            
                if runner.val != current:
                    prev = runner
                else:
                    prev.next = runner.next
                runner = runner.next

            n = n.next      

        return head

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    #head.next.next.next.next.next = ListNode(3)
    Solution().removeDups(head)
    LinkedList().printList(Solution().removeDups(head))