class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal=[]
        for i in range(numRows):
            if i==0:
                pascal.append([1])
                continue
            row=[1]
            j=0
            while(j<len(pascal[i-1])-1):
                x=pascal[i-1][j]+pascal[i-1][j+1]
                row.append(x)
                j+=1
            row.append(1)
            pascal.append(row)
        return pascal
                
