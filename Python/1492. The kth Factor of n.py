class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        x=0
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                x+=1
                if x==k:
                    return i
        if x+1==k:
            return n
        return -1
