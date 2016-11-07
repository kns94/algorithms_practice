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


    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if not digits:
            return 1

        if not digits.next:
            if digits.val != 9:
                digits.val += 1
            else:
                digits.val = 1
                digits.next = ListNode(0)

            return digits

        rev = self.reverse(digits)

        if rev.val != 9:
            carry = 0
            rev.val += 1
        else:
            rev.val = 0
            carry = 1
            prev = rev
            n = rev.next

            while n:
                new = carry + n.val
                carry = 0
                n.val = new
                if new >= 10:
                    n.val = 0
                    carry = 1
                else:
                     break
                prev = n
                n = n.next
            if carry == 1:
                prev.next = ListNode(1)

        rev = self.reverse(rev)
        return rev


if __name__ == "__main__":
    head = ListNode(9)
    head.next = ListNode(9)
    #head.next.next = ListNode(9)
    #head.next.next.next = ListNode(3)
    rev = Solution().plusOne(head)
    LinkedList().printList(rev)