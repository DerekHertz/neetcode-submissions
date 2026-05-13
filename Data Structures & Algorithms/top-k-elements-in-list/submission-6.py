class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {i: nums.count(i) for i in nums}
        sorted_by_values = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_by_values.keys())[:k]
        