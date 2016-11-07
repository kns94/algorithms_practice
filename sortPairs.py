# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):

    '''

    def swap(self, previous, first, second):
        
        #print first.val, second.val
        #if second.next != None:
        if not previous:
            temp = first
            first = second
            first.next = second.next
            second = temp
            second.next = first

        else:
            temp = first
            first = second
            first.next = second.next
            second = temp
            second.next = first
            previous.next = second
            
        
        else:
            if not previous:
                second.next = first
                first.next = None
            else:
                previous.next = second
                second.next = first
                first.next = None
        
        return first, second
    '''

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head
        
        #temp = ListNode(0)
        #temp.next = head

        runner = ListNode(0)
        runner.next = head

        previous = runner

        while 1:
            first = previous.next

            if not first or not first.next:
                break

            
            second = previous.next.next
            previous.next = second
            first.next = second.next
            second.next = first

            previous = first

        return runner.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    new = Solution().swapPairs(head)
    runner = new

    while runner != None:
        print runner.val
        runner = runner.next