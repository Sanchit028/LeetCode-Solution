class Solution:
    def firstUniqChar(self, s: str) -> int:
        alphas='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in alphas if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
