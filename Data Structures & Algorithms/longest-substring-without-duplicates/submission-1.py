class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        seen = {}
        
        for right in range(len(s)):
            if s[right] in seen:
                left = max(seen[s[right]]+1, left)
            seen[s[right]] = right
            res = max(res, right - left + 1)
        
        return res