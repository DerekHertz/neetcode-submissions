class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        l = 0

        for r in range(k, len(nums) + 1):
            print(f"current window: [{l}:{r}]")
            print(nums[l:r])
            res.append(max(nums[l:r]))
            l+=1
        return res