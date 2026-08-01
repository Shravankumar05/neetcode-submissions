class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_builder = {}

        for i in range(len(strs)):
            curr = str(sorted(strs[i]))
            if curr in res_builder:
                res_builder[curr].append(i)
            else:
                res_builder[curr] = [i]
        
        res = []
        for key, value in res_builder.items():
            curr = []
            for idx in value:
                curr.append(strs[idx])
            if curr:
                res.append(curr)
        
        return res