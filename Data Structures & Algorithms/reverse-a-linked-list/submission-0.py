# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        q = deque([head])
        res = ListNode(head.val)

        while q:
            curr_node = q.popleft()
            next_node = curr_node.next

            if next_node:
                q.append(next_node)
                res = ListNode(next_node.val, res)
        return res

        