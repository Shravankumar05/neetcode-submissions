class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        left = 0

        while left < len(s) and i < len(t):
            if s[left] == t[i]:
                i += 1
            left += 1
        
        return len(t)-i