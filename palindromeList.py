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
        prev = None
        slow = head
        fast = head

        while fast:
            temp = slow.next
            print temp.val
            slow.next = prev
            prev = slow
            slow = temp

            if not fast.next:
                #print slow.val
                break

            fast = fast.next.next

            if not fast:
                slow = slow.next

        #print slow.val

        return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    rev = Solution().isPalindrome(head)
    LinkedList().printList(rev)