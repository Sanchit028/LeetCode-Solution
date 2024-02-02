# Please note that this was a premium question and I haven't purchased it. Hence, this code hasn't been gone through submission

class solution:
    def missingNums(self, nums:List[int], lower: int, higher: int)-> List[String]:
        nums.insert(0,lower)
        nums.append(higher+1)
        res=[]
        for i in range(1,len(nums)):
            if(nums[i]-nums[i-1]<=1):
                continue
            elif(nums[i]-nums[i-1]==2):
                res.append(str(nums[i]-nums[i-1]))
                continue
            else:
                s=str(nums[i-1]+1)+"->"+str(nums[i]-1)
                res.append(s)
        return res
