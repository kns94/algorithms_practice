# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

    class Solution(object):
        def getIntersectionNode(self, headA, headB):
            """
            :type head1, head1: ListNode
            :rtype: ListNode
            """
            
            if not headA or not headB:
                return None

            length1 = 1
            length2 = 1

            n = headA.next

            while n:
                n = n.next
                length1 += 1

            n = headB.next

            while n:
                n = n.next
                length2 += 1

            if length1 > length2:
                diff = length1 - length2

                i = 0

                while headA:
                    if i == diff:
                        break
                    else:
                        headA = headA.next
                        i += 1
            else:
                diff = length2 - length1

                i = 0

                while headB:
                    if i == diff:
                        break
                    else:
                        headB = headB.next
                        i += 1

            while headA and headB:
                if headA.val == headB.val:
                    return headA
                else:
                    headA = headA.next
                    headB = headB.next