class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums=sorted(nums)
        res=[]
        ans=[]
        c=0
        for i in range(len(nums)):
            if i%3==0:
                ans.append(nums[i])
                c=1
            elif (i-1)%3==0 and nums[i]-ans[0]<=k:
                ans.append(nums[i])
                c=2
            elif (i-2)%3==0 and nums[i]-ans[0]<=k and nums[i]-ans[1]<=k:
                ans.append(nums[i])
                res.append(ans)
                ans=[]
                c=0
            else:
                return []
        if ans==[]:
            return res
        return []
