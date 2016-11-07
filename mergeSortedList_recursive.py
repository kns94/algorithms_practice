class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
            
        if not l1:
            return l2
            
        if not l2:
            return l1
            
        if l1.val >= l2.val:
            result = l2
            result.next = self.mergeTwoLists(l1, l2.next)
        else:
            result = l1
            result.next = self.mergeTwoLists(l1.next, l2)
                
        return result