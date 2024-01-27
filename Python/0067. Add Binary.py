class Solution(object):
    def addBinary(self, a, b):
        m=a if len(a) < len(b) else b
        res=''
        temp =0
        i = 0
        while (i<=len(m)-1):
            if a[len(a) - i -1] == '0' and b[len(b) - i -1] == '0':
                if temp == 0:
                    res='0'+res
                elif temp == 1:
                    res= '1'+res
                    temp = 0
            elif ((a[len(a) - i -1] == '0' and b[len(b) - i -1] == '1') or (a[len(a) - i -1] == '1' and b[len(b) - i -1] == '0')):
                if temp == 0:
                    res='1'+res
                elif temp == 1:
                    res='0'+res
            elif (a[len(a) - i -1] == '1' and b[len(b) - i -1] == '1'):
                if temp == 0:
                    res='0'+res
                    temp=1
                elif temp == 1:
                    res='1'+res
            i=i+1
        n=a if len(a) > len(b) else b
        n= n[0:len(n)-len(m)]
        if temp == 0:
            res=n+res
            return res
        elif temp==1:
            i =len(n)-1
            while (i>=0):
                if temp == 0:
                    n=n[0:i+1]
                    break;
                elif (n[i] == '0'):
                    res = '1'+res
                    n=n[0:i]
                    temp =0
                elif (n[i] == '1'):
                    res = '0'+res
                    n=n[0:i]
                i=i-1
        
        if temp==1:
            res='1'+n+res
            return res
        else:
            res=n+res
            return res
