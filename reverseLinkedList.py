class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def set_next(self, y):
        self.next = y

    def get_data(self):
        return self.val

    def get_next(self):
        return self.next

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
    
    def insert_node(self, v):
        node = ListNode(v)
        self.head.next = node

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return None
        
        p = head
        while p.next is not None:
            n = p.next
            p.next = n.next
            n.next = head
            head = n
        return head
        

if __name__ == "__main__":
    ll = ListNode(3)
    ll.next = 4
    ll.next = 1
    ll.next = 7