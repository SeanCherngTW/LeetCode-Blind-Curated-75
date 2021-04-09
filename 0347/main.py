class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)
        return [num for num, count in counter[:k]]
