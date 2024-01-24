class Solution:
    def partitionString(self, s: str) -> int:
        res=0
        s2=""
        for i in s:
            if s2.find(i)!=-1:
                res+=1
                s2=""
            s2=s2+i
        return res+1
