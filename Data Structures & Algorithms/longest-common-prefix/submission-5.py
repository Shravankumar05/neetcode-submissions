class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        j = 0
        while j < len(strs[0]):
            i = 1
            curr = strs[0][j]
            while i < len(strs):
                if j >= len(strs[i]) or curr != strs[i][j]:
                    return res
                i += 1
            res += curr
            j += 1
        return res