class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_sorted = sorted(set(nums))
        print(nums_sorted)
        counter = 1 if len(nums) else 0
        consecutive_runs = []
        print(f"len num: {len(nums)}")
        if len(nums) == 0:
            return 0
        elif len(set(nums)) == 1:
            return 1
        else:
            for i in range(0, len(nums_sorted)):
                if i + 1 < len(nums_sorted):
                    diff = nums_sorted[i + 1] - nums_sorted[i]
                    print(f"diff: {diff}")
                    if diff > 1:
                        counter = 1
                    elif diff == 1 and nums_sorted[i] != nums_sorted[i + 1]:
                        counter += 1
                        consecutive_runs.append(counter)
                    print(f"counter[{nums_sorted[i]} {nums_sorted[i + 1]}]: {counter}")
            return max(consecutive_runs)