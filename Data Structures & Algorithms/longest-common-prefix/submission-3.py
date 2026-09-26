class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        i = 0
        j = 0
        while j < len(strs[0]):
            curr = strs[0][j]
            x = 0
            while x < len(strs):
                if j >= len(strs[x]):
                    return res
                if curr != strs[x][j]:
                    return res
                x += 1
            res += curr
            j += 1
        return res