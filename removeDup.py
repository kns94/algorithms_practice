# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None  or head.next == None:
            return head
            
        n = head

        while n.next is not None:

            while n.next is not None and n.val == n.next.val:
                n.next = n.next.next
                
            n = n.next
            if n == None:
                break
        return head  

if __name__ == "__main__":
    #print Solution().deleteDuplicates()