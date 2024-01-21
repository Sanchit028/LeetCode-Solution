class Solution:
    def climbStairs(self, n: int) -> int:
        #It is a Fibonacci Series
        if n==1:
            return 1
        elif n==2:
            return 2
        
        a,b=1,1
        res,temp=0,1
        while (temp<n):
            res =a+b
            a=b
            b=res
            temp=temp+1
        return res
