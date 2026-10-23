class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        x = {}
        i = 0 # right

        while i < len(s):
            if s[i] in x:
                left = max(left, x[s[i]]+1)
            x[s[i]] = i
            res = max(res, i-left+1)
            i += 1
        
        return res