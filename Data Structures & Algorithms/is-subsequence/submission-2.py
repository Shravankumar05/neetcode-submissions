class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        i = 0

        while i < len(t):
            if left == len(s):
                return True
            if s[left] == t[i]:
                left += 1
            if left == len(s):
                return True
            
            i += 1
        
        return False