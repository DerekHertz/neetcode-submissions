from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        q = deque()
        l = 0

        for r in range(len(nums)):
            # A. Maintain Monotonicity (Cleanup from the Right)
            # Pop indices from the back while their values are <= nums[r]
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            q.append(r)
            
            # B. Remove Old Indices (Cleanup from the Left)
            # If the index at the front is outside the window [l, r], pop it
            if q[0] < l:
                q.popleft() # <--- Your implementation here
            
            # 3. Append Result
            # The window is fully formed when r + 1 >= k.
            if r >= k - 1:
                # The max element is always at the front of the deque
                res.append(nums[q[0]]) 
                # Move the left pointer forward
                l += 1
            r += 1
        
        return res