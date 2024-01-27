#Solution 1:

#ASCII Value for a = 97 to z = 122
#ASCII Value for A = 65 to Z = 090
#ASCII Value for 0 = 48 to 9 = 57
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1
        
        while left < right:
            if not ((ord(s[left])>=48 and ord(s[left])<=57) or (ord(s[left])>=65 and ord(s[left])<=90) or (ord(s[left])>=97 and ord(s[left])<=122)):
                left += 1
                continue
            if not ((ord(s[right])>=48 and ord(s[right])<=57) or (ord(s[right])>=65 and ord(s[right])<=90) or (ord(s[right])>=97 and ord(s[right])<=122)):
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True


#Solution 2:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")

        for c in """:.,?/;@!#$%^&*()<>_-+=~\|}{]["'`""":
            if c in s:
                s = s.replace(c, "")
        if s == s[::-1]:
            return True
        else:
            return False
