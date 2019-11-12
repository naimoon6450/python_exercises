# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None
        
        slow = head
        fast = head.next
        
        while slow is not fast:
            if fast is None or fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next
        
        print(slow.val, fast.val)
        # now find the length
        # length = 1
        # lenPt = head
        # while lenPt is not fast:
        #     lenPt = lenPt.next
        #     length += 1
        
        # since fast started at head.next, bring slow to head.next to find the starting pos
        start = head
        fast = fast.next
        # for i in range(length):
        #     fast = fast.next
        
        while start is not fast:
            start = start.next
            fast = fast.next
            
        return start