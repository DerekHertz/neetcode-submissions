class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_num = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                min_num = min(min_num, nums[l])
                break

            m = (l + r) // 2
            if nums[m] >= nums[l]:
                print(f"nums at m ({nums[m]}) is >= nums at l ({nums[l]}) ... moving l")
                l = m + 1
            else:
                r = m - 1
            min_num = min(min_num, nums[m])
        return min_num
