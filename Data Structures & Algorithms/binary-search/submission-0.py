class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            # mid point
            mid = r - l // 2
            # print("mid point is: ", mid)
            if target == nums[mid]:
                return mid

            # target is in right portion
            elif target > nums[mid]:
                l = mid + 1
                
            # target is in left portion
            else:
                r = mid - 1
                
        # not found
        return -1