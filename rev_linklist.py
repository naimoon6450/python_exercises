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
