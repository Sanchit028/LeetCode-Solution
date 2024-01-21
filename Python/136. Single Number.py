class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        temp=nums[0]
        for i in range(len(nums)):
            if nums[i]==temp:
                continue
            if i == len(nums)-1:
                return nums[i]
            elif nums[i]==nums[i+1]:
                temp=nums[i]
            else:
                return nums[i]
        return nums[0]
