class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    print(f"nums at m ({nums[m]}) is less than target {target} and nums at m is greater than nums at l ({nums[l]}) ... moving l")
                    l = m + 1
                else:
                    print("moving r")
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        print("did not find return -1")
        return -1