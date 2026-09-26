class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_builder = {}
        
        for i in range(len(strs)):
            sorted_word = ''.join(sorted(strs[i]))
            if sorted_word in res_builder:
                res_builder[sorted_word].append(i)
            else:
                res_builder[sorted_word] = [i]
        
        res = []
        for key, value in res_builder.items():
            curr = []
            for val in value:
                curr.append(strs[val])
            res.append(curr)
        return res