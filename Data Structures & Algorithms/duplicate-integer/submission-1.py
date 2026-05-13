class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_count = {i: nums.count(i) for i in nums}
        if len(nums):
            return max(num_count.values()) > 1
        else:
            return False