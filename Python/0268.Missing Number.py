class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nsum = 0
        
        for num in nums:
            nsum += num

        return sum(range(1, len(nums)+1))-nsum
