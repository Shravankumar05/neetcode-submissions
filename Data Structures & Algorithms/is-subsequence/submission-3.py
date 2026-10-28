class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        i = 0

        while i < len(t) and left < len(s):
            if s[left] == t[i]:
                left += 1
            
            i += 1
        
        return left == len(s)