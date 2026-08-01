class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        i = 0
        while i < len(strs[0]):
            j = 1
            curr = strs[0][i]
            while j < len(strs):
                if i > len(strs[j])-1:
                    return res
                elif strs[j][i] != curr:
                    return res
                j += 1
            res += curr
            i += 1
        return res