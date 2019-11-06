# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        """
        Recursive solution
        time: O(n)
        space: O(1)
        """

        if (head is None or head.next is None):
            return head

        result = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return result

        """
        time: O(n)
        space: O(1) in place solution
        """
        # initialize pointers
#         prev = None
#         curr = head
#         nextP = None

#         if (head is None):
#             return head

#         while(curr is not None):
#             # hold on to the next
#             nextP = curr.next
#             # point next to previous value
#             curr.next = prev
#             # change prev val to current val
#             prev = curr
#             # change position of curr to next
#             curr = nextP

#         return prev

        """
        time: O(n)
        space: O(n) creating new nodes
        """
        # initialize first node
#         if (head is None):
#             return head

#         newList = ListNode(head.val)
#         pointNewList = newList

#         pointToOldList = head
#         # create new node upon traversing
#         while (pointToOldList.next != None):
#             # go to next val
#             pointToOldList = pointToOldList.next
#             # create new node
#             newListNode = ListNode(pointToOldList.val)
#             # point to other created node
#             newListNode.next = pointNewList
#             pointNewList = newListNode

#         return pointNewList

        """
        time: O(n) or O(3n)
        space: O(3n) creating in array... not right approach
        """
#         store = []
#         temp = head
#         # print(temp.val)
#         while (temp is not None):
#             store.append(temp.val)
#             temp = temp.next

        # revStore = store[::-1]
#         temp2 = head
#         index = 0
#         while(temp2 is not None):
#             temp2.val = revStore[index]
#             index += 1
#             temp2 = temp2.next

#         return head



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
in O(1) space
prev = null
s = head
f = head.next

p  s    f
   1 -> 2 -> 3 -> 4 -> 5 -> NULL

        p    s   f
NULL <- 1 <- 2 -> 3 -> 4 -> 5 -> NULL

final result

                            p    s    f
NULL <- 1 <- 2 <- 3 -> 4 -> 5 -> NULL




  5 -> 4 -> 3 -> 2 -> 1 -> NULL
"""

class RetryRevLL(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # recursive     
        if (head is None or head.next is None):
            return head
        else:
            # capture the returned node, which is 5 at first
            returnedNode = self.reverseList(head.next)
            # head will be at 4 first then 3 2 1 where returnNode will be at 5
            head.next.next = returnedNode




            


        # prev = None
        # slow = head
        # fast = head.next

        # while(slow.next is not None):
        #     # change directions and move pointers
        #     slow.next = prev
        #     # set prev to where slow curr is
        #     prev = slow
        #     # set slow equal to next item which is currently fast
        #     slow = fast
        #     # move fast one
        #     fast = fast.next
        
        # return head
        
revObj = new RetryRevLL()