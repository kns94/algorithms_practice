'''
Return K to Nth element in Linkedlist
'''

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Linkedlist():
    def calculateLength(self, head):

        if not head:
            return 0

        if not head.next:
            return 1

        l = 0
        while head:
            l += 1
            head = head.next
        return l

class Solution():

    def kToNth(self, head, k):
        
        #n = Linkedlist().calculateLength(head)

        if head is None:
            return 0

        index = self.kToNth(head.next, k) + 1

        if index == k:
            print head.val

        return index

        #if index == k:
        #    print head.val


if __name__ == "__main__":
    #print Linkedlist().calculateLength([])
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    #head.next.next.next = ListNode(3)
    Solution().kToNth(head, 4)