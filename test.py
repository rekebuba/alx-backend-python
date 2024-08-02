from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        visited = set()
        for num in nums:
            if num not in visited:
                occurrences = nums.count(num)
                if occurrences > 1:
                    result += sum(range(occurrences))
                visited.update([num])
        return result
        