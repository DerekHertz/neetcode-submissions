"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        q = deque([node])
        new_start_node = Node(node.val)
        visited = {}
        visited = {node.val: new_start_node,}

        while q:
            
            node = q.popleft()
            # list of nodes
            val, neighbors = node.val, node.neighbors
            curr_clone = visited[val]
            for n in range(len(neighbors)):
                n_val = neighbors[n].val

                if n_val not in visited:
                    visited[n_val] = Node(n_val)
                    q.append(neighbors[n])
                
                curr_clone.neighbors.append(visited[n_val])


        return new_start_node

        