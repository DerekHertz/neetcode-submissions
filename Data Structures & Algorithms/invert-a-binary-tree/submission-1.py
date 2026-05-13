# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # check if root exists
        # init q, add first node to q 
        # while there are things in the q,
        # take the next node in q,
        # swap its left and right pointer
        # if a node exists (left or right) explore that node (add to q)
        # return the tree

        if not root:
            return None

        q = deque([root])

        while q:
            node = q.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return root