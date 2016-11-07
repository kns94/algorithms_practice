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

        counter = {}
        counter[head.val] = 1

        #previous = None
        n = head.next
        prev = head
        i = 0

        while n is not None:
          
            if n.val not in counter:
                counter[n.val] = 1
                prev = n
            else:
                prev.next = n.next

            n = n.next      

        return head

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    #head.next.next = ListNode(2)
    #head.next.next.next = ListNode(3)
    Solution().removeDups(head)
    LinkedList().printList(Solution().removeDups(head))