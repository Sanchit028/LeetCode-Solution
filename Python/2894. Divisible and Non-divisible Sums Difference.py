class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nondiv=0
        for i in range(1,n+1):
            if i%m!=0:
                nondiv=nondiv+i
            else:
                nondiv=nondiv-i
        return nondiv